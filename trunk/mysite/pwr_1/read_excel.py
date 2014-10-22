#!/usr/bin/env python
# -*- coding: UTF-8 -*
import xlrd
import re

class ReadExcel(object):
    
    def __init__(self,file_path):
        self.ex = xlrd.open_workbook(file_path)
    
    def get_test_items_list(self):
        self.sh = self.ex.sheet_by_name(u'Test Items')
        
        row_number = self.sh.nrows
        patt_1  = '.\..\..*'
        self.test_item_list     = []
        self.index_list         = []
        
        # row_number-6 ,because it is test result comment in the last 6 rows
        for i in range(0,row_number-6):
            try:
                value_t = self.sh.cell(i,0).value
                value_1 = str(value_t)
                res_1   = re.match(patt_1,value_1)
                # find 1.1.x, record, otherwise, continue
                if res_1:
                    self.index_list.append(res_1.group())
                    self.test_item_list.append(self.sh.cell(i,1).value)
                else:
                    continue
            except:
                continue
        return [self.test_item_list,self.index_list]
    
    
    
if __name__ == '__main__':
    
    path = 'C://pwrcyl.xls'
    a = ReadExcel(file_path=path)
    [item_list,index_list] = a.get_test_items_list()
    print item_list
    print index_list
    b = raw_input('please press enter to quit!')