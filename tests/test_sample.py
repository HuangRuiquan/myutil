# Sample Test passing with nose and pytest
from myutil.ioutil import Path


def test_pass():
    assert test_path_get_sub_folder_list(), "path_get_sub_folder_list test Fail"
    assert test_path_get_one_sub_folder_name_list(), "path_get_one_sub_folder_name_list test Fail"
    assert test_path_get_file_name(), "path_get_file_name test Fail"
    assert test_path_get_all_sub_folder_list(), "path_get_all_sub_folder_list test Fail"
    assert test_path_get_all_file_list(), "path_get_all_file_list test Fail"
    print("simple test pass")


def test_path_get_sub_folder_list():
    return Path(r"folder").get_sub_folder_list().__len__() == 4


def test_path_get_one_sub_folder_name_list():
    return Path(r"folder").get_one_sub_folder_name_list() == \
           ['file_0_3.4.txt', 'folder_1_1', 'folder_1_2', 'folder_1_3']


def test_path_get_file_name():
    return Path(r"folder/file_0_1.txt").get_file_name() == "file_0_1.txt" and \
           Path(r"folder/file_0_1.txt").get_file_name(False) == "file_0_1"


def test_path_get_all_sub_folder_list():
    return Path(r"folder").get_all_sub_folder_list().__len__() == 11


def test_path_get_all_file_list():
    """
    测试Path get_all_file_list方法跟get_file_list_at_present_dir 方法
    :return:
    """
    return Path(r"folder").get_all_file_list([".png", ".rtf"]).__len__() == 2


if __name__ == "__main__":
    test_pass()
