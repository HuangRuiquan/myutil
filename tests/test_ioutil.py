# -*- coding:utf-8 -*-
# @Author   :HRQ
# @Time     :2023/3/27

from myutil.ioutil import Path


class Test_ioutil_path:
    def test_get_all_sub_folder_list(self):
        """
        测试get_all_sub_folder_list方法及 get_sub_folder_list方法
        :return:
        """
        assert Path("test_data\\folder").get_all_sub_folder_list().__len__() == 7, \
            "get_all_sub_folder_list或get_sub_folder_list方法没通过测试"
