from Model import Model
from View import View
import tkinter as tk

class Controller(object):
    ''' A class for controlling a graph-analyser. '''
    def __init__(self, graph_img=None):
        ''' A class for managing a GUI graph-analyser.

        Users select an image of a graph, then identify three points with well-
            defined locations, then add as many points as desired to the graph.
            Both the selected points and the resulting graph image are saveable.
        
        Constructor: Controller.__init__(*str)

        '''
        # initialise data storage
        self._model = Model()

        # initialise display and event bindings
        self._root = tk.Tk() # overarching 'main' window for the application
        self._view = View(self._root, graph_img)
        self._add_bind_functions()

        # turn over the code to event-driven, waiting for user input/actions
        self._root.mainloop() 

    def _add_bind_functions(self):
        ''' Add event binding functions to the View.

        Controller._add_bind_functions(None) -> None

        '''
        self._view.add_binding_func('save_data', self._model.save_data)
        self._view.add_binding_func('clear_data',self._model.clear_data)
        self._view.add_binding_func('new_point', self._model.add_stored_point)
        self._view.add_binding_func('clear_stored_pts',
                                    self._model.clear_stored_points)
        self._view.add_binding_func('set_def_pts',
                                    self._model.set_defining_points)

if __name__ == '__main__':
    C1 = Controller()
