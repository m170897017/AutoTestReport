__author__ = 'Lin'

from functools import wraps
import logging

import MySQLdb

from mysite import settings


file_handler = logging.FileHandler(filename='site.log')
file_handler.setFormatter(
    logging.Formatter('%(asctime)s %(levelname)s %(filename)s(line%(lineno)d) in function :%(funcName)s'
                      '\n%(message)s'))
file_handler.setLevel(logging.DEBUG)
logger = logging.getLogger('auto_test_report_log')
logger.addHandler(file_handler)


def exception_handler(func):
    def you_will_never_see_my_name(*args):
        try:
            func(*args)
        except IOError, e:
            # logger.error('IOError: ' + e.message)
            print e
        except NameError, e:
            # logger.error('NameError: ' + e.message)
            print e
        except Exception, e:
            # logger.error('Exception: ' + e.message)
            print e

    return you_will_never_see_my_name


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
    @mysql_con('show databases;')
    def test(info):
        print 'in test:', info
        return info

    res = test()
    print res