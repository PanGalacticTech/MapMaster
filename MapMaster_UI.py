from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps
import tkinter.font as TkFont
from tkinter.filedialog import asksaveasfile
import tkinter.simpledialog as sd

import json_savefiles as save
from open_new_window import newWindow
import mirrorCanvas


root = Tk()
root.geometry("1600x980")
root.title("MapMaster DM's Tool")
root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")
                  # self.s ?!/ no idea




ICON_SIZE = 25   # pixel val for new icons
MAIN_WINDOW_BACKGROUND = UE.DARK_GREY

'''
Using Method from:
https://stackoverflow.com/questions/42322966/how-to-display-and-move-multiple-images-as-same-image-in-same-time-python-tkinte
'''

class movingIconCanvas:
    def __init__(self, root):
        self.root = root
        self.s = ttk.Style()
        self.s.theme_use('classic')
        self.root.configure(background=UE.DARK_GREY)
        self.title_font = TkFont.Font(family='Consolas', size=24, weight='bold')
        self.norm_font = TkFont.Font(family='Consolas', size=10)
        self.top_frame = UE.darkFrame(self.root, bg=UE.DARKER_GREY)
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.live_map_active = False
        self.dm_show_mask = False
        self.live_show_mask = True
        self.drawing_active = False
        self.add_mask = True
        self.grid_lines = []
        # Setout all othe Frames
        self.setout_frames(self.top_frame)
        self.placeholder_text()

        #Button Wigets




        # Create Canvas
        self.create_dm_canvas(self.map_frame)

        self.__move = False








        #List to hold images/references

        #self.icon_f_list = []    # Holds Filelinks to images
        self.icon_list = []      # hold img_refs
        self.live_map_list = []   # holds more img_refs  I think only useful for avoiding garbage collection,m might be a better way of doing this like declairing global but I dont understand that atm
        #self.icon_xy = []        # holds list of list of xy positions
        self.canvas_obj_list = [] #??? Holds objects once in canvas? IDK
        #self.icon_no = 0           # Dont like this but currently used to track new items into the array // Actually dont think this ever got used

        # The above is stupid. Why use lists and have to match and do all kinds of crazy complicated stuff. Just use a dictionary!

        self.icon_dic = save.proto_icon_dic

        # Always hold the cursor position using event for things like deleting stuff
        self.cursor_x = 0
        self.cursor_y = 0

        # Uncomment to load default game on startup
        self.load_map_from_dic(save.saved_map)





        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )



        #self.root.bind("<Left>", self.left)
        #self.root.bind("<Right>", self.right)
        #self.root.bind("<Up>", self.up)
        #self.map_canvas.bind("<Down>", self.down)



        #self.m_canvas.bind("<Double-B1", self.move)  # Double click binding (We will use this later)





        # Configure the row/col of our frame and root window to be resizable and fill all available space / May be reused if re-written with .pack
        #self.top_frame.grid(row=0, column=0, sticky="NESW")
        #self.top_frame.grid_rowconfigure(0, weight=1)
        #self.top_frame.grid_columnconfigure(0, weight=1)
        #self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(0, weight=1)



        self.root.mainloop()


    def create_dm_canvas(self, container):
        print("Creating DM Canvas")
        self.canvas_width = 1308
        self.canvas_height = 800
        self.map_canvas = Canvas(container, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        # self.map_canvas = mirrorCanvas(self.map_frame, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.map_canvas.grid(padx=10, pady=10, row=0, column=0)


        #self.create_mask_window()

        #Also need to re-bind everything to new canvas (of course hehe)
        self.bind_movement_events()
        self.init_x = self.canvas_width // 2
        self.init_y = self.canvas_height // 2
        self.background_center_x = self.init_x
        self.background_center_y = self.init_y


#TODO DONT THINK THIS WORKS AHHH
    def create_mask_window(self):
        # https://stackoverflow.com/questions/53021603/how-to-make-a-tkinter-canvas-background-transparent
        # https://www.reddit.com/r/Tkinter/comments/tw74cq/can_i_create_a_transparent_background_in_a_canvas/

        self.mask_win = tk.Tk()
        self.mask_win.config(highlightbackground = "#000000")
        self.mask_canvas = Canvas(self.mask_win, width=self.canvas_width, height=self.canvas_height, background="#000000")
        self.mask_canvas.pack()
        self.mask_win.overrideredirect(True)
        self.mask_win.wm_attributes('-transparentcolor', '#000000')
        self.mask_win.wm_attributes('-topmost', True)


        #self.dm_mask_canvas = Canvas(container, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        #self.map_canvas.grid(padx=10, pady=10, row=0, column=0)


    def bind_movement_events(self):
        # Also need to re-bind everything to new canvas (of course hehe)
        self.map_canvas.bind("<Button-1>", self.startMovement)
        self.map_canvas.bind("<ButtonRelease-1>", self.stopMovement)
        self.map_canvas.bind("<Motion>", self.movement)
        self.root.bind("<Delete>", self.delete_icon)

    def unbind_movement_events(self):
        self.map_canvas.unbind("<Button-1>")
        self.map_canvas.unbind("<ButtonRelease-1>")
        self.map_canvas.unbind("<Motion>")
        self.root.unbind("<Delete>")


    def destroy_dm_canvas(self):
        print("Destroying DM Canvas")
        try:
            self.map_canvas.destroy()
            self.map_canvas = None      ## This seems nessissary to clean the object
            self.mouse_label.destroy()
            self.mouse_label = None
        except:
            print("No DM Canvas Found")

    def create_live_canvas(self, container):
        print("Creating Live Canvas")
        self.live_map_canvas = Canvas(container, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.live_map_canvas.grid(padx=10, pady=10, sticky="NESW")

    def destroy_live_canvas(self):
        print("Destroying Live Canvas")
        try:
            self.live_map_canvas.destroy()
            self.live_map_canvas = None
        except:
            print("No Live Canvas Found")



    def setout_frames(self, root_container):
        ## Assuming existance of top_frame
        self.titlebox = UE.darkBorderless(root_container)
        self.titlebox.grid(padx=10, pady=5, sticky="NW", row=0, column=0)
        self.sidebar_title = UE.darkLabelTitle(self.titlebox, text="MapMaster DM's Tool")
        self.sidebar_title.grid(padx=10, pady=5, sticky="NSEW", row=0)

        self.side_frame = UE.darkFrame(root_container, bg=UE.DARKER_GREY, height=1400)  # , text="MapMaster DMs Map & Resource Manager" ,
        self.side_frame.grid(padx=10, pady=10, sticky="NW", row=1, column=0)
        #Dont forget buttons
        self.save_buttons_widget(self.side_frame, 0 , 0)

        self.object_frame = UE.darkFrame(self.side_frame, bg=UE.BLACK)
        self.object_frame.grid(column=0, padx=10, pady=10, row=1)

        self.background_image_widget(self.side_frame, 2, 0)
        self.add_icon_widget(self.side_frame, 4, 0)

        self.side_frame_two = UE.darkBorderless(self.side_frame, height=1400)  # , text="MapMaster DMs Map & Resource Manager" ,
        self.side_frame_two.grid(padx=10, pady=10, row=9, column=0)

        self.mouse_label = UE.colorLabel(self.side_frame, text="Mouse: ", bg=UE.DARKER_GREY, fg=UE.grey_picker(0.65))
        self.mouse_label.grid(padx=10, pady=10, row=10, column=0)    #sticky="SE"

        self.map_name_var = tk.StringVar()
        self.map_name_var.set("[BATTLE MAP TITLE]")
        self.map_name_text = "[BATTLE MAP TITLE]"    # still need this for dictionary
        self.background_file = ""

        ##Outer Frame (To help center map)
        #self.out_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)  # , text="MapMaster DMs Map & Resource Manager" , height=1000 #TODO: Dont need this frame?
        #self.out_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

        #self.battle_map_title = UE.darkLabelTitle(self.top_frame, text=self.map_name_text)
        self.battle_map_title = UE.darkLabelTitle(self.top_frame, textvariable=self.map_name_var)
        self.battle_map_title.grid(padx=10, pady=5, row=0, column=1, columnspan=2, sticky="N")
         ## Map Frame
        self.map_frame = UE.darkFrame(self.top_frame, bg=UE.DARKER_GREY)  # , text="MapMaster DMs Map & Resource Manager" ,height=1000
        self.map_frame.grid(padx=10, pady=10, sticky="NSEW", row=1, column=1, columnspan=2)

        ## Live Map Control Frame
        self.live_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.live_frame.grid(padx=10, pady=10, sticky="W", row=4, column=0, columnspan=2)
        self.live_buttons_wiget(self.live_frame)

        ## Mask Manipulation Frame
        self.mask_box = UE.darkBorderless(self.side_frame_two)
        self.mask_box.grid(padx=10, pady=5, row=0, column=0)
        self.mask_wiget(self.mask_box)

        ## Range and Character Control Frame
        self.range_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.range_frame.grid(padx=10, pady=10, sticky="E", row=4, column=2, columnspan=2)

    def placeholder_text(self):
        # Button Placeholders
        self.PLACEHOLDER_TEXT3 = UE.darkLabelTitle(self.side_frame, text="[Create Token]")
        self.PLACEHOLDER_TEXT3.grid(padx=10, pady=10, sticky="NSEW", row=7)
        self.PLACEHOLDER_TEXT5 = UE.darkLabelTitle(self.side_frame, text="[Map Filters]")
        self.PLACEHOLDER_TEXT5.grid(padx=10, pady=10, sticky="NSEW", row=8)

        #Placeholder Icons
        self.PLACEHOLDER_ICON = UE.darkLabel(self.object_frame, text="[Icon1]")
        self.PLACEHOLDER_ICON.grid(column=0, row=1, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON2 = UE.darkLabel(self.object_frame, text="[Icon2]")
        self.PLACEHOLDER_ICON2.grid(column=1, row=1, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON3 = UE.darkLabel(self.object_frame, text="[Icon3]")
        self.PLACEHOLDER_ICON3.grid(column=0, row=2, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON4 = UE.darkLabel(self.object_frame, text="[Icon4]")
        self.PLACEHOLDER_ICON4.grid(column=1, row=2, padx=10, pady=10, sticky="NSEW")



        self.PLACEHOLDER_BUTTON3 = UE.darkLabelTitle(self.range_frame, text="[Cone & Areas]")
        self.PLACEHOLDER_BUTTON3.grid(padx=10, pady=10, row=0, column=0, sticky="S")
        self.PLACEHOLDER_BUTTON4 = UE.darkLabelTitle(self.range_frame, text="[Range]")
        self.PLACEHOLDER_BUTTON4.grid(padx=10, pady=10, row=0, column=1, sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[Set Scale]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10, row=0, column=2, sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[John Maddon]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10, row=0, column=3, sticky="S")


    def live_buttons_wiget(self, container):
        self.livebox = UE.darkBorderless(container)
        self.livebox.grid(padx=10, pady=5, sticky="N")
        self.live_map_button = UE.selectButton(self.livebox, text="Activate Live Map", command=self.open_live_map)
        self.live_map_button.grid(padx=10, pady=10, row=0, column=0, sticky="S")
        self.PLACEHOLDER_BUTTON1 = UE.darkLabelTitle(self.livebox, text="[Blackout]")
        self.PLACEHOLDER_BUTTON1.grid(padx=10, pady=10, row=0, column=1, sticky="S")
        self.show_mask_button = UE.selectButton(self.livebox, text="Show Mask", command=self.show_mask)
        self.show_mask_button.grid(padx=10, pady=10, row=0, column=2, sticky="S")

    def show_mask(self):
        if self.dm_show_mask == True:
            self.dm_show_mask = False
            print("Hiding DM's Mask")
            self.show_mask_button.config(text="Show Mask", fg=UE.TEXT_GREY)
            self.add_tomask_button.grid_forget()
            self.subtract_button.grid_forget()
            self.hide_grid()
            self.delete_items_with_tag("mask")   ##TODO We will need to grab all the coordinates of the mask before deleteing
            self.unbind_drawing_events()
            self.bind_movement_events()
        else:
            self.dm_show_mask = True    ## This might not be needed as we are binding and unbinding the correct events now
            self.add_mask = True
            print("Showing DM's Mask")
            self.show_mask_button.config(text="Hide Mask", fg=UE.YELLOW_ORANGE)
            self.add_tomask_button.grid(padx=10, pady=10, row=0, column=0, sticky="S")
            self.subtract_button.grid(padx=10, pady=10, row=1, column=0, sticky="S")
            self.show_grid(50, UE.grey_picker(0.6))
            self.unbind_movement_events()
            self.bind_drawing_events()
            #TODO We will need to use the record of the added mask to reapply it when opened

    def show_grid(self, spacing, colour):
        quantity_y = int(self.canvas_height/spacing)
        quantity_x = int(self.canvas_width/spacing)
        print(f"Line Spacing: {spacing}, Quantity_x: {quantity_x}, Quantity_Y: {quantity_y}")
        for n in range(0, quantity_x):
            grid_line = (self.map_canvas.create_line(spacing*n, 0, spacing*n, self.canvas_height, fill=colour, tag="grid"))
        for m in range(0, quantity_y):
            grid_line = (self.map_canvas.create_line(0, spacing*m,self.canvas_width ,spacing*m , fill=colour, tag="grid"))

        #TODO This grid returns quantity of X and Y lines, this can be used to make a dictionary of tuples that either store a 1 or 0

    def hide_grid(self):
        self.delete_items_with_tag("grid")


    def delete_items_with_tag(self, in_tag):
        items = self.map_canvas.find_all()
        print(F"Searching Items: \n {items} \n for tag: \n{in_tag}")
        for item in items:
            for tag in self.map_canvas.gettags(item):  ## Check object isnt the background
                print(f" Current Tags for Item: {item}: {tag}")
                if (tag == in_tag):
                    self.map_canvas.delete(item)  ## Delete image in the canvas
                    #if self.live_map_active:
                        #self.live_map_canvas.delete(img_id)




    def bind_drawing_events(self):
        print("Binding Drawing Events")
        self.map_canvas.bind("<Button-1>", self.startDrawing)
        self.map_canvas.bind("<ButtonRelease-1>", self.stopDrawing)
        self.map_canvas.bind("<Motion>", self.do_drawing)


    def unbind_drawing_events(self):
        print("Unbinding Drawing Events")
        self.map_canvas.unbind("<Button-1>")
        self.map_canvas.unbind("<ButtonRelease-1>")
        self.map_canvas.unbind("<Motion>")

    def startDrawing(self, event):
        print("Starting Drawing")
        self.drawing_active = True


    def stopDrawing(self, event):
        print("Stopping Drawing")
        self.drawing_active = False


    def do_drawing(self, event):
        if self.drawing_active == True:
            if self.add_mask == True:
                print("Drawing Mask")
                # Draw a Circle
                circle_icons = self.map_canvas.create_oval(event.x, event.y, event.x+50, event.y+50, width=0, fill=UE.grey_picker(0.1), tag="mask")
            else:
                #print("Erasing Mask")
                self.delete_mask_object()

#TODO Fix this delete mask objects shite
    def delete_mask_object(self):
        img_canvas_id = self.map_canvas.find_closest(self.cursor_x, self.cursor_y, halo=5)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
        img_id = img_canvas_id[0]  ## Extract ID from tuple
        mask_id = self.map_canvas.find_above(img_id)
        for tag in self.map_canvas.gettags(mask_id):  ## Check object isnt the background
            print(f" Current Tags in {mask_id}: {tag}")
            if (tag == "mask"):
                mask_id = self.map_canvas.find_above(img_id)
                self.map_canvas.delete(img_id)
                print(f" Deleting Img: {mask_id}")


    def mask_wiget(self, container):
        self.add_tomask_button = UE.selectButton(container, text="Add Mask", command=self.add_to_mask)
        self.subtract_button = UE.selectButton(container, text="Subtract Mask", command=self.subtract_mask)

        if self.add_mask == True:
            self.add_tomask_button.config(fg=UE.YELLOW_ORANGE)
        else:
            self.subtract_button.config(fg=UE.YELLOW_ORANGE)



    def add_to_mask(self):
        print("Adding to Mask")
        self.add_mask = True
        self.add_tomask_button.config(fg=UE.YELLOW_ORANGE)
        self.subtract_button.config(fg=UE.TEXT_GREY)


    def subtract_mask(self):
        print("Subtracting from Mask")
        self.add_mask = False
        self.add_tomask_button.config(fg=UE.TEXT_GREY)
        self.subtract_button.config(fg=UE.YELLOW_ORANGE)



    def apply_mask_live_map(self):
        print("Applying Mask to Live Map")




    def open_live_map(self):
        if self.live_map_active == True:
            self.live_map_active = False
            print("Live Map Closed")
            self.live_map_button.config(text="Activate Live Map", bg=UE.DARKER_GREY, fg=UE.ACTIVE_BLUE)
            self.close_live_window()
        else:
            self.live_map_active = True
            print("Live Map Active")
            self.live_map_button.config(text="Close Live Map", bg=UE.ACTIVE_BLUE, fg=UE.DARKER_GREY )
            self.live_canvas()





    def live_canvas(self):
        print("Opening Live Canvas")
        self.live_map_win = Toplevel(self.root)
        self.live_map_win.configure(background=UE.DARK_GREY)
        self.create_live_canvas(self.live_map_win)
        self.set_live_canvas()


    def set_live_canvas(self):
        map_dic = self.create_map_dic()  ## Update the map dictionary
        self.load_live_map_from_dic(map_dic)
        print(f"Set Live Canvas")

    def update_live_canvas(self):
        print(f"Update Live Canvas")


    def close_live_window(self):
        self.live_map_canvas.destroy()
        self.live_map_win.destroy()


            # Save Buttons
    def save_buttons_widget(self, container, wiget_row, wiget_column):
        self.savebox = UE.darkBorderless(container)
        self.savebox.grid(padx=10, pady=5, sticky="N", row=wiget_row, column=wiget_column)
        self.open_button = UE.selectButton(self.savebox, text="Open File", command=self.open_save_game)
        self.open_button.grid(padx=10, pady=5)
        self.saveas_button = UE.selectButton(self.savebox, text="Save As", command=self.save_game)
        self.saveas_button .grid(padx=10, pady=5)
        self.save_button = UE.selectButton(self.savebox, text="Save", command=self.save_game)
        self.save_button.grid(padx=10, pady=5)
        self.rename_button = UE.selectButton(self.savebox, text="Rename Map", command=self.rename_map)
        self.rename_button.grid(padx=10, pady=5)


    def rename_map(self):
        print("Enter Map Title:")
        new_name = sd.askstring(title='Rename Map', prompt="New Map Name", bg=UE.DARKER_GREY)   ## Worked but could not recolour
        print(f"New Name: {new_name}")
        self.map_name_var.set(new_name)
        self.map_name_text = new_name






    def open_save_game(self):
        print("Open Save Game")
        print("Opening File Dialog")
        try:
            file_path = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\saved_games",
                    filetypes = [("Json File", "*.json")],
                    title = "Choose a Saved .json file")
            recalled_dic = save.recall_json_map(file_path)
            print(recalled_dic)
            print("Clearing Canvas")
            self.delete_map()
            self.delete_all_icons()
            print("Map Cleared")
            print("Destroying Canvases")
            self.destroy_dm_canvas()
            self.destroy_live_canvas()
            print("Creating Canvases")
            self.create_dm_canvas(self.map_frame)
            self.load_map_from_dic(recalled_dic)
            if self.live_map_active:
                self.create_live_canvas(self.live_map_win)
                self.set_live_canvas()
        except:
            print("problems recalling saved file")


    def save_game(self):
        print("Saving File")
        #first we need a dictionary of the current map
        map_dic = self.create_map_dic()
        try:
            json_file = save.return_json_str(map_dic)
            print(json_file)
            self.save_file(json_file)
            #save.save_json_map()
            #json_file = asksaveasfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\saved_games",
           #        defaultextension=[("Json File", "*.json")],
           #        title = "Save Map as .json File")
        except:
            print("problems saving file")



    def create_map_dic(self):
        #map_dic = save.proto_map_dic               ## Start with the prototype dictionary
        map_dic = {}                               ## Does it even need prototype?
        print(f"Saving Map: {self.map_name_text}")
        map_dic["name"] = self.map_name_text
        map_dic["background"] = self.background_file
        #map_item_list = self.map_canvas.find_all()
        #print(f"Map Item List: {map_item_list}")
        print(f"Icon Dictionary: {self.icon_dic}")
        map_dic["icons"] = {}   # Create the empty icon dictionary
        for item in self.icon_dic:
            try:
                tags = self.map_canvas.gettags(item)
                print(f"tags: {tags[0]}")
                if tags[0] == "icon":
                    print("Current Icon ID: ", item)
                    coords_tuple = self.map_canvas.coords(item)
                    print("coords tuple[0]")
                    print(f"Coords Tuple: {coords_tuple}")
                    self.icon_dic[item]["pos_x"] = round(coords_tuple[0])    ## Update item dictionaryu
                    self.icon_dic[item]["pos_y"] = round(coords_tuple[1])
                    print(f"Item Dictionary{self.icon_dic[item]}")
                    map_dic["icons"][item] = {}
                    map_dic["icons"][item]["file"] = self.icon_dic[item]["file"]
                    map_dic["icons"][item]["pos_x"] = self.icon_dic[item]["pos_x"]
                    map_dic["icons"][item]["pos_y"] = self.icon_dic[item]["pos_y"]
                    map_dic["icons"][item]["tag"] = self.icon_dic[item]["tag"]
            except:
                print(f"Error Finding Tags for Object {item}.")
        print("End of Create Map Dictionary")
        print(f"New Map Dictionary: {map_dic}")
        return map_dic

    def save_file(self, json_file):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".json", initialdir="D:\Pan Galactic Engineering\MapMaster\saved_games",)
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        f.write(json_file)
        f.close()


    def load_live_map_from_dic(self, map_dic):
        try:
            background_file = map_dic["background"]
            print(f"Background File Found: {background_file}")
            self.add_bg_live_map(background_file)
        except:
            print("No background found")
        try:
            print(map_dic["icons"])
            for icons in map_dic["icons"]:      # Icons just returns a (list?) of the numbers of the dictionarys of items - AS A STRING
                print(icons)
                current_file = map_dic["icons"][icons]["file"]
                print(f"Loading File: {current_file}")
                icon_x = int(map_dic["icons"][icons]["pos_x"])
                icon_y = int(map_dic["icons"][icons]["pos_y"])
                print(f"Placing Icon at: X[{icon_x}], Y[{icon_y }]")
                try:
                    object_id = self.add_place_live_map(icon_x, icon_y, current_file)
                    print(f"Placing Icon at: X[{icon_x}], Y[{icon_y}]")
                except:
                    print("Problem inserting Object into Canvas")
        except:
            print("Problem Loading Map from Dictionary")
        print(f"All Items Added to Live Map")
        print("The following lists should match")
        self.print_all_live_items()



    def load_map_from_dic(self, map_dic):
        #self.battle_map_title.config(text= map_dic["name"])
        self.map_name_text = map_dic["name"]
        self.map_name_var.set(self.map_name_text)
        try:
            self.background_file = map_dic["background"]
            print(f"Background File Found: {self.background_file}")
            self.add_background(self.background_file)
        except:
            print("No background found")
        try:
            print(map_dic["icons"])
            for icons in map_dic["icons"]:      # Icons just returns a (list?) of the numbers of the dictionarys of items - AS A STRING
                print(icons)
                current_file = map_dic["icons"][icons]["file"]
                print(f"Loading File: {current_file}")
                icon_x = int(map_dic["icons"][icons]["pos_x"])
                icon_y = int(map_dic["icons"][icons]["pos_y"])
                try:
                    object_id = self.add_place_icon(icon_x, icon_y, current_file)
                except:
                    print("Problem inserting Object into Canvas")
        except:
            print("Problem Loading Map from Dictionary")








            #Background Images
    def background_image_widget(self, container, item_row, item_column):
        self.backgound_button = UE.selectButton(container, text="Open Background Map", command=self.select_bg_dialog)
        self.backgound_button.grid(padx=5, pady=5, row=item_row, column=item_column)
        self.delete_map_button = UE.selectButton(container, text="Delete Background Map", command=self.delete_map)
        self.delete_map_button.grid(padx=5, pady=5, row=item_row+1, column=item_column)

        #self.canvas = Canvas(self.map_frame, width=1200, height=850, bg=UE.DARKER_GREY, highlightcolor=UE.ACTIVE_BLUE, bd=0, relief="sunken")
        #self.canvas.grid(sticky="NSEW", padx=5, pady=5)


    def select_bg_dialog(self):
        try:
            self.background_file = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_backgrounds")
            self.add_background(self.background_file)
        except:
            print("User Closed Dialogue Box")

    def add_background(self, file_path):
        resized_image = self.resize_map(file_path)
        self.background_file = file_path
        bg_image = ImageTk.PhotoImage(resized_image)
        self.map_canvas.bg_image = bg_image
        bg_id = self.map_canvas.create_image(self.background_center_x, self.background_center_y, image=self.map_canvas.bg_image, tags="background")  # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
        print(f"Background ID: {bg_id}")
        # This line is not working sometimes, its quitting here and going to except.
        try:
            items =  self.map_canvas.find_all()
            print(items)
            lowest_item_id = items[0]
            print(f"Finding Lowest Item ID: {lowest_item_id}")
            self.map_canvas.tag_lower(bg_id, lowest_item_id)
            print(self.map_canvas.find_all())
        except:
            print("Problem tagging background lower")
            return 0
        print("New Map Background Applied")

    def add_bg_live_map(self, file_path):
        resized_image = self.resize_map(file_path)
        self.background_file = file_path
        bg_image = ImageTk.PhotoImage(resized_image)
        self.live_map_canvas.bg_image = bg_image
        bg_id = self.live_map_canvas.create_image(self.background_center_x, self.background_center_y, image=self.live_map_canvas.bg_image, tags="background")  # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
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

    def delete_map(self):
        print("Deleting Map Background")
        items = self.map_canvas.find_all()
        print(items)
        for item in items:
            print(item)
            for tag in self.map_canvas.gettags(item):  ## Check object isnt the background
                print(tag)
                if (tag == "background"):
                    self.map_canvas.delete(item)
                    self.background_file = "" # Also delete the file reference so that does not get saved in our JSON database
                    print(self.map_canvas.find_all())  # get all canvas objects ID



    #Adding Icons

    def add_icon_widget(self, container, item_row, item_column):
        self.add_icon_button = UE.selectButton(container, text="Add Icon", command=self.add_icon_dialog)
        self.add_icon_button.grid(padx=5, pady=5, row=item_row, column=item_column)
        self.add_image_button = UE.selectButton(container, text="Add Image", command=self.add_image_dialog)
        self.add_image_button.grid(padx=5, pady=5, row=item_row+1, column=item_column)

    # Same as add icon but does not resize image
    def add_image_dialog(self):
        try:
            filepath = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_icons")
            self.add_place_image(self.init_x, self.init_y, filepath)
            print("New Image Added")
            if self.live_map_active:
                self.add_place_live_image(self.init_x, self.init_y, filepath)
        except:
            print("User Closed Dialogue Box")

#https://www.digitalocean.com/community/tutorials/python-add-to-dictionary



    def add_place_image(self, x, y, filepath):
        img = Image.open(filepath)
        print(f"Opening Icon: {filepath}")
        print(f"IconSize: {img.size[0]}, {img.size[1]}")
        #if (img.size[0] > 50) or (img.size[1] > 50):
        #    print("Icon Too Large: Resizing Icon")
        #img = self.resize_image(filepath, 25, 25)
        img_ref = ImageTk.PhotoImage(img)
        print(f"img_ref: {img_ref}")
        img_canvas_id = self.map_canvas.create_image(x, y, image=img_ref, tags="image")
        print(f"img_canvas_id: {img_canvas_id}")
        self.icon_dic[img_canvas_id] = {}
        self.icon_dic[img_canvas_id].update({
            "file": filepath,
            "pos_x": x,
            "pos_y": y,
            "ref" : img_ref,                           # Even if img_ref isnt used it helps maintain it as global object to avoid garbage collection
            "tag": "icon"})
        print(self.icon_dic)
        print(self.map_canvas.find_all())  # get all canvas objects ID

    def add_place_live_image(self, x, y, filepath):
        img = Image.open(filepath)
        print(f"Opening Icon: {filepath}")
        print(f"IconSize: {img.size[0]}, {img.size[1]}")
        #if (img.size[0] > 50) or (img.size[1] > 50):
        #    print("Icon Too Large: Resizing Icon")
        #img = self.resize_image(filepath, 25, 25)
        img_ref = ImageTk.PhotoImage(img)
        self.live_map_list.append(img_ref)
        print(f"img_ref: {img_ref}")
        img_canvas_id = self.live_map_canvas.create_image(x, y, image=img_ref, tags="image")
        print(f"img_canvas_id: {img_canvas_id}")
        print(self.map_canvas.find_all())  # get all canvas objects ID


    def add_icon_dialog(self):
        try:
            filepath = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_icons")
            self.add_place_icon(self.init_x, self.init_y, filepath)
            print("New Icon Added")
            if self.live_map_active:
                self.add_place_live_map(self.init_x, self.init_y, filepath)
        except:
            print("User Closed Dialogue Box")



    def add_place_icon(self, x, y, filepath):
        img = Image.open(filepath)
        print(f"Opening Icon: {filepath}")
        print(f"IconSize: {img.size[0]}, {img.size[1]}")
        if (img.size[0] > 50) or (img.size[1] > 50):
            print("Icon Too Large: Resizing Icon")
            img = self.resize_image(filepath, 25, 25)
        img_ref = ImageTk.PhotoImage(img)
        print(f"img_ref: {img_ref}")
        img_canvas_id = self.map_canvas.create_image(x, y, image=img_ref, tags="icon")
        print(f"img_canvas_id: {img_canvas_id}")
        self.icon_dic[img_canvas_id] = {}
        self.icon_dic[img_canvas_id].update({
            "file": filepath,
            "pos_x": x,
            "pos_y": y,
            "ref" : img_ref,                           # Even if img_ref isnt used it helps maintain it as global object to avoid garbage collection
            "tag": "icon"})
        print(self.icon_dic)
        print(self.map_canvas.find_all())  # get all canvas objects ID

    def add_place_live_map(self,  x, y, filepath):
        img = Image.open(filepath)
        print(f"Opening Icon: {filepath}")
        print(f"IconSize: {img.size[0]}, {img.size[1]}")
        if (img.size[0] > 50) or (img.size[1] > 50):
            print("Icon Too Large: Resizing Icon")
            img = self.resize_image(filepath, 25, 25)
        img_ref = ImageTk.PhotoImage(img)     # I think this imageref needs to be saved as a global to avoid garbage collection
        self.live_map_list.append(img_ref)
        print(f"img_ref: {img_ref}")
        img_canvas_id = self.live_map_canvas.create_image(x, y, image=img_ref, tags="icon")
        print(f"img_LIVE_canvas_id: {img_canvas_id}")
        print(self.live_map_canvas.find_all())  # get all canvas objects ID):

    def resize_image(self, filepath, Wmax, Hmax):
        img = Image.open(filepath)
        #print(filepath)
        #print(img.size[0], ", ", img.size[1])
        # resize_img = ImageOps.fit(img, (900,900),method=0,bleed=0.0,centering=(0.5,0.5))
        img.thumbnail((Wmax, Hmax))  # Needs to be passed type tuple ## This does NOT RETURN IMAGE. it works on img object
        print("New Image Size")
        print(img.size[0], img.size[1])
        return img


    def save_resize_image(self, filepath, Wmax, Hmax, new_filename):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        # resize_img = ImageOps.fit(img, (900,900),method=0,bleed=0.0,centering=(0.5,0.5))
        img.thumbnail((Wmax, Hmax))  # Needs to be passed type tuple ## This does NOT RETURN IMAGE. it works on img object
        print("New Image Size")
        print(img.size[0], img.size[1])
        new_filepath = "D:\Pan Galactic Engineering\MapMaster\map_icons\\" + new_filename + ".png"
        print(new_filepath)
        img.save(new_filepath)
        return new_filepath

#Events
    #Delete an Icon - SEMI BROKEN works but only if move Icon to upper corner of canvas
    def delete_icon(self, event):
        img_canvas_id = self.map_canvas.find_closest(self.cursor_x, self.cursor_y, halo=1)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
        img_id = img_canvas_id[0]                                                               ## Extract ID from tuple
        print(f" Deleting Img: {img_id}")
        for tag in self.map_canvas.gettags(img_id):                                    ## Check object isnt the background
            print(f" Current Tags in {img_id}: {tag}")
            if (tag == "icon" or tag == "image"):
                self.map_canvas.delete(img_id)                                        ## Delete image in the canvas
                if self.live_map_active:
                    self.live_map_canvas.delete(img_id)
                print(f"Found Match for tag: {tag}, Deleting Item")
                print(f"Remaining Items: {self.map_canvas.find_all()}")  # get all canvas objects ID
                print("Icon Dictionary Original")
                self.print_dictionary(self.icon_dic[img_id])
                del self.icon_dic[img_id]  ## Also delete from dictionary
                print("Icon Dictionary Item Removed")
                self.print_dictionary(self.icon_dic)
            #if (tag == "background"):
            #    print("Background Selected - exiting")
            #    break
            #else:
            #    self.map_canvas.delete(item)
            #    print(self.map_canvas.find_all())  # get all canvas objects ID

    def delete_icon_from_dic(self, img_id):
        print("Icon Dictionary Original")
        self.print_dictionary(self.icon_dic[img_id])
        del self.icon_dic[img_id]  ## Also delete from dictionary
        print("Icon Dictionary Item Removed")
        self.print_dictionary(self.icon_dic)


    def delete_all_icons(self):
        print("Deleting All Icons & Images")
        items = self.map_canvas.find_all()
        print(f"Items, {items}")
        for item_id in items:
            #item_id = item[0]
            print(f"Deleting Item: {item_id}")
            self.map_canvas.delete(item_id)
            try:
                del self.icon_dic[item_id]  ## Also delete from dictionary
                print("Icon Dictionary Item Removed")
            except:
                print("Item Not Found In Dictionary")
        try:
            self.print_dictionary(self.icon_dic)
            del self.icon_dic[1]  ## Also Delete entry 1 incase no other item was in dictionary
            self.print_dictionary(self.icon_dic)
        except:
            print("Problem Deleting Items")
        print("All Items Deleted")




    def print_dictionary(self, dictionary):
        try:
            for key, value in dictionary.items():
                print(key, " : ", value)
        except:
            print("Unable to Print Dictionary")



    def down(self, event):
        print("Down arrow pressed")

# Event Methods for moving icons
    def startMovement(self, event):
        self.initi_x = event.x
        self.initi_y = event.y
        #print('startMovement init', self.initi_x, self.initi_y)
        item = self.map_canvas.find_closest(self.initi_x, self.initi_y, halo=1)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
        #live_item = self.live_map_canvas.find_closest(self.initi_x, self.initi_y, halo=1)
        for tag in self.map_canvas.gettags(item):                                    ## Check object isnt the background
            print(tag)
            if (tag == "background"):
                print("Background Selected - exiting")
                self.__move = False
                break
            else:
                self.__move = True  ## Moving this to avoid errors
                self.movingimage = item  # get canvas object ID of where mouse pointer is
                print(self.movingimage)
                #print(self.map_canvas.find_all())  # get all canvas objects ID Just makes a mess of debug logs

    def stopMovement(self, event):
        self.__move = False


    def movement(self, event):
        if self.__move:
            self.mouse_label.config(text="Mouse: " + str(event.x) + ", " + str(event.y))
            #end_x = c.canvasx(event.x)  # Translate mouse x screen coordinate to canvas coordinate
            #end_y = c.canvasy(event.y)  # Translate mouse y screen coordinate to canvas coordinate  // dont think I need this because done already
            end_x = event.x
            end_y = event.y
            #print('movement end', end_x, end_y)
            deltax = end_x - self.initi_x  # Find the difference
            deltay = end_y - self.initi_y
            #print('movement delta', deltax, deltay)
            self.initi_x = end_x  # Update previous current with new location
            self.initi_y = end_y
            #print('movement init', self.initi_x, self.initi_y)
            self.map_canvas.move(self.movingimage, deltax, deltay)  # move object
            if self.live_map_active:
                self.live_map_canvas.move(self.movingimage, deltax, deltay)
            self.map_canvas["cursor"] = "hand2"
        self.cursor_x = event.x
        self.cursor_x = event.y


    def print_all_live_items(self):   # Prints all items on both live map and DM map
        try:
            map_items = self.map_canvas.find_all()
            live_map_items = self.live_map_canvas.find_all()
            print(f"DM's Map: \n{map_items}")
            print(f"Live Map: \n{live_map_items}")
        except:
            print("ERROR: Canvas Objects missing or not found")


GUI = movingIconCanvas(root)














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''