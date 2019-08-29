#! /usr/bin/python
# -*- coding:utf-8  -*-

import datetime
import difflib
# datetime.datetime.now()
#
# for i in dir(datetime.datetime):
#     if not i.startswith("_"):
#         if hasattr(eval("datetime.datetime.%s"%i), "__call__"):
#             print(i, end=" ==== ")
#             try:
#                 print(eval("datetime.datetime.%s()"%i))
#             except TypeError as e:
#                 print("")
#
# from datetime import datetime, timedelta
#
# now = datetime.now() + timedelta(hours=24, seconds=24)
# print(now)
# print(timedelta(hours=24, seconds=24) == timedelta(hours=24, seconds=24))
# print(timedelta(hours=(1/7)).total_seconds())
# print(datetime.now().astimezone())
import json
import re

o = "123\n567\n89\n"
p = "123\n567\n8910\n"

a = difflib.context_diff(o, p)
b = difflib.unified_diff(o, p)
b = difflib.unified_diff(o, p)
# print(list(b))
# print(json.dumps(list(a), indent=4))

string = """
H3C Comware Software, Version 7.1.070, Release 7576
Copyright (c) 2004-2018 New H3C Technologies Co., Ltd. All rights reserved.
H3C S7506E-X uptime is 46 weeks, 1 day, 14 hours, 36 minutes
Last reboot reason : Cold reboot
"""
data = re.search("version ([\d\.]+)", string, flags=2)
data = re.search("reserved\.\n(.+?) uptime", string, flags=2)
if data:
    print(data.group(1))
