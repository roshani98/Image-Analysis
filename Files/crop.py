from PIL import Image

i = 1984

while i<2017:
    a = str(i);
    a  =  a + '.jpg'
    img = Image.open(a)
    width = img.size[0]
    height = img.size[1]
    print(width)
    print(height)
    img3 = img.crop((315,45,width-350,height-175))
    new_name = str(i);
    new_name = new_name + '_crop.jpg'
    img3.save(new_name)
    i=i+1
