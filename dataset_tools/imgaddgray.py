import cv2
import os

def read_path(file_pathname):
    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        ####change to gray
        imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        height = img.shape[0]
        width = img.shape[1]
        for i in range(height):
            for j in range(width):
                min = 300
                index = 0
                for k in range(3):
                    if img[i,j,k] < min:
                        min = img[i,j,k]
                        index = k
                if imggray[i,j] > min:
                    img[i,j,index] = imggray[i,j]
        #####save figure
        cv2.imwrite('/home/jari/guoshi/tool/mixgrayrgb/trainval/VOCdevkit/VOC2007/JPEGImages'+"/"+filename,img)       

read_path("/home/jari/guoshi/tool/mixgrayrgb/trainval/VOCdevkit/VOC2007/JPEGImages")
#print(os.getcwd())
