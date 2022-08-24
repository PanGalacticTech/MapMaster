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
NEW_WIN_GEOMETRY = "300x100"
WIN_ICON = "D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico"

PLACEHOLDER = "Placeholder"

'''
The new window opens as a non top level window, and will use the map dictionary to reconstruct the
canvas as seen by the DM.

However, this will either need constant updating or ahhhh move event could also be used to call a move event for 
the 2nd canvas. 
'''

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
        #self.top_frame.grid(row=0, column=0, sticky="NESW")

        #Button Wigets
        self.text_input_wiget()

        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def text_input_wiget(self):
        self.text_entry = UE.darkEntry(self.top_frame)
        self.text_entry.grid(padx=10, pady=5)
        ## Live Map Control Frame
        self.button_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.button_frame.grid(row=1)
        self.apply_button = UE.selectButton(self.button_frame, text="Apply Name", command=self.apply_name)
        self.apply_button.grid(padx=10, pady=5,row=0, column=0)
        self.cancel_button = UE.selectButton(self.button_frame, text="Cancel", command=self.cancel_process)
        self.cancel_button.grid(padx=10, pady=5,row = 0, column=1)


    def apply_name(self):
        new_name = self.text_entry.get()
        print(f"Applying New Name: {new_name}")
        self.close_window()
        return new_name

    def cancel_process(self):
        print(f"Cancelling Process")
        self.close_window()



    def close_window(self):
        print(f"Closing Window")
        self.root.destroy()




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