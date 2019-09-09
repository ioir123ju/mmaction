#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   generate_filelist.py
@Contact :   juzheng@hxdi.com
@License :   (C)Copyright 2018-2019, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/9/6 16:32   juzheng      1.0         None
"""

import os
import glob
import numpy as np
# dirs = os.listdir("data/hmdb51/rawframes/fall_floor")
# with open("data.txt", 'w') as f:
#
#     for path in dirs:
#         path_file_number = glob.glob("data/hmdb51/rawframes/fall_floor/" + path+"/*") #获取当前文件夹下个数
#         num = len(path_file_number)
#         path_of_video = os.path.join("fall_floor", path)
#         data_class = 100
#         data = str(path_of_video) + " " + str(num) + " " + str(data_class)
#         f.write(data + '\n')


if __name__ == "__main__":
    # 生成labels
    labels = {}
    dirs = os.listdir("data/hmdb51/rawframes")
    for i, path in enumerate(sorted(dirs)):
        labels[path] = i
    with open("data/hmdb51/labels.txt", 'w') as f:
        for key in labels:
            f.write(key + ' ' + str(labels[key]) + '\n')

    labels = {}
    # 加载数据路径
    with open("data/hmdb51/labels.txt", 'r') as f:
        for line in f:
            labels[line.split(' ')[0]] = int(line.split(' ')[1])

    all_data = []
    for key in labels:
        ann_dir = "data/hmdb51/rawframes/" + key
        dirs = os.listdir(ann_dir)
        for path in dirs:
            sub_path = ann_dir + "/" + path + "/*"
            path_file_number = glob.glob(r'' + sub_path)
            num = len(path_file_number)
            if num == 0:
                print(ann_dir + "/" + path + "/*")

            path_of_video = os.path.join(key, path)
            data_class = labels[key]
            data = str(path_of_video) + " " + str(num) + " " + str(data_class)
            all_data.append(data)
    split_index = np.random.choice(['train', 'val', 'test'], size=len(all_data), p=[0.6, 0.2, 0.2])
    with open("data/hmdb51/train_split.txt", 'w') as f:
        split_data = np.where(split_index == 'train')
        for i in split_data[0].flat:
            f.write(all_data[int(i)] + '\n')
    with open("data/hmdb51/val_split.txt", 'w') as f:
        split_data = np.where(split_index == 'val')
        for i in split_data[0].flat:
            f.write(all_data[int(i)] + '\n')
    with open("data/hmdb51/test_split.txt", 'w') as f:
        split_data = np.where(split_index == 'test')
        for i in split_data[0].flat:
            f.write(all_data[int(i)] + '\n')