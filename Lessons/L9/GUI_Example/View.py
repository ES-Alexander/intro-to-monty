import tkinter as tk
from PIL import ImageGrab

class View(object):
    ''' A class for a graph-analysis GUI. '''
    def __init__(self, graph_img=None):
        ''' A class for managing the display of a graph-analysis GUI.

        Constructor: View([image filename])

        '''
        root = tk.Tk()
        
