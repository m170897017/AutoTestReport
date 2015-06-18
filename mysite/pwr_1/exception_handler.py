__author__ = 'Lin'

import logging

file_handler = logging.FileHandler(filename='site.log')
file_handler.setFormatter(logging.Formatter( '%(asctime)s %(levelname)s %(filename)s(line%(lineno)d) in function :%(funcName)s'
    '\n%(message)s'))
file_handler.setLevel(logging.INFO)
logger = logging.getLogger('auto_test_report_log')
logger.addHandler(file_handler)


def exception_handler(func):
    def you_will_never_see_my_name():
        try:
            func()
        except IOError, e:
            logger.info(e)
        except Exception, e:
            logger.info(e)
    return you_will_never_see_my_name

