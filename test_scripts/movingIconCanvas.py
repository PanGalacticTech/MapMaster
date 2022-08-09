from tkinter import *
from tkinter import filedialog
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps


root = Tk()
root.geometry("1600x1050")
root.title("Moving Icons with Mouse")
root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")

ICON_SIZE = 25   # pixel val for new icons


'''
Using Method from:
https://stackoverflow.com/questions/42322966/how-to-display-and-move-multiple-images-as-same-image-in-same-time-python-tkinte
'''

class movingIconCanvas:
    def __init__(self, root):
        self.root = root
        self.top_frame = UE.darkFrame(self.root, bg=UE.DARKER_GREY)
        # Canvas Width
        self.canvas_width = 1200
        self.canvas_height = 850
        self.map_canvas = Canvas(self.top_frame, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.map_canvas.grid(padx=10, pady=10)
        self.__move = False

        self.init_x = self.canvas_width // 2
        self.init_y = self.canvas_height // 2

        #List to hold images/references

        self.icon_f_list = []    # Holds Filelinks to images
        self.icon_list = []      # hold img_refs
        self.icon_xy = []        # holds list of list of xy positions
        self.canvas_obj_list = [] #??? Holds objects once in canvas? IDK
        self.icon_no = 0           # Dont like this but currently used to track new items into the array

        # Check image size and Add image to ref list
        self.add_icon("D:\Pan Galactic Engineering\MapMaster\map_icons\enemy_dot.png")
        # Place image on canvas
        self.place_icon(self.init_x, self.init_y, self.icon_no)

        self.add_icon("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Orange_Dot.png")
        # Place image on canvas
        self.canvas_obj_list.append(self.map_canvas.create_image(self.init_x, self.init_y, image=self.icon_list[1]))

        # Label to output xy of mouse
        self.mouse_label = UE.colorLabel(self.top_frame, text="Mouse: ",bg=UE.DARKER_GREY, fg=UE.grey_picker(0.65))
        self.mouse_label.grid(padx=10, pady=10, sticky="SE")


        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )

        self.background_image_widget(self.top_frame)
        self.add_icon_widget(self.top_frame)

        #self.root.bind("<Left>", self.left)
        #self.root.bind("<Right>", self.right)
        #self.root.bind("<Up>", self.up)
        #self.root.bind("<Down>", self.down)

        self.map_canvas.bind("<Button-1>", self.startMovement)
        self.map_canvas.bind("<ButtonRelease-1>", self.stopMovement)
        self.map_canvas.bind("<Motion>", self.movement)

        #self.m_canvas.bind("<Double-B1", self.move)  # Double click binding (We will use this later)





        # Configure the row/col of our frame and root window to be resizable and fill all available space
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)



        self.root.mainloop()





    #Background Images
    def background_image_widget(self, container):
        self.backgound_button = UE.selectButton(container, text="Open Background Map", command=self.select_bg_dialog)
        self.backgound_button.grid(padx=5, pady=5)
        #self.canvas = Canvas(self.map_frame, width=1200, height=850, bg=UE.DARKER_GREY, highlightcolor=UE.ACTIVE_BLUE, bd=0, relief="sunken") #TODO change canvas border colour
        #self.canvas.grid(sticky="NSEW", padx=5, pady=5)


    def select_bg_dialog(self):
        try:
            file_path = filedialog.askopenfilename()
            resized_image = self.resize_map(file_path)
            bg_image = ImageTk.PhotoImage(resized_image)
            self.map_canvas.bg_image = bg_image
            bg_id = self.map_canvas.create_image(600,425, image=self.map_canvas.bg_image, tags="background") # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
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

    def add_icon_widget(self, container):
        self.add_icon_button = UE.selectButton(container, text="Add Icon", command=self.add_icon_dialog)
        self.add_icon_button.grid(padx=5, pady=5)


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