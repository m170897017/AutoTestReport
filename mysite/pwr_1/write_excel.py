#!/usr/bin/env python
# -*- coding: UTF-8 -*
from xlwt import *
import time



def write_xls_oper(file_name, rec, headings, data, heading_xf, data_xfs):
    book = Workbook()

    # write test result definition
    title_format = 'font: bold on;\
                  align: wrap on, vert center, horiz center;\
                  pattern: pattern solid, fore-color gray25;\
                  borders: left 0x01, right 0x01, top 0x01, bottom 0x01'
    content_format = 'align: wrap on; borders: left 0x01, right 0x01, top 0x01, bottom 0x01'
    content_format_1 = 'align: horiz center; borders: left 0x01, right 0x01, top 0x01, bottom 0x01'



    ### add sheet Basic Information ###
    sheet0 = book.add_sheet('Basic Information')

    # change cell width   1mm equals 260
    sheet0.col(0).width = int(13 * 260)
    sheet0.col(1).width = int(63 * 260)

    rowx = 0
    sheet0.write_merge(r1=rowx, r2=rowx, c1=0, c2=1, label='Tester Information', style=easyxf(title_format))

    rowx = 1
    sheet0.write(rowx, 0, 'Tester', easyxf(content_format))
    sheet0.write(rowx, 1, rec.tester, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Test Date', easyxf(content_format))
    sheet0.write(rowx, 1, rec.test_date, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Test Summary', easyxf(content_format))
    sheet0.write(rowx, 1, rec.test_summary, easyxf(content_format))
    # beacause of wrap on, code below is no longer needed
    #    fnt = Font()
    #    fnt.height = int(3*260)
    #    style = XFStyle()
    #    style.font = fnt
    #    sheet0.row(rowx).set_style(style)

    rowx += 1
    sheet0.write(rowx, 0, 'Test Duration', easyxf(content_format))
    sheet0.write(rowx, 1, rec.test_duration, easyxf(content_format))

    rowx += 1
    sheet0.write_merge(r1=rowx, r2=rowx, c1=0, c2=1, label='DUT Information', style=easyxf(title_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Model', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_model, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Sample Size', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_sample_size, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Summary', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_summary, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Chipset', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_chipset, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Power', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_power, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Shell', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_shell, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Antenna', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_antenna, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Driver', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_driver, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'HW Version', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_hw_version, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'SW Version', easyxf(content_format))
    sheet0.write(rowx, 1, rec.dut_sw_version, easyxf(content_format))

    rowx += 1
    sheet0.write_merge(r1=rowx, r2=rowx, c1=0, c2=1, label='SUT Information', style=easyxf(title_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Model', easyxf(content_format))
    sheet0.write(rowx, 1, rec.sut_model, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Driver', easyxf(content_format))
    sheet0.write(rowx, 1, rec.sut_driver, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'OS', easyxf(content_format))
    sheet0.write(rowx, 1, rec.sut_os, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'HW Version', easyxf(content_format))
    sheet0.write(rowx, 1, rec.sut_hw_version, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'SW Version', easyxf(content_format))
    sheet0.write(rowx, 1, rec.sut_sw_version, easyxf(content_format))

    rowx += 1
    sheet0.write_merge(r1=rowx, r2=rowx, c1=0, c2=1, label='Testbed Information', style=easyxf(title_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Name', easyxf(content_format))
    sheet0.write(rowx, 1, rec.testbed_name, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Topo', easyxf(content_format))
    sheet0.write(rowx, 1, rec.testbed_topo, easyxf(content_format))

    rowx += 1
    sheet0.write(rowx, 0, 'Remark', easyxf(content_format))
    sheet0.write(rowx, 1, rec.testbed_remark, easyxf(content_format))


    ### add sheet Test Items ###
    sheet = book.add_sheet('Test Items')

    # write sheet and set format
    rowx = 0
    for colx, value in enumerate(headings):
        sheet.write(rowx, colx, value, heading_xf)
    sheet.set_panes_frozen(True)  # frozen headings instead of split panes
    sheet.set_horz_split_pos(rowx + 1)  # in general, freeze after last heading row
    sheet.set_remove_splits(True)  # if user does unfreeze, don't leave a split there

    # change cell width   1mm equals 260
    sheet.col(0).width = int(10.57 * 260)
    sheet.col(1).width = int(93.86 * 260)
    sheet.col(4).width = int(10.15 * 260)
    sheet.col(5).width = int(40 * 260)

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
                sheet.write(rowx, colx, value, data_xfs[colx])

    rowx += 3
    sheet.write(rowx, 0, 'Bug ID', easyxf(title_format))
    sheet.write(rowx, 1, 'Bug Summary', easyxf(title_format))

    for c, v in enumerate(bsum):
        rowx += 1
        sheet.write(rowx, 0, bid[c], easyxf(content_format))
        sheet.write(rowx, 1, v, easyxf(content_format))


    # write test result and definition
    rowx += 3
    sheet.write(rowx, 0, 'Test Result', easyxf(title_format))
    sheet.write(rowx, 1, 'Definition', easyxf(title_format))
    rowx += 1
    sheet.write(rowx, 0, 'P', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Pass. 待测设备符合相关测试项的要求', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'F', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Fail. 待测设备不符合相关测试项的要求，或同经验值有质的差距。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'W', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Warn. 告警，待测设备测试结果同经验值仅有“量”的差距，严重性较轻，此项无绝对判断标准。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'Ref', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Reference. 此项测试数据仅供参考，或测试结果同经验值相当，但需记录相关结果。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'N/A', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Not Applicable. 待测设备不支持此项测试所要求的功能项。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'N/T', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Not Tesed. 不对待测设备应用此类测试。但需对不测试的原因进行解释。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, 'Level', easyxf(title_format))
    sheet.write(rowx, 1, 'Definition', easyxf(title_format))
    rowx += 1
    sheet.write(rowx, 0, '1', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Blocker. 阻塞。可以中止测试。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, '2', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Critical. 致命。极大地影响了DUT的功能或性能，甚至导致功能不可用或无性能', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, '3', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Major. 严重。严重影响了DUT的功能或性能，影响DUT的使用。', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, '4', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Normal. 一般。一般性的功能或性能缺陷，不会对DUT的基本使用造成太大影响', easyxf(content_format))
    rowx += 1
    sheet.write(rowx, 0, '5', easyxf(content_format_1))
    sheet.write(rowx, 1, u'Enhancement. 建议。对DUT的功能或性能提出建设性的建议。', easyxf(content_format))

    # save excel
    book.save(file_name)


def write_excel(record=None, data=None):
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
    write_xls_oper('pwrcyl_test_record'+str(time.time())+'.xls', record, hdngs, data, heading_xf, data_xfs)


if __name__ == '__main__':
    write_excel()    
