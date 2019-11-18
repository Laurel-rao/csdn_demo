#! /usr/bin/python
# -*- coding:utf-8  -*-

# 进行数据处理，根据操作进行数据转换

import random as r
import sys

square = (2, 2, 2, 4)


def prime_data():
    # 起始布局
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pp = r.choice(square)
    pp1 = r.choice(square)
    location = r.sample([i for i in range(16)], 2)
    data[location[0]] = pp
    data[location[1]] = pp1
    return data


def tran_data(data, n):
    # 根据操转换为４个小数据列表
    # 操作的反向为底边 zero
    small_list = []
    # print(data)
    if n == 0:  # 向上操作
        for i in range(4):
            zero = [data[i], data[i + 4], data[i + 8], data[i + 12]]
            small_list.append(zero)
    elif n == 1:  # 向右操作
        zero = data[0:4][::-1]
        one = data[4:8][::-1]
        two = data[8:12][::-1]
        three = data[12:16][::-1]
        small_list = [three, two, one, zero]
    elif n == 2:  # 向下操作
        for i in range(12, 16):
            zero = [data[i], data[i - 4], data[i - 8], data[i - 12]]
            small_list.append(zero)
    elif n == 3:  # 向左操作
        zero = data[:4]
        one = data[4:8]
        two = data[8:12]
        three = data[12:]
        small_list = [three, two, one, zero]
    return small_list


def add_number(data, n):
    # 数据处理函数
    lis = []
    small_list = tran_data(data, n)
    for p in small_list:
        try:
            for x in range(4):
                p.remove(0)
        except ValueError:
            pass
        while True:
            s = len(p)
            if s < 4:
                p.append(0)
            else:
                break
        if p[0] == p[1]:
            if p[2] == p[3]:
                p[0] += p[1]
                p[1] = p[2] + p[3]
                p[2], p[3] = 0, 0
            else:
                p[0] += p[1]
                p[1], p[2], p[3] = p[2], p[3], 0
        elif p[2] == p[1]:
            p[1] += p[2]
            p[2], p[3] = p[3], 0
        elif p[2] == p[3]:
            p[2] += p[3]
            p[3] = 0
        lis.append(p)
    data = tran_list(lis, n)
    return data


def tran_list(small_list, n):
    big_list = []
    if n == 0:
        for x in range(4):
            for i in range(4):
                big_list.append(small_list[i][x])
    elif n == 1:
        for i in [3, 2, 1, 0]:
            s = small_list[i][::-1]
            for x in s:
                big_list.append(x)

    elif n == 2:
        for x in range(4):
            for i in [3, 2, 1, 0]:
                big_list.append(small_list[i][x])
        big_list = big_list[::-1]
    elif n == 3:
        for i in [3, 2, 1, 0]:
            for x in small_list[i]:
                big_list.append(x)

    return big_list


def judgement(big_list):
    # 生成并修改数据
    s = []
    for i in range(16):
        if not big_list[i]:
            p = i
            s.append(p)
    try:
        l = r.choice(square)
        z = r.choice(s)
    except (ValueError, IndexError):
        s = input("游戏结束，请按任意键退出")
        raise NameError("　游戏结束！")
    big_list[z] = l
    return big_list


def data_handle(data):
    n = input("W A S D(上下左右)－－－＞")
    if len(n) > 1:
        n = n[-1]
    if n in ("w"):
        # 向上划
        data = add_number(data, 0)
    elif n in ("d"):
        # 向右划
        data = add_number(data, 1)
    elif n in ("s"):
        # 向下划
        data = add_number(data, 2)
    elif n in ("a"):
        # 向左划
        data = add_number(data, 3)
    elif n in "q":
        raise OSError
    else:
        raise StopIteration("请输入正确操作")
    data = judgement(data)
    return data  # 返回数据给游戏界面


def read_data(filename="archive.txt"):
    s = []
    try:
        file = open(filename)
        for i in file:
            p = i.strip()
            pp = int(p)
            s.append(pp)
        file.close()
    except OSError:
        print("文件打开失败")
    return s


def save_data(data, filename="archive.txt"):
    try:
        file = open(filename, "w")
        for i in data:
            file.write(str(i))
            file.write("\n")
        file.close()
    except OSError:
        print("文件打开错误")

