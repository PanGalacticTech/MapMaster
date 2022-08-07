from PIL import Image


def in_range(valA, valB, range):
    if (valA < valB + range and valA > valB - range):
        print("in Range")
        return True
    else:
        return False

def in_xy_range(obj_x, obj_y, m_x, m_y, range):
    if (in_range(obj_x, m_x, range) and in_range(obj_y, m_y, range)):
        print("in X & Y Range")
        return True
    else:
        return False


#in_range(10, 20, 25)

#in_xy_range(10, 100, 20, 122, 25)


