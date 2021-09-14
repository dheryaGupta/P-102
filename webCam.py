import cv2
import random
import time
import dropbox

start_time=time.time()

def  takeSnapshot ():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print ("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="ZZALgC36yTIAAAAAAAAAAbXQtr-BIefccb0vx0SWQKqcMfJgayHs8tUS_FIRTk6M"
    file=img_name
    file_from=file
    file_to="/Test/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-start_time)>=2):
            name=takeSnapshot()
            upload_file(name)

main()