from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from uuid import getnode as get_mac
import time
import cv2

#Exportando os eventos para o txt
def event_txt(event, user):

    name = "event"
    try:

        f = open(name + ".txt", "r+")

        lines = f.readlines()
        f.seek(0)

        f.write("|" + str(event) +"|" + str(user) +"|" + str(datetime.now().date()) + "|" + str(
            datetime.now().hour) + ":" + str(datetime.now().minute) + "|" + '\n')

        for line in lines:
            f.write(line)
        f.close()

    except:

        f = open(name + ".txt", "w")

        f.write("|" + str(event) + "|" + str(user) + "|" + str(datetime.now().date()) + "|" + str(
            datetime.now().hour) + ":" + str(datetime.now().minute) + "|" + '\n')

        f.close()

def email(event, user):


    try:
        path_img = <"/dir/face.jpg">
        img = "face.jpg"
        fromaddr = "rafaelalais18@hotmail.com"
        toaddrs = "rbfe18@gmail.com"
        passwd = "password"
        local = "reference"

        mac_Adress = get_mac()
        mac = ':'.join(("%012X" % mac_Adress)[i:i + 2] for i in range(0, 12, 2))
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = <"Email subject">

        body = str(local) + "|" + str(event) + "|" + str(user) + "|" + str(datetime.now().date()) + "|" + str(
                datetime.now().hour) + ":" + str(datetime.now().minute)

        msg.attach(MIMEText(body, 'plain'))
        filename = img
        attachment = open(path_img, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

        print("sending mail...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, passwd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print("email sent!")

    except:

        try:

            f = open("datalog.txt", "r+")

            lines = f.readlines()
            f.seek(0)

            f.write("|" + str(event) + "|" + str(user) + "|" + str(datetime.now().date()) + "|" + str(
                datetime.now().hour) + ":" + str(datetime.now().minute) + "|" + '\n')

            for line in lines:
                f.write(line)
            f.close()

        except:

            f = open("datalog.txt" + ".txt", "w")

            f.write("|" + str(event) + "|" + str(user) + "|" + str(datetime.now().date()) + "|" + str(
                datetime.now().hour) + ":" + str(datetime.now().minute) + "|" + '\n')

            f.close()

def take_picture():
    cam = cv2.VideoCapture(0)
    time.sleep(0.1)
    ret, frame = cam.read()
    time.sleep(0.4)
    cv2.imwrite("face.jpg", frame)
    del cam


