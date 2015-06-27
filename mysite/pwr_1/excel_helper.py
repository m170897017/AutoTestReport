#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import os
import time
import copy

import xlrd
from xlwt import *

from pwr_1_decorators import mysql_con


DEFAULT_PATH = os.path.dirname(os.path.dirname(__file__)) + '\\test records\\pwrcyl.xls'


class ExcelHelper(object):
    """
    A self-defined class to handle event between excel and database.
    """

    def __init__(self, file_path=DEFAULT_PATH):
        self.test_item_list = None
        self.index_list = None
        self.ex = xlrd.open_workbook(file_path)
        self.sh = self.ex.sheet_by_name(u'Test Items')

    def get_test_items_list(self):
        """
        Get test items list from original test report template. Store index list and item list to instance attribute.
        :return: None
        """

        # test_item_list is used for test case description, like C-15551:power_cycle_func_wps_button_long_press
        self.test_item_list = []
        # index_list is used for test case id, like 1.1.1
        self.index_list = []
        row_number = self.sh.nrows
        patt_1 = '.\..\..*'

        # row_number-6 ,because it is test result comment in the last 6 rows
        for i in xrange(0, row_number - 6):

            try:
                value_t = self.sh.cell(i, 0).value
                value_1 = str(value_t)
                res_1 = re.match(patt_1, value_1)
                # find 1.1.x, record, otherwise, continue
                if res_1:
                    self.index_list.append(res_1.group())
                    self.test_item_list.append(self.sh.cell(i, 1).value)

                else:
                    continue
            except:
                continue
        assert len(self.index_list) == len(self.test_item_list), 'each test case should have one test case id!!\
            Check the test record template if you see this error message!!'


    @staticmethod
    @mysql_con('select * from pwr_1_pwr_test_item;')
    def get_test_items_list_from_db(*args, **kwargs):
        """
        Get test items from database.
        :param args: Used for detail handling.
        :param kwargs: Used for detail handling.
        :return: A tuple of sql result.
        """
        return args[0] if args else None

    @staticmethod
    @mysql_con('select * from pwr_1_pwr_test_item;')
    def get_fieldsets_for_admin(*args, **kwargs):
        """
        Get test items from database and generate fieldsets for admin.
        :param args: Used for detail handling.
        :param kwargs: Used for detail handling.
        :return: A tuple for fieldsets in admin.
        """


        fieldsets = [('Tester Information', {'fields': ('tester', 'test_date', 'test_summary', 'test_duration'),
                                             'classes': ('collapse', 'collapse-closed')}),
                     ('DUT Information', {'fields': ('dut_model', 'dut_sample_size', 'dut_summary', 'dut_chipset',
                                                     'dut_power', 'dut_shell', 'dut_antenna', 'dut_driver',
                                                     'dut_hw_version', 'dut_sw_version'),
                                          'classes': ('collapse', 'collapse-closed')}),
                     ('SUT Information',
                      {'fields': ('sut_model', 'sut_driver', 'sut_os', 'sut_hw_version', 'sut_sw_version'),
                       'classes': ('collapse', 'collapse-closed')}),
                     ('Testbed Information', {'fields': ('testbed_name', 'testbed_topo', 'testbed_remark'),
                                              'classes': ('collapse', 'collapse-closed')}),
                     ]

        if args:
            sql_result = args[0]
            test_items_num = len(sql_result)
            # sql_result will look like: ((1L, '1.1.1', 'C-15551:power_cycle_func_wps_button_long_press'), ...)

            # we have at most 30 lines now. But we use 2 to debug here
            test_items_num = 2
            for i in xrange(test_items_num):
                item_name = ''.join(
                    [sql_result[i][1], ' ', sql_result[i][2]])
                number = str(i)

                fieldsets.append((item_name, {'fields': (
                    'test_result_' + number, 'bug_level_' + number, 'bug_id_' + number, 'bug_summary_' + number,
                    'test_comment_' + number)}))

        return copy.deepcopy(tuple(fieldsets))

    @classmethod
    def _write_xls_oper(cls, file_name, rec, headings, data, heading_xf, data_xfs):
        """
        Operation for writing a new excel file.
        :param file_name: File name of final test report file.
        :param rec: database instance got from admin to handle database search.
        :param headings: The first line of final test report.
        :param data: Detail data for final test report.
        :param heading_xf: Heading format.
        :param data_xfs: Data format.
        :return: None.
        """

        book = Workbook()

        # write test result definition
        title_format = 'font: bold on;\
                      align: wrap on, vert center, horiz center;\
                      pattern: pattern solid, fore-color gray25;\
                      borders: left 0x01, right 0x01, top 0x01, bottom 0x01'
        content_format = 'align: wrap on; borders: left 0x01, right 0x01, top 0x01, bottom 0x01'
        content_format_1 = 'align: horiz center; borders: left 0x01, right 0x01, top 0x01, bottom 0x01'

        #############
        # write first sheet here
        #############

        sheet0 = book.add_sheet('Basic Information')

        # change cell width   1mm equals 260
        sheet0.col(0).width = int(13 * 260)
        sheet0.col(1).width = int(63 * 260)

        col_A = ['Tester Information', 'Tester', 'Test Date', 'Test Summary', 'Test Duration', 'DUT Information',
                 'Model', 'Sample Size', 'Summary', 'Chipset', 'Power', 'Shell', 'Antenna', 'Driver', 'HW Version',
                 'SW Version', 'SUT Information', 'Model', 'Driver', 'OS', 'HW Version', 'SW Version',
                 'Testbed Information', 'Name', 'Topo', 'Remark', ]
        col_B = ['For merge', rec.tester, rec.test_date, rec.test_summary, rec.test_duration, 'For merge',
                 rec.dut_model,
                 rec.dut_sample_size, rec.dut_summary, rec.dut_chipset, rec.dut_power, rec.dut_shell, rec.dut_antenna,
                 rec.dut_driver, rec.dut_hw_version, rec.dut_sw_version, 'For merge', rec.sut_model, rec.sut_driver,
                 rec.sut_os, rec.sut_hw_version, rec.sut_sw_version, 'For merge', rec.testbed_name, rec.testbed_topo,
                 rec.testbed_remark, ]

        for rowx in xrange(len(col_A)):
            if 'For merge' == col_B[rowx]:
                sheet0.write_merge(r1=rowx, r2=rowx, c1=0, c2=1, label=col_A[rowx], style=easyxf(title_format))
                continue
            sheet0.write(rowx, 0, col_A[rowx], easyxf(content_format))
            sheet0.write(rowx, 1, col_B[rowx], easyxf(content_format))

        #############
        # write second sheet here
        #############

        sheet1 = book.add_sheet('Test Items')

        # write sheet and set format
        rowx = 0
        for colx, value in enumerate(headings):
            sheet1.write(rowx, colx, value, heading_xf)
        sheet1.set_panes_frozen(True)  # frozen headings instead of split panes
        sheet1.set_horz_split_pos(rowx + 1)  # in general, freeze after last heading row
        sheet1.set_remove_splits(True)  # if user does unfreeze, don't leave a split there

        # change cell width   1mm equals 260
        sheet1.col(0).width = int(10.57 * 260)
        sheet1.col(1).width = int(93.86 * 260)
        sheet1.col(4).width = int(10.15 * 260)
        sheet1.col(5).width = int(40 * 260)

        # if there is bug id and bug summary, write it to the bottom of the sheet
        bsum = []
        bid = []
        for row in data:
            rowx += 1
            for colx, value in enumerate(row):
                if colx == len(row) - 1:
                    if value is not u'' or row[colx - 2] is not u'':
                        bsum.append(value)
                        bid.append(row[colx - 2])
                    else:
                        continue
                else:
                    sheet1.write(rowx, colx, value, data_xfs[colx])

        rowx += 3
        sheet1.write(rowx, 0, 'Bug ID', easyxf(title_format))
        sheet1.write(rowx, 1, 'Bug Summary', easyxf(title_format))

        for c, v in enumerate(bsum):
            rowx += 1
            sheet1.write(rowx, 0, bid[c], easyxf(content_format))
            sheet1.write(rowx, 1, v, easyxf(content_format))

        # write test result and definition
        col_A = ['Test Result', 'P', 'F', 'W', 'Ref', 'N/A', 'N/T', 'Level', '1', '2', '3', '4', '5', ]
        col_B = ['Definition', u'Pass. 待测设备符合相关测试项的要求', u'Fail. 待测设备不符合相关测试项的要求，或同经验值有质的差距。',
                 u'Warn. 告警，待测设备测试结果同经验值仅有“量”的差距，严重性较轻，此项无绝对判断标准。', u'Reference. 此项测试数据仅供参考，或测试结果同经验值相当，但需记录相关结果。',
                 u'Not Applicable. 待测设备不支持此项测试所要求的功能项。', u'Not Tesed. 不对待测设备应用此类测试。但需对不测试的原因进行解释。', 'Definition',
                 u'Blocker. 阻塞。可以中止测试。', u'Critical. 致命。极大地影响了DUT的功能或性能，甚至导致功能不可用或无性能',
                 u'Major. 严重。严重影响了DUT的功能或性能，影响DUT的使用。', u'Normal. 一般。一般性的功能或性能缺陷，不会对DUT的基本使用造成太大影响',
                 u'Enhancement. 建议。对DUT的功能或性能提出建设性的建议。', ]
        for row_num in xrange(len(col_A)):
            if 'Definition' == col_B[row_num]:
                sheet1.write(rowx + 3 + row_num, 0, col_A[row_num], easyxf(title_format))
                sheet1.write(rowx + 3 + row_num, 1, col_B[row_num], easyxf(title_format))
                continue
            sheet1.write(rowx + 3 + row_num, 0, col_A[row_num], easyxf(content_format_1))
            sheet1.write(rowx + 3 + row_num, 1, col_B[row_num], easyxf(content_format))

        # save excel
        book.save(file_name)

    @classmethod
    def write_excel(cls, record=None, data=None):
        """
        Interface for writing excel.
        :param record: DB instance got from admin used for searchig.
        :param data: Test result details
        :return: None
        """
        hdngs = ['No.', 'Test Case', 'Test Result', 'Level', 'Bug ID', 'Remark']
        kinds = 'int      text_1          text          text    text         text'.split()

        # set heading format
        heading_xf = easyxf('font: bold on; \
                           align: wrap on, vert centre, horiz center; \
                           pattern: pattern solid, fore-color grey25;\
                           borders: left 0x01, right 0x01, top 0x01, bottom 0x01')

        # set data format
        kind_to_xf_map = {
            'int': easyxf('align: horiz center;\
                                        pattern: pattern solid, fore-color grey25;\
                                        borders: left 0x01,right 0x01, top 0x01,bottom 0x01'),
            'text': easyxf('align: wrap on,horiz center;\
                                        font: italic on; \
                                        borders: left 0x01,right 0x01, top 0x01,bottom 0x01 '),
            'text_1': easyxf('font: italic on; \
                                        borders: left 0x01,right 0x01, top 0x01,bottom 0x01 ')
        }
        data_xfs = [kind_to_xf_map[k] for k in kinds]
        cls._write_xls_oper('pwrcyl_test_record' + str(time.time()) + '.xls', record, hdngs, data, heading_xf, data_xfs)


excel_helper = ExcelHelper()

if __name__ == '__main__':
    my_helper = ExcelHelper()
    # my_helper.get_test_items_list()
    # print my_helper.index_list
    # print my_helper.test_item_list
    # print zip(my_helper.index_list, my_helper.test_item_list)

    print my_helper.get_fieldsets_for_admin()

