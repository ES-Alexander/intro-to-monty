#!/usr/bin/env python3

# library imports
import tkinter as tk # GUI library
from tkinter import * # get package constants (e.g. YES, NW, etc)
from tkinter import filedialog # nice file access for opening/saving
# Python Image Library (Pillow)
from PIL.ImageTk import PhotoImage # more image format support (jpg,png,...)
from PIL import Image, ImageGrab # resizeable images, screenshots
# platform dependence
from os import sys

class View(object):
    ''' A class for a graph-analysis GUI. '''

    # cursor options for each internal mode
    CURSOR = {'define':'circle', 'add':'crosshair', 'delete':'draped_box'}
    # the set of valid external bindings used in the class
    _external_bindings = ['save_data', 'clear_data', 'clear_stored_pts',
                          'set_def_pts', 'new_point', 'del_point']
    
    def __init__(self, master, graph_img=None):
        ''' A class for managing the display of a graph-analysis GUI.

        Constructor: View(tk.Tk/tk.Frame, *str)

        '''
        self._init_master(master)       # initialise the master window
        self._init_binding_options()    # initialise event binding options
        self._setup_display()           # set up the blank display
        self._set_img(graph_img)        # initialise (or get) graph image
        self._add_event_bindings()      # add (non-button) event bindings
        self._display_instructions()    # display usage instructions

    def _init_master(self, master):
        ''' Initialises the master container of this.

        View._init_master(tk.Tk/tk.Frame) -> None

        '''
        self._master = master # set the overarching master of the view
        self._master.title("Data From Graph") # set a title for the view
        
        # set the window to be 2/3 of the full size of the screen (int division)
        sw = self._master.winfo_screenwidth()
        sh = self._master.winfo_screenheight()
        self._master.geometry("{}x{}".format(sw*2//3,sh*2//3))
        
        # turn off resizing in the x and y directions
        self._master.resizable(0, 0)
        
        # make GUI as tall as window
        self._master.rowconfigure(0, weight=1)

    def _init_binding_options(self):
        ''' Initialises all bindings.

        External bindings are set to do nothing if called.

        View._init_binding_options() -> None

        '''
        self._bindings = {}
        for binding in (View.get_external_bindings() + ['']):
            self._bindings[binding] = lambda *args, **kwargs: None

        self._bindings['define'] = lambda pp: self._add_def_point(pp)
        self._bindings['add'] = lambda pp: self._add_stored_point(pp)
        self._bindings['delete'] = self._delete_point

    def _change_mode_to(self, mode):
        ''' Changes the interaction mode to that specified, for stored points.

        Includes changing the cursor when over the graph canvas.

        'mode' can validly be 'define', 'add', or 'delete'.

        View._change_mode_to(str) -> None

        '''
        self._mode = mode
        self._graph_canvas.config(cursor=View.CURSOR[mode])

    def _setup_display(self):
        ''' Initialises the display as blank, with relevant widgets.

        Display is split into two panes, as:

                +-------------------------+
                | MENUBAR (file/edit)     |
                +---------------+---------+
                |               | def_pts |
                |               | ------- |
                |               | add_pt  |
                |  graph image  | del_pt  |
                |               | clr_pts |
                |               | ------- |
                |               | errors  |
                +---------------+---------+
                
        View._setup_display() -> None

        '''
        self._setup_graph()
        self._setup_controls()
        self._setup_menubar()

    def _setup_graph(self):
        ''' Initialises the graph canvas in its own frame.

        Provides an example of basic usage of 'grid' geometry management.

        View._setup_graph() -> None

        '''
        # create a frame for the graph canvas, in the master window
        graph_frame = tk.Frame(self._master)
        self._master.columnconfigure(0, weight=1)
        graph_frame.rowconfigure(0, weight=1)
        graph_frame.columnconfigure(0, weight=1)
        # create the graph canvas, inside the graph frame
        self._graph_canvas = tk.Canvas(graph_frame, bg='gray')

        # put the graph frame and canvas into their grids
        #   (default: column=0, row=next available)
        #   (sticky to all 4 sides -> stretch widget as much as possible)
        graph_frame.grid(sticky=N+S+E+W)
        self._graph_canvas.grid(sticky=N+S+E+W)

    def _setup_controls(self):
        ''' Initialises the controls in their own frame.

        View._setup_controls() -> None

        '''
        # create a frame for the controls
        control_frame = tk.Frame(self._master)
        # create a frame for the defining points controls
        def_pt_frame = tk.Frame(control_frame)

        # put the controls frames in their grids
        # control frame sticks to the top (north), with 10 pixels of external
        #   vertical padding (on top and bottom)
        control_frame.grid(row=0, column=1, pady=10, sticky=N)
        def_pt_frame.grid(ipady=10) # vertical padding inside the frame
        # add the defining points controls
        self._setup_def_pt_controls(def_pt_frame)

        # add the control buttons under the defining points controls
        self._setup_control_buttons(control_frame)

        # add the error window
        self._setup_error_window(control_frame)

    def _setup_def_pt_controls(self, master):
        ''' Initialises the defining-point controls.

        View._setup_def_pt_controls(tk.Tk/tk.Frame) -> None

        '''
        # create a heading label and a frame for the defining points
        heading = tk.Label(master, text='Set Defining Points')
        grid_frame = tk.Frame(master)

        # pack the heading and frame into the control frame grid
        heading.grid()
        grid_frame.grid()

        self._def_pt_controls = {}
        for point_id in range(3):
            self._def_pt_controls[point_id] = DefPointControl(grid_frame,
                                                              point_id)
            self._def_pt_controls[point_id].set_view_select(self._def_pt_select)
            self._def_pt_controls[point_id].set_view_submit(self._def_pt_submit)

    def _def_pt_select(self, index):
        ''' Set the defining point with given index as selected.

        'index' can be 0, 1, or 2.

        View._def_pt_select(int) -> None

        '''
        # update view state
        self._change_mode_to('define')
        self._dpid = index

        # update relevant controls
        self._def_pt_controls[index].select()

    def _def_pt_submit(self, index):
        ''' Set the defining point with given index as submitted.

        'index' can be 0, 1, or 2.

        View._def_pt_submit(int) -> None

        '''
        # check if valid time to submit this def point
        if not self._graph_canvas.find_withtag('dpid{}'.format(index)):
            self._errors.set('Please set a defining point location on the ' +
                             'graph before submitting')
            return # invalid starting point - do not continue
        
        # update controls
        self._def_pt_controls[index].submit()
        
        # check if all 3 points defined (ready to submit to external Model)
        currently_defined = self._graph_canvas.find_withtag('define')
        if len(currently_defined) == 3:
            # all points are defined
            self._def_pts_submit_external() # submit def points
            self._change_mode_to('add')     # change to add mode
        else:
            # one or more def points undefined -> set to edit for next def point
            index = (index + 1) % 3 # get the next def point (0->1,1->2,2->0)
            self._def_pt_select(index)

    def _def_pts_submit_external(self):
        ''' Submit the defining points to the external data (Model).

        All 3 defining points need to be specified.

        View._def_pts_submit_external() -> None

        '''
        def_pts_mapping = {}
        for point in range(3):
            pid = self._graph_canvas.find_withtag('dpid{}'.format(point))[0]
            point_coords = self._graph_canvas.coords(pid)
            # extract pixel center value from oval coords
            pixel_point = (int(point_coords[0])+2, int(point_coords[1])+2)
            gp_data = self._def_pt_controls[point].entry_vals
            try:
                # attempt to get meaningful data out of user specified
                #   graph points (from entries)
                graph_point = (float(gp_data[0].get()),
                               float(gp_data[1].get()))
            except Exception as e:
                self._errors.set(
                    'Def point {} caused the error:\n'.format(point)+\
                    str(e))
                return
            def_pts_mapping[pixel_point] = graph_point
        # submit points to external data storage
        self._call_bind_func('set_def_pts', def_pts_mapping)

    def _reset_def_points(self):
        ''' Reset the defining point controls, and 'select' the first.

        View._reset_def_points() -> None

        '''
        # reset controls
        for point in range(3):
            self._def_pt_controls[point].reset()
            
        # set to defining first def pt
        self._def_pt_select(0)
        
    def _setup_control_buttons(self, master):
        ''' Initialises the stored-points control buttons.

        Adds 'Add/Move Graph Points', 'Delete Graph Points', and
            'Clear Graph Points' buttons to the control panel.

        Provides an example of anonymous widgets put in their grid at
            definition. Reminder: only anonymous widgets can be put in position
            in their definition statement.

        View._setup_control_buttons(tk.Tk/tk.Frame) -> None

        '''
        button_width = 20
        tk.Button(master, text='Add/Move Graph Points', width=button_width,
                  command=lambda:self._change_mode_to('add')).grid(pady=5)
        tk.Button(master, text='Delete Graph Points', width=button_width,
                  command=lambda:self._change_mode_to('delete')).grid(pady=5)
        # only use a lambda function if you need to pass arguments
        tk.Button(master, text='Clear Graph Points', width=button_width,
                  command=self._clear_stored_points).grid(pady=5)

    def _setup_error_window(self, master):
        ''' Initialises a window for error display, with red text.

        View._setup_error_window(tk.Tk/tk.Frame) -> None

        '''
        self._errors = StringVar() # variable to set the text
        self._errors.set('')
        tk.Label(master, textvariable=self._errors, fg='red', justify=tk.LEFT,
                 wraplength=200).grid(pady=10)
        
    def _setup_menubar(self):
        ''' Initialises the menubar with the desired menus.

        View._setup_menubar() -> None

        '''
        # create an overarching menubar
        self._menubar = tk.Menu(self._master)

        # create some dropdown menus
        self._setup_filemenu()
        self._setup_editmenu()
        self._setup_helpmenu()

        # display the full menubar
        self._master.config(menu=self._menubar)

    def _setup_filemenu(self):
        ''' Initialises the dropdown File menu.

        Adds options to select a graph image, save the stored data, and exit
            the application.

        View._setup_filemenu() -> None

        '''
        filemenu = tk.Menu(self._menubar, tearoff=0)
        filemenu.add_command(label="Select Graph", command=self._set_img)
        filemenu.add_separator() # add a separation line (denote sections)
        filemenu.add_command(label="Save Data", command=self._save_data)
        filemenu.add_command(label="Save Graph", command=self._save_graph)
        
        # add to the menubar
        self._menubar.add_cascade(label="File", menu=filemenu)

    def _setup_editmenu(self):
        ''' Initialises the dropdown Edit menu.

        Adds the option to clear the user-specified data points.

        View._setup_editmenu() -> None

        '''
        editmenu = tk.Menu(self._menubar, tearoff=0)
        editmenu.add_command(label="Clear Data", command=self._clear_data)
        # add to the menubar
        self._menubar.add_cascade(label="Edit", menu=editmenu)

    def _setup_helpmenu(self):
        ''' Initialises the dropdown Help menu.

        Adds the option to re-display the initial instructions.

        View._setup_helpmenu() -> None

        '''
        helpmenu = tk.Menu(self._menubar, tearoff=0)
        helpmenu.add_command(label="Display Instructions",
                             command=self._display_instructions)
        # add to the menubar
        self._menubar.add_cascade(label="Help", menu=helpmenu)

    def _set_img(self, graph_img=None):
        ''' Sets the current graph image.

        Opens a file dialog if graph_img unspecified.

        View._set_img(*str) -> None

        '''
        # get image filename if necessary
        if not graph_img:
            graph_img =  tk.filedialog.askopenfilename(
                    title = "Select graph image",
                    filetypes = (("JPEG image","*.jpg"), ("PNG image","*.png"),
                                 ("All Files","*.*")))
        
        img = Image.open(graph_img) # extract image as PIL Image
        # scale image to take up the full canvas (stretching is fine)
        size = (self._graph_canvas.winfo_width(),
                self._graph_canvas.winfo_height())
        resized = img.resize(size, resample=Image.BILINEAR)
        # convert to tkinter PhotoImage, store externally to make visible
        self._img = PhotoImage(resized)
        
        # add the image to the canvas (modify existing if possible)
        canvas_image = self._graph_canvas.find_withtag('graph_image')
        if canvas_image:
            self._graph_canvas.itemconfig(canvas_image[0],image=self._img)
        else:
            self._graph_canvas.create_image(0, 0, image=self._img, anchor=NW,
                                            tags='graph_image')
        
        # new graph specified, so re-initialise data and view
        self._clear_data()          # clear all data
        self._reset_def_points()    # reset defining points controls

    def _save_data(self, filename=None):
        ''' Saves the graph points to a csv format.

        Prompts the user for a filename if not provided.

        View._save_data(*str) -> None

        '''
        if not filename:
            filename = tk.filedialog.asksaveasfilename(title = "Save Data As",
                filetypes = (("Comma Separated Value","*.csv"),
                             ("All Files","*.*")))
        
        self._call_bind_func('save_data', filename)

    def _clear_data(self):
        ''' Clears all data from the graph display and model.

        View._clear_data() -> None
        
        '''
        self._graph_canvas.delete('point') # delete all view points
        self._call_bind_func('clear_data') # clear external point data
        self._reset_def_points()           # reset defining points controls

    def _clear_stored_points(self):
        ''' Clears the stored points from the graph display and model data.

        Does not clear the defining points.

        View._clear_stored_points() -> None

        '''
        self._call_bind_func('clear_stored_pts') # clear external data

        # delete all points with tag 'stored'
        self._graph_canvas.delete('stored')

    def _clear_defining_points(self):
        ''' Clears the defining points from the graph display.

        View._clear_defining_points() -> None

        '''
        # delete all points with tag 'define'
        self._graph_canvas.delete('define') 

    def _add_stored_point(self, pixel_point):
        ''' Add a new stored point to the external data and the graph.

        If adding to the external data (Model) fails, does not add to the graph.

        View._add_stored_point(tuple(int,int)) -> None

        '''
        # check if point can be added (try adding to external data)
        point_added = self._call_bind_func('new_point', pixel_point)
        
        if point_added:
            self._draw_point(pixel_point, {'outline':'','fill':'blue',
                                           'tags':('stored','point')})

    def _add_def_point(self, pixel_point):
        ''' Add a new defining point to the graph.

        Pre-existing points are overwritten and moved to the new location.

        View._add_def_point(tuple(int,int)) -> None

        '''
        dpid_tag = 'dpid{}'.format(self._dpid) # get the current defining point
        self._graph_canvas.delete(dpid_tag) # remove previous placements
        # draw the new point on the view
        self._draw_point(pixel_point, {'outline':'','fill':'red',
                'tags':('define',dpid_tag,'point')})

    def _draw_point(self, pixel_point, properties):
        ''' Draw a point on the graph canvas with the given properties.

        'pixel_point' should be (x,y) coordinates of the point
        'properties' should be a dictionary of desired properties of the point

        View._draw_point(tuple(int,int), dict) -> 

        '''
        ppx, ppy = pixel_point # extract coordinates
        self._graph_canvas.create_oval(ppx-2, ppy-2, ppx+3, ppy+3, **properties)

    def _delete_point(self, pixel_point, max_dist=5):
        ''' Deletes the point nearest pixel_point, if within max_dist.

        'pixel_point' should be (x,y) coordinates of the point

        View._delete_point(tuple(int,int), *float) -> None

        '''
        if not self._graph_canvas.find_withtag('stored'):
            # no stored points defined
            return
        
        # remove the point from the external data storage
        point_removed = self._call_bind_func('del_point', pixel_point, max_dist)
        
        if point_removed:
            # if a point was removed, it must satisfy the max_dist condition,
            #   so remove the closest point (to pixel_point) from the view
            ppx, ppy = pixel_point
            gc = self._graph_canvas
            gc.delete(gc.find_enclosed(ppx-max_dist, ppy-max_dist,
                                       ppx+max_dist, ppy+max_dist))

    def _save_graph(self):
        ''' Saves the current view of the graph as an image.

        User is internally requested to select a save location.

        View._save_graph() -> None

        '''
        filename = tk.filedialog.asksaveasfilename(title="Save graph as",
                filetypes=(("PNG image","*.png"),("All Files","*.*")))
        self._master.update_idletasks() # update winfo values for snapshot
        View.snapshot(self._graph_canvas, filename)

    def _add_event_bindings(self):
        ''' Adds the non-button event bindings.

        View._add_event_bindings() -> None

        '''
        self._graph_canvas.bind('<ButtonPress-1>', lambda event:
                                self._graph_click(event))
        # respond to a mouse release depending on current mode (self._mode)
        self._graph_canvas.bind('<ButtonRelease-1>', lambda e:
                                self._call_bind_func(self._mode, (e.x,e.y)))

    def _graph_click(self, event):
        ''' Respond to a graph click (press) depending on mode (self._mode).

        If mode is 'add', deletes the closest point if within a small range
                -> effective move behaviour

        View._graph_click(tk.Event) -> None

        '''
        if self._mode == 'add':
            pixel_point = (event.x, event.y)
            self._delete_point(pixel_point)
        
    def _call_bind_func(self, binding, *args):
        ''' Call a binding function with the given arguments.

        Returns the return value of the function, or None if an error is raised.

        Model._call_bind_func(str, *args) -> None/unknown

        '''
        try:
            self._errors.set('')                    # clear error display
            return self._bindings[binding](*args)   # run the function
        except Exception as e:
            self._errors.set(str(e))                # display error if occurs
            return None

    def _display_instructions(self):
        ''' Display usage instructions on startup.

        View._display_instructions() -> None
        
        '''
        instructions = 'Choose 3 defining points which specify the plane ' +\
            'your graph is on (click to select point location, then specify ' +\
            'where the point is before pressing submit). Then add additional' +\
            ' points at the locations that you wish to export, before ' +\
            'pressing File/Save Data or File/Save Graph to save.'
        self._errors.set(instructions)

    def add_binding_func(self, binding, callback):
        ''' Adds the specified callback to the given binding, if valid.

        A valid binding must be in the list returned by
            View.get_external_bindings().

        Raises Exception on invalid binding.

        View.add_binding_func(str, func) -> None

        '''
        if binding in View.get_external_bindings():
            self._bindings[binding] = callback
        else:
            raise Exception('Invalid binding option {!r} -'.format(binding),
                            'Valid bindings are found using ',
                            'View.get_external_bindings()')

    @classmethod
    def _get_valid_bindings(cls):
        ''' Returns the list of valid bindings used by the class.

        View._get_valid_bindings() -> list[str]
        
        '''
        return cls.get_external_bindings() + cls._get_internal_bindings()

    @classmethod
    def _get_internal_bindings(cls):
        ''' Returns the list of valid internal bindings used by the class.

        View._get_internal_bindings() -> list[str]

        '''
        return list(cls.CURSOR.keys())

    @classmethod
    def get_external_bindings(cls):
        ''' Returns the list of valid external bindings used by the class.

        View.get_external_bindings() -> list[str]
        
        '''
        return cls._external_bindings[:]

    @staticmethod
    def snapshot(widget, filename, scale=None):
        ''' Save a screen clipping of the specified widget to filename.

        For some reason tkinter halves my screen resolution in its calculations,
            so scaling is necessary. Modify if your graph saving isn't scaled
            correctly.

        View.snapshot(tk.widget, str, *float) -> None

        '''
        if scale is None:
            platform = sys.platform
            if platform == 'darwin':
                scale = 2 # computer is a mac
            else:
                scale = 1 # assume everything is fine
                
        # determine minimum bounds of widget
        x_min = widget.winfo_rootx() * scale
        y_min = widget.winfo_rooty() * scale
        # determine maximum bounds of widget
        x_max = x_min + widget.winfo_width() * scale
        y_max = y_min + widget.winfo_height() * scale
        # take screenshot, crop to widget extent, and save as filename
        save_image = ImageGrab.grab(bbox=(x_min,y_min,x_max,y_max))

        try:
            save_image.save(filename)
        except Exception:
            save_image.save(filename + '.png')
            

class DefPointControl(object):
    ''' A class for a defining point control in a View. '''
    def __init__(self, master, r):
        ''' A class for the widgets to control a defining point in a View.

        'r' is the row/point ID of the defining point being controlled.

        Constructor: DefPointControl(tk.Tk/tk.Frame, int)

        '''
        self._id = r
        # initialise external functinos to do nothing until set externally
        self._view_submit = lambda: None
        self._view_select = lambda: None
        
        # set up some variables to easily extract Entry values later
        xr = StringVar();           yr = StringVar()
        xr.set('x{}'.format(r));    yr.set('y{}'.format(r))
        
        # create "Def Pt r (_,_)"
        self._button = tk.Button(master, text='Def Pt {}'.format(r), width=9,
                                 command=lambda: self._view_select(self._id))
        a = tk.Label(master, text='(')
        x_entry = tk.Entry(master, textvariable=xr, width=7,
                           state='disabled')
        b = tk.Label(master, text=',')
        y_entry = tk.Entry(master, textvariable=yr, width=7,
                           state='disabled')
        c = tk.Label(master, text=')')

        # put widgets into grid_frame grid
        for col,widget in enumerate([self._button, a, x_entry, b, y_entry, c]):
            widget.grid(row=r, column=col)

        # store entries for later access
        self._entries = [x_entry, y_entry]
        self.entry_vals = [xr, yr]

    def set_view_submit(self, submit_func):
        ''' Sets the external submit function for this defining point.

        DefPointControl.set_view_submit(func) -> None

        '''
        self._view_submit = submit_func

    def set_view_select(self, select_func):
        ''' Sets the external select function for this defining point.

        DefPointControl.set_view_select(func) -> None

        '''
        self._view_select = select_func

    def select(self):
        ''' The internal select function for this defining point.

        Updates the relevant widgets to be in selected mode.

        DefPointControl.select() -> None

        '''
        # update button and entries to be in edit mode for this def pt
        self._button.config(text='Submit',
                            command=lambda: self._view_submit(self._id))
        for entry in self._entries:
            entry.config(state='normal')
        self._entries[0].focus() # set the focus to the first entry

    def submit(self):
        ''' The internal submit function for this defining point.

        Updates the relevant widgets to be in submitted mode.

        DefPointControl.submit() -> None

        '''
        self._button.config(text='Edit',
                            command=lambda: self._view_select(self._id))
        for entry in self._entries:
            entry.config(state='disabled')
            
    def reset(self):
        ''' The internal reset function for this defining point.

        Updates the relevant widgets to be in default mode.

        DefPointControl.reset() -> None

        '''
        self._button.config(text='Def Pt {}'.format(self._id),
                            command=lambda: self._view_select(self._id))
        xy = ['x','y']
        for entry in range(2):
            self.entry_vals[entry].set('{}{}'.format(xy[entry], self._id))
            self._entries[entry].config(state='disabled')
