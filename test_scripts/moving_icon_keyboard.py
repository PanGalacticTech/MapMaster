from tkinter import *
import UI_elements as UE
from PIL import Image, ImageTk, ImageOps


class moving_image_mouse():
    def __init__(self):
        self.root = Tk()
        self.root.title("Moving Icon with Keyboard")
        self.root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon256.ico")
        self.root.geometry("1000x800")
        self.root.configure(background=UE.DARK_GREY)
        self.top_frame = UE.darkFrame(self.root, bg=UE.DARKER_GREY)


        # Canvas Width
        self.canvas_width = 800
        self.canvas_height = 600
        self.icon_x = self.canvas_width // 2
        self.icon_y = self.canvas_height // 2


        self.canvas_win = Canvas(self.top_frame, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.canvas_win.grid(padx=10, pady=10)

        # add image to canvas
        icon_filepath = self.save_resize_image("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Enemy_Dot.png", 25, 25, "enemy_dot")
        img = PhotoImage(file=icon_filepath)
        self.my_img = self.canvas_win.create_image(self.icon_x, self.icon_y, image=img)  # anchor=NW

        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )

        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Up>", self.up)
        self.root.bind("<Down>", self.down)

        # Configure the row/col of our frame and root window to be resizable and fill all available space
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        self.root.mainloop()




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

    def left(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_x > 0:
            x = -10
            y = 0
            self.canvas_win.move(self.my_img, x, y)
            self.icon_x = self.icon_x + x     # This updates the global variable so we can keep track of where the item is


    def right(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_x < self.canvas_width:
            x = +10
            y = 0
            self.canvas_win.move(self.my_img, x, y)
            self.icon_x = self.icon_x + x

    def up(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_y > 0:
            x = 0
            y = -10
            self.canvas_win.move(self.my_img, x, y)
            self.icon_y = self.icon_y + y

    def down(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_y < self.canvas_height:
            x = 0
            y = +10
            self.canvas_win.move(self.my_img, x, y)
            self.icon_y = self.icon_y + y





GUI = moving_image_mouse()














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''