from PIL import Image

def convertToPNG():
    img = Image.open('./GREY-01.jpg')#image path and name
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    print(datas[0])
    for item in datas:
        if item[0] >= 220 and item[1] >= 220 and item[2] >= 220:
            newData.append((200, 201, 198, 255))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("./TransparentImage.png", 'PNG')#converted Image name
    print('Done')

convertToPNG()
