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

    def add_stored_point(self, pixel_point):
        ''' Adds a point to the set of stored points.

        The inputted pixel_point is stored as both a pixel point and respective
            graph point. Defining points must be set to add a stored point.

        Raises Exception on invalid point, or if defining points not set.

        Model.add_stored_point(tuple/list[int,int]) -> None

        '''
        # check if defining points are empty
        if not self._defining_points:
            raise Exception(
                "Defining points must be set to add a stored point.")
        
        self._verify_point(pixel_point) # raises exception on failure
        self._stored_points[tuple(pixel_point)] = \
                self.get_graph_point(pixel_point)

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
