import cv2


modelo = cv2.CascadeClassifier("cascades\haarcascade_eye.xml")
video = True

def normalize_grayimage(imagem):
    imagem = cv2.equalizeHist(imagem)
    cv2.imshow("Equalized img", imagem)

    return imagem


camera = cv2.VideoCapture(0)
sample = 1
a, imagem = camera.read()
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
gray = normalize_grayimage(gray)
largura, altura = 150, 150
facesDetectadas = modelo.detectMultiScale(gray, scaleFactor=1.5, minSize=(30,30))

for(x, y, l, a) in facesDetectadas:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    if cv2.waitKey(1) & 0xFF == ord(
            'q'):  # Sempre que apertar a tecla 'q', o comando abaixo será  selecionado (Salvar ImagemFace)
        imagemFace = cv2.resize(gray[y:y + a, x:x + l], (largura, altura))
        cv2.imwrite("fotos\pessoa." + str(id) + "." + str(sample) + ".jpg", imagemFace)
        print("[foto" + str(sample) + "capturada com sucesso]")
        sample += 1

cv2.imshow("Detect", imagem)
cv2.waitKey()
