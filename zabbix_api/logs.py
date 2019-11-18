#! /usr/bin/python
# -*- coding:utf-8  -*-

import logging
import os
import time

logger = logging.getLogger(__name__)

def handler_setting():
    # logger-2019-11-11.log
    filename = os.path.join(os.path.dirname(__file__), "logger-%s.log"%time.strftime("%Y-%m-%d"))

    # create a handler
    fileHandler = logging.FileHandler(filename)
    streamHandler = logging.StreamHandler()

    # setting of log format
    formatter = logging.Formatter("%(asctime)s-[%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")

    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    fileHandler.setLevel(logging.INFO)
    streamHandler.setLevel(logging.DEBUG)

    # use the file and stream
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


handler_setting()

