#! /usr/bin/python
# -*- coding:utf-8  -*-

import time

for i in dir(time):
    if not i.startswith("_"):
        if hasattr(eval("time.%s"%i), "__call__"):
            print(i, end=" ==== ")
            try:
                print(eval("time.%s()"%i))
            except TypeError as e:
                print("")
print(time.perf_counter())
print(time.clock())
print(time.clock())
