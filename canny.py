import cv2
import numpy as np
from matplotlib import pyplot as plt

main = cv2.imread("comp.jpg")
main = cv2.cvtColor(main, cv2.COLOR_BGR2RGB)
effect = cv2.Canny(main, 100, 200)

titles = ['Image', 'Canny']
images = [main, effect]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
