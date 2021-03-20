import cv2
import matplotlib.pyplot as plt

photo = cv2.imread('orzel.jpg')

cv2.imshow('Okno1', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(photo[:, :, ::-1])