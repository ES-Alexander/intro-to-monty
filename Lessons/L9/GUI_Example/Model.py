#!/usr/bin/env python3

import cv2 # opencv (open computer vision) library
import numpy as np # numerical python library

class Model(object):
    ''' A class for the data of a graph-analyser. '''
    def __init__(self):
        ''' A class for storing user-specified points on a graph.

        Users specify defining points mapping the pixel-plane to the graph-
            plane. The Model stores the mapping, and converts additional pixel-
            point values to graph-points.
        
        Constructor: Model.__init__()
        
        '''
        # initialise memory and points
        self.clear_data()

    def set_defining_points(self, points_map):
        ''' Sets the defining points of the graph.

        'points_map' should be a mapping of three point pairs, matching pixel-
            coordinates with graph-coordinates. Points should be stored as
            tuples, with image points comprised of integers (x,y), and graph
            points as ints/floats (x2,y2). The points must not be collinear.

        Raises Exception on invalid points map input.

        Model.set_defining_points(dict{(int,int):(float,float),...}) -> None

        '''
        self._verify_points_map(points_map) # raises exception on failure
        self._defining_points = dict(points_map) # deep copy
        self._affine_transform = self.get_affine_transform(
            self._defining_points)
        self._update_stored_points()

    def add_stored_point(self, pixel_point):
        ''' Adds a point to the set of stored points, returns graph point.

        The inputted pixel_point is stored as both a pixel point and respective
            graph point. Defining points must be set to add a stored point.

        Raises Exception on invalid point, or if defining points not defined.

        Model.add_stored_point(tuple/list[int,int]) -> tuple(float,float)

        '''
        self._verify_defined() # check if defining points defined
        self._verify_point(pixel_point) # validate input

        graph_point = self.get_graph_point(pixel_point)
        self._stored_points[tuple(pixel_point)] = graph_point

        return graph_point

    def remove_stored_point(self, pixel_point, max_dist=10):
        ''' Returns the removed graph point from the set of stored points.

        If pixel_point is not stored, removes the closest point if
            within 'max_dist' pixels distance.

        If no point is removed, returns None.

        Raises Exception if defining points not defined.

        Model.remove_stored_point(tuple/list[int,int], *int) ->
                tuple(float,float)/None

        '''
        self._verify_defined() # check if defining points defined

        # try to remove the exact point
        point_removed = self._stored_points.pop(pixel_point, None)
        
        if point_removed is None:
            # pixel_point is not a key in stored points, find nearest
            closest_point, dist = Model.get_closest(pixel_point,
                    list(self._stored_points.keys()))
            if dist < max_dist:
                point_removed = self._stored_points.pop(closest_point)
                
        return point_removed

    def _update_stored_points(self):
        ''' Updates all stored points based off the current affine transform.

        Model._update_stored_points() -> None

        '''
        for pixel_point in self._stored_points:
            self.add_stored_point(pixel_point)

    def clear_data(self):
        ''' Clears the defining and stored points.

        Model.clear_data(None) -> None

        '''
        self.clear_defining_points()
        self.clear_stored_points()

    def clear_defining_points(self):
        ''' Clears the defining points.

        Model.clear_defining_points(None) -> None

        '''
        self._defining_points = {}

    def clear_stored_points(self):
        ''' Clears the stored points.

        Model.clear_stored_points(None) -> None

        '''
        self._stored_points = {}

    def get_graph_point(self, pixel_point):
        ''' Returns the graph point related to the specified pixel point.

        Relation determined by the pre-specified defining points.

        Model.get_graph_point(tuple(int,int)) -> tuple(float,float)

        '''
        # [xg, yg]' = A_T * [xp, yp, 1]'
        point = self._affine_transform * np.transpose(np.matrix(
            list(pixel_point) + [1]))
        return (point.item(0), point.item(1)) # (xg, yg)

    def save_data(self, filename, pixel_point=False):
        ''' Saves the stored points into the specified file, in a csv format.

        'filename' should have extension '.csv' or '.txt'.
        'pixel_point' is a boolean specifying if the pixel points are also saved
            with their corresponding graph points

        Model.save_data(str.csv, *bool) -> None

        '''
        if pixel_point:
            output = 'pixelX,pixelY,graphX,graphY\n'
            for point in self._stored_points:
                add_str = list(point) + list(self._stored_points[point])
                output += ','.join([str(i) for i in add_str]) + '\n'
        else:
            output = 'graphX,graphY\n'
            for pixel_point in self._stored_points:
                graph_point = self._stored_points[pixel_point]
                output += ','.join([str(i) for i in graph_point]) + '\n'

        # write output to file, closes itself on completion
        with open(filename, 'w') as file:
            file.write(output)

    def _verify_defined(self):
        ''' Check if the defining points have been defined yet, else Exception.

        Model._verify_defined() -> None

        '''
        # check if defining points are empty
        if not self._defining_points:
            raise Exception(
                "Defining points must be set to add/remove a stored point.")

    @staticmethod
    def _verify_points_map(points_map):
        ''' Checks if a defining points mapping is valid.

        'points_map' should have three keys, each tuples of integer points, x,y,
            with each respective value a tuple of float points, x2,y2.

        Model._verify_points_map(dict{(int,int):(float,float),...}) -> None

        '''
        if len(points_map.keys()) != 3:
            raise Exception('Invalid number of defining points - should be 3.')

        # check all points are tuples
        for point in points_map.items():
            if type(point) is not tuple:
                raise Exception(("Invalid defining point type {}".format(
                    type(point)), "- should be tuple."))

        # check pixel values are integers
        for pixel_point in points_map.keys():
            Model._verify_point(pixel_point, int)

        # check graph values are integers/floats
        for graph_point in points_map.values():
            Model._verify_point(graph_point)
        
            
    @staticmethod
    def _verify_point(point, value_type=None):
        ''' Checks if a point is valid.

        A valid point has 2 values of type value_type (if specified) else
            values should be of type int or float.

        Raises Exception if either check fails.

        Model._verify_point(tuple/list[int/float,int/float], *type) -> None

        '''
        num_vals = len(point)
        if num_vals == 2:
            for coord in point:
                if value_type is None:
                    if type(coord) is not float and type(coord) is not int:
                        raise Exception(("Invalid point type: {} -".format(
                                        type(coord))),
                                        "point values should be int/float.")
                elif type(coord) is not value_type:
                    raise Exception(("Invalid point type: {} -".format(
                                    type(coord)),
                                     "point values should be {}.".format(
                                     value_type)))
            return # no issues, continue where left off
        
        raise Exception(("Invalid point length: {}".format(num_vals),
                         "- points should have 2 values"))

    @staticmethod
    def get_affine_transform(points_map):
        ''' Determines an affine transformation between 2D planes.

        'points_map' should be a 2D point mapping dictionary for 3 point pairs.

        An affine transform maintains parallel lines, but allows for
            translation, rotation, scaling, skewing, and mirroring. It is
            exactly defined by three point pair mappings.

        Model.get_affine_transform(dict{p1N:p2N}) -> np.matrix

        '''
        pixel_points = np.float32(list(points_map.keys()))
        graph_points = np.float32(list(points_map.values()))
        return cv2.getAffineTransform(pixel_points, graph_points)

    @staticmethod
    def get_closest(check_point, search_points):
        ''' Returns the closest point and the shortest distance to check_point.

        Returns None if no search points are provided.

        Search is performed in ND domain, but dimension of check_point must
            match that of the search_points.

        Model.get_closest(tuple(float), tuple(tuple(float))) ->
                tuple(tuple(float),float)

        '''
        # check if any points exist
        if len(search_points) == 0:
            return (None, np.Inf)
        # convert to numpy elements
        cp = np.matrix(check_point)
        sps = np.matrix(search_points)
        diff = sps - cp
        
        # get a list of the distance between check_point and each search point
        dists = [np.linalg.norm(i) for i in diff]
        # 'zip' joins N iterables for the first m elements, where m is the
        #   length of the shortest iterable
        #   -> Iterator[(dist[i],search_point[i])]
        # 'key' in 'min' specifies the values being searched over (in this case
        #   the values of dists). Also available in 'max' function.
        min_dist, closest_point = min(zip(dists,search_points),
                                      key=lambda dist_sp: dist_sp[0])
        
        return (closest_point, min_dist)
