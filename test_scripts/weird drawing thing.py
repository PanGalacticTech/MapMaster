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


        self.m_canvas = Canvas(self.top_frame, width=self.canvas_width, height=self.canvas_height, bg=UE.DARK_GREY)
        self.m_canvas.grid(padx=10, pady=10)

        #List to hold images/references
        self.icon_list = []
        self.img_list = []

        # add image to canvas
        icon_filepath = self.save_resize_image("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Enemy_Dot.png", 25, 25, "enemy_dot")
        self.temp_icon_filepath = icon_filepath
        self.place_icon(self.temp_icon_filepath, self.icon_x, self.icon_y, 0)

        #
        # add 2nd image
        icon2_path = self.save_resize_image("D:\Pan Galactic Engineering\MapMaster\\test_scripts\\test_icons\Enemy_Dot.png", 25, 25, "enemy_dot2")
        icon2_newpath = self.img_recolor(icon2_path, 0, 0, 0, "enemy_dot2")
        self.place_icon(icon2_newpath, self.icon_x+50, self.icon_y+50, 1)


        # Label to output xy of mouse
        self.mouse_label = UE.colorLabel(self.top_frame, text="Mouse: ",bg=UE.DARKER_GREY, fg=UE.grey_picker(0.65))
        self.mouse_label.grid(padx=10, pady=10, sticky="SE")

        # Draw a Circle
        # circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )

        #self.root.bind("<Left>", self.left)
        #self.root.bind("<Right>", self.right)
        #self.root.bind("<Up>", self.up)
        #self.root.bind("<Down>", self.down)

        self.m_canvas.bind("<B1-Motion>", self.move)

        #self.m_canvas.bind("<Double-B1", self.move)  # Double click binding (We will use this later)





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

    def place_icon(self, filepath, x, y, n):
        #global img
        #img = PhotoImage(file=filepath)  #
        self.img_list.append(PhotoImage(file=filepath))
        self.icon_x = x
        self.icon_y = y
       # self.my_img = self.m_canvas.create_image(x, y, image=img)  # anchor=NW
        self.icon_list.append(self.m_canvas.create_image(x, y, image=self.img_list[n])) # anchor=NW

    def move(self, event):
        #print("X: ",self.icon_x, event.x, "Y:", self.icon_y, event.y)
        self.mouse_label.config(text="Mouse: " + str(event.x) + ", " + str(event.y))
        if self.in_xy_range(self.icon_x, self.icon_y , event.x , event.y, 25):
            self.place_icon(self.temp_icon_filepath, event.x, event.y, 0)



    def left(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_x > 0:
            x = -10
            y = 0
            self.canvas_win.move(self.icon_list[0], x, y)
            self.icon_x = self.icon_x + x     # This updates the global variable so we can keep track of where the item is


    def right(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_x < self.canvas_width:
            x = +10
            y = 0
            self.canvas_win.move(self.icon_list[0], x, y)
            self.icon_x = self.icon_x + x

    def up(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_y > 0:
            x = 0
            y = -10
            self.canvas_win.move(self.icon_list[0], x, y)
            self.icon_y = self.icon_y + y

    def down(self, event):
        print(self.icon_x, self.icon_y)
        if self.icon_y < self.canvas_height:
            x = 0
            y = +10
            self.canvas_win.move(self.icon_list[0], x, y)
            self.icon_y = self.icon_y + y

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


    def img_recolor(self, filepath, r, g, b, new_filename):
        img = Image.open(filepath)
        img = img.convert("RGBA")
        bands = img.split()
        bands[0].point(lambda i:i*0+204)
        bands[1].point(lambda i:i * 0)
        bands[2].point(lambda i:i * 0)
        img2 = Image.merge("RGBA",( bands[0], bands[1], bands[2], bands[3]))
        new_filepath = "D:\Pan Galactic Engineering\MapMaster\map_icons\\" + new_filename + ".png"
        img2.save(new_filepath)
        return new_filepath





GUI = moving_image_mouse()














'''
https://www.youtube.com/watch?v=Z4zePg2M5H8  Moving Icons with Mouse

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
'''