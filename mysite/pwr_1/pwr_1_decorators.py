__author__ = 'Lin'

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps
    
import logging
import os

import MySQLdb

from mysite import settings

def get_logger():

    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'site.log')
    file_handler = logging.FileHandler(filename=log_path)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s %(filename)s(line%(lineno)d) in function :%(funcName)s'
                          '\n%(message)s'))
    logger = logging.getLogger('auto_test_report_log')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    return logger


def exception_handler(func):
    logger = get_logger()
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IOError, e:
            logger.error('IOError: ' + e.message)
        except NameError, e:
            logger.error('NameError: ' + e.message)
        except Exception, e:
            logger.error('Exception: ' + e.message)

    return wrapper



def mysql_con(sql_cmd):
    def decorator(func):
        @wraps(func)
        def wrapper():
            db = MySQLdb.connect(host=settings.DATABASES['default']['HOST'], user=settings.DATABASES['default']['USER'],
                                 passwd=settings.DATABASES['default']['PASSWORD'],
                                 db=settings.DATABASES['default']['NAME'])
            cur = db.cursor()
            cur.execute(sql_cmd)
            info = cur.fetchall()
            result = func(info)
            db.close()
            return result

        return wrapper

    return decorator


if __name__ == '__main__':
    # @mysql_con('show databases;')
    # def test(info):
    #     print 'in test:', info
    #     return info
    #
    # res = test()
    # print res

    logger.warning('hahaha')
    logger.debug('info!!!!')