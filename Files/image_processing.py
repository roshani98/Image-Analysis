from PIL import Image

def cmp(a, b):
    return (a > b) - (a < b)

def flag_value_red(flag):
    flag = flag+1
    flag = flag%4
    return flag

def flag_value_blue(flag):
    flag = flag+1
    flag = flag%15
    return flag

k = 1984
b = '2016_crop.jpg'

while(k<2016):
    a = str(k)
    a = a + '_crop.jpg'
    im1 = Image.open(a, 'r')
    im2 = Image.open(b,'r')
    img2 = Image.new( im2.mode, im2.size)
    pixelsNew2 = img2.load()
    flag = 0
    for i in range(img2.size[0]):
        for j in range(img2.size[1]):
            if (cmp(im1.getpixel((i,j)),im2.getpixel((i,j)))>=1 and i<img2.size[0]/2 and j<img2.size[1]/2):#
                if(flag==0):
                    pixelsNew2[i,j] = (255,0,0)
                    flag = flag_value_red(flag)
                else:
                    pixelsNew2[i,j] = im2.getpixel((i,j))
                    flag = flag_value_red(flag)
            elif(cmp(im1.getpixel((i,j)),im2.getpixel((i,j)))>=1 and i<img2.size[0]/2 and j>img2.size[1]/2):
                if(flag==0):
                    pixelsNew2[i,j] = (0,0,255)
                    flag = flag_value_blue(flag)
                else:
                    pixelsNew2[i,j] = im2.getpixel((i,j))
                    flag = flag_value_blue(flag)
            elif (cmp(im1.getpixel((i,j)),im2.getpixel((i,j)))>=1 and i>img2.size[0]/2 and j>=img2.size[1]/2):
                if(flag==0):
                    pixelsNew2[i,j] = (255,0,0)
                    flag = flag_value_red(flag)
                else:
                    pixelsNew2[i,j] = im2.getpixel((i,j))
                    flag = flag_value_red(flag)
            elif(cmp(im1.getpixel((i,j)),im2.getpixel((i,j)))>=1 and i>img2.size[0]/2 and j<img2.size[1]/2):
                if(flag==0):
                    pixelsNew2[i,j] = (0,0,255)
                    flag = flag_value_blue(flag)
                else:
                    pixelsNew2[i,j] = im2.getpixel((i,j))
                    flag = flag_value_blue(flag)
            else:
                pixelsNew2[i,j] = im2.getpixel((i,j))
    c = str(k)
    c = c + '_2016.jpg'
    img2.save(c)
    print(c + " image processed")
    k = k + 1
