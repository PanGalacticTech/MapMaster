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
NEW_WIN_GEOMETRY = "1600x1000"
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
        print("newWindow Open \n\n\n\n")
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
        self.background_file = ""
        #self.top_frame.grid(row=0, column=0, sticky="NESW")
        #self.map_frame = UE.darkFrame(self.top_frame, bg=UE.DARKER_GREY)  # , text="MapMaster DMs Map & Resource Manager" ,height=1000
        #self.map_frame.grid(padx=10, pady=10, sticky="NSEW") #row=1, column=1, columnspan=2
        #Button Wigets
        #self.text_input_wiget()

        self.canvas_width = 1308
        self.canvas_width = 876

        self.live_map_canvas = Canvas(self.top_frame, width=self.canvas_width, height=self.canvas_width, bg=UE.DARK_GREY)
        self.live_map_canvas.grid(padx=10, pady=10)


        #self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.top_frame.grid(padx=10, pady=10, sticky="NSEW", row=0, column=0, columnspan=2)
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



    def load_map_from_dic(self, map_dic, item_dic, background_ref):
        # self.battle_map_title.config(text= map_dic["name"])
        #self.map_name_text = map_dic["name"]
        #self.map_name_var.set(self.map_name_text)
        try:
            self.add_background_ref(background_ref)
            self.background_file = map_dic["background"]
            print(f"Background File Found: {self.background_file}")
            self.add_background(self.background_file)
        except:
            print("No background found [0]")
        try:
            print(map_dic["icons"])
            for icons in map_dic[ "icons"]:  # Icons just returns a (list?) of the numbers of the dictionarys of items - AS A STRING
                print(icons)
                print(item_dic[icons]) # Testing using the reference saved in item dic instead of file saved in map dic
                current_file = map_dic["icons"][icons]["file"]
                print(f"Loading File: {current_file}")
                icon_x = int(map_dic["icons"][icons]["pos_x"])
                icon_y = int(map_dic["icons"][icons]["pos_y"])
                ref = item_dic[icons]["ref"]
                try:
                    object_id = self.add_place_icon_obj(icon_x, icon_y, ref)
                    #object_id = self.add_place_icon(icon_x, icon_y, current_file)
                except:
                    print("Problem inserting Object into Canvas")
        except:
            print("Problem Loading Map from Dictionary")


    def add_background(self, file_path):
        resized_image = self.resize_map(file_path)
        #self.background_file = file_path
        bg_image = ImageTk.PhotoImage(resized_image)
        self.live_map_canvas.bg_image = bg_image
        bg_id = self.live_map_canvas.create_image(654, 438, image=self.live_map_canvas.bg_image, tags="background")  # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
        print(f"Background ID: {bg_id}")
        # This line is not working sometimes, its quitting here and going to except.
        try:
            items = self.live_map_canvas.find_all()
            print(items)
            lowest_item_id = items[0]
            print(f"Finding Lowest Item ID: {lowest_item_id}")
            self.live_map_canvas.tag_lower(bg_id, lowest_item_id)
            print(self.live_map_canvas.find_all())
        except:
            print("Problem tagging background lower")
            return 0
        print("New Map Background Applied")

    def add_background_ref(self, img_ref):
        bg_image = ImageTk.PhotoImage(img_ref)
        self.live_map_canvas.bg_image = bg_image
        bg_id = self.live_map_canvas.create_image(654, 438, image=self.live_map_canvas.bg_image,
                                                  tags="background")  # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
        print(f"Background ID: {bg_id}")
        # This line is not working sometimes, its quitting here and going to except.
        try:
            items = self.live_map_canvas.find_all()
            print(items)
            lowest_item_id = items[0]
            print(f"Finding Lowest Item ID: {lowest_item_id}")
            self.live_map_canvas.tag_lower(bg_id, lowest_item_id)
            print(self.live_map_canvas.find_all())
        except:
            print("Problem tagging background lower")
            return 0
        print("New Map Background Applied")


# Opens image from passed filepath. Resizes image to fit background area
    def resize_map(self, filepath):
        img = Image.open(filepath)
        img.thumbnail((1000,850))    #Needs to be passed type tuple ## This does NOT RETURN IMAGE. it works on img object
        print("New Image Size")
        print(img.size[0],img.size[1])
        return img

    def add_place_icon_obj(self, x, y, img_ref):
        #img = Image.open(filepath)
        #print(f"Opening Icon: {filepath}")
        #print(f"IconSize: {img.size[0]}, {img.size[1]}")
        #if (img.size[0] > 50) or (img.size[1] > 50):
         #   print("Icon Too Large: Resizing Icon")
        #    img = self.resize_image(filepath, 25, 25)
        #img_ref = ImageTk.PhotoImage(img)
        print(f"img_ref: {ref}")
        img_canvas_id = self.live_map_canvas.create_image(x, y, image=img_ref, tags="icon")
        print(f"img_canvas_id: {img_canvas_id}")
        # self.icon_dic[img_canvas_id] = {}             ### Do not need to update item dic as we are using the
        # self.icon_dic[img_canvas_id].update({
        #    "file": filepath,
        #    "pos_x": x,
        #   "pos_y": y,
        #   "ref" : img_ref,                           # Even if img_ref isnt used it helps maintain it as global object to avoid garbage collection
        #    "tag": "icon"})
        # print(self.icon_dic)
        print(self.live_map_canvas.find_all())  # get all canvas objects ID


    def add_place_icon(self, x, y, filepath):
        img = Image.open(filepath)
        print(f"Opening Icon: {filepath}")
        print(f"IconSize: {img.size[0]}, {img.size[1]}")
        if (img.size[0] > 50) or (img.size[1] > 50):
            print("Icon Too Large: Resizing Icon")
            img = self.resize_image(filepath, 25, 25)
        img_ref = ImageTk.PhotoImage(img)
        print(f"img_ref: {img_ref}")
        img_canvas_id = self.live_map_canvas.create_image(x, y, image=img_ref, tags="icon")
        print(f"img_canvas_id: {img_canvas_id}")
        #self.icon_dic[img_canvas_id] = {}             ### Do not need to update item dic as we are using the
        #self.icon_dic[img_canvas_id].update({
        #    "file": filepath,
        #    "pos_x": x,
         #   "pos_y": y,
         #   "ref" : img_ref,                           # Even if img_ref isnt used it helps maintain it as global object to avoid garbage collection
        #    "tag": "icon"})
        #print(self.icon_dic)
        print(self.live_map_canvas.find_all())  # get all canvas objects ID

    def resize_image(self, filepath, Wmax, Hmax):
        img = Image.open(filepath)
        #print(filepath)
        #print(img.size[0], ", ", img.size[1])
        # resize_img = ImageOps.fit(img, (900,900),method=0,bleed=0.0,centering=(0.5,0.5))
        img.thumbnail((Wmax, Hmax))  # Needs to be passed type tuple ## This does NOT RETURN IMAGE. it works on img object
        print("New Image Size")
        print(img.size[0], img.size[1])
        return img


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