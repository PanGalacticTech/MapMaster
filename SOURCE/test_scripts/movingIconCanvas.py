from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps
import tkinter.font as TkFont

root = Tk()
root.geometry("1600x1100")
root.title("MapMaster DM's Tool")
root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")





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
        self.icon_no = 0           # Dont like this but currently used to track new items into the array




        # Check image size and Add image to ref list
        try:
            print("WTF")
            #self.add_icon("D:\Pan Galactic Engineering\MapMaster\map_icons\enemy_dot.png")
        # Place image on canvas
            #self.place_icon(self.init_x, self.init_y, self.icon_no)

            #self.add_icon("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Orange_Dot.png")
        # Place image on canvas
            #self.canvas_obj_list.append(self.map_canvas.create_image(self.init_x, self.init_y, image=self.icon_list[1]))

        except:
            print("Icons Not Found - Skipping")




        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )



        #self.root.bind("<Left>", self.left)
        #self.root.bind("<Right>", self.right)
        #self.root.bind("<Up>", self.up)
        #self.root.bind("<Down>", self.down)

        self.map_canvas.bind("<Button-1>", self.startMovement)
        self.map_canvas.bind("<ButtonRelease-1>", self.stopMovement)
        self.map_canvas.bind("<Motion>", self.movement)
        self.map_canvas.bind("<Del>", self.delete_icon)

        #self.m_canvas.bind("<Double-B1", self.move)  # Double click binding (We will use this later)








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
        self.add_icon_widget(self.side_frame, 3, 0)


        ##Outer Frame (To help center map)
        #self.out_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)  # , text="MapMaster DMs Map & Resource Manager" , height=1000 #TODO: Dont need this frame?
        #self.out_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")
        self.battle_map_title = UE.darkLabelTitle(self.top_frame, text="[BATTLE MAP TITLE]")
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
        self.PLACEHOLDER_TEXT3.grid(padx=10, pady=10, sticky="NSEW", row=4)
        self.PLACEHOLDER_TEXT5 = UE.darkLabelTitle(self.side_frame, text="[Map Filters]")
        self.PLACEHOLDER_TEXT5.grid(padx=10, pady=10, sticky="NSEW", row=6)

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
        self.open_button = UE.selectButton(self.savebox, text="Open File", command=self.open_file)
        self.open_button.grid(padx=10, pady=5)
        self.saveas_button = UE.selectButton(self.savebox, text="Save As", command=self.open_file)
        self.saveas_button .grid(padx=10, pady=5)
        self.save_button = UE.selectButton(self.savebox, text="Save", command=self.open_file)
        self.save_button.grid(padx=10, pady=5)



    def open_file(self):
        print("Opening File Dialog")


    #Background Images
    def background_image_widget(self, container, item_row, item_column):
        self.backgound_button = UE.selectButton(container, text="Open Background Map", command=self.select_bg_dialog)
        self.backgound_button.grid(padx=5, pady=5, row=item_row, column=item_column)
        #self.canvas = Canvas(self.map_frame, width=1200, height=850, bg=UE.DARKER_GREY, highlightcolor=UE.ACTIVE_BLUE, bd=0, relief="sunken") #TODO change canvas border colour
        #self.canvas.grid(sticky="NSEW", padx=5, pady=5)


    def select_bg_dialog(self):
        try:
            file_path = filedialog.askopenfilename()
            resized_image = self.resize_map(file_path)
            bg_image = ImageTk.PhotoImage(resized_image)
            self.map_canvas.bg_image = bg_image
            bg_id = self.map_canvas.create_image(654,438, image=self.map_canvas.bg_image, tags="background") # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
            print(f"Background ID: {bg_id}")
            self.map_canvas.tag_lower(bg_id, 1)    ## Lower the background to the lowest position
            print("New Map Background Applied")
        except:
            print("User Closed Dialogue Box")


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


    #Adding Icons

    def add_icon_widget(self, container, item_row, item_column):
        self.add_icon_button = UE.selectButton(container, text="Add Icon", command=self.add_icon_dialog)
        self.add_icon_button.grid(padx=5, pady=5, row=item_row, column=item_column)


    def add_icon_dialog(self):
        try:
            file_path = filedialog.askopenfilename()
            item_id = self.add_icon(file_path)
            print(f"Icon ID: {item_id}")
            self.place_icon(self.init_x, self.init_y , item_id)
            print("New Icon Added Applied")
        except:
            print("User Closed Dialogue Box")

    #Adds an icon from filepath - checks image is suitable size for icon, if too large - resizes
    def add_icon(self, filepath):               ## This needs to return ID number of the added file
        img = Image.open(filepath)
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
        self.canvas_obj_list.append(self.map_canvas.create_image(x, y, image=self.icon_list[img_n]))




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
    def delete_icon(self, event):
        print("Deleting Icon")


# Event Methods for moving icons
    def startMovement(self, event):
        self.initi_x = event.x
        self.initi_y = event.y
        #print('startMovement init', self.initi_x, self.initi_y)
        item = self.map_canvas.find_closest(self.initi_x, self.initi_y, halo=1)  # get canvas object ID of where mouse pointer is  try [0] after this line? seen it on anothe solution
        for tag in self.map_canvas.gettags(item):                                    ## Check object isnt the background
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














GUI = movingIconCanvas(root)














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''