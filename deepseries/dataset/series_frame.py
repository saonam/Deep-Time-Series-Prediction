# encoding: utf-8
"""
@author : zhirui zhou
@contact: evilpsycho42@gmail.com
@time   : 2020/4/1 16:28
"""
from torch.utils.data import DataLoader


class SeriesFeature:
    pass


class SeriesFrame(object):

    def __init__(self, raw_x, raw_x_valid=None):
        self.raw_x


class Data:

    def __iter__(self):
        for i in range(5):
            yield i