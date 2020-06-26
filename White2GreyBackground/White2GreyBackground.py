from PIL import Image

def changeBG():
    
    img = Image.open('./GREY-01.jpg')                            # Image path
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    
    for item in datas:
        if item[0] >= 220 and item[1] >= 220 and item[2] >= 220: # Background Color with threshold of 35
            newData.append((200, 201, 198, 255))                 # RGBA value for the new background color, use A = 0  for transparent background 
        else:
            newData.append(item)
    
    img.putdata(newData)
    img.save("./ChangedBG.png", 'PNG')#converted Image name
    print('Done')

changeBG()
