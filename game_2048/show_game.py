#! /usr/bin/python
# -*- coding:utf-8  -*-


def game_interface(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4):
    # 游戏打印界面

    l = list((a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4))

    a1 = " " if not a1 else a1
    a2 = " " if not a2 else a2
    a3 = " " if not a3 else a3
    a4 = " " if not a4 else a4
    b1 = " " if not b1 else b1
    b2 = " " if not b2 else b2
    b3 = " " if not b3 else b3
    b4 = " " if not b4 else b4
    c1 = " " if not c1 else c1
    c2 = " " if not c2 else c2
    c3 = " " if not c3 else c3
    c4 = " " if not c4 else c4
    d1 = " " if not d1 else d1
    d2 = " " if not d2 else d2
    d3 = " " if not d3 else d3
    d4 = " " if not d4 else d4

    print("\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(a1).center(7), str(a2).center(7), str(a3).center(7), str(a4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(b1).center(7), str(b2).center(7), str(b3).center(7), str(b4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(c1).center(7), str(c2).center(7), str(c3).center(7), str(c4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(d1).center(7), str(d2).center(7), str(d3).center(7), str(d4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n", end="")

    for i in l:
        s = int(i)
        if s > 2000:
            raise ImportError("恭喜达到2048！！！")

