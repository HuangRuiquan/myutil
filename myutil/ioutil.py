import os

__all__ = [
    "Path"
]

from typing import List


class FooError(ValueError):
    pass


class Path:
    def __init__(self, path):
        """
        用于操作跟路径有关的类
        :param path: 绝对路径
        """

        self.path = os.path.abspath(path)

    def get_one_sub_folder_list(self) -> List[str]:
        """
        根据提供的路径返回路径下的子文件夹列表
        :return:
        """
        if not os.path.isdir(self.path):
            raise FooError(f"提供的路径不存在或者不是文件夹:{self.path}")
        path_list = [os.path.join(self.path, p) for p in os.listdir(self.path)]
        folder_list = []
        for p in path_list:
            if os.path.isdir(p):
                folder_list.append(p)
        return folder_list

    def get_file_list_at_present_dir(self, suffix: List[str] = None) -> List[str]:
        """
        根据提供的路径返回路径下的文件列表,可指定后缀
        :param suffix:指定文件后缀名列表
        :return: 返回文件列表
        """
        if suffix is None:
            if not os.path.isdir(self.path):
                raise FooError(f"提供的路径不存在或者不是文件夹:{self.path}")
            path_list = [os.path.join(self.path, p) for p in os.listdir(self.path)]
            folder_list = []
            for p in path_list:
                if os.path.isfile(p):
                    folder_list.append(p)
            return folder_list

    def get_one_sub_folder_name_list(self) -> List[str]:
        """
        返回当前路径下文件夹名称，不包含路径
        :return: 文件夹名称列表
        """
        path_list = self.get_one_sub_folder_name_list()
        folder_name_list = []
        for path in path_list:
            folder_name_list.append(os.path.basename(path))
        return folder_name_list


if __name__ == "__main__":

    print(Path(r"D:\python\myutil\tests\folder").get_one_sub_folder_name_list())
