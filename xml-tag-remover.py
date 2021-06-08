import xml.etree.ElementTree as ET
import glob
cnt = 0
prevfile = None
for i in glob.glob('/home/amangoyal/Documents/CVIT/IDD_Detection_Rider/Annotations/*/*/*'):
    tree = ET.parse(i)
    root = tree.getroot()
    for obj in root.findall('object'):
        anomaly = obj.find('name').text
        if anomaly != 'rider':
            root.remove(obj)

    tree.write(i)
