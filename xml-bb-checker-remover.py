import xml.etree.ElementTree as ET
import glob

for i in glob.glob('/home/amangoyal/Documents/CVIT/IDD_Detection_Rider/Annotations/*/*/*'):
    tree = ET.parse(i)
    root = tree.getroot()
    bb = {}
    dims = []
    check = 0

    for size in root.findall('size'):
        width = int(size.find('width').text)
        dims.append(width)
        height = int(size.find('height').text)
        dims.append(height)

    for obj in root.findall('object'):
        anomaly = obj.find('name').text
        if anomaly == 'rider' :
            for bndbox in obj.findall('bndbox'):
                bb['xmin'] = int(bndbox.find('xmin').text)
                bb['xmax'] = int(bndbox.find('xmax').text)
                bb['ymin'] = int(bndbox.find('ymin').text)
                bb['ymax'] = int(bndbox.find('ymax').text)
            width = bb['xmax'] - bb['xmin']
            height = bb['ymax'] - bb['ymin']
            w_r = width/dims[0]
            h_r = height/dims[1]
            if w_r >= 0.023 and h_r >= 0.087:
                continue
            else:
                check +=1
                root.remove(obj)
    if check>0:
        tree.write(i)
