'''
输入一个文件夹路径，列出该文件夹中的所有图片，并把所有图片名字输出到文件夹上一层目录的file_list.txt里

@author: zz
@date: 2020.10.14
'''

import os
from glob import glob


img_file = "test_align_yaw/Images"
save_file = os.path.join(os.path.dirname(img_file), "file_list.txt")

assert os.path.exists(img_file), print(f"[Error] {img_file} doesn't exist!")

imgs = glob(img_file+'/*.jpg')
with open(save_file, 'w') as fout:
    for img in imgs:
        fout.write(os.path.basename(img)+'\n')

print("Done.")



