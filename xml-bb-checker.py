from lxml import etree
import glob
import shutil 

for i in glob.glob('/home/amangoyal/Documents/CVIT/IDD_Detection_Rider/Annotations/*/*/*'):
    with open(i, 'rb') as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)

    dims = []
    bb = {}
    check = []

    arr_split = i.split('/')
    firstpart = arr_split[-1]
    dest_filename = firstpart.split('.')[0]
    parent_folder = i.split('/')[7]
    
    for annotation in root.getchildren():
        for size in annotation.getchildren():
            if size.tag == 'width':
                dims.append(int(size.text))
            if size.tag == 'height':
                dims.append(int(size.text))
    for annotation in root.getchildren():
        for obj in annotation.getchildren():
            if obj.tag == 'name' and obj.text == 'rider':
                for bndbox in obj.getnext():
                    if bndbox.tag == 'xmin':
                        bb['xmin'] = int(bndbox.text)
                    if bndbox.tag == 'xmax':
                        bb['xmax'] = int(bndbox.text)
                    if bndbox.tag == 'ymin':
                        bb['ymin'] = int(bndbox.text)
                    if bndbox.tag == 'ymax':
                        bb['ymax'] = int(bndbox.text)
                width = bb['xmax'] - bb['xmin']
                height = bb['ymax'] - bb['ymin']
                w_r = width/dims[0]
                h_r = height/dims[1]
                if w_r >= 0.023 and h_r >= 0.087:
                    check.append(1)
                else:
                    check.append(0)

    if 1 in check:
        shutil.copyfile(i,'/home/amangoyal/Documents/CVIT/Arranged_Data/' + parent_folder + 'Above_Range/' + dest_filename + '.xml')
    else:
        shutil.copyfile(i,'/home/amangoyal/Documents/CVIT/Arranged_Data/' + parent_folder + 'Below_Range/' + dest_filename + '.xml')
        


                
