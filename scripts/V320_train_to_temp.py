# -*- coding:utf-8 -*-
# @Author   :HRQ
# @Time     :2023/4/12


import cv2
from tqdm import tqdm
from src.myutil.ioutil import Path

save_path = r"\\192.168.1.247\Pictures\Train_V320\socket_polarity\temp"
train_path = r"\\192.168.1.247\Pictures\Train_V320\socket_polarity\train"


def rotation(image, angle):
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        return image


folder_list = [
    save_path + "\\0",
    save_path + "\\1",
    save_path + "\\2",
    save_path + "\\3"
]
for folder in folder_list:
    Path(folder).makedir()

dir_list = Path(train_path).get_sub_folder_list()
for d in dir_list:
    file_list = Path(d).get_file_list_at_present_dir([".bmp"])
    if Path(d).get_file_name() == "0":
        angle_list = [0, 90, 180, 270]
        for file in tqdm(file_list, desc="正在转换0"):
            img = cv2.imread(file)
            for i in range(4):
                file = folder_list[i] + "\\" + Path(file).get_file_name()
                cv2.imwrite(file, rotation(img, angle_list[i]))

    elif Path(d).get_file_name() == "1":
        angle_list = [270, 0, 90, 180]
        for file in tqdm(file_list, desc="正在转换1"):
            img = cv2.imread(file)
            for i in range(4):
                file = folder_list[i] + "\\" + Path(file).get_file_name()
                cv2.imwrite(file, rotation(img, angle_list[i]))

    elif Path(d).get_file_name() == "2":
        angle_list = [180, 270, 0, 90]
        for file in tqdm(file_list, desc="正在转换2"):
            img = cv2.imread(file)
            for i in range(4):
                file = folder_list[i] + "\\" + Path(file).get_file_name()
                cv2.imwrite(file, rotation(img, angle_list[i]))

    elif Path(d).get_file_name() == "3":
        angle_list = [90, 180, 270, 0]
        for file in tqdm(file_list, desc="正在转换3"):
            img = cv2.imread(file)
            for i in range(4):
                file = folder_list[i] + "\\" + Path(file).get_file_name()
                cv2.imwrite(file, rotation(img, angle_list[i]))
