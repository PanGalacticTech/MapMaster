'''
MapMaster Graphical User Interface

Using Tkinter

'''


import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
import UI_elements as UE


#USER VARIABLES:
MAIN_WINDOW_TITLE = "MapMaster - Dungeon Master Manager"

MAIN_WINDOW_WIDTH = "1400"
MAIN_WINDOW_HEIGHT = "800"
MAIN_WINDOW_BACKGROUND = UE.DARK_GREY










class UI_main_window():
    def __init__(self):
        # Window dims
        WIDTH = MAIN_WINDOW_WIDTH
        HEIGHT = MAIN_WINDOW_HEIGHT
        self.root = tk.Tk(className=MAIN_WINDOW_TITLE)
        # root.config(background=atk.DEFAULT_COLOR)
        self.root.geometry(WIDTH + "x" + HEIGHT)
        self.root.configure(background=UE.DARK_GREY)

# it is recommended to select tkinter theme required for things to be right on windows,
# 'alt', 'default', or 'classic' work fine on windows
        self.s = ttk.Style()
        self.s.theme_use('classic')                    # self.s ?!/ no idea

        self.title_font = TkFont.Font(family='Consolas', size=24, weight='bold')
        self.norm_font = TkFont.Font(family='Consolas', size=10)
        #self.ft_title = UE.title_font
        #self.ft_norm   = UE.norm_font


        ## Set out Frames First

        self.top_frame = tk.LabelFrame(self.root, font=self.title_font, bg=UE.DARK_GREY, fg=UE.TEXT_GREY, relief="ridge", bd=2,
                                       height=100, text="MapMaster DMs Map & Resource Manager")
        self.top_frame.grid()


        self.root.mainloop()                              #end of Main UI Window call