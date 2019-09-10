import numpy as np
from pylab import *
from PIL import Image
import pickle as p
import matplotlib.pyplot as pyplot
import os
import os.path as osp

a = np.arange(0, 216)
print('a=np.arange(0,216):' + '\n')
print(a)
a = a.reshape(6, 6, 6)
print('a=a.reshape(6,6,6):' + '\n')
print(a)
a = a.reshape(2, 3, 6, 6)
print('a=a.reshape(2,3,6,6):' + '\n')
print(a)
a = uint8(a)
print('uint8a:' + '\n')
print(a)
for i in range(2):
    b = a[i]
    print('b=a[i]:' + '\n')
    print(b)
    # three channels of a
    print(b[0])
    r = Image.fromarray(b[0]).convert('L')
    g = Image.fromarray(b[1]).convert('L')
    b = Image.fromarray(b[2]).convert('L')

    ###merge the three channels###
    image = Image.merge("RGB", (r, g, b))

    ###show image####
    pyplot.imshow(image)
    pyplot.show()