import tkinter as tk # GUI library
from tkinter import * # get package constants (e.g. YES, NW, etc)
from tkinter import filedialog # nice file access for opening/saving
from PIL.ImageTk import PhotoImage
from PIL import Image

class View(object):
    ''' A class for a graph-analysis GUI. '''

    MODE = {'define':{'func':'set_def_pts','cursor':'circle'},
            'add':{'func':'new_point','cursor':'crosshair'},
            'delete':{'func':'','cursor':'draped_box'}}
    
    def __init__(self, master, graph_img=None):
        ''' A class for managing the display of a graph-analysis GUI.

        Constructor: View(tk.Tk/tk.Frame, *str)

        '''
        self._init_master(master)       # initialise the master window
        self._init_binding_options()    # initialise event binding options
        self._setup_display()           # set up the blank display
        self._set_img(graph_img)        # initialise (or get) graph image
        self._add_event_bindings()      # add (non-button) event bindings

    def _init_master(self, master):
        ''' Initialises the master container of this.

        View._init_master(tk.frame/tk.Tk/tk.window) -> None

        '''
        self._master = master # set the overarching master of the view
        self._master.title("Data From Graph") # set a title for the view
        
        # set the window to be the full size of the screen
        sw = self._master.winfo_screenwidth()
        sh = self._master.winfo_screenheight()
        self._master.geometry("{}x{}".format(sw*2//3,sh*2//3))
        
        # turn off resizing in the x and y directions
        self._master.resizable(0, 0)
        
        # make GUI as tall as window
        self._master.rowconfigure(0, weight=1)

    def _setup_display(self):
        ''' Initialises the display as blank, with relevant widgets.

        Display is split into two panes, as:

                +-------------------------+
                | MENUBAR (file/edit)     |
                +---------------+---------+
                |               |         |
                |               | def_pts |
                |               | ------- |
                |  graph image  |  add_pt |
                |               |  del_pt |
                |               | clr_pts |
                |               |         |
                +---------------+---------+
                
        View._setup_display() -> None

        '''
        self._setup_graph()
        self._setup_controls()
        self._setup_menubar()
        self._master.update()

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
        #   (no options -> column=0, row=next available)
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
        control_frame.grid(row=0,column=1)
        def_pt_frame.grid(ipady=10) # vertical padding inside the frame
        # add the defining points controls
        self._setup_def_pt_controls(def_pt_frame)

        # add the control buttons under the defining points controls
        self._setup_control_buttons(control_frame)

    def _setup_def_pt_controls(self, master):
        ''' '''
        # create a heading label and a frame for the defining points
        heading = tk.Label(master, text='Set Defining Points')
        grid_frame = tk.Frame(master)

        # pack the heading and frame into the control frame grid
        heading.grid()
        grid_frame.grid()
        
        self._graph_pt_entries = []
        for r in range(3):
            # set up some variables to easily extract Entry values later
            xr = StringVar();           yr = StringVar()
            xr.set('x{}'.format(r));    yr.set('y{}'.format(r))
            
            # create "Def Pt r (_,_)"
            a = tk.Label(grid_frame, text='Def Pt {} ('.format(r))
            x_entry = tk.Entry(grid_frame, textvariable=xr, width=7)
            b = tk.Label(grid_frame, text=',')
            y_entry = tk.Entry(grid_frame, textvariable=yr, width=7)
            c = tk.Label(grid_frame, text=')')

            # put widgets into grid_frame grid
            a.grid(row=r, column=0)
            x_entry.grid(row=r, column=1)
            b.grid(row=r,column=2)
            y_entry.grid(row=r,column=3)
            c.grid(row=r,column=4)

            # store entries for later access
            self._graph_pt_entries.append([xr,yr])
        

    def _setup_control_buttons(self, master):
        ''' '''
        tk.Button(master, text='Add Graph Points', width=20,
                  command=lambda:self._change_mode_to('add')).grid(pady=5)
        tk.Button(master, text='Delete Graph Points', width=20,
                  command=lambda:self._change_mode_to('delete')).grid(pady=5)
        tk.Button(master, text='Clear Graph Points', width=20,
                  command=lambda:self._call_bind_func('clear_stored_pts')
                  ).grid(pady=5)

    def _setup_menubar(self):
        ''' Initialises the menubar with the desired menus.

        View._setup_menubar() -> None

        '''
        pass

    def _set_img(self, graph_img=None):
        ''' '''
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
        # add the image to the canvas
        self._graph_canvas.create_image(0, 0, image=self._img, anchor=NW)

    def _change_mode_to(self, mode):
        ''' '''
        self._mode = View.MODE[mode]['func']
        self._graph_canvas.config(cursor=View.MODE[mode]['cursor'])

    def _init_binding_options(self):
        ''' '''
        # Initialise bindings to do nothing if called
        self._bindings = {}
        for binding in (View.get_valid_bindings() + ['']):
            self._bindings[binding] = lambda *args, **kwargs: None

        self._mode = ''

    def _add_event_bindings(self):
        ''' '''
        self._graph_canvas.bind('<ButtonRelease-1>', lambda event:
                                self._graph_click_release(event))

    def _graph_click_release(self, event):
        ''' Respond appropriately to the mouse-click release on the graph.

        self._mode:
            ADD_MODE -> add a stored point at (event.x, event.y)
            DEFINING_MODE -> add a defining point at (event.x, event.y)
            PASSIVE_MODE -> do nothing
        
        View._graph_click_release(event) -> None

        '''
        pixel_point = (event.x, event.y)
        self._bindings[self._mode](pixel_point)
        #self._call_bind_func(self._mode, pixel_point)
        pass # ADD IN VIEW AS WELL (not just model)

    def _call_bind_func(self, binding, *args):
        ''' Call a binding function with the given arguments.

        Model._call_bind_func(str, *args) -> None

        '''
        self._bindings[binding](*args)

    def add_binding_func(self, binding, callback):
        ''' Adds the specified callback to the given binding, if valid.

        A valid binding must be in the list returned by
            View.get_valid_bindings().

        Raises Exception on invalid binding.

        View.add_binding_func(str, func) -> None

        '''
        if binding in View.get_valid_bindings():
            self._bindings[binding] = callback
        else:
            raise Exception('Invalid binding option {} -'.format(binding),
                            'Valid bindings are found using ',
                            'View.get_valid_bindings()')

    def save_graph(self):
        ''' Saves the current view of the graph as an image.

        User is internally requested to select a save location.

        View.save_graph() -> None

        '''
        """
        filename =  tk.filedialog.asksaveasfilename(initialdir = "/",
                title = "Save graph as", filetypes = (("jpeg files","*.jpg"),
                                                      ("all files","*.*")))
        """
        filename =  tk.filedialog.asksaveasfilename(title = "Save graph as",
                filetypes = (("JPEG image","*.jpg"), ("PNG image","*.png"),
                             ("All Files","*.*")))
        View.snapshot(self._graph_canvas, filename)

    @staticmethod
    def snapshot(widget, filename):
        ''' Saves a screen clipping of the specified widget to filename.

        Code from B.Jenkins response on stackoverflow.com/questions/9886274
        Comments added separately.

        View.snapshot(tk.widget, str) -> None

        '''
        # determine minimum bounds of widget
        x = root.winfo_rootx() + widget.winfo_x()
        y = root.winfo_rooty() + widget.winfo_y()
        # determine maximum bounds of widget
        x1 = x + widget.winfo_width()
        y1 = y + widget.winfo_height()
        # take screenshot, crop to widget extent, and save as filename
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

    @staticmethod
    def get_valid_bindings():
        ''' Returns the list of valid bindings used by the class.

        View.get_valid_bindings() -> list[str]
        
        '''
        return ['save_data', 'clear_data', 'clear_stored_pts',
                'set_def_pts', 'new_point']
