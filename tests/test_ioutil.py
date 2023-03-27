# -*- coding:utf-8 -*-
# @Author   :HRQ
# @Time     :2023/3/27
import unittest
from myutil.ioutil import Path


class Test_ioutil_path(unittest.TestCase):
    def test_get_all_sub_folder_list(self):
        """
        测试get_all_sub_folder_list方法及 get_sub_folder_list方法
        :return:
        """
        assert Path(r"E:\Py\myutil\tests\test_data\folder").get_all_sub_folder_list().__len__() == 7, \
            "get_all_sub_folder_list或get_sub_folder_list方法没通过测试"

    def test_get_all_file_list(self):
        assert Path(r"E:\Py\myutil\tests\test_data\folder").get_all_file_list().__len__() == 18, \
            "get_all_file_list或者get_file_list_at_present_dir方法没通过测试"

    def test_get_file_name(self):
        assert Path(r"E:\Py\myutil\tests\test_data\folder\doc_1.doc").get_file_name() == "doc_1.doc"
        assert Path(r"E:\Py\myutil\tests\test_data\folder\doc_1.doc").get_file_name(False) == "doc_1"

    def test_get_filename_list_at_present_dir(self):
        assert Path(r"E:\Py\myutil\tests\test_data\folder").get_filename_list_at_present_dir([".txt"]).__len__() == 3


if __name__ == "__main__":
    unittest.main()
