from PIL import Image
import os
original_month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
original_path = "/home/pmimoon/Documents/ocean_conv_1/zosystem"

for i in original_month:
    file_list = os.listdir(original_path+"/"+i)
    img_list = [i for i in file_list if i.endswith(".tif")]
    for img_name in img_list:
        img = Image.open(original_path+"/"+i+"/"+img_name)
        x = 0
        y = 0
        area = (x,y,x+256,y+256)
        cropped_img = img.crop(area)
        cropped_img.save(original_path+"/"+"256X256/"+i+"/"+img_name)
