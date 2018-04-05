import cv2

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('C:/Users/User/Downloads/Case-16-U-27-2.jpg',0)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    wartoscSuwaka = cv2.getTrackbarPos('R','image')
    ret, th1 = cv2.threshold(img, wartoscSuwaka, 255, cv2.THRESH_BINARY)
    cv2.imshow('image',th1)

cv2.destroyAllWindows()