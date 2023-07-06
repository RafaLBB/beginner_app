import cv2

detectorFace = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 2
imagem = camera.read()
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30,30))

for(x, y, l, a) in facesDetectadas:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    if cv2.waitKey(1) & 0xFF == ord(
            'q'):  # Sempre que apertar a tecla 'q', o comando abaixo será  selecionado (Salvar ImagemFace)
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (l, a)
        cv2.imwrite("fotos\\pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
        print("[foto" + str(amostra) + "capturada com sucesso]")
        amostra += 1

cv2.imshow("Detectado", imagem)
cv2.waitKey()