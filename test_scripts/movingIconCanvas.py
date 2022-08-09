from tkinter import *
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps


root = Tk()
root.geometry("1000x800")
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
        self.canvas_width = 800
        self.canvas_height = 600
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

        # Check image size and Add image to ref list
        self.add_image("D:\Pan Galactic Engineering\MapMaster\map_icons\enemy_dot.png")
        # Place image on canvas
        self.canvas_obj_list.append(self.map_canvas.create_image(self.init_x, self.init_y, image=self.icon_list[0]))

        self.add_image("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Orange_Dot.png")
        # Place image on canvas
        self.canvas_obj_list.append(self.map_canvas.create_image(self.init_x, self.init_y, image=self.icon_list[1]))

        # Label to output xy of mouse
        self.mouse_label = UE.colorLabel(self.top_frame, text="Mouse: ",bg=UE.DARKER_GREY, fg=UE.grey_picker(0.65))
        self.mouse_label.grid(padx=10, pady=10, sticky="SE")

        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )

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



    def startMovement(self, event):
        print("startMovement")
        self.__move = True
        #self.initi_x = c.canvasx(event.x)  # Translate mouse x screen coordinate to canvas coordinate
        #self.initi_y = c.canvasy(event.y)  # Translate mouse y screen coordinate to canvas coordinate
        self.initi_x = event.x
        self.initi_y = event.y
        #print('startMovement init', self.initi_x, self.initi_y)
        self.movingimage = self.map_canvas.find_closest(self.initi_x, self.initi_y, halo=1)  # get canvas object ID of where mouse pointer is
        print(self.movingimage)
        print(self.map_canvas.find_all())  # get all canvas objects ID

    def stopMovement(self, event):
        print("stopMovement")
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



    def add_image(self, filepath):
        img = Image.open(filepath)
        print(filepath)
        print(img.size[0], ", ", img.size[1])
        if (img.size[0] > 50) or (img.size[1] > 50):
            img = self.resize_image(filepath, 25, 25, )
        #self.icon_f_list.append(filepath)
        img_ref = ImageTk.PhotoImage(img)
        self.icon_list.append(img_ref)

    def place_image(self, filepath, x, y, img_n):
        self.icon_list[img_n] = self.map_canvas.create_image(x, y, image=filepath)


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

    def place_icon(self, filepath, x, y, n):
        global img
        img = PhotoImage(file=filepath)  #
        #self.img_list.append(PhotoImage(file=filepath))
        self.icon_xy[n][0] = x
        self.icon_xy[n][1] = y
        self.my_img = self.m_canvas.create_image(x, y, image=img)  # anchor=NW
        #self.icon_list = (self.m_canvas.create_image(x, y, image=img)) # anchor=NW









    def in_xy_range(self, obj_x, obj_y, m_x, m_y, range):
        if (self.in_range(obj_x, m_x, range) and self.in_range(obj_y, m_y, range)):
            return True
        else:
            return False

    def in_range(self, valA, valB, range):
        if (valA < valB + range and valA > valB - range):
            return True
        else:
            return False






GUI = movingIconCanvas(root)














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''