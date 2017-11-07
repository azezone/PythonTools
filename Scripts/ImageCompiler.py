import  os
from PIL import Image

def getAllImage(path):
    dirs = os.listdir(path)
    images = list()
    for dir in dirs:
        temp_path = path+'\\'+dir
        if(os.path.isdir(temp_path)):
            images.extend(getAllImage(temp_path))
        elif(os.path.isfile(temp_path) and not temp_path.endswith('.meta')):
            images.append(temp_path)
        elif(temp_path.endswith('.meta')):
            os.remove(temp_path)
    return images

def splitAlpha(path):
    if(path.__contains__('_alpha') or path.__contains__('_rgb')):
        print('has oprate the image!')
        return
    im = Image.open(path,"r")
    colors = im.getcolors()
    rgbtex = Image.new("RGB", im.size, (255, 255, 255))
    alphatex = Image.new("RGB", im.size, (255, 255, 255))
    (w,h) = im.size
    for x in range(w):
        for y in range(h):
            rgba = im.getpixel((x,y))
            if(rgba.__len__() == 4):
                (r, g, b, a) = rgba
                rgbtex.putpixel((x,y),(r,g,b))
                alphatex.putpixel((x,y),(a,a,a))
            elif(rgba.__len__() == 3):
                return
    root = os.path.dirname(path)
    rgb_name = os.path.basename(path)

    info = rgb_name.split('.')
    if(info.__len__() == 1):
        return
    else:
        rgb_name = info[0]+'_rgb.jpg'
        alpha_name = info[0]+'_alpha.jpg'

    rgbtex.save(root + '\\' + rgb_name)
    alphatex.save(root + '\\' + alpha_name)
    os.remove(path)

images = getAllImage(r'D:\WorkSpace\Learn\Python\Learn\Resource\Sprites')
for image in images:
    splitAlpha(image)

