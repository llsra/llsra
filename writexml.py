import os
import shutil

root_dirs='generate'
i=0
category='loose_s'
for root, dirs, files in os.walk(root_dirs):
    for file in files:
        i+=1
        shutil.copyfile('generate/'+file, 'after/' + category+'/'+str(i) + '.jpg')
        fp = open('after/'+category+'xml/'+str(i)+'.xml','w')
        fp.write('<annotation><folder>JPEGImages</folder><filename>'+str(i) + '.jpg</filename><path>after/' + category+'/'+str(i) + '.jpg</path><source><database>Unknown</database></source><size><width>64</width><height>64</height><depth>1</depth></size><segmented>0</segmented><object><name>'+category+'</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox><xmin>0</xmin><ymin>0</ymin><xmax>64</xmax><ymax>64</ymax></bndbox></object></annotation>')
        fp.close()