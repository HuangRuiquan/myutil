import os

__all__ = []


def get_one_sub_folder_list(path):
    path_list = os.listdir(path)

    print(path_list)


if __name__ =="__main__":
    get_one_sub_folder_list(r"D:\python\myutil\tests\folder")