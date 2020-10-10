#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/10
# @Author: Lingchen
# @Prescription:
#   演示__missing__是如何被dict.__getitem__调用的
#   在查询的时候把非字符串的键转换为字符串


class StrKeyDict0(dict):
    """
    在查询的时候把非字符串的键转换为字符串
    """
    def __missing__(self, key):
        """
        若找不到的键本身就是字符串，那就抛出异常
        :param key:
        :return:
        """
        if isinstance(key, str):
            raise KeyError(key)

        # 若找不到的键不是字符串，那么把它转换成字符串再进行查找
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # get方法把查找工作用self[key]的形式委托给__getitem__，这样在宣布查找失败之前
            # 还能通过__missing__再给某个键一个机会
            return self[key]
        except KeyError:
            # 若抛出KeyError, 那么说明__missing__也失败了，于是返回default
            return default


def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()


print('测试StrKeyDict0，__missing__操作：')
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
# print(d['2'])
#
# print(d['4'])

# print(d[4])

# KeyError: '1'
# print(d[1])

# print(d.get('2'))

# print(d.get('4'))

print(d.get(1, 'N/A'))


