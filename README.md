# MapMaster V1.0 - Alpha Release
## DM's Virtual Tabletop Tool
DMs Map Manager - Virtual Tabletop Software with DM Screen and Live Map Window. Designed live streaming of battle, world and town maps & combat management.

![image](https://user-images.githubusercontent.com/53580358/187942315-fe25e3a0-fd7a-435d-83c9-bdf126443dd4.png)

If you use/enjoy this software, consider [buying me a coffee](https://ko-fi.com/imogenwren).

### Virtual Tabletop Functions
_This **free** and **Open Source** virtual tabletop software currently has the following functions._
- Set Image generated with online or offline mapmaking tools as background
- Insert Icons and Images for player tokens & meeples
- Save and Recall progress, allowing combat encounters to easily resume on the next session
- Set masked areas that block players from seeing further than they are able.
- DMs Screen and seperate players window to use via screen share or 2nd monitor
- Designed to make sharing maps over discord or video conferenceing easy and clean using window share
- Easy intergration into live streaming setups. Clean interface for streaming.


## Installing:
Download zippled .exe file from releases. It is best to keep this bundled with the folders contained in this folder:
- Icons
- logs
- map_backgrounds
- map_icons
- saved_games

You can also compile yourself using `compile_exe.py` in the SOURCE folder. Feel free to adapt and use this software as you wish.

## Using MapMaster

MapMaster opens with default map & icons loaded. <br>

### Changing The Background
To change background image, select `Open Background Map` <br>
Then select a new image to insert as the background. I use [Inkcarnate](https://inkarnate.com/maps/) to create my maps, then screenshot and save the files into the
`map_backgrounds` folder. MapMaster will resize the image to fit the window.

### Adding & Deleting Icons & Images
#### Icons
Adding new icons using image files is accomplished by selecting `Add Icon` and selecting any image file. Adding an image as an Icon, will reduce its size down to **25x25px**. For this reason it is best to use icons that remain clear at this small size. I included some examples in the default map, using bright colours and large text. I used [draw.io](https://app.diagrams.net/) to create all the icons, then imported them into graphics software to remove the background and export as a transparent PNG. You can also use player character pictures and artwork.
- To Be Added: I want to include a slider to increase or decrease the size of player Icons.

#### Images
Adding images is a similar process to Icons, select `Add Image` and select an image file to insert. Images are NOT resized to fit the window. I wish to add this feature in the future. But for now, either use the python script included in SOURCE `XXXXXX(Coming Soon)` To quickly resize and save images at a suitable size, or resize them using your favourite image editor. I tend to use images to show players artwork, eg of a monster they have just encountered, but then use Icons for combat encounters. I mostly added this to avoid having to drop images into group chat.
- To Be Added: I want to include a slider to increase or decrease the size of Inserted Images.

![image](https://user-images.githubusercontent.com/53580358/187944880-311692dc-4197-458a-9181-c292dbcb8e78.png)
_Insert an image of a large troll to shock your players into running away like cowards_

#### Deleting Icons and Images
Deleting an icon or image is done by dragging it towards the top left hand corner of the DM's map, and pressing the delete button. I wish to improve the function of this in later releases.

### The Live Map
The live map is intended as the window the players can view. It lets the DM hide parts of the map, images and tokens they may be arranging out of sight of the players.
If using MapMaster for Discord or Zoom games, or for Streaming Setups, the Live Map should be activated with `Activate Live Map`, and this window can be set as the source for Video Conferencing or Window Capture in streaming setups.

#### Live Map View with Mask Set
If your players are trapped in a dungeon, make sure they can only see as far as the nearest doorway.
![image](https://user-images.githubusercontent.com/53580358/187944434-8859e05e-5b4c-4073-8d90-077abfb3ba01.png)


### Map Mask
To set a map mask, click the `Show Mask` button. This will show a grid and the current applied mask on the DM's Screen map. The Current Applied Mask will ALWAYS be visible on the Live Map, letting the DM pre-select a mask, ensuring the players dont get to see a dungeon layout or hidden trap that they shouldnt be able to see yet.
The live map mask will update when the DM's Screen Map Mask is closed using `Hide Mask` 
Use the `Add Mask` and `Subtract Mask` buttons to add or remove mask squares. `Clear Mask` will both clear the entire mask, and update the live map, so use with care. I will change the function of this later to avoid mistakes. <br><br>

_The mask can be set on the DM's screen, then applied to the Live Map._
##### Setting the Mask DM's View 
![image](https://user-images.githubusercontent.com/53580358/187763344-93782c36-8850-483e-850b-ba7e16ba25d5.png)
##### Applied Mask on Players Window
![image](https://user-images.githubusercontent.com/53580358/187764725-d6034b7a-d337-4e55-b162-6a0a41ab41c8.jpg)
<br><br>
_Have enemies lurking just out of sight for a more realistic reveal of the world around your players_ <br><br>
__Players View__
![image](https://user-images.githubusercontent.com/53580358/187945792-f96c449a-1f56-4ba7-a6c4-3144d002152b.png)
__DM's View__
![image](https://user-images.githubusercontent.com/53580358/187946089-9fb7aeb6-7123-48ab-bb25-e4905859dbae.png)




### Blackout
Blackout is set with the `Blackout` button. It applies a black mask to the entire Live Map screen, allowing for scene changes out of sight of the players.

### Rename Map
`Rename Map` Button to change the text at the top of the map. Thats it thats all it does.

### Saving Map
`Save As` and `Save` Buttons both open a file dialogue to name and save the file in JSON format. 
`Open File` will let you recall saved maps. Ensuring that you can save progress mid encounter to resume at a later session.

### Range and Scale Functions
_Coming in a later release_

### Icon Window
_Any opened icons should be visible here to avoid opening a new file each time a new icon is required. To be added in a later release_

### Create Token
_Create player Icons and Meeples with basic graphical shapes and text. To be added in a later release._






# Known issues
- On Hiding Mask after using Subtract Mask function, some mask squares occasionally do not clear. Showing the mask and removing them again will clear them from the live map.
- Sometimes Live map does not update with a newly inserted background map. Reinserting the image usually works the 2nd time.
- Occasional exception errors. If found- Please save log and [Email Me](emailto:imogen.wren91@gmail.com)
- Images may not always save with the saved game. This does not seem to affect Icons




## GUI Initial Concept

![image](https://user-images.githubusercontent.com/97303986/182613180-b6b04986-23dd-40ca-b5b4-4d873431d7eb.png)



## Desired Features

- Open image as background
- Open image and save to object palette
- Place Objects from palette onto map area
- Save Map & Object locations
- Recall Saved Maps
- Show live map in second window with live updates
- Freeze 2nd window map, and update only on "live map active" button press
- Apply blackout mask to 2nd window map
- Button to show/hide blackout mask on master map
- Blackout button, keeps 2nd window open but in blackout mode
- Movement - Highlights movement distance + dash action as coloured radius
- Range - Highlight spell/Distance attack range as coloured radius (Could be combined with movement?)
- Area of Attack - Highlight area of attack, cone & Cube shaped attacks with button click
- Set Scale - Click on grid/map area twice to set 5ft, 10ft or 15ft scale
- Map filters - Apply gradient filters for underground or nighttime maps




 
