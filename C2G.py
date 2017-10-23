import cv2

#User input
img=input("Which image do you want to to convert in gray?"+ "\n")

#Convert the picture in gray
img_c = cv2.imread(img,1)
img_g = cv2.cvtColor(img_c, cv2.COLOR_BGR2GRAY)

#Create the file for the gray image
cv2.imwrite((img+"_gray.png"),img_g)

#Display the two pictures and wait for a keyboard strike
cv2.imshow("Colour",img_c)
cv2.imshow("Grey",img_g)
cv2.waitKey(5000)

#Close the program
cv2.destroyAllWindows()
