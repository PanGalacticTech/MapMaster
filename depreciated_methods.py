




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




def resize_map(self, basewidth, filepath):  # DEPRECIATED NOT USED ATM
    img = Image.open(filepath)
    print(filepath)
    print(img.size[0], ", ", img.size[1])
    wpercent = (basewidth / float(img.size[0]))
    print(wpercent, "%")
    hsize = int((float(img.size[1]) * float(wpercent)))
    print("New Image Size")
    print(basewidth, hsize)
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img.save('mapbackground.jpg')
    return img

# self.initi_x = c.canvasx(event.x)  # Translate mouse x screen coordinate to canvas coordinate
# self.initi_y = c.canvasy(event.y)  # Translate mouse y screen coordinate to canvas coordinate

def place_icon(self, filepath, x, y, n):
    global img
    img = PhotoImage(file=filepath)  #
    #self.img_list.append(PhotoImage(file=filepath))
    self.icon_xy[n][0] = x
    self.icon_xy[n][1] = y
    self.my_img = self.m_canvas.create_image(x, y, image=img)  # anchor=NW
    #self.icon_list = (self.m_canvas.create_image(x, y, image=img)) # anchor=NW


# Dont think this one ever worked
def place_icon(self, filepath, x, y, img_n):
    self.icon_list[img_n] = self.map_canvas.create_image(x, y, image=filepath)