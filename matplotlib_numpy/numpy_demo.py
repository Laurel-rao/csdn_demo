#! /usr/bin/python
# -*- coding:utf-8  -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plot


#打开一个画布：

figure = plot.figure()

#画出三维坐标系：

axes = Axes3D(figure)



"""

x ** 2 + y ** 2 + z ** 2 = 9

function picture

"""


#限定x和y的画图范围：

x = np.arange(0, 3, 0.1)


y = np.arange(0, 3, 0.1)

#限定图形的样式是网格线的样式：

x, y = np.meshgrid(x, y)

Z = np.sqrt(10 - (x**2 + y**2))
# print(Z)

#绘制曲面，采用彩虹色着色：

axes.plot_surface(x, x, Z,cmap='rainbow')

#图形可视化：

plot.show()

