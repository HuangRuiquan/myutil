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
            raise FooError(f"提供的路径不存在或不是文件夹:{self.path}")
        path_list = [os.path.join(self.path, p) for p in os.listdir(self.path)]
        folder_list = []
        for p in path_list:
            if os.path.isdir(p):
                folder_list.append(p)
        return folder_list


if __name__ == "__main__":

    print(Path(r"D:\python\myutil\tests\folder").get_one_sub_folder_list())
