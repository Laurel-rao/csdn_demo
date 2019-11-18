#! /usr/bin/python
# -*- coding:utf-8  -*-

import time
from core import *
from show_game import game_interface


def menu():
    print("+{}+".format("-" * 30))
    print("|%s|" % ("1．进入游戏".center(25)))
    print("|%s|" % ("2．载入进度".center(25)))
    print("|%s|" % ("3．保存游戏".center(25)))
    print("|%s|" % ("4．退出游戏".center(25)))
    print("+{}+".format("-" * 30))


def showtime():
    # 主程序
    data = prime_data()  # 初始数据
    while True:
        menu()
        option = int(input("请输入您要进行的操作："))
        if option == 1:
            game_interface(*data)
            while True:
                try:
                    data = data_handle(data)
                    game_interface(*data)
                except NameError as e:
                    print(e)
                    break
                except ImportError as e:
                    print(e)
                    time.sleep(10)
                    break
                except OSError:
                    break
                except StopIteration as e:
                    print(e)
                    continue
        elif option == 2:
            # 载入数据
            data = read_data(filename="archive.txt")
            game_interface(*data)
            while True:
                try:
                    data = data_handle(data)
                    game_interface(*data)
                except NameError as e:
                    print(e)
                    break
                except ImportError as e:
                    print(e)
                    time.sleep(10)
                    break
                except OSError:
                    break
                except StopIteration as e:
                    print(e)
                    continue
        elif option == 3:
            # 保存数据
            save_data(data, filename="archive.txt")
        elif option == 4:
            exit()


if __name__ == "__main__":
    showtime()
