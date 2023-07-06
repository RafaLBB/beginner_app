import cv2

classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

while True:
    a, image = camera.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facedetected = classifier.detectMultiScale(gray_image, scaleFactor=1.5, minSize=(150, 150))

    for(x, y, l, a) in facedetected:
        cv2.rectangle(image, (x, y), (x+l, y+a), (0, 255, 255), 2)

    cv2.imshow("Face", image)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imshow("Face", image)
camera.release()
