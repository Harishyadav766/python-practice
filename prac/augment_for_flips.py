import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
import shutil
from os import listdir, path
import xml.etree.ElementTree as ET
import xmltodict


out_path = "C:\\Users\\Manas\\Desktop\\test_abg\\bb_box.txt"
data_path = "C:\\Users\\Manas\\Desktop\\test_abg\\image\\"
img_path = "C:\\Users\\Manas\\Desktop\\test_abg\\image\\"
xml_path = "C:\\Users\\Manas\\Desktop\\test_abg\\annotations\\"
# file_path = "C:\\Users\\Manas\\Desktop\\test_abg\\annotations\\125.xml"


def pca_color_augmentation(image):
    assert image.ndim == 3 and image.shape[2] == 3
    assert image.dtype == np.uint8
    img = image.reshape(-1, 3).astype(np.float32)
    sf = np.sqrt(3.0/np.sum(np.var(img, axis=0)))
    img = (img - np.mean(img, axis=0))*sf 
    cov = np.cov(img, rowvar=False) # calculate the covariance matrix
    value, p = np.linalg.eig(cov) # calculation of eigen vector and eigen value 
    rand = np.random.randn(3)*0.08
    delta = np.dot(p, rand*value)
    delta = (delta*255.0).astype(np.int32)[np.newaxis, np.newaxis, :]
    img_out = np.clip(image+delta, 0, 255).astype(np.uint8)
    return img_out

xml_paths = [os.path.join(xml_path, s) for s in os.listdir(xml_path)]
# print(xml_paths)

pwd_lines = []
for xml_file in xml_paths:
    et = ET.parse(xml_file)
    element = et.getroot()
    element_objs = element.findall('object') 
    element_filename = element.find('filename').text
    base_filename = os.path.join(data_path, element_filename)
    print(base_filename)                               
    img = cv2.imread(base_filename)
    rows, cols = img.shape[:2] 
    img_split = element_filename.strip().split('.jpg')

    for element_obj in element_objs:
        # count = count+1
        class_name = element_obj.find('name').text # return name tag ie class of disease from xml file
        obj_bbox = element_obj.find('bndbox')
        #print(obj_bbox)
        x1 = int(round(float(obj_bbox.find('xmin').text)))
        y1 = int(round(float(obj_bbox.find('ymin').text)))
        x2 = int(round(float(obj_bbox.find('xmax').text)))
        y2 = int(round(float(obj_bbox.find('ymax').text)))
        # print("Height  :  ",h)
        # print("width  :  ",w)
        print("x1 : ",x1)
        print("y1 : ",y1)
        print("x2 : ",x2)
        print("y2 : ",y2)
        # objects=[{'name': 'HMV', 'bbox': [x1, y1, x2, y2]}, {'name': 'HMV', 'bbox': [x1, y1, x2, y2]}]
# if you specify range(1) total number of augmented data is 6 for one image
# 6 types of augmentation means pca, horizontal and vertical flip, 3 rotation
# if you specify range(2) total number of augmented data is 12 for one image
        for color in range(1):
            img_color = pca_color_augmentation(img)
            color_name = img_split[0]+ '-color' + str(color)
            color_name = img_split[0]
            color_jpg = color_name + '.jpg'
            new_path = os.path.join(img_path, color_jpg) # join with augmented image path
            # lines = [color_jpg, ',', str(x1), ',', str(y1), ',', str(x2), ',', str(y2), ',', class_name, '\n']
            # pwd_lines.append(lines)
            # if not os.path.isfile(new_path):
            #     cv2.imwrite(new_path, img_color)
            
            #for horizontal and vertical flip
            f_points = [1]
            for f in f_points:
                f_img = cv2.flip(img_color, f)
                h,w = img_color.shape[:2]
                
                if f == 1:
                    f_x1 = w-x2
                    f_y1 = y1
                    f_x2 = w-x1
                    f_y2 = y2
                    f_str = 'f1'
                # if f == 0:
                #     f_x1 = x1
                #     f_y1 = h-y2
                #     f_x2 = x2
                #     f_y2 = h-y1
                #     f_str = 'f0'
                print("----------------------------------------------------",str(f_x1))
                print("----------------------------------------------------",str(f_y1))
                print("----------------------------------------------------",str(f_x2))
                print("----------------------------------------------------",str(f_y2))
                new_name = color_name + '-' + f_str + '.jpg'
                new_path = os.path.join(img_path, new_name)
                
                lines = [new_name, ',', str(f_x1), ',', str(f_y1), ',', str(f_x2), ',', str(f_y2), '\n']
                pwd_lines.append(lines)
                if not os.path.isfile(new_path):
                    cv2.imwrite(new_path, f_img)

            new_x1 = str(f_x1)
            new_y1 = str(f_y1)
            new_x2 = str(f_x2)
            new_y2 = str(f_y2)


            old_x1 = obj_bbox.find('xmin') 
            old_y1 = obj_bbox.find('ymin') 
            old_x2 = obj_bbox.find('xmax') 
            old_y2 = obj_bbox.find('ymax') 

            old_x1.text = new_x1
            old_y1.text = new_y1
            old_x2.text = new_x2
            old_y2.text = new_y2

            print(old_x1.text)
            print(old_y1.text)
            print(old_x2.text)
            print(old_y2.text)
            
            et.write(xml_file)
                    
            # # for angle 90
            # img_transpose = np.transpose(img_color, (1,0,2))
            # img_90 = cv2.flip(img_transpose, 1)
            # h,w = img_color.shape[:2]
            # angle_x1 = h - y2
            # angle_y1 = x1
            # angle_x2 = h -y1
            # angle_y2 = x2
            # new_name = color_name + '-' + 'rotate_90' + '.jpg'
            # new_path = os.path.join(img_path, new_name)
            # lines = [new_name, ',', str(angle_x1), ',', str(angle_y1), ',', str(angle_x2), ',', str(angle_y2), ',', class_name, '\n']
            # pwd_lines.append(lines)
            # if not os.path.isfile(new_path):
            #     cv2.imwrite(new_path,img_90)
                
            # #for angle 180
            # h,w = img_color.shape[:2]
          

            # img_180 = cv2.flip(img_color, -1)
          
            # ang_x1 = w - x2
            # ang_y1 = h - y2
            # ang_x2 = w - x1
            # ang_y2 = h - y1
            # new_name_180 = color_name + '-' + 'rotate_180' + '.jpg'
            # new_path_180 = os.path.join(img_path, new_name_180)
            # print("----------------------------------------------------",str(ang_x1))
            # print("----------------------------------------------------",str(ang_y1))
            # print("----------------------------------------------------",str(ang_x2))
            # print("----------------------------------------------------",str(ang_y2))

            # obj_xml = root.findall('object')
            # print("trrrreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",tree.find('.//xmin').text)
            # try:
            # obj_xml = root.findall('object')
            # print(obj_xml)
            # print("skdvhs;elijb;rtjt;drj;bijhdr;bj;rttjb'rob'sjr;bih;bhj'seokb'lsrjtb;khrt;uighw;eog;seojhtf",len(obj_xml))
            # for obj in obj.xml:
            #     print(obj)
            # print(obj_xml[0])




            '''
            if(int(tree.find('.//xmin').text) == x1):
                obj_bbox.find('.//xmin').text = str(ang_x1)
            # else:
            #     break
​
            if(int(tree.find('.//ymin').text) == y1):
                obj_bbox.find('.//ymin').text == str(ang_y1)
​
            # else:
            #     break
            if(int(tree.find('.//xmax').text ) == x2):
                obj_bbox.find('.//ymin').text == str(ang_y1)
​
            # else:
            #     break
            if(int(tree.find('.//ymax').text) == y2):
                obj_bbox.find('.//ymax').text == str(ang_y2)
​
            # else:
            #     break
            '''
            # if ():​
            # # for obj in root.iter(obj_xml):
            #     print("inside for loop---------------------------- ")
            #     bbox_original =root.findall('bndbox')
            #     bbox_original.find('xmin').text = str(ang_x1)
            #     # print( bbox_original.find('xmin').text)
            #     # print(bbox_original.find('xmin')[objLen], 'found here')
            #     bbox_original.find('ymin').text = str(ang_y1)
            #     bbox_original.find('xmax').text = str(ang_x2)
            #     bbox_original.find('ymax').text = str(ang_y2)

            # except Exception as e:
            #     print(e)​
            # lines_180 = [new_name_180, ',', str(ang_x1), ',', str(ang_y1), ',', str(ang_x2), ',', str(ang_y2), '\n']
            # pwd_lines.append(lines_180)

            # # print("---------------------------------------",color_name)
            # # print("Received the 1")
            # if not os.path.isfile(new_path_180):
            #     cv2.imwrite(new_path_180,img_180)
                
            # #for angle 270
            # img_transpose_270 = np.transpose(img_color, (1,0,2))
            # img_270 = cv2.flip(img_transpose_270, 0)
            # an_x1 = y1
            # an_y1 = w - x2
            # an_x2 = y2
            # an_y2 = w - x1
            # new_name_270 = color_name + '-' + 'rotate_270' + '.jpg'
            # new_path_270 = os.path.join(img_path, new_name_270)
            # lines_270 = [new_name_270, ',', str(an_x1), ',', str(an_y1), ',', str(an_x2), ',', str(an_y2), ',', class_name, '\n']
            # pwd_lines.append(lines_270)
            # if not os.path.isfile(new_path_270):
            #     cv2.imwrite(new_path_270, img_270)

# try:
#     # print(pwd_lines)
# except Exception as e:
#     print(e)
# yupp = len(pwd_lines)
# print(yupp)
# if(yupp > 0):
#     with open(out_path, 'w') as f:
#         for line in pwd_lines:
#             f.writelines(line)
#     f.close()
            
# print('End')
