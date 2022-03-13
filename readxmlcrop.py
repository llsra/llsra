import os
from xml.dom import minidom
from PIL import Image
import shutil

root_dirs='xml'
a={}
class binghai:
    def __init__(self,graph=0,name=0,xmin=0,ymin=0,xmax=0,ymax=0,graphwidth=0,graphheight=0):
        self.graph=graph
        self.graphwidth=graphwidth
        self.graphheight=graphheight
        self.name=name
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
    def printbinghai(self):
        print(self.graph,self.name,self.xmin,self.xmax,self.ymin,self.ymax)

i=0
for root, dirs, files in os.walk(root_dirs):
    for file in files:
        doc = minidom.parse('xml/'+file)
        root=doc._get_documentElement()
        nodes1 = root.getElementsByTagName('object')
        nodes2=root.getElementsByTagName('size')
        filenames=root.getElementsByTagName('filename')
        for node1 in nodes1:
            for node2 in nodes2:
                graphwidth=node2.getElementsByTagName('width')
                graphheight=node2.getElementsByTagName('height')
            i+=1
            names = node1.getElementsByTagName('name')
            xmins = node1.getElementsByTagName('xmin')
            ymins = node1.getElementsByTagName('ymin')
            xmaxs = node1.getElementsByTagName('xmax')
            ymaxs = node1.getElementsByTagName('ymax')
            a[i]=binghai(filenames[0].firstChild.data,names[0].firstChild.data,xmins[0].firstChild.data,ymins[0].firstChild.data,xmaxs[0].firstChild.data,ymaxs[0].firstChild.data,graphwidth[0].firstChild.data,graphheight[0].firstChild.data)
            #print('---',i,':')
            #binghai.printbinghai(a[i])
loose_l=0
loose_s=0
poor_l=0
porous=0

for num in range(1,i+1):#计数
    name=a[num].name
    if name=='loose_l':
        loose_l+=1
    if name=='poor_l':
        poor_l+=1
    if name == 'porous':
        porous += 1
    if name == 'loose_s':
        loose_s +=1

    nocroppedname='class/'+name+'/'+a[num].graph  #命名
    croppedname='cropped/'+name+'/'+str(num)+'.jpg'
    croppedname2 = 'squarecropped/' + name + '/' + str(num) + '.jpg'
    croppedname3 = 'doublecropped/' + name + '/' + str(num) + '.jpg'
    img=Image.open('data/'+a[num].graph)
    l=int(a[num].xmin)
    u=int(a[num].ymin)
    r=int(a[num].xmax)
    lo=int(a[num].ymax)

    '''img.save(nocroppedname)
    stem,suffix=os.path.splitext(a[num].graph)
    shutil.copyfile('xml/'+stem+'.xml', 'class/'+name+'xml/'+stem+'.xml')'''


    cropped=img.crop((l,u,r,lo))#正常裁剪
    cropped.save(croppedname)

    weight = r - l  #正方形裁剪
    height = lo - u
    if weight<height:
        squarecropped = img.crop(((r + l) / 2-height/2, u, (r + l) / 2 + height/2, lo))
        squarecropped.save(croppedname2)
    else:
        if ((u+lo)/2-weight/2<0)and((u+lo)/2+weight/2>float(a[num].graphheight)):
            squarecropped = img.crop(((l+r)/2-float(a[num].graphheight)/2,0,(l+r)/2+float(a[num].graphheight)/2,float(a[num].graphheight)))
            squarecropped.save(croppedname2)
        elif (u+lo)/2-weight/2<0:
            squarecropped = img.crop(((l+r)/2-((u + lo) / 2 + weight / 2)/2, 0,(l+r)/2+((u + lo) / 2 + weight / 2)/2 , (u + lo) / 2 + weight / 2))
            squarecropped.save(croppedname2)
        elif (u+lo)/2+weight/2>float(a[num].graphheight):
            squarecropped = img.crop(((l+r)/2-(float(a[num].graphheight)-(u + lo) / 2 + weight / 2)/2, (u + lo) / 2 - weight / 2, (l+r)/2+(float(a[num].graphheight)-(u + lo) / 2 + weight / 2)/2, float(a[num].graphheight)))
            squarecropped.save(croppedname2)
        else:
            squarecropped = img.crop((l, (u+lo)/2-weight/2,r, (u+lo)/2+weight/2))
            squarecropped.save(croppedname2)

    if height>(weight/2):#两倍高度裁剪
        doublecropped = img.crop((l, (u + lo) / 2 - weight / 2, r, (u + lo) / 2 + weight / 2))
        doublecropped.save(croppedname3)
    else:
        doublecropped = img.crop((l, (u + lo) / 2 -  height, r, (u + lo) / 2 +  height))
        doublecropped.save(croppedname3)

print('loose_l:',loose_l,'\npoor_l:',poor_l,'\nporous:',porous,'\nloose_s:',loose_s)




