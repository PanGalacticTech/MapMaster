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



class selectButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        self.bld_ft = TkFont.Font(family='Consolas', size=10, weight='bold')
        tk.Radiobutton.__init__(self, master, bg = BG_GREY, fg=TEXT_GREY, font=self.bld_ft, selectcolor="Black",
                                activebackground = FEATURE_GREY, **kwargs)



class darkLabelTitle(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.tl_ft = TkFont.Font(family='Consolas', size=14, weight='bold')
        tk.Label.__init__(self, master, font=self.tl_ft, bg=DARK_GREY, fg=LIGHT_GREY, **kwargs)


class darkLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.lbl_ft = TkFont.Font(family='Consolas', size=12, weight='bold')
        tk.Label.__init__(self, master, font=self.lbl_ft, bg=DARK_GREY, fg=LIGHT_GREY, **kwargs)


class darkMessage(tk.Message):
    def __init__(self, master=None, **kwargs):
        self.def_ft = TkFont.Font(family='Consolas', size=10)
        self.disp_text = tk.StringVar()
        tk.Message.__init__(self, master, textvar=self.disp_text, font=self.def_ft, bg= DARK_GREY, fg= LIGHT_GREY, **kwargs)
