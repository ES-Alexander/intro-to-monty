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
        self._controller = Controller(self._root)
        self._widgets = L9Tests.get_children(self._root)
                
        super().run_tests(*args, **kwargs)
        self._root.destroy()

    def _clear_root(self):
        ''' Clears all widgets from self._root. '''
        for widget in self._root.winfo_children():
            widget.destroy()

    @staticmethod
    def get_children(widget):
        ''' Get the top_level children in this widget in a dict of class. '''
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
    def test_top_level_widgets(self):
        ''' '''
        assert len(self._widgets['Frame']) >= 2, \
               "Both the Canvas and Controls should have their own Frames."
        assert len(self._widgets['Menu']) >= 1, \
               "A Menubar should be made, with a File menu included."

    def test_menubar(self):
        ''' '''
        menubar = self._widgets['Menu']

        # check 'File' cascade exists
        file_cascade = None
        for menu_item in menubar:
            item_type = menu_item.type(0)
            label = menu_item.entrycget(0, 'label')
            if  item_type == 'cascade' and label == 'File':
                file_cascade = menu_item
        assert file_cascade is not None, "Menubar should include a 'File' menu."

        # check 'Clear All' command exists
        clear_command = None
        filemenu = L9Tests.get_children(file_cascade)['Menu']
        for menu_item in filemenu:
            item_type = menu_item.type(0)
            label = menu_item.entrycget(0, 'label')
            if item_type == 'command' and label == 'Clear All':
                clear_command = menu_item
        assert clear_command is not None, \
               "File menu should include a 'Clear All' command."

    def test_canvas_frame(self):
        ''' '''
        frames = self._widgets['Frame']

        # check Frame in column 1 contains a Canvas (frame on the right)
        for frame in frames:
            contents = L9Tests.get_children(frame)
            col = frame.grid_info()['column']
            if col == 1 and 'Canvas' in contents:
                return

        assert False, \
               "The Frame in column 1 should contain a Canvas element."

    def test_control_frame(self):
        ''' '''
        frames = self._widgets['Frame']

        # check frame in column 0 contains the controls (frame on the left)
        for frame in frames:
            contents = L9Tests.get_children(frame)
            col = frame.grid_info()['column']
            # initialise checks for this frame
            valid_label = False
            valid_button = False
            if col == 0:
                # assume we have the Controls frame
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
                    
        assert False, \
               "The Frame in column 0 should contain your controls, which " +\
               "should include a Label with text 'Scale Controls', an Entry " +\
               "for entering the scale, a Button for submitting the scale, " +\
               "and a Label for the display of instructions and errors."

    def test_master_title(self):
        ''' '''
        assert self._root.title() == 'Parametric Polygon', \
               "Title of the master window should be 'Parametric Polygon'."
                
        


#------------------------------ Example Solution ------------------------------#

if __name__ == '__main__':
    import random
    import numpy as np

    class Model(object):
        ''' '''
        def __init__(self):
            ''' '''
            self._polygon_points = np.array([])
            self._reference_point = np.array([])

        def set_polygon_points(self, points):
            ''' '''
            self._polygon_points = np.array(points)

        def set_reference_point(self, point):
            ''' '''
            self._reference_point = np.array(point)

        def clear_data(self):
            ''' '''
            self.set_polygon_points([])
            self.set_reference_point([])

        def scale_polygon(self, scale_factor):
            ''' '''
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
        # class variables
        SELECT_SCALE_POINT = 'ssp'
        valid_bindings = ['set_ref_pt', 'set_poly_pts', 'clear_data',
                          'scale_poly_pts']
        
        def __init__(self, master):
            self._master = master
            self._master.title('Parametric Polygon')
            
            self._setup_controls()
            self._setup_canvas()
            self._setup_menubar()
            self._init_bindings()
            
        def _setup_controls(self):
            # creation
            control_frame = tk.Frame(self._master)
            self._label = tk.Label(control_frame, text='Scale Controls')
            self._entry = tk.StringVar()
            self._entry.set('Scale Value')
            entry = tk.Entry(control_frame, textvariable=self._entry)
            button = tk.Button(control_frame, text='Scale',
                               command=self._scale_polygon)

            self._errors = tk.StringVar()
            error_label = tk.Label(control_frame, textvariable=self._errors)

            # geometry management
            control_frame.grid(row=0, column=0)
            self._label.grid()
            entry.grid()
            button.grid()
            error_label.grid()

        def _scale_polygon(self):
            ''' '''
            pass
        
        def _setup_canvas(self):
            # creation
            canvas_frame = tk.Frame(self._master)
            self._canvas = tk.Canvas(canvas_frame)

            # geometry management
            canvas_frame.grid(row=0,column=1)
            self._canvas.grid()
            
        def _change_mode(self, new_mode):
            ''' '''
            self._mode = new_mode   

        def _setup_menubar(self):
            # creation
            menubar = tk.Menu(self._master)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Clear All", command=self._clear_all)

            # add to the menubar
            menubar.add_cascade(label="File", menu=filemenu)

            # display the full menubar
            self._master.config(menu=menubar)

        def _init_bindings(self):
            ''' '''
            self._bindings = {}
            for binding in View.valid_bindings:
                self._bindings[binding] = lambda: None

        def _add_canvas_bindings(self):
            ''' '''
            pass

        def _set_ref_point(self):
            '''  '''
            pass

        def _set_polygon_points(self):
            ''' '''
            pass

        def _clear_all(self):
            ''' '''
            pass

        def _call_bind_func(self, binding, *args, **kwargs):
            ''' '''
            try:
                self._bindings[binding](*args, **kwargs)
            except Exception as e:
                self._errors.set(str(e))

        def add_binding_func(self, binding, bind_func):
            ''' '''
            if binding in View.valid_bindings:
                self._bindings[binding] = bind_func
            else:
                self._errors.set('Invalid binding:', binding)

    class Controller(object):
        ''' '''
        def __init__(self, master):
            self._root = master             # initialise top-level window
            
            self._model = Model()           # initialise empty Model
            self._view = View(self._root)   # initialise View from root

            self._add_bindings()            # link View to Model

        def _add_bindings(self):
            ''' '''
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

    
