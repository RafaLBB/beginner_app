# Versão para salas(Projeto final-Henrique)
from function_escudo import face_recg
import timeit
import cv2
import time
# camera = cv2.VideoCapture(1)
arquivo_txt = "time_out"

name_end = 55
pasta = input("Qual o diretório do dataset de teste? ex:/home/pi/escudo/ ")

path_dnn = "/home/rafaela/Área de Trabalho/Senfio/Rafaela_vc/face_detection_model/"
#path_img = "/home/rafaela/Área de Trabalho/Senfio/Rafaela_vc/teste/" + tipo + "/test" + str(name) + ".jpg"


path_model = "/home/rafaela/Área de Trabalho/Senfio/Rafaela_vc/encodings/SVC.pickle"
path_data = "/home/rafaela/Área de Trabalho/Senfio/Rafaela_vc/encodings/encodings.pickle"


def reconhecer():
    path_img = str(pasta) + str(arquivo) + ".jpg"
    #print(path_img)
    # aux=time.time()
    # time.sleep(0.8)
    # return_value, image = camera.read()
    # cv2.imwrite("/home/rafaela/Documentos/escudo/treinamento_web/Saída/"+ str(aux)+".png", image)
    # cv2.imwrite("/home/rafaela/img.png", image)
    # cv2.destroyAllWindows()
    # imagePath = "/home/rafaela/Documentos/escudo/treinamento_web/Saída/"+str(aux)+".png"
    # imagePath = "/home/rafaela/Documentos/escudo/treinamento_web/Saída/img.png"

    try:
        start = timeit.default_timer()
        name = face_recg.face_rec2(path_dnn_face_detector=path_dnn,
                                   data_encodings=path_data,
                                   image=path_img,
                                   classification_model=path_model,
                                   cnt = str(arquivo), face_detection_method="haar"
                                   )
        print(name)
        stop = timeit.default_timer()
        execution_time = stop - start
        try:

            f = open(arquivo_txt + ".txt", "r+")

            lines = f.readlines()
            f.seek(0)

            f.write("|" + str(arquivo) + str(name) + "|" + "Total: " + str(execution_time) + "|" + '\n')

            for line in lines:
                f.write(line)
            f.close()

        except:

            f = open(arquivo_txt + ".txt", "w")

            f.write("|" + str(arquivo) +"|"+ str(name) + "|" + "Total: " + str(execution_time) + "|" + '\n')

            f.close()
        print("Process executed in " + str(execution_time))
        del stop, start, execution_time
        return True

    except:
        print("Nenhuma pessoa cadastrada")
        return False


action = input("Começar o reconhecimento? \n y or n \n")

if action == "y":
    arquivo = 1
    while True:

        name = reconhecer()
        time.sleep(3)
        arquivo += 1
        if arquivo >= name_end + 1:
            break
else:
    print("Processo interrompido")
