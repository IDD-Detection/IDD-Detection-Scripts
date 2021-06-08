import glob
import shutil
import xml.etree.ElementTree as ET
cnt = 0
for i in glob.glob('/home/amangoyal/Documents/CVIT/IDD_Detection/Annotations/*/*/*'):
    tree = ET.parse(i)
    root = tree.getroot()
    newfile_xml = i.split('.')[0]
    newfile_xml_name = newfile_xml.split('/')[-1]
    parent_folder = i.split('/')[7]
    eltlist = []
    cnt+=1
    for event in root.findall('object'):
        party = event.find('name')
        parties = party.text
        eltlist.append(parties)

    if 'motorcycle' and 'rider' in eltlist:
        shutil.copyfile(i,'/home/amangoyal/Documents/CVIT/IDD_Detection_Rider_2/Annotations/' + parent_folder + '/' + newfile_xml_name + '_' + str(cnt) + '.xml')

