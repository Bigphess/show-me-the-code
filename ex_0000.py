import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 

image = mpimg.imread('kabi.png')
plt.text(250,80,'4',fontsize = 80, color = 'red')

plt.imshow(image)
# plt.axis('off')
plt.show()
