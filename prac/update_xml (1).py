from os import listdir, path
import xml.etree.ElementTree as ET
import natsort

#mypath = "C:\\Users\\Manas\\Desktop\\Files for mine video\\HMV\\xml\\"
mypath = "\\home\\harish\\Desktop\\videosforabg\\HMV\\xml1\\"

files = [path.join(mypath, f) for f in listdir(mypath) if f.endswith('.xml')]

files = natsort.natsorted(files,reverse=False)

start_num = 1
for file in files:
	
	tree = ET.parse(file)
	root = tree.getroot()
   
	# img_path = root.find('path')
	file_name = root.find('filename')
	# folder_name = root.find('folder')
	
	# new_img_path = '/home/badri/video_analytics/abg_poc/examples/drone_lmv/train/images'+ str(start_num) + '.jpg'
	new_file_name = str(start_num) + '.jpg' 
	# new_folder_name = 'images'

	# img_path.text = new_img_path
	file_name.text = new_file_name
	# folder_name.text = new_folder_name

	tree.write(file)

	start_num+=1

