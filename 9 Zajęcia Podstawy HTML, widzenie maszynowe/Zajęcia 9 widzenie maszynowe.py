import cv2
import matplotlib.pyplot as plt

photo = cv2.imread('orzel.jpg')

# cv2.imshow('Okno1', photo)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(photo[:, :, 0])
# plt.imshow(photo[:, :, 1])
# plt.imshow(photo[:, :, 2])

# plt.imshow(photo[:, :, ::-1])

grayPhoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
plt.imshow(grayPhoto, cmap='gray')

sobelx = cv2.Sobel(grayPhoto,cv2.CV_64F,1,0,ksize=3)
plt.imshow(sobelx, cmap='gray')

sobely = cv2.Sobel(grayPhoto,cv2.CV_64F,0,1,ksize=3)
# plt.imshow(sobely, cmap='gray')

# laplacian = cv2.Laplacian(grayPhoto,cv2.CV_64F)
# plt.imshow(laplacian, cmap="gray")

# edges = cv2.Canny(grayPhoto,100,200)
# plt.imshow(edges, cmap="gray")

# photo = cv2.imread('las.jpg')
# plt.imshow(photo[:, :, ::-1])
# grayPhoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(grayPhoto,300,450)
# plt.imshow(edges, cmap="gray")

# photo = cv2.imread('znaki.jpg')
# plt.imshow(photo[:, :, ::-1])
# grayPhoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
# plt.imshow(grayPhoto, cmap='gray')
# edges = cv2.Canny(grayPhoto,150,300)
# plt.imshow(edges, cmap="gray")