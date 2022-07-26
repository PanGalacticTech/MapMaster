'''
MapMaster User Interface Elements


'''



import tkinter as tk

import tkinter.font as TkFont


#USER COLOURS:
DARK_GREY = "#212121"
FEATURE_GREY = "#666666"
LIGHT_GREY = "#e6e6e6"
TEXT_GREY = "#eeeeee"
BG_GREY = "#303030"
ACTIVE_BLUE = "#09dceb"
YELLOW_ORANGE = "#e8b60e"


#USER FONTS




#UI ELEMENTS
class darkFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Frame.__init__(self, master, bg=DARK_GREY, relief="ridge", bd=2, **kwargs)

