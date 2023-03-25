# Sample Test passing with nose and pytest
from myutil.ioutil import Path


def test_pass():
    assert test_path_get_one_sub_folder_list()\
           and test_path_get_one_sub_folder_name_list()\
           and test_path_get_file_name(), "class_Path test Fail"


def test_path_get_one_sub_folder_list():
    return Path(r"folder").get_one_sub_folder_list() == [
        r"D:\python\myutil\tests\folder\folder_1_1",
        r"D:\python\myutil\tests\folder\folder_1_2",
        r"D:\python\myutil\tests\folder\folder_1_3"
    ]


def test_path_get_one_sub_folder_name_list():
    return Path(r"folder").get_one_sub_folder_name_list() == [
        r"folder_1_1",
        r"folder_1_2",
        r"folder_1_3"
    ]


def test_path_get_file_name():
    return Path(r"folder/file_0_1.txt").get_file_name() == "file_0_1.txt" and \
           Path(r"folder/file_0_1.txt").get_file_name(False) == "file_0_1"


if __name__ == "__main__":
    test_pass()
