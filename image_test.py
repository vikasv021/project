<<<<<<< HEAD
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()
=======
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()
>>>>>>> bd435bd331fc4b9ac95462651b8dc939df95fc48
