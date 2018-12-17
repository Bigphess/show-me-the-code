import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 

image = mpimg.imread('kabi.png')
plt.text(250,80,'4',fontsize = 60, color = 'black', bbox={'facecolor':'red', 'alpha':0.8, 'boxstyle':'round'})

plt.imshow(image)
# plt.axis('off')
plt.show()
