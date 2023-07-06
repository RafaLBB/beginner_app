import cv2
import os
import numpy as np
from PIL import Image

face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#recognizer = cv2.face.EigenFaceRecognizer_create()
#recognizer.read("classificadorEigenYale.yml")
#recognizer = cv2.face.FisherFaceRecognizer_create()
#recognizer.read("classificadorFisherYale.yml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("classificadorLBPHYale.yml")

allhits = 0
percent = 0.0
precision = 0.0

caminhos = [os.path.join('yalefaces/teste', f) for f in os.listdir('yalefaces/teste')]
for caminhoImagem in caminhos:
    imagemFace = Image.open(caminhoImagem).convert('L')
    imagemFaceNP = np.array(imagemFace, 'uint8')
    facesDetectadas = face_detect.detectMultiScale(imagemFaceNP)
    for (x, y, l, a) in facesDetectadas:
        idprevisto, confianca = recognizer.predict(imagemFaceNP)
        idatual = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
        print(str(idatual) + " foi classificado como " + str(idprevisto) + " - " + str(confianca))
        if idprevisto == idatual:
            allhits += 1
            precision += confianca
        #cv2.rectangle(imagemFaceNP, (x, y), (x + l, y + a), (0, 0, 255), 2)
        #cv2.imshow("Face", imagemFaceNP)
        #cv2.waitKey(1000)
percent = (allhits / 30) * 100
precision = precision / allhits
print("Percentual de acerto: " + str(percent))
print("Total confiança: " + str(precision))

