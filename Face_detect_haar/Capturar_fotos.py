import cv2

classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
sample = 0
num_samples = 20
id = input("Digite seu identificador")
w, h = 220, 165                          #Tamanho da foto que eu vou tirar


while True:
    a, image = camera.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facedetected = classifier.detectMultiScale(gray_image, scaleFactor=1.5, minSize=(150, 150))

    for(x, y, l, a) in facedetected:
        cv2.rectangle(image, (x, y), (x+l, y+a), (0, 255, 255), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            imageFace = cv2.resize(gray_image[y:y + a, x:x + l], (w, h))
            cv2.imwrite("image/people." + str(id) + "." + str(sample) + ".jpg", imageFace)
            print("[foto" + str(sample) + "capturada com sucesso]")
            sample += 1

    cv2.imshow("Face", image)
    cv2.waitKey(1)
    if sample >= num_samples + 1:
        break
print("Faces Captured Successfully")

cv2.imshow("Face", image)
#cv2.waitKey(1)
camera.release()
