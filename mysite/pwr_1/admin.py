import os

from django.contrib import admin
from django.core.mail.message import EmailMessage

from pwr_1.models import pwr
from read_excel import ReadExcel
import write_excel



# from django.core.mail import send_mail

#class TestItems(admin.TabularInline):
#    model = test_item


class pwr_admin(admin.ModelAdmin):
    """
    This class is used for admin page of website
    """

    test_record_line_num_for_test = 2

    exc = ReadExcel()
    item_list, index_list = exc.get_test_items_list()

    row_number = len(item_list)
    fs = [('Tester Information', {'fields': ('tester', 'test_date', 'test_summary', 'test_duration'),
                                  'classes': ('collapse', 'collapse-closed')}),
          ('DUT Information', {'fields': ('dut_model', 'dut_sample_size', 'dut_summary', 'dut_chipset',
                                          'dut_power', 'dut_shell', 'dut_antenna', 'dut_driver',
                                          'dut_hw_version', 'dut_sw_version'),
                               'classes': ('collapse', 'collapse-closed')}),
          ('SUT Information', {'fields': ('sut_model', 'sut_driver', 'sut_os', 'sut_hw_version', 'sut_sw_version'),
                               'classes': ('collapse', 'collapse-closed')}),
          ('Testbed Information', {'fields': ('testbed_name', 'testbed_topo', 'testbed_remark'),
                                   'classes': ('collapse', 'collapse-closed')})]

    # we have at most 29 lines now. But we use 2 to debug here
    for i in xrange(0, test_record_line_num_for_test):
        number = str(i)
        test_result = 'test_result_' + number
        test_com = 'test_comment_' + number
        bug_level = 'bug_level_' + number
        bug_id = 'bug_id_' + number
        bug_sum = 'bug_summary_' + number

        item_name = index_list[i] + ' ' + item_list[i]
        fs.append((item_name, {'fields': (test_result, bug_level, bug_id, bug_sum, test_com)}))

    fieldsets = tuple(fs)

    list_display = ('tester', 'test_date', 'test_summary')
    search_fields = ['tester']
    list_filter = ['test_date']
    #    fieldsets = (
    #                 ('test line 1',{'fields':('test1','tester')}),
    #                 ('test line 2',{'fields':('test2','test_date')}),
    #                 )
    #


    def email_send(self, message):
        """
        Send specific message to someone.
        :param message: message in string format.
        """
        assert isinstance(message, str), 'message must be string!!'
        mail = EmailMessage(subject='my e-mail',
                            body=message,
                            from_email='linchenhang@tp-link.net',
                            to=['linchenhang@tp-link.net'],
                            cc=['linchenhang@tp-link.net'])
        #        mail.attach_file('pwrcyl_test_record.xls')
        mail.send()
        # send_mail(u'test1',u'test2','linchenhang@tp-link.net',['linchenhang@tp-link.net'],fail_silently=False)


    def get_data(self, obj):
        """
        get data from database
        """
        #        data = [[1,'WPS Button test.............','Pass','N/A',12345,'None','None'],
        #            [2,'Power Button test','Pass','N/A',12345, 'None', 'None'],]

        data = []
        for i in xrange(0, pwr_admin.test_record_line_num_for_test):
            temp = []
            no = self.index_list[i]
            case_name = self.item_list[i]
            result_name = 'test_result_' + str(i)
            exec ("result = obj." + result_name)
            comment_content = 'test_comment_' + str(i)
            exec ("comment = obj." + comment_content)
            bug = 'bug_level_' + str(i)
            exec ("bug_level = obj." + bug)
            bug_id = 'bug_id_' + str(i)
            exec ("bug_id = obj." + bug_id)
            bug_sum = 'bug_summary_' + str(i)
            exec ("bug_summary = obj." + bug_sum)
            temp.append(no)
            temp.append(case_name)
            temp.append(result)
            temp.append(bug_level)
            # bug id should be bug summary position minus 2
            temp.append(bug_id)
            temp.append(comment)
            # bug summary should be the last one to be added because of
            # it's to be the bottom of the sheet
            temp.append(bug_summary)
            data.append(temp)
        return data


    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        super(pwr_admin, self).save_model(request, obj, form, change)

        data = self.get_data(obj=obj)
        per = request.user.user_permissions.select_related()

#        self.email_send(message=per)
        write_excel.write_excel(record=obj, data=data)

admin.site.register(pwr, pwr_admin)


