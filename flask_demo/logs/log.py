import logging
import os
import time

logger = logging.getLogger(__name__)


def initial_log():
    logger.setLevel(logging.DEBUG)
    filename = "logger_{}.log".format(time.strftime("%Y-%m-%d", time.localtime(time.time())))

    log_file = os.path.join(os.path.dirname(__file__), filename)

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

initial_log()
