#!/usr/bin/env python3

from Model import Model
from View import View
import tkinter as tk

class Controller(object):
    ''' A class for controlling a graph-analyser. '''
    def __init__(self, master, graph_img=None):
        ''' A class for managing a GUI graph-analyser.

        Users select an image of a graph, then identify three points with well-
            defined locations, then add as many points as desired to the graph.
            The selected points are saveable in a csv format, and the graph
            image is saveable as a PNG image.

        Could be expanded to include zooming, logarithmic axis scaling,
            automatic line detection, saving of state (to reopen where you left
            off), or full automation with automatic axis detection and line
            detection combined.

        Constructor: Controller(tk.Tk, *str)

        '''
        # initialise data storage
        self._model = Model()

        # initialise display and event bindings
        self._root = master # overarching 'main' window for the application
        self._view = View(self._root, graph_img)
        self._add_bind_functions()

    def _add_bind_functions(self):
        ''' Link the Model functionality to View binding functions.

        self._add_bind_functions() -> None

        '''
        self._view.add_binding_funcs(
            save_data        = self._model.save_data,
            clear_data       = self._model.clear_data,
            clear_stored_pts = self._model.clear_stored_points,
            set_def_pts      = self._model.set_defining_points,
            new_point        = self._model.add_stored_point,
            del_point        = self._model.remove_stored_point,
        )


if __name__ == '__main__':
    root = tk.Tk()
    C1 = Controller(root)
    # turn over the code to event-driven, waiting for user input/actions
    root.mainloop()
