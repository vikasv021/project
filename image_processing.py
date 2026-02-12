import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("test.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Resize image
resized = cv2.resize(gray, (256, 256))

plt.imshow(resized, cmap="gray")
plt.title("Resized Image (256x256)")
plt.axis("off")
plt.show()

# Edge detection using Canny
edges = cv2.Canny(resized, 100, 200)

plt.imshow(edges, cmap="gray")
plt.title("Edge Detection")
plt.axis("off")
plt.show()
