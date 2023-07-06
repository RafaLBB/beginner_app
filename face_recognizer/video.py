import time
import picamera
 
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.start_recording('/home/rafa/video.h264')
    time.sleep(10)
    camera.stop_recording()
    camera.stop_preview()
