# Sample Test passing with nose and pytest
from myutil.ioutil import Path

def test_pass():
    assert True, "dummy sample test"


def test_Path_get_one_sub_folder_list():
    return Path(r"folder").get_one_sub_folder_list() == [
                                                        r"D:\python\myutil\tests\folder\folder_1_1",
                                                        r"D:\python\myutil\tests\folder\folder_1_2",
                                                        r"D:\python\myutil\tests\folder\folder_1_3"
                                                         ]
