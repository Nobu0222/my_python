from PIL import Image
import numpy as np

im = np.array(Image.open('img_sample/huuu.jpg'))
print(im.dtype)
print(im.ndim)
print(im.shape)