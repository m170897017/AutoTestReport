__author__ = 'Lin'

import logging

file_handler = logging.FileHandler(filename='site.log')
file_handler.setFormatter(logging.Formatter( '%(asctime)s %(levelname)s %(filename)s(line%(lineno)d) in function :%(funcName)s'
    '\n%(message)s'))
file_handler.setLevel(logging.DEBUG)
logger = logging.getLogger('auto_test_report_log')
logger.addHandler(file_handler)


def exception_handler(func):
    def you_will_never_see_my_name(*args):
        try:
            func(*args)
        except IOError, e:
            logger.error('IOError: ' + e.message)
        except NameError, e:
            logger.error('NameError: ' + e.message)
        except Exception, e:
            logger.error('Exception: ' + e.message)

    return you_will_never_see_my_name



if __name__ == '__main__':
    # tests for function exception_handler
    @exception_handler
    def test1():
        a
    test1()

    @exception_handler
    def test2(a):
        print a
    test2(2)


