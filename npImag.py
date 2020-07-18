from numpy import asarray
from PIL import Image

#open the image
image = Image.open('24722.jpg').convert('L').resize((500,500))
print(image.format)
print(image.size)
print(image.mode)
image.show()

#covert image to numpy array
data = asarray(image)

#ima=data[50:55,65:99] #to trim
#print("After trimming:",ima.shape)
#print(data.shape)
print(data)

# save manupulated image
L_image = Image.fromarray(data).save('shaju.png')
