'''
MapMaster Graphical User Interface

Using Tkinter

'''


import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont

#from tkinter import filedialog

#from PIL import ImageTk, Image

from tkinter import Tk, filedialog, Frame, Button, Canvas
from PIL import Image, ImageTk, ImageOps


import UI_elements as UE




#USER VARIABLES:
MAIN_WINDOW_TITLE = "MapMaster - Dungeon Master's Game Management System"

MAIN_WINDOW_WIDTH = "1600"
MAIN_WINDOW_HEIGHT = "1050"
MAIN_WINDOW_BACKGROUND = UE.DARK_GREY



'''
https://www.pythontutorial.net/tkinter/tkinter-grid/
'''







class UI_main_window():
    def __init__(self):
        # Window dims
        WIDTH = MAIN_WINDOW_WIDTH
        HEIGHT = MAIN_WINDOW_HEIGHT
        self.root = tk.Tk(className=MAIN_WINDOW_TITLE)
        # root.config(background=atk.DEFAULT_COLOR)
        self.root.geometry(WIDTH + "x" + HEIGHT)
        self.root.configure(background=UE.DARK_GREY)
        self.root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")

# it is recommended to select tkinter theme required for things to be right on windows,
# 'alt', 'default', or 'classic' work fine on windows
        self.s = ttk.Style()
        self.s.theme_use('classic')                    # self.s ?!/ no idea

        self.title_font = TkFont.Font(family='Consolas', size=24, weight='bold')
        self.norm_font = TkFont.Font(family='Consolas', size=10)
        #self.ft_title = UE.title_font
        #self.ft_norm   = UE.norm_font

        ## Set out global variables





        ## First Set out top Frame

        ## Top Frame
        self.top_frame = UE.darkFrame(self.root, bg=UE.DARKER_GREY,  height=1000)   #, text="MapMaster DMs Map & Resource Manager"
        self.top_frame.grid(padx=10, pady=10, sticky="NSEW")                         #

        # configure the grid for top frame
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        # Side Button Frame
        self.side_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.side_frame.grid(column=0, sticky="NW", padx=10, pady=10)

        # Button Placeholders
        self.PLACEHOLDER_TEXT = UE.darkLabelTitle(self.side_frame, text="[Open Map]")
        self.PLACEHOLDER_TEXT.grid( padx=10, pady=10,sticky="NSEW", row= 0)
        self.PLACEHOLDER_TEXT2 = UE.darkLabelTitle(self.side_frame, text="[Save Map]")
        self.PLACEHOLDER_TEXT2.grid(padx=10, pady=10, sticky="NSEW",row= 1)
        self.PLACEHOLDER_TEXT3 = UE.darkLabelTitle(self.side_frame, text="[Add Icon]")
        self.PLACEHOLDER_TEXT3.grid(padx=10, pady=10, sticky="NSEW",row= 3)
        self.PLACEHOLDER_TEXT3 = UE.darkLabelTitle(self.side_frame, text="[Create Token]")
        self.PLACEHOLDER_TEXT3.grid(padx=10, pady=10, sticky="NSEW", row=4)
        self.PLACEHOLDER_TEXT5 = UE.darkLabelTitle(self.side_frame, text="[Map Filters]")
        self.PLACEHOLDER_TEXT5.grid(padx=10, pady=10, sticky="NSEW", row=6)


        # Object Palette
        self.object_frame = UE.darkFrame(self.side_frame, bg=UE.BLACK)
        self.object_frame.grid(column=0, padx=10, pady=10, row=2)
        self.palette_title = UE.darkLabel(self.object_frame, text="[Object Palette]")
        self.palette_title.grid(column=0, row=0, padx=10, pady=10, sticky="N", columnspan=2)

        # Object Items
        self.PLACEHOLDER_ICON = UE.darkLabel(self.object_frame, text="[Icon1]")
        self.PLACEHOLDER_ICON.grid(column=0, row=1, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON2 = UE.darkLabel(self.object_frame, text="[Icon2]")
        self.PLACEHOLDER_ICON2.grid(column=1, row=1, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON3 = UE.darkLabel(self.object_frame, text="[Icon3]")
        self.PLACEHOLDER_ICON3.grid(column=0, row=2, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_ICON4 = UE.darkLabel(self.object_frame, text="[Icon4]")
        self.PLACEHOLDER_ICON4.grid(column=1, row=2, padx=10, pady=10, sticky="NSEW")

        ##Outer Frame (To help center map)
        self.out_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK, height=1000)  # , text="MapMaster DMs Map & Resource Manager"  #TODO: Dont need this frame?
        self.out_frame.grid( row=0, column=1, padx=10, pady=10, sticky="NSEW")
        self.PLACEHOLDER_MAP_TITLE = UE.darkLabelTitle(self.out_frame, text="[BATTLE MAP TITLE]")
        self.PLACEHOLDER_MAP_TITLE.grid(padx=10, pady=10, row=0, column=0, columnspan=2, sticky="NSEW")

        ## Map Frame
        self.map_frame = UE.darkFrame(self.out_frame, bg=UE.DARKER_GREY,  height=1000)  # , text="MapMaster DMs Map & Resource Manager"
        self.map_frame.grid(padx=10, pady=10, sticky="NSEW", row=1, column=0, columnspan=2)

        ##self.MAP_PLACEHOLDER = UE.darkLabel(self.map_frame, text="[Map Missing]")          #TODO: change this so only shows when map not loaded
        ##self.MAP_PLACEHOLDER.grid(padx=10, pady=10, sticky="NSEW", row=1, column=0)

        ## Bottom Button Frame
        #self.down_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)  # , text="MapMaster DMs Map & Resource Manager"
        #self.down_frame.grid(padx=10, pady=10, row=4, column=0, columnspan=2) #, sticky="S"

        ## Live Map Control Frame

        self.live_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.live_frame.grid(padx=10, pady=10, sticky="W", row=4, column=0, columnspan=2)

        self.PLACEHOLDER_BUTTON = UE.darkLabelTitle(self.live_frame, text="[Live Map Active]")
        self.PLACEHOLDER_BUTTON.grid(padx=10, pady=10,row=0, column=0, sticky="S")
        self.PLACEHOLDER_BUTTON1 = UE.darkLabelTitle(self.live_frame, text="[Blackout]")
        self.PLACEHOLDER_BUTTON1.grid(padx=10, pady=10,row=0, column=1,sticky="S")
        self.PLACEHOLDER_BUTTON2 = UE.darkLabelTitle(self.live_frame, text="[Show Mask]")
        self.PLACEHOLDER_BUTTON2.grid(padx=10, pady=10, row=0, column=2,sticky="S")

        ## Range and Character Control Frame
        self.range_frame = UE.darkFrame(self.top_frame, bg=UE.BLACK)
        self.range_frame.grid(padx=10, pady=10, sticky="E", row=4, column=1, columnspan=2)

        self.PLACEHOLDER_BUTTON3 = UE.darkLabelTitle(self.range_frame, text="[Cone & Areas]")
        self.PLACEHOLDER_BUTTON3.grid(padx=10, pady=10, row=0, column=0,sticky="S")
        self.PLACEHOLDER_BUTTON4 = UE.darkLabelTitle(self.range_frame, text="[Range]")
        self.PLACEHOLDER_BUTTON4.grid(padx=10, pady=10,row=0,  column=1,sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[Set Scale]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10,row=0, column=2,sticky="S")
        self.PLACEHOLDER_BUTTON5 = UE.darkLabelTitle(self.range_frame, text="[John Maddon]")
        self.PLACEHOLDER_BUTTON5.grid(padx=10, pady=10, row=0, column=3, sticky="S")


        # Return the name and location of the file.
        #self.file_dialog = filedialog.askopenfilename(initialdir="/Pictures", title="select a file",
        #                                       filetypes=(("png files", "*.jpg"), ("all file", "*.*")))

        # Display dir of file selected
        #my_lbl = Label(self.file_dialog_box, text=filedialog.filename).grid()

        # Display image
        #my_img = ImageTk.PhotoImage(Image.open(root.filename))
        #my_lbl2 = Label(image=my_img).grid()


        ## Buttons and Widgets Go Here

        self.background_image_widget()

        self.root.mainloop()                              #end of Main UI Window call



    def background_image_widget(self):
        self.select = UE.selectButton(self.side_frame, text="Open Background Map", command=self.select_background)
        self.select.grid(padx=5, pady=5)
        self.canvas = Canvas(self.map_frame, width=1200, height=850, bg=UE.DARKER_GREY, highlightcolor=UE.ACTIVE_BLUE, bd=0, relief="sunken") #TODO change canvas border colour
        self.canvas.grid(sticky="NSEW", padx=5, pady=5)


    def select_background(self):
        try:
            file_path = filedialog.askopenfilename()
            resized_image = self.resize_image(file_path)
            bg_image = ImageTk.PhotoImage(resized_image)
            self.canvas.bg_image = bg_image
            self.canvas.create_image(600,425, image=self.canvas.bg_image) # ,anchor="s" # (Numbers specify the CENTER of the image- FFS NOT WELL DOCUMENTED AT ALL WANKERS)
            print("New Map Background Applied")
        except:
            print("User Closed Dialogue Box")

    def resize_map(self, basewidth, filepath):   # DEPRECIATED NOT USED ATM
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0],", ",img.size[1])
        wpercent = (basewidth / float(img.size[0]))
        print(wpercent,"%")
        hsize = int((float(img.size[1]) * float(wpercent)))
        print("New Image Size")
        print(basewidth,hsize)
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        #img.save('mapbackground.jpg')
        return img


    def resize_image(self, filepath):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        #resize_img = ImageOps.fit(img, (900,900),method=0,bleed=0.0,centering=(0.5,0.5))
        img.thumbnail((1000,850))    #Needs to be passed type tuple ## This does NOT RETURN IMAGE. it works on img object
        print("New Image Size")
        print(img.size[0],img.size[1])
        return img


#TODO: https://www.youtube.com/watch?v=Z4zePg2M5H8  Watch how to code drag and drop tomorrow
'''
NOTES
https://www.youtube.com/watch?v=Z4zePg2M5H8  # How to do drag and drop py

https://pillow.readthedocs.io/en/stable/reference/Image.html#examples
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

https://stackoverflow.com/questions/65473027/python3-open-image-with-dialog-box-in-tkinter
https://stackoverflow.com/questions/53912628/how-to-open-the-filedialog-after-pressing-the-button
https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter
https://pythonguides.com/python-tkinter-canvas/
ImageOps.fit(image, size, method, bleed, centering) => image
Syntax: PIL.ImageOps.fit(image, size, method=0, bleed=0.0, centering=(0.5, 0.5))

Parameters:
image – The image to size and crop.
size – The requested output size in pixels, given as a (width, height) tuple.
method – What resampling method to use. Default is PIL.Image.NEAREST.
bleed – Remove a border around the outside of the image from all four edges.
centering – Control the cropping position.

Use (0.5, 0.5) for center cropping (e.g. if cropping the width, take 50% off of the left side, and therefore 50% off the right side).
(0.0, 0.0) will crop from the top left corner (i.e. if cropping the width, take all of the crop off of the right side, and if cropping the height, take all of it off the bottom).
(1.0, 0.0) will crop from the bottom left corner, etc. (i.e. if cropping the width, take all of the crop off the left side, and if cropping the height take none from the top, and therefore all off the bottom).
Returns: An image.
'''