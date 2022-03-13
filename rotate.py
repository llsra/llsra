#coding=utf-8
from PIL import Image
import torchvision.transforms as transforms
import random
import os

def Jpg(dir_line):
    try:
        im=Image.open(dir_line)
    except IOError as er_info:
        print(er_info)
        exit()
    x=im.size[0]
    y=im.size[1]
    img=im.load()
    c = Image.new("RGB",(x,y))
    for i in range (0,x):
        for j in range (0,y):
            w=x-i-1
            h=y-j-1
            rgb=img[w,j] #镜像翻转
            #rgb=img[w,h] #翻转180度
            #rgb=img[i,h] #上下翻转
            c.putpixel([i,j],rgb)
            image_transforms = transforms.Compose([transforms.Grayscale(1)])
            c = image_transforms(c)
            c.save('rotate/'+str(m)+'.jpg')

if __name__=="__main__":
    m=0
    path='squarecropped/test/'
    path_image = os.listdir(path)
    for path in path_image:
        m+=1
        Jpg('squarecropped/loose_s/'+path)