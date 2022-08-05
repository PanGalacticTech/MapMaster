from tkinter import *

import UI_elements as UE


root = Tk()
root.title("Moving Icon with Keyboard")
root.iconbitmap("D:\Pan Galactic Engineering\MapMaster\Icons\MapMaster_Icon.bmp")
root.geometry("800x600")



#Canvas Width
w = 600
h = 400
x = w//2
y = h//2

canvas_win = Canvas(root, width=w, height=h, bg=UE.DARK_GREY)
canvas_win.grid(padx=10, pady=10)


# add image to canvas
#img = PhotoImage("D:\Pan Galactic Engineering\MapMaster\test_scripts\test_icons\Enemy_Dot-01.png")
#my_img = canvas_win.create_image(260,125, anchor=NW, image=img)

# Draw a Circle
circle_icon = canvas_win.create_oval(x, y, x+30, y+30, width=2, fill="orange" )





def left(event):
    x = -10
    y = 0
    canvas_win.move(circle_icon, x, y)

def right(event):
    x = +10
    y = 0
    canvas_win.move(circle_icon, x, y)

def up(event):
    x = 0
    y = -10
    canvas_win.move(circle_icon, x, y)

def down(event):
    x = 0
    y = +10
    canvas_win.move(circle_icon, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


root.mainloop()



'''
https://www.youtube.com/watch?v=xifcE6xvnyg&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=69  Moving Icons with Arrow Keys
'''