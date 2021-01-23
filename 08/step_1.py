import numpy as np
import matplotlib.pyplot as plt

with open('input.txt') as f:
    blob = f.read()[:-1]

width = 25
height = 6
layers = len(blob) // (width * height)

# mooi klusje voor Numpy

images = np.array([int(c) for c in blob]).reshape((layers,height,width))

n_zeros_in_image = (images == 0).sum(axis=(1,2))
n_ones_in_image  = (images == 1).sum(axis=(1,2))
n_twos_in_image  = (images == 2).sum(axis=(1,2))

layer_with_fewest_zeros = np.argmin(n_zeros_in_image)

print('\n\n  answer :', n_ones_in_image[layer_with_fewest_zeros] * 
                        n_twos_in_image[layer_with_fewest_zeros]   )

# part two, matplotlib klusje op het einde

final_image = np.empty((height,width), dtype=np.int)
for h in range(height):
    for w in range(width):
        final_pixel = None
        stack = images[::-1,h,w] 
        for pixel in stack:
            if pixel != 2:
                final_pixel = pixel
        final_image[h,w] = final_pixel

plt.imshow(final_image)
plt.show()
plt.savefig('image.png')

