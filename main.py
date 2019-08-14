import glob
import os
from getMouseClick import click_save
from generate_densitymap import generate_dm

pick_path = 'D:/Tbx/ShanghaiTech/part_B/7'
pick_list = []
try:
    for img_name in glob.glob(os.path.join(pick_path, '*.jpg')):
        lst_name = img_name.replace('.jpg', '.lst')
        click_save(img_name, lst_name)
        generate_dm(lst_name)
except:
    print('program end')
