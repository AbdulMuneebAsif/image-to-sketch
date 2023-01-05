import cv2

imageName = input("Enter image file location : ")
imageToSave = input("Enter the image name (with file extension i.e. .jpg, .png etc) in you want to choose for your "
                    "sketch : ")
scaleValue = eval(input("Enter the scale value of image (0.0 - 300.0) : "))

image = cv2.imread(imageName)
greyImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(greyImg)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(greyImg, invertedBlur, scale=scaleValue)

cv2.imwrite(imageToSave, sketch)


"""
OUTPUT:

Enter image file location : image.jpg
Enter the image name (with file extension i.e. .jpg, .png etc) in you want to choose for your sketch : sketch.png
Enter the scale value of image (0.0 - 300.0) : 210.0

"""