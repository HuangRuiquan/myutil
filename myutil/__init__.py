"""myutil - 对一些包包装成个人使用的包"""
from . import myutil
from . import ioutil
from .ioutil import *


__version__ = '0.1.0'
__author__ = 'HRQ <2510853126@qq.com>'
__all__ = []
__all__ += ioutil.__all__
