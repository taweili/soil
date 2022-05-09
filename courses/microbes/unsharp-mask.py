import imp
from numpy import size
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

img = img_as_float(io.imread("scene00701.png", as_gray=True))

gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

img2 = (img - gaussian_img)*2

img3 = img + img2

from matplotlib import pyplot as plt

fig, axes = plt.subplots(1, 3)
axes[0].imshow(img, cmap="gray")
axes[1].imshow(img2, cmap='gray')
axes[2].imshow(img3, cmap='gray')
plt.show()
