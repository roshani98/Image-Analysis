from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

k = 1984

# Declaring three arrays which will be storing count of blue pixels representing water in the image , counting green pixels representating vegetation land and years
count_blue = np.array([])
count_green = np.array([])
years = np.array([])

while(k<2016):
    a = str(k)
    a = a + '_crop.jpg'
    b = 'Images/Cropped Images/' + a

    # Opening the image to be used in python
    im1 = Image.open(b, 'r')
    blue = 0
    green = 0
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            l = im1.getpixel((i,j))

            # If in (R,G,B) value of a pixel, value of B is more than 178 then it is a blue pixel representing water
            # Hence increament the local count for blue pixel of that image
            if(l[2]>178):
                blue=blue+1

            # If in (R,G,B) value of a pixel, value of G is more than 178 then it is a green pixel representing vegetation land
            # Hence increament the local count for green pixel of that image
            if(l[1]>178):
                green=green+1

    # Concatenate the newly updated values in the actual array
    ans = np.array([blue])
    count_blue = np.concatenate((count_blue, ans))
    ans = np.array([green])
    count_green = np.concatenate((count_green, ans))
    year = np.array([k])
    years = np.concatenate((years, year))

    # Increament k to go to the image of next year
    k = k + 1

# Maximum number of blue pixels and its corresponding year
maximum_index_blue = np.argmax(count_blue)
print('Maximum value of blue pixels in any image : ' + str(np.amax(count_blue)) + ' Year : ' + str(years[maximum_index_blue]))

# Minimum number of blue pixels and its corresponding year
minimum_index_blue = np.argmin(count_blue)
print('Minimum value of blue pixels in any image : ' + str(np.amin(count_blue)) + ' Year : ' + str(years[minimum_index_blue]))

# Calculate the change in blue pixels in consecutive years to study whether it increased or decreased
change_blue = np.array([])

for i in range(0,count_blue.size-1):
    ans = count_blue[i+1]-count_blue[i]
    value = np.array([ans])
    change_blue = np.concatenate((change_blue,value))

# Maximum change in blue pixels was observed in which year
maximum_index_change_blue = np.argmax(change_blue)
print('Maximum change in blue pixels was observed in year : ' + str(np.amax(change_blue)) + ' ' + str(years[maximum_index_change_blue]))

value = np.array([count_blue.size])
change_blue = np.concatenate((change_blue,value))

# Maximum number of green pixels and its corresponding year
maximum_index_green = np.argmax(count_green)
print('Maximum value of blue pixels in any image : ' + str(np.amax(count_green)) + ' Year : ' + str(years[maximum_index_green]))

# Minimum number of green pixels and its corresponding year
minimum_index_green = np.argmin(count_green)
print('Minimum value of blue pixels in any image : ' + str(np.amin(count_green)) + ' Year : ' + str(years[minimum_index_green]))

# Calculate the change in green pixels in consecutive years to study whether it increased or decreased
change_green = np.array([])

for i in range(0,count_green.size-1):
    ans = count_green[i+1]-count_green[i]
    value = np.array([ans])
    change_green = np.concatenate((change_green,value))

# Maximum change in green pixels was observed in which year
maximum_index_change_green = np.argmax(change_green)
print('Maximum change in green pixels was observed in year : ' + str(np.amax(change_green)) + ' ' + str(years[maximum_index_change_green]))

value = np.array([count_blue.size])
change_green = np.concatenate((change_green,value))

# Plot the line graph using plt
plt.plot(years,count_blue,'b',label='Blue pixels')
plt.plot(years,count_green,'g',label='Green pixels')
plt.ylabel('Count of pixels')
plt.xlabel('Years')
plt.grid(True)
plt.legend(loc='upper right')
plt.title('Count of pixels v/s Years')
plt.savefig('Graphs/Graph_1.png')
plt.show()

# Plot the line graph to show the difference between count of blue pixels in consecutive years
plt.plot(years,change_blue)
plt.ylabel('Change of blue pixels')
plt.xlabel('Years')
plt.grid(True)
plt.title('Change of blue pixels v/s Years')
plt.savefig('Graphs/Graph_2.png')
plt.show()

# Plot the line graph to show the difference between count of green pixels in consecutive years
plt.plot(years,change_green)
plt.ylabel('Change of green pixels')
plt.xlabel('Years')
plt.grid(True)
plt.title('Change of green pixels v/s Years')
plt.savefig('Graphs/Graph_3.png')
plt.show()

# Plot the line graph to show the trend of overall blue pixels in the image
plt.plot(years,count_blue)
plt.ylabel('Count of blue pixels')
plt.xlabel('Years')
plt.grid(True)
plt.title('Count of blue pixels v/s Years')
plt.savefig('Graphs/Graph_4.png')
plt.show()

# Plot the line graph to show the trend of overall blue pixels in the image
plt.plot(years,count_green)
plt.ylabel('Count of green pixels')
plt.xlabel('Years')
plt.grid(True)
plt.title('Count of green pixels v/s Years')
plt.savefig('Graphs/Graph_5.png')
plt.show()

# Conclusion : From the graph one can see that number of blue pixels decrease and green increases although change in green pixels is not significant
