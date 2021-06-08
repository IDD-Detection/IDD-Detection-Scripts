import glob
import shutil
import xml.etree.ElementTree as ET

for path in glob.glob('/home/aman/Documents/CVIT/IDD_Detection_Rider/Annotations/*/*/*/*'):
    tree = ET.parse(i)
    root = tree.getroot()
    foldername = root[1].text
    source_filename = path.split('/')[-1].split('.')[0]
    parent_folder = path.split('/')[7]
    if parent_folder == 'highquality_16k':
        a = foldername.split('_')
        foldername = '_'.join(a[:-1])
    else:
        foldername = foldername.split('_')[:-2]
        foldername = '_'.join(foldername)

    source_location = '/home/amangoyal/Documents/CVIT/IDD_Detection/JPEGImages/' + parent_folder + '/' + foldername + '/' + source_filename + '.jpg'
    try:
        shutil.copyfile(source_location, '/home/amangoyal/Documents/CVIT/Training/Images/' + parent_folder + source_filename + '.jpg')
    except:
        continue


