from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps
import tkinter.font as TkFont
from tkinter.filedialog import asksaveasfile

import json_savefiles as save



root = Tk()
root.geometry("1600x1100")
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

        # Setout all othe Frames
        self.setout_frames(self.top_frame)
        self.placeholder_text()

        #Button Wigets




        # Canvas Width
        self.canvas_width = 1308
        self.canvas_height = 876


        self.map_canvas = Canvas(self.map_frame, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.map_canvas.grid(padx=10, pady=10)
        self.__move = False
        # Label to output xy of mouse
        self.mouse_label = UE.colorLabel(self.map_frame, text="Mouse: ", bg=UE.DARKER_GREY, fg=UE.grey_picker(0.65))
        self.mouse_label.grid(padx=10, pady=10, sticky="SE")




        self.init_x = self.canvas_width // 2
        self.init_y = self.canvas_height // 2

        #List to hold images/references

        self.icon_f_list = []    # Holds Filelinks to images
        self.icon_list = []      # hold img_refs
        self.icon_xy = []        # holds list of list of xy positions
        self.canvas_obj_list = [] #??? Holds objects once in canvas? IDK
        self.icon_no = 0           # Dont like this but currently used to track new items into the array // Actually dont think this ever got used

        # Always hold the cursor position using event for things like deleting stuff
        self.cursor_x = 0
        self.cursor_y = 0

        #self.load_map_from_dic(save.saved_map)


        # Check image size and Add image to ref list
        #self.add_icon("D:\Pan Galactic Engineering\MapMaster\map_icons\enemy_dot.png")
        # Place image on canvas
        #self.place_icon(self.init_x, self.init_y, 0)

        #self.add_icon("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Orange_Dot.png")
        # Place image on canvas
       # self.canvas_obj_list.append(self.map_canvas.create_image(self.init_x, self.init_y, image=self.icon_list[1]))
        #self.place_icon(self.init_x, self.init_y, 1)



        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )



        #self.root.bind("<Left>", self.left)
        #self.root.bind("<Right>", self.right)
        #self.root.bind("<Up>", self.up)
        #self.map_canvas.bind("<Down>", self.down)

        self.map_canvas.bind("<Button-1>", self.startMovement)
        self.map_canvas.bind("<ButtonRelease-1>", self.stopMovement)
        self.map_canvas.bind("<Motion>", self.movement)
        self.root.bind("<Delete>", self.delete_icon)

        #self.m_canvas.bind("<Double-B1", self.move)  # Double click binding (We will use this later)





        # Configure the row/col of our frame and root window to be resizable and fill all available space
        #self.top_frame.grid(row=0, column=0, sticky="NESW")
        #self.top_frame.grid_rowconfigure(0, weight=1)
        #self.top_frame.grid_columnconfigure(0, weight=1)
        #self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(0, weight=1)



        self.root.mainloop()

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

        self.map_name_text = "[BATTLE MAP TITLE]"
        self.background_file = ""

        ##Outer Frame (To help center map)
        #self.out_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)  # , text="MapMaster DMs Map & Resource Manager" , height=1000 #TODO: Dont need this frame?
        #self.out_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")
        self.battle_map_title = UE.darkLabelTitle(self.top_frame, text=self.map_name_text)
        self.battle_map_title.grid(padx=10, pady=5, row=0, column=1, columnspan=2, sticky="N")
         ## Map Frame
        self.map_frame = UE.darkFrame(self.top_frame, bg=UE.DARKER_GREY)  # , text="MapMaster DMs Map & Resource Manager" ,height=1000
        self.map_frame.grid(padx=10, pady=10, sticky="NSEW", row=1, column=1, columnspan=2)

        ## Live Map Control Frame
        self.live_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.live_frame.grid(padx=10, pady=10, sticky="W", row=4, column=0, columnspan=2)
        ## Range and Character Control Frame
        self.range_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.range_frame.grid(padx=10, pady=10, sticky="E", row=4, column=1, columnspan=2)

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

        self.PLACEHOLDER_BUTTON = UE.darkLabelTitle(self.live_frame, text="[Live Map Active]")
        self.PLACEHOLDER_BUTTON.grid(padx=10, pady=10, row=0, column=0, sticky="S")
        self.PLACEHOLDER_BUTTON1 = UE.darkLabelTitle(self.live_frame, text="[Blackout]")
        self.PLACEHOLDER_BUTTON1.grid(padx=10, pady=10, row=0, column=1, sticky="S")
        self.PLACEHOLDER_BUTTON2 = UE.darkLabelTitle(self.live_frame, text="[Show Mask]")
        self.PLACEHOLDER_BUTTON2.grid(padx=10, pady=10, row=0, column=2, sticky="S")

        self.PLACEHOLDER_BUTTON3 = UE.darkLabelTitle(self.range_frame, text="[Cone & Areas]")
        self.PLACEHOLDER_BUTTON3.grid(padx=10, pady=10, row=0, column=0, sticky="S")
        self.PLACEHOLDER_BUTTON4 = UE.darkLabelTitle(self.range_frame, text="[Range]")
        self.PLACEHOLDER_BUTTON4.grid(padx=10, pady=10, row=0, column=1, sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[Set Scale]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10, row=0, column=2, sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[John Maddon]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10, row=0, column=3, sticky="S")



        # Save Buttons
    def save_buttons_widget(self, container, wiget_row, wiget_column):
        self.savebox = UE.darkBorderless(container)
        self.savebox.grid(padx=10, pady=5, sticky="N", row=wiget_row, column=wiget_column)
        self.open_button = UE.selectButton(self.savebox, text="Open File", command=self.open_save_game)
        self.open_button.grid(padx=10, pady=5)
        self.saveas_button = UE.selectButton(self.savebox, text="Save As", command=self.save_game)
        self.saveas_button .grid(padx=10, pady=5)
        self.save_button = UE.selectButton(self.savebox, text="Save", command=self.open_save_game)
        self.save_button.grid(padx=10, pady=5)




    def open_save_game(self):
        print("Opening File Dialog")
        try:
            file_path = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\saved_games",
                    filetypes = [("Json File", "*.json")],
                    title = "Choose a Saved .json file")
            recalled_dic = save.recall_json_map(file_path)
            print(recalled_dic)
            self.load_map_from_dic(recalled_dic)
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
            #       defaultextension=[("Json File", "*.json")],
             #      title = "Save Map as .json File")
        except:
            print("problems recalling saved file")



    def create_map_dic(self):
        map_dic = save.proto_map_dic
        map_dic["name"] = self.map_name_text
        map_dic["background"] = self.background_file
        map_item_list = self.map_canvas.find_all()
        print(map_item_list)
        print(self.icon_f_list)
        print(f"Number of icons: {len(map_item_list)}")
        print(f"Number of Files: {len(self.icon_f_list)}")
        for icon_id in map_item_list:
            print("Current Icon ID: ", icon_id)
            print(self.map_canvas.gettags(icon_id))
            tags = self.map_canvas.gettags(icon_id)
            if "icon" in tags:
            #first we need to make empty dictionary entry for this icon
                map_dic["icons"][icon_id] = {}
                coords = self.map_canvas.coords(icon_id)                             # grab the coordinates of all objects in canvas
                map_dic["icons"][icon_id]["file"] = self.icon_f_list[icon_id-1]     # subtract 1
                map_dic["icons"][icon_id]["pos_x"] = coords[0]
                map_dic["icons"][icon_id]["pos_y"] = coords[1]
                print(map_dic["icons"][icon_id])
            else:
                print("No Icon Found")
        print("End of Create Map Dictionary")
        print(map_dic)
        return map_dic

    def save_file(self, json_file):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".json")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        f.write(json_file)
        f.close()

    def load_map_from_dic(self, map_dic):
        self.battle_map_title.config(text= map_dic["name"])
        self.add_background(map_dic["background"])
        print(map_dic["icons"])
        for icons in map_dic["icons"]:      # Icons just returns a (list?) of the numbers of the dictionarys of items - AS A STRING
            print(icons)
            current_file = map_dic["icons"][icons]["file"]
            print(f"Loading File: {current_file}")
            object_id = self.add_icon(current_file)
            icon_x =  int(map_dic["icons"][icons]["pos_x"])
            icon_y =  int(map_dic["icons"][icons]["pos_y"])
            self.place_icon(icon_x, icon_y, object_id)
            #self.icon_f_list.append(icons["file"])







            #Background Images
    def background_image_widget(self, container, item_row, item_column):
        self.backgound_button = UE.selectButton(container, text="Open Background Map", command=self.select_bg_dialog)
        self.backgound_button.grid(padx=5, pady=5, row=item_row, column=item_column)
        self.delete_map_button = UE.selectButton(container, text="Delete Background Map", command=self.delete_map)
        self.delete_map_button.grid(padx=5, pady=5, row=item_row+1, column=item_column)

        #self.canvas = Canvas(self.map_frame, width=1200, height=850, bg=UE.DARKER_GREY, highlightcolor=UE.ACTIVE_BLUE, bd=0, relief="sunken") #TODO change canvas border colour
        #self.canvas.grid(sticky="NSEW", padx=5, pady=5)


    def select_bg_dialog(self):
        try:
            self.background_file = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_backgrounds")
            self.add_background(self.background_file)
        except:
            print("User Closed Dialogue Box")

    def add_background(self, file_path):
        resized_image = self.resize_map(file_path)
        bg_image = ImageTk.PhotoImage(resized_image)
        self.map_canvas.bg_image = bg_image
        bg_id = self.map_canvas.create_image(654, 438, image=self.map_canvas.bg_image,
                                             tags="background")  # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
        print(f"Background ID: {bg_id}")
        self.map_canvas.tag_lower(bg_id, 1)  ## Lower the background to the lowest position
        print("New Map Background Applied")


    # Opens image from passed filepath. Resizes image to fit background area
    def resize_map(self, filepath):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        #resize_img = ImageOps.fit(img, (900,900),method=0,bleed=0.0,centering=(0.5,0.5))
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
                    print(self.map_canvas.find_all())  # get all canvas objects ID



    #Adding Icons

    def add_icon_widget(self, container, item_row, item_column):
        self.add_icon_button = UE.selectButton(container, text="Add Icon", command=self.add_icon_dialog)
        self.add_icon_button.grid(padx=5, pady=5, row=item_row, column=item_column)
        self.add_image_button = UE.selectButton(container, text="Add Image", command=self.add_icon_dialog)
        self.add_image_button.grid(padx=5, pady=5, row=item_row+1, column=item_column)

    # Same as add icon but does not resize image
    def add_image_dialog(self):
        try:
            file_path = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_icons")
            item_id = self.add_image(file_path)
            print(f"Icon ID: {item_id}")
            self.place_icon(self.init_x, self.init_y, item_id)
            print("New Image Added")
        except:
            print("User Closed Dialogue Box")

    def add_image(self, filepath):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        #if (img.size[0] > 50) or (img.size[1] > 50):
        #    img = self.resize_image(filepath, 25, 25, )
        # self.icon_f_list.append(filepath)
        img_ref = ImageTk.PhotoImage(img)
        print(img_ref)
        self.icon_list.append(img_ref)
        item_id = len(self.icon_list)
        item_id = item_id - 1  # Because its used in an indexed 0 list later
        return item_id


    def add_icon_dialog(self):
        try:
            file_path = filedialog.askopenfilename(initialdir="D:\Pan Galactic Engineering\MapMaster\map_icons")
            item_id = self.add_icon(file_path)
            print(f"Icon ID: {item_id}")
            self.place_icon(self.init_x, self.init_y , item_id)
            print("New Icon Added")
        except:
            print("User Closed Dialogue Box")

    #Adds an icon from filepath - checks image is suitable size for icon, if too large - resizes
    def add_icon(self, filepath):               ## This needs to return ID number of the added file
        img = Image.open(filepath)
        self.icon_f_list.append(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        if (img.size[0] > 50) or (img.size[1] > 50):
            img = self.resize_image(filepath, 25, 25, )
        #self.icon_f_list.append(filepath)
        img_ref = ImageTk.PhotoImage(img)
        print(img_ref)
        self.icon_list.append(img_ref)
        item_id = len(self.icon_list)
        item_id = item_id-1   #Because its used in an indexed 0 list later
        return item_id

    #Places icon from list onto canvas
    def place_icon(self,  x, y, img_n):
        self.canvas_obj_list.append(self.map_canvas.create_image(x, y, image=self.icon_list[img_n], tags="icon"))




    def resize_image(self, filepath, Wmax, Hmax):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
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
        print("Deleting Icon")
        item = self.map_canvas.find_closest(self.cursor_x, self.cursor_y, halo=1)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
        print(item)
        for tag in self.map_canvas.gettags(item):                                    ## Check object isnt the background
            print(tag)
            if (tag == "icon"):
                self.map_canvas.delete(item)
                print(self.map_canvas.find_all())  # get all canvas objects ID

            #if (tag == "background"):
            #    print("Background Selected - exiting")
            #    break
            #else:
            #    self.map_canvas.delete(item)
            #    print(self.map_canvas.find_all())  # get all canvas objects ID





    def down(self, event):
        print("Down arrow pressed")

# Event Methods for moving icons
    def startMovement(self, event):
        self.initi_x = event.x
        self.initi_y = event.y
        #print('startMovement init', self.initi_x, self.initi_y)
        item = self.map_canvas.find_closest(self.initi_x, self.initi_y, halo=1)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
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
                print(self.map_canvas.find_all())  # get all canvas objects ID

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
            self.map_canvas["cursor"] = "hand2"
        self.cursor_x = event.x
        self.cursor_x = event.y














GUI = movingIconCanvas(root)














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''