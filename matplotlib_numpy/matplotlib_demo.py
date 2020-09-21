#! /usr/bin/python
# -*- coding:utf-8  -*-

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 360, 0.01)
y = np.arctan(x)

plt.title("Matplotlib Learning")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x,y)
plt.show()