# -*- coding:utf-8 -*-
# @Author   :HRQ
# @Time     :2023/4/12


import cv2
from tqdm import tqdm
from src.myutil.ioutil import Path

train_0_path = r"\\192.168.1.247\Pictures\Train_V320\socket_polarity\train\0"
file_list = Path(train_0_path).get_file_list_at_present_dir([".bmp"])


for file in tqdm(file_list, desc="正在转换0"):
    img = cv2.imread(file)
    cv2.namedWindow("win", cv2.WINDOW_NORMAL)
    cv2.imshow("win", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
