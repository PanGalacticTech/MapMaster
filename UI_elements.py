'''
MapMaster User Interface Elements


'''



import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
import tkinter.simpledialog


#USER COLOURS:


FEATURE_GREY = "#666666"
LIGHT_GREY = "#e6e6e6"
TEXT_GREY = "#eeeeee"
BG_GREY = "#303030"
ACTIVE_BLUE = "#09dceb"
YELLOW_ORANGE = "#e8b60e"
## GreyPalete
BLACK = "#000000"         # Grey 0%
DARKER_GREY = "#1c1c1c"   # Grey 11%
DARK_GREY = "#212121"     # Grey 13%
MID_GREY = "#2b2b2b"      # Grey 17%
GREY = "#383838"          # Grey 22%
GREY2 = "#474747"          # Grey 28%


def grey_picker(percentage):
    int_i = int(255*percentage)
    hex_o = hex(int_i)
    hex_o = hex_o[2:]
    while len(hex_o) < 2:
        hex_o = "0" + hex_o
    outstring = "#" + hex_o + hex_o + hex_o
    return outstring

#grey_picker(0.01)

def display_colour(color):
    root = tk.Tk(className="Display Colour")
    #root.config(background=atk.DEFAULT_COLOR)
    root.geometry("400x400")
    root.configure(background=color)
    root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")
    s = ttk.Style()
    s.theme_use('classic')
    color_label = tk.Label(root, text=color, bg=DARKER_GREY, fg=grey_picker(0.65))
    color_label.grid(padx=10, pady=10, sticky="SE")
    root.mainloop()

#display_colour(grey_picker(1))


#USER FONTS


'''
https://stackoverflow.com/questions/61566043/how-to-set-background-color-of-tk-simpledialog
https://rszalski.github.io/magicmethods/
'''

#Dark Popup:

'''
class darkDialog(tk.simpledialog.Dialog):
    def buttonbox(self):
        value = self.entry_box()
        print(value)
        super().buttonbox()
        for _ in self.children.values(): _.configure(bg=DARKER_GREY)
        self.configure(bg=DARKER_GREY)


    def entry_box(self):
        self.new_name_text = darkLabel(self, text="Enter New Map Title")
        self.new_name_text.pack(padx=10, pady=10)
        self.new_name_entry = darkEntry(self)
        self.new_name_entry.pack(padx=10, pady=5)

        value = self.new_name_entry.get()
        print(f"Input Box Value: {value}")
        return value

'''






#UI ELEMENTS
class darkFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Frame.__init__(self, master, relief="ridge", bd=3, **kwargs)       #bg=DARK_GREY

class int_entry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        self.inpt_ft = TkFont.Font(family='Consolas', size=10)
        tk.Entry.__init__(self, master, textvariable=self.var, font=self.inpt_ft, bg=DARK_GREY, fg=TEXT_GREY, highlightbackground=YELLOW_ORANGE,
                      insertbackground='cyan', disabledbackground=FEATURE_GREY , **kwargs)




class darkEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        self.inpt_ft = TkFont.Font(family='Consolas', size=10)
        tk.Entry.__init__(self, master, textvariable=self.var, font=self.inpt_ft, bg=DARK_GREY, fg=TEXT_GREY, highlightbackground=YELLOW_ORANGE,
                      insertbackground='cyan', disabledbackground=FEATURE_GREY , **kwargs)





class darkBorderless(tk.Frame):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Frame.__init__(self, master, bg=DARK_GREY, relief="ridge", **kwargs)



class radioButton(tk.Button):                            ## THIS IS A RADIO BUTTON WTF
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        self.bld_ft = TkFont.Font(family='Consolas', size=10, weight='bold')
        tk.Radiobutton.__init__(self, master, bg = BG_GREY, fg=TEXT_GREY, font=self.bld_ft, selectcolor="Black",
                                activebackground = FEATURE_GREY, **kwargs)


class selectButton(tk.Button):                            ## THIS IS A RADIO BUTTON WTF
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        self.bld_ft = TkFont.Font(family='Consolas', size=10, weight='bold')
        tk.Button.__init__(self, master, bg = BG_GREY, fg=TEXT_GREY, font=self.bld_ft,
                                activebackground = FEATURE_GREY, **kwargs) #selectcolor="Black",



class darkLabelTitle(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.tl_ft = TkFont.Font(family='Consolas', size=14, weight='bold')
        tk.Label.__init__(self, master, font=self.tl_ft, bg=DARK_GREY, fg=LIGHT_GREY, **kwargs)


class darkLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Label.__init__(self, master, font=self.lbl_ft, bg=DARK_GREY, fg=LIGHT_GREY, **kwargs)

class colorLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Label.__init__(self, master, font=self.lbl_ft, **kwargs)


class darkMessage(tk.Message):
    def __init__(self, master=None, **kwargs):
        self.def_ft = TkFont.Font(family='Consolas', size=10)
        self.disp_text = tk.StringVar()
        tk.Message.__init__(self, master, textvar=self.disp_text, font=self.def_ft, bg= DARK_GREY, fg= LIGHT_GREY, **kwargs)
