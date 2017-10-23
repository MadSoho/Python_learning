import cv2, glob

for img in (glob.glob(".\Exo 09\*.jpg")):
    #img_temp = cv2.imread(img,1)
    #resized = cv2.resize(cv2.imread(img,1), (100, 100))
    cv2.imwrite(img+"_small.jpg",cv2.resize(cv2.imread(img,1), (100, 100)))
