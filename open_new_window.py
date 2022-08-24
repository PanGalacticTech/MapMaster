# Add oBject Window
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps
import tkinter.font as TkFont
from tkinter.filedialog import asksaveasfile

import json_savefiles as save

WINDOW_TITLE = "Enter Map Name"
NEW_WIN_GEOMETRY = "500x300"
WIN_ICON = "D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico"

class newWindow:
    def __init__(self):
        self.root = Tk()
        self.s = ttk.Style()
        self.s.theme_use('classic')
        self.root.configure(background=UE.DARK_GREY)
        self.root.geometry(NEW_WIN_GEOMETRY)
        self.root.title(WINDOW_TITLE)
        self.root.iconbitmap(WIN_ICON)
        self.title_font = TkFont.Font(family='Consolas', size=24, weight='bold')
        self.norm_font = TkFont.Font(family='Consolas', size=10)
        self.top_frame = UE.darkFrame(self.root, bg=UE.DARKER_GREY)
        self.top_frame.grid(row=0, column=0, sticky="NESW")

        # our root
        #self.root = tk.Tk(className="Skyrora Safe Distance Calculator - Input Form")
        # root.config(background=atk.DEFAULT_COLOR)
        #self.root.geometry(WIDTH + "x" + HEIGHT)
        #self.root.configure(background=DARK_GREY)

        #Button Wigets

    def text_input_wiget(self):










'''
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Enter Name")
        # sets the geometry of toplevel
    newWindow.geometry("700x1000")

    newWindow.configure(background=UE.DARK_GREY)
'''