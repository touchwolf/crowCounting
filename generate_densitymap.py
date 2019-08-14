import numpy as np
import h5py
from utils_gen import gen_density_map_gaussian

def generate_dm(lst_name):
    lst_name = lst_name
    with open(lst_name, 'r') as f:
        shape = eval(f.readline().strip())
        gt = []
        for line in f.readlines():
            gt.append(eval(line.strip()))
        gt = np.array(gt)
    #k : imgshape
    #gt : point coordinates of label
    #sigma : size of gaussian kernel
    k = np.zeros((shape[0], shape[1]))
    sigma = 10
    for i in range(len(gt)):
        if gt[i][1]<shape[0] and gt[i][0]<shape[1]:
            k[gt[i][1], gt[i][0]] = 1
    DM = gen_density_map_gaussian(k, gt, sigma=sigma)
    file_path = lst_name.replace('.lst', '.h5')
    with h5py.File(file_path, 'w') as hf:
        hf['density'] = DM

if __name__ == '__main__':
    generate_dm('C:/Users/sh/Desktop/_models/IMG_1123.lst')