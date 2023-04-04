# -*- coding:utf-8 -*-
# @Author   :HRQ
# @Time     :2023/3/27

import os
from typing import List

__all__ = [
    "Path",
]


class FooError(ValueError):
    """
    自定义报错类
    """
    pass


class Path:
    """
    对路径操作的类
    """

    def __init__(self, path):
        """
        用于操作跟路径有关的类
        :param path: 绝对路径
        """

        self.path = os.path.abspath(path)

    @property
    def isfile(self):
        """
        路径为文件时返回True，否则返回False
        """
        if os.path.isfile(self.path):
            return True
        return False

    @property
    def isdir(self):
        """
        路径为文件夹时返回True，否则返回False
        """

        if os.path.isdir(self.path):
            return True
        return False

    def get_sub_folder_list(self, folder_name_include_char: List[str] = None) -> List[str]:
        """
        根据提供的路径返回路径下的子文件夹列表
        :return: 返回子文件夹列表
        """
        if not os.path.isdir(self.path):
            raise FooError(f"提供的路径不存在或者不是文件夹:{self.path}")
        path_list = [os.path.join(self.path, p) for p in os.listdir(self.path)]
        folder_list = []
        for p in path_list:
            if os.path.isdir(p):
                if folder_name_include_char is None:
                    folder_list.append(p)
                else:
                    basename = os.path.basename(p)
                    for char in folder_name_include_char:
                        if char in basename:
                            folder_list.append(p)
        return folder_list

    def get_file_list_at_present_dir(self, suffix: List[str] = None) -> List[str]:
        """
        根据提供的路径返回路径下的文件列表,可指定后缀
        :param suffix:指定文件后缀名列表
        :return: 返回文件列表
        """
        if not self.isdir:
            raise FooError(f"提供的路径不存在或者不是文件夹:{self.path}")
        path_list = [os.path.join(self.path, p) for p in os.listdir(self.path)]
        folder_list = []
        for p in path_list:
            if os.path.isfile(p):
                if (suffix is None) or ("*.*" in suffix) or (".*" in suffix) or ("." in suffix):
                    folder_list.append(p)
                else:
                    if os.path.splitext(p)[1] in suffix:
                        folder_list.append(p)
        return folder_list

    def get_sub_folder_name_list_at_present_dir(self) -> List[str]:
        """
        返回当前路径下文件夹名称
        :return: 文件夹名称列表
        """
        path_list = self.get_sub_folder_list()
        folder_name_list = []
        for path in path_list:
            folder_name_list.append(os.path.basename(path))
        return folder_name_list

    def get_file_name(self, retain_suffix=True) -> str:
        """
        获取文件名，可以指定是否带有后缀名，默认带有后缀
        :param retain_suffix: 是否带后缀
        :return: 返回文件名
        """
        if retain_suffix:
            return os.path.basename(self.path)
        else:
            return os.path.splitext(os.path.basename(self.path))[0]

    def get_all_sub_folder_list(self, folder_name_include_char: List[str] = None) -> List[str]:
        """
        获取文件夹下所有子文件夹绝对路径
        Args:
            folder_name_include_char: 文件夹名称中需包含的字符串 组成的列表

        Returns:所有子文件夹绝对路径

        """
        folder_list = self.get_sub_folder_list(folder_name_include_char)
        for folder in folder_list:
            f_list = Path(folder).get_sub_folder_list(folder_name_include_char)
            if not f_list.__len__():
                continue
            else:
                folder_list.extend(f_list)
                Path(folder).get_all_sub_folder_list(folder_name_include_char)
        return folder_list

    def get_all_file_list(self, suffix: List[str] = None) -> List[str]:
        """
        获取当前文件夹及所有子文件夹下的文件的绝对路径
        :param suffix: 文件后缀名列表
        :return: 返回文件的绝对路径列表
        """
        folder_list = self.get_all_sub_folder_list()
        file_list = self.get_file_list_at_present_dir(suffix)
        for folder in folder_list:
            file_list.extend(Path(folder).get_file_list_at_present_dir(suffix))
        return file_list

    def get_filename_list_at_present_dir(self, suffix: List[str] = None) -> List[str]:
        """
        获取当前文件夹下文件名列表
        Args:
            suffix: 文件后缀列表

        Returns:文件名列表

        """
        filename_list = []
        for file in self.get_file_list_at_present_dir(suffix):
            filename_list.append(os.path.basename(file))
        return filename_list

    def makedir(self, mode=0o777):
        """
        创建文件夹，不用考虑文件夹是否是单层文件已存在也不报错
        Args:
            mode:要为目录设置的权限数字模式，默认的模式为 0o777 (八进制)
        """
        os.makedirs(self.path, mode, exist_ok=True)

    def change_suffix(self, suffix: str) -> str:
        """
        修改文件后缀名
        Args:
            suffix: 后缀名  example：".doc"

        Returns:返回改变了后缀名的文件路径

        """
        if not self.isfile:
            raise FooError("不是文件路径")
        else:
            path, suf = os.path.splitext(self.path)
            return path + suffix

    def change_filename_not_change_suffix(self, filename: str, add_to=False, ) -> str:
        """
        修改文件名称，不改后缀
        Args:
            filename: 文件名
            add_to:默认为False，为True时将filename追加到原名称后
        Returns:新的文件绝对路径

        """
        if not self.isfile:
            raise FooError("不是文件路径")
        else:
            path, suffix = os.path.splitext(self.path)
            if add_to:
                return path + filename + suffix
            path_ = os.path.split(path)[0]
            return os.path.join(path_, filename) + suffix


if __name__ == "__main__":
    # print(Path("..\\tests\\test_data\\folder\\new_dir1\\new_dir2\\new_dir3").makedir())
    print(Path("..\\..\\tests\\test_data\\folder").get_all_sub_folder_list())
    # help(Path)
    pass
