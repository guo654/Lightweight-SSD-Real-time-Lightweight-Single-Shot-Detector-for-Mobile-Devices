import cv2
import os



def read_path(file_pathname):
    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        ####change to gray
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        image_np=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        #####save figure
        cv2.imwrite('/home/jari/guoshi/tool/grayvoc/test/VOCdevkit/VOC2007/JPEGImages'+"/"+filename,image_np)       

read_path("/home/jari/guoshi/tool/grayvoc/test/VOCdevkit/VOC2007/JPEGImages")
#print(os.getcwd())
