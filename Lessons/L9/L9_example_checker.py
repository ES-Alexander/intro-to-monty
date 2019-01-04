#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the LN_1_examples file.             #
################################################################################

# imports all the variables/functions/classes from L9_1_examples
from L9_1_examples import *
import sys
sys.path.append('..')
from TestRun import TestRun

import tkinter as tk

class L9Tests(TestRun):
    def run_tests(self, *args, **kwargs):
        ''' Wraps running tests with a GUI creation/deletion protocol. '''
        self._root = tk.Tk()
        try:
            self._controller = Controller(self._root)
        except Exception as e:
            print('Controller setup failed, due to:\n', e)
            self._controller = View(self._root)
            
        self._widgets = L9Tests.get_children(self._root)
                
        super().run_tests(*args, **kwargs)
        self._root.destroy()

    def _clear_root(self):
        ''' Clears all widgets from self._root. '''
        for widget in self._root.winfo_children():
            widget.destroy()

    @staticmethod
    def get_children(widget):
        ''' Get the top_level children in this widget in a dict of class.

        L9Tests.get_children(tk.widget) -> dict{str'Type':list[tk.widget]}

        '''
        widgets = {}
        for child in widget.winfo_children():
            child_class = child.winfo_class()
            if child_class in widgets:
                widgets[child_class] += [child]
            else:
                widgets[child_class] = [child]
        return widgets
        
    # class existence
    def test_classes_exist(self):
        ''' Testing for existence of relevant classes. '''
        for class_name in ['Model','View','Controller']:
            try:
                test = eval('{}'.format(class_name))
            except NameError:
                assert False, "Class {} does not exist".format(class_name)

    # required setup methods
    def test_setup_controls(self):
        ''' Testing for existence of _setup_io in View. '''
        assert '_setup_controls' in dir(View), 'Controls not set up with ' +\
               '_setup_controls method in View.'

    def test_setup_canvas(self):
        ''' Testing for existence of _setup_canvas in View. '''
        assert '_setup_canvas' in dir(View), 'Canvas not set up with ' +\
               '_setup_canvas method in View.'

    def test_setup_menubar(self):
        ''' Testing for existence of _setup_menubar in View. '''
        assert '_setup_menubar' in dir(View), 'Menubar not set up with ' +\
               '_setup_menubar method in View.'

    def test_init_bindings(self):
        ''' Testing for existence of _init_bindings in View. '''
        assert '_init_bindings' in dir(View), 'Bindings not initialised with' +\
               ' _init_bindings method in View.'

    def test_add_bindings(self):
        ''' Testing for existence of _add_bindings in Controller. '''
        assert '_add_bindings' in dir(Controller), 'Bindings not set up with' +\
               ' _add_bindings method in Controller.'

    # required widgets
    def test_menubar(self):
        ''' Testing for correct setup of the menubar in View.

        View should include a menubar with at least a 'File' menu, which should
            include a 'Clear All' command.

        '''
        # check for menubar existence
        assert 'Menu' in self._widgets, \
               "GUI should include a menubar, with at least a 'File' menu."
        menubar = self._widgets['Menu']

        # check 'File' cascade exists
        file_cascade = None
        for menu in menubar:
            menu_type = menu.type(0)
            if  menu_type != 'cascade':
                continue
            label = menu.entrycget(0, 'label')
            if label == 'File':
                file_cascade = menu
        assert file_cascade is not None, "Menubar should include a 'File' menu."

        # check 'Clear All' command exists in 'File' menu
        clear_command = None
        filemenu = L9Tests.get_children(file_cascade)['Menu']
        for menu_item in filemenu:
            item_type = menu_item.type(0)
            if item_type != 'command':
                continue
            label = menu_item.entrycget(0, 'label')
            if label == 'Clear All':
                clear_command = menu_item
        assert clear_command is not None, \
               "'File' menu should include a 'Clear All' command."

    def test_canvas_frame(self):
        ''' Testing for correct setup of the canvas frame in View.

        View should include a frame on the right hand side, which contains at
            least a 'Canvas' widget.

        Widgets should use the 'grid' geometry manager.

        '''
        assert 'Frame' in self._widgets, "GUI should contain at least 2 frames."
        frames = self._widgets['Frame']

        # check Frame in column 1 contains a Canvas (frame on the right)
        for frame in frames:
            contents = L9Tests.get_children(frame)
            try:
                col = frame.grid_info()['column']
            except AttributeError:
                assert False, \
                       "GUI elements should use the grid geometry manager."
            if col == 1 and 'Canvas' in contents:
                return

        assert False, \
               "The Frame in column 1 should contain a Canvas element."

    def test_controls_frame(self):
        ''' Testing for correct setup of the controls frame in View.

        View should include a frame on the left hand side, which contains at
            least a 'Label' widget with text 'Scale Controls', an 'Entry'
            widget, a 'Button' widget with text 'Scale', and another 'Label'
            widget for errors and instructions.

        Widgets should use the 'grid' geometry manager.

        '''
        assert 'Frame' in self._widgets, "GUI should contain at least 2 frames."
        frames = self._widgets['Frame']

        # check frame in column 0 contains the controls (frame on the left)
        for frame in frames:
            contents = L9Tests.get_children(frame)
            try:
                col = frame.grid_info()['column']
            except AttributeError:
                assert False, \
                       "GUI elements should use the grid geometry manager."
            # initialise checks for this frame
            valid_label = False
            valid_button = False
            if col == 0:
                # assume we have the Controls frame
                try:
                    if len(contents['Label']) >=2 and \
                       len(contents['Entry']) >= 1 and \
                       len(contents['Button']) >= 1:
                        # required widget types present
                        for label in contents['Label']:
                            if label.cget('text') == 'Scale Controls':
                                valid_label = True
                                break
                        for button in contents['Button']:
                            if button.cget('text') == 'Scale':
                                valid_button = True
                                break
                        if valid_label and valid_button:
                            return # checks validated
                except KeyError:
                    continue
                    
        assert False, \
               "The Frame in column 0 should contain your controls, which " +\
               "should include a Label with text 'Scale Controls', an Entry " +\
               "for entering the scale, a Button for submitting the scale, " +\
               "and a Label for the display of instructions and errors."

    def test_master_title(self):
        ''' Test for correct setup of the master window title. '''
        assert self._root.title() == 'Parametric Polygon', \
               "Title of the master window should be 'Parametric Polygon'."
                
        


#------------------------------ Example Solution ------------------------------#

if __name__ == '__main__':
    import random
    import numpy as np

    class Model(object):
        ''' A class for the data of a parametrically controlled polygon. '''
        def __init__(self):
            ''' A class for storing user-specified points of a polygon.

            Users specify defining points of the polygon, and a reference point
                about which to scale the polygon. Scaling is then applied on
                user request, relative to the current polygon points.

            Constructor: Model()
            
            '''
            self._polygon_points = np.array([])
            self._reference_point = np.array([])

        def set_polygon_points(self, points):
            ''' Set the internal polygon points to the specified points.

            self.set_polygon_points(list[list[float,float]]) -> None

            '''
            self._polygon_points = np.array(points)

        def set_reference_point(self, point):
            ''' Set the internal reference point to the specified point.

            self.set_reference_point(list[float,float]) -> None

            '''
            self._reference_point = np.array(point)

        def clear_data(self):
            ''' Clears the internally stored reference and polygon points.

            self.clear_data() -> None

            '''
            self.set_polygon_points([])
            self.set_reference_point([])

        def scale_polygon(self, scale_factor):
            ''' Returns current polygon points scaled by 'scale_factor'.

            If the reference or polygon points are currently undefined, raises
                Exception with a relevant message.

            The polygon is scaled about the current reference point.

            self.scale_polygon(float) -> list[list[float,float]]

            '''
            if self._polygon_points.size == 0:
                raise Exception('Polygon not defined - cannot scale')
            if self._reference_point.size == 0:
                raise Exception('Reference point not defined - cannot scale')

            # scale internal points directly
            self._polygon_points = (self._polygon_points - \
                                    self._reference_point) * scale_factor +\
                                    self._reference_point
            
            # convert back to standard python list for external output
            output = []
            for point in self._polygon_points:
                output.append(list(point))
            return output
    
    class View(object):
        ''' A class for displaying a paramtrically controlled polygon. '''
        
        # valid external bindings used by the class
        valid_bindings = ('set_ref_pt', 'set_poly_pts', 'clear_data',
                          'scale_poly_pts')
        
        def __init__(self, master):
            ''' A class for managing the display of a polygon control GUI.

            Display is split into two panes, as:

                    +--------------------------------+
                    | MENUBAR (file)                 |
                    +-------------+------------------+
                    |   Scale     |                  |
                    |  Controls   |                  |
                    | ___ |scale| |                  |
                    |             |  Polygon Canvas  |
                    |             |                  |
                    |             |                  |
                    |             |                  |
                    |             |                  |
                    +-------------+------------------+


            Constructor: View(tk.Tk)

            '''
            self._master = master
            self._master.title('Parametric Polygon')

            self._master.geometry("{}x{}".format(500,300))
            # set GUI to take up full window height
            self._master.rowconfigure(0, weight=1)
            # set canvas cell to take up extra width
            self._master.columnconfigure(1, weight=1)
            
            self._setup_controls()
            self._setup_canvas()
            self._setup_menubar()
            self._init_bindings()
            self._display_instructions()
            
        def _setup_controls(self):
            ''' Initialises the control pane of the GUI, in its own Frame.

            self._setup_controls() -> None

            '''
            # creation
            control_frame = tk.Frame(self._master)
            self._label = tk.Label(control_frame, text='Scale Controls')
            self._scale = tk.StringVar()
            entry = tk.Entry(control_frame, textvariable=self._scale, width=10)
            button = tk.Button(control_frame, text='Scale',
                               command=self._scale_polygon)

            self._errors = tk.StringVar()
            error_label = tk.Label(control_frame, textvariable=self._errors,
                                   fg='red', wraplength=130, justify=tk.LEFT)

            # geometry management
            control_frame.grid(row=0, column=0, padx=20, pady=5, sticky='n')
            self._label.grid(columnspan=2)
            entry.grid(row=1,column=0)
            button.grid(row=1,column=1)
            error_label.grid(columnspan=2, pady=10)

        def _scale_polygon(self):
            ''' Scales the displayed polygon by the specified value (if valid).

            If there is no polygon available, or no reference point set, or
                scale factor cannot be determined, displays a relevant error
                message.
            
            Scale factor is valid if scaling does not cause any polygon points
                to leave the canvas. Appropriate error message is displayed if
                the current scale factor is invalid.

            Scaling is applied by the external binding referenced by
                'scale_poly_pts'.

            self._scale_polygon() -> None

            '''
            if not self._polygon_set:
                self._errors.set('Cannot scale nonexistant polygon. Click at' +\
                                 ' least 3 polygon points, then double-click' +\
                                 ' to create the polygon.')
                return # do not attempt to scale
            elif not self._ref_pt:
                self._errors.set('Cannot scale with respect to nonexistent ' +\
                                 'reference point.')
                return # do not attempt to scale

            try:
                scale_factor = float(self._scale.get())
            except Exception as e:
                self._errors.set('Failed to extract scale value.\n{}'.format(
                    str(e)))
                return # do not continue

            new_points = self._call_bind_func('scale_poly_pts', scale_factor)
            # check points within canvas
            if self._points_in_canvas(new_points):
                self._poly_pts = new_points
                # config polygon on canvas to new position
                self._draw_polygon()
            else:
                # reset external storage to previous points (unscaled)
                self._call_bind_func('set_poly_pts', self._poly_pts)
                self._errors.set('Current scale factor moves the polygon ' +\
                                 'outside the canvas. Please change the '  +\
                                 'reference point or scale factor and try '+\
                                 'again.')
        
        def _setup_canvas(self):
            ''' Initialises the canvas pane of the GUI, in its own Frame.

            self._setup_canvas() -> None

            '''
            # creation
            canvas_frame = tk.Frame(self._master)
            # set canvas_frame to take up any extra available space
            canvas_frame.rowconfigure(0, weight=1)
            canvas_frame.columnconfigure(0, weight=1)
            self._canvas = tk.Canvas(canvas_frame, bg='snow3')

            # geometry management (RHS, stick to all sides, 2 pixel padding)
            canvas_frame.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')
            self._canvas.grid(sticky='nsew')

            self._startup_state() # set to initial state for startup

        def _startup_state(self):
            ''' Sets the data state to that at startup.

            self._startup_state() -> None

            '''
            self._poly_click_pts = []
            self._poly_pts = []
            self._polygon_set = False
            self._ref_pt = []
            self._mode = 'polygon'

        def _setup_menubar(self):
            ''' Initialises the menubar of the GUI, with a File menu.

            self._setup_menubar() -> None

            '''
            # creation
            menubar = tk.Menu(self._master)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Clear All", command=self._clear_all)

            # add to the menubar
            menubar.add_cascade(label="File", menu=filemenu)

            # display the full menubar
            self._master.config(menu=menubar)

        def _init_bindings(self):
            ''' Initialises internal and external binding functions.

            External binding functions are initialised to do nothing until
                they are externally overwritten.

            Internal canvas bindings are added with desired functionality.

            self._init_bindings() -> None

            '''
            self._bindings = {}
            for binding in View.valid_bindings:
                self._bindings[binding] = lambda: None
            
            self._add_canvas_bindings()

        def _add_canvas_bindings(self):
            ''' Adds the internal canvas bindings.

            self._add_canvas_bindings() -> None

            '''
            self._canvas.bind('<ButtonRelease-1>', lambda e:
                              self._draw_point((e.x,e.y)))
            self._canvas.bind('<Double-Button-1>', lambda e:
                              self._end_polygon())

        def _draw_point(self, pixel_point):
            ''' Draws a point on the canvas at pixel_point, if within canvas.

            If the point is outside the canvas, no point is added and an
                appropriate error message is displayed.

            self._draw_point(list[float,float]) -> None

            '''
            if not self._valid_point(pixel_point):
                self._errors.set('Cannot draw a point outside the canvas')
                return
            
            ppx, ppy = pixel_point # extract coordinates
            if self._mode == 'polygon':
                self._canvas.create_oval(ppx-2, ppy-2, ppx+3, ppy+3,
                                         outline='', fill='red', tags='poly_pt')
                self._poly_pts += [pixel_point]
            else:
                # delete current reference point (if exists)
                if self._ref_pt:
                    pvx, pvy = self._ref_pt # get previous values
                    self._canvas.move('ref', ppx-pvx, ppy-pvy)
                else:
                    self._canvas.create_oval(ppx-2, ppy-2, ppx+3, ppy+3,
                            outline='', fill = 'blue', tags='ref')
                # set the reference point
                self._set_ref_point(pixel_point)

            self._errors.set('')

        def _points_in_canvas(self, points):
            ''' Returns True if all 'points' are within the canvas, else False.

            self._points_in_canvas(list[list[float,float]]) -> bool

            '''
            for point in points:
                if not self._valid_point(point):
                    return False
            return True

        def _valid_point(self, pixel_point):
            ''' Returns True if pixel_point is within the canvas, else False.

            self._valid_point(list[float,float]) -> bool

            '''
            ppx, ppy = pixel_point
            x_max = self._canvas.winfo_width()
            y_max = self._canvas.winfo_height()
            
            if 0 < ppx < x_max and 0 < ppy < y_max:
                return True
            return False

        def _set_ref_point(self, pixel_point):
            ''' Sets the specified pixel_point to the reference point.

            Reference point is the point about which the polygon is scaled.

            self._set_ref_point(list[int,int]) -> None

            '''
            self._ref_pt = pixel_point
            self._call_bind_func('set_ref_pt', pixel_point)

        def _end_polygon(self):
            ''' Ends polygon defining mode, and draws the current points.

            self._end_polygon() -> None

            '''
            if len(self._poly_pts) < 3:
                self._errors.set(
                    'Cannot create polygon with fewer than 3 points.')
                return
            
            self._draw_polygon()
            self._mode = 'ref'

        def _draw_polygon(self):
            ''' Draw the current polygon on the canvas.

            If a polygon already exists, moves it to the new position.

            self._draw_polygon() -> None

            '''
            points = []
            for point in self._poly_pts:
                points += point # needs to be flat (e.g. [x,y,x2,y2,...])
                
            if self._polygon_set:
                self._canvas.coords('polygon', points)
            else:
                self._canvas.create_polygon(points, fill='red', outline='blue',
                                            tags='polygon')
                self._polygon_set = True
            self._call_bind_func('set_poly_pts', self._poly_pts)

            self._errors.set('')

        def _clear_all(self):
            ''' Clear data and reset state to startup.

            self._clear_all() -> None

            '''
            self._startup_state()

            self._canvas.delete('all')
            self._scale.set('')
            self._call_bind_func('clear_data')
            self._display_instructions()

        def _display_instructions(self):
            ''' Display usage instructions on startup.

            self._display_instructions() -> None
            
            '''
            self._errors.set('Click points to make a polygon, then double-' +\
                             'click to complete. Next click a reference '   +\
                             'point to scale about, and change the scale. ' +\
                             'Press the "Scale" button to apply the scale-' +\
                             'factor to the polygon.')

        def _call_bind_func(self, binding, *args, **kwargs):
            ''' Call a binding function with the given arguments.

            Returns the return value of the function, or None if an error is
                raised.

            self._call_bind_func(str, *args) -> None/unknown

            '''
            try:
                return self._bindings[binding](*args, **kwargs)
            except Exception as e:
                self._errors.set(str(e))

        def add_binding_func(self, binding, bind_func):
            ''' Overwrite a binding function's functionality.

            'binding' should be one of the options in View.valid_bindings.
                If not, no binding is set, and an appropriate error message
                is displayed.

            'bind_func' is the function with the new functionality (intended
                for external setting of binding functions).

            self._add_binding_func(str, func) -> None

            '''
            if binding in View.valid_bindings:
                self._bindings[binding] = bind_func
            else:
                self._errors.set('Invalid binding:', binding)

    class Controller(object):
        ''' A class for controlling a parametric polygon GUI. '''
        def __init__(self, master):
            ''' A class for managing a parametric polygon display and model.

            Users select points to define their polygon, then double-click
                to create the polygon and switch to reference selection mode.
                Once a reference is selected, the polygon can be scaled about
                it by a user-specified scaling factor. The reference point can
                be changed between scales, and a File menu provides the option
                to Clear All and reset the GUI. Scaling by a negative factor
                flips the polygon about the reference point. Scaling by 0 turns
                the polygon into the point of no return.

            Could be expanded to include other transformations of the polygon,
                including rotations, skewing, or modifying sides and the
                defining points. Could also include saving/exporting, multiple
                polygons, multiple shapes, and other more complex functionality.

            Constructor: Controller(tk.Tk)

            '''
            self._root = master             # initialise top-level window
            
            self._model = Model()           # initialise empty Model
            self._view = View(self._root)   # initialise View from root

            self._add_bindings()            # link View to Model

        def _add_bindings(self):
            ''' Link the Model functionality to View binding functions.

            self._add_bindings() -> None

            '''
            self._view.add_binding_func('set_ref_pt',
                                        self._model.set_reference_point)
            self._view.add_binding_func('set_poly_pts',
                                        self._model.set_polygon_points)
            self._view.add_binding_func('clear_data',
                                        self._model.clear_data)
            self._view.add_binding_func('scale_poly_pts',
                                        self._model.scale_polygon)
            

    L9 = L9Tests()
    L9.run_tests(verbose=True)  # run tests before running GUI

    # run the GUI
    root = tk.Tk()
    C1 = Controller(root)
    root.mainloop()

    
