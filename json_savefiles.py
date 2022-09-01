'''
  Creating and Recalling json save files

'''

#import tkFileDialog

import json

import io

# Prototype Icon dictionary
proto_icon_dic = {
        1: {
        "file"  : "",
        "ref" : "",
        "pos_x" : 0,
        "pos_y" : 0,
        "tag"   : ""
        }
}

#Example Saved Map - Used for loading at start

saved_map = {
    "name": "Bullywug Cavern",
    "background" : "\map_backgrounds\Froghemoth Bullywug Caverns.jpg",
    "icons" : {
        1: {
        "file" : "\map_icons\Silver.png",
        "pos_x" : 970,
        "pos_y" : 700,
        "tag" : "icon",
        "id_tag" : "icon1",
        },
        2: {
        "file" : "\map_icons\Meridith.png",
        "pos_x" : 1000,
        "pos_y" : 700,
        "tag" : "icon",
        "id_tag" :"icon2",
        },
        3: {
        "file" : "\map_icons\Coal.png",
        "pos_x" : 1030,
        "pos_y" : 700,
        "tag" : "icon",
        "id_tag": "icon3",
        },
        4: {
        "file" : "\map_icons\Faen.png",
        "pos_x" : 1060,
        "pos_y" : 700,
        "tag" : "icon",
        "id_tag": "icon4",
        },
        5: {
        "file" : "\map_icons\\1_red.png",
        "pos_x" : 20,
        "pos_y" : 60,
        "tag" : "icon",
        "id_tag": "icon5",
        },
        6: {
        "file" : "\map_icons\\2_orange.png",
        "pos_x" : 20,
        "pos_y" : 80,
        "tag" : "icon",
        "id_tag": "icon6",
        },
        7: {
        "file" : "\map_icons\\3_yellow.png",
        "pos_x" : 20,
        "pos_y" : 100,
        "tag" : "icon",
        "id_tag": "icon7",
        },
        8: {
        "file" : "\map_icons\\4_lime.png",
        "pos_x" : 20,
        "pos_y" : 120,
        "tag" : "icon",
        "id_tag": "icon8",
        },
        9: {
        "file" : "\map_icons\\5_green.png",
        "pos_x" : 20,
        "pos_y" : 140,
        "tag" : "icon",
        "id_tag": "icon9",
        },
        10: {
        "file" : "\map_icons\\6_aqua.png",
        "pos_x" : 20,
        "pos_y" : 160,
        "tag" : "icon",
        "id_tag": "icon10",
        },
        11: {
        "file" : "\map_icons\\7_sky.png",
        "pos_x" : 20,
        "pos_y" : 180,
        "tag" : "icon",
        "id_tag": "icon11",
        },
        12: {
        "file" : "\map_icons\\8_blue.png",
        "pos_x" : 20,
        "pos_y" : 200,
        "tag" : "icon",
        "id_tag" : "icon12"
        },
        13: {
        "file" : "\map_icons\\9_purple.png",
        "pos_x" : 20,
        "pos_y" : 220,
        "tag" : "icon",
        "id_tag" : "icon13",
        },
        14: {
        "file" : "\map_icons\\10_pink.png",
        "pos_x" : 20,
        "pos_y" : 240,
        "tag" : "icon",
        "id_tag" : "icon14",
        }
    }
}


proto_map_dic = {
    "name": "",
    "background" : "",
    "icons" : {
        1: {
        "file" : "",
        "pos_x" : 0,
        "pos_y" : 0,
        },
        2: {
        "file" : "",
        "pos_x" : 0,
        "pos_y" : 0,
        }
    }
}





'''

'''


# Accessing this dictionary
#print(saved_map["name"])
#print(saved_map["icons"][13])
#print(saved_map["icons"][13]["file"])

# Convert to JSON

#output_json = json.dumps(saved_map, indent=4 ) #, sort_keys=True

#print(output_json)

#output_dictionary = json.loads(output_json)

#print(output_dictionary)


# -*- coding: utf-8 -*-
#import json

# Make it work for Python 2+3 and with Unicode

#try:
#    to_unicode = unicode
#except NameError:
#    to_unicode = str


# Write JSON file

def return_json_str(map_object):
    map_name = map_object["name"]
    json_str = json.dumps(map_object, indent=4, separators=(',', ': '), ensure_ascii=False)  # sort_keys=True
    return json_str

'''
def file_save(json_string):
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    #text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(json_string)
    f.close() # `()` was missing
'''


def save_json_map(map_object):
    map_name = map_object["name"]
    filename = map_name + ".json"
    print(f"Saving Map As File: {filename}")
    with io.open(filename, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(saved_map, indent=4, separators=(',', ': '), ensure_ascii=False) #sort_keys=True
        #outfile.write(to_unicode(str_))
        outfile.write(str_)

    # Read JSON file
    recall_json_map(filename)
    print(saved_map == data_loaded)


def recall_json_map(filename):
    print(f"Opening File: {filename}")
    try:
        with open(filename) as save_file:
            data_loaded = json.load(save_file)
        return data_loaded
    except:
        print("Problem Loading File, check file name")
        return 0

