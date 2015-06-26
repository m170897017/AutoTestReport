# /usr/bin/env python
# coding:utf-8

from django.contrib import admin
from django.core.mail.message import EmailMessage

from pwr_1.models import pwr, pwr_test_item
from excel_helper import excel_helper
from exception_handler import logger, exception_handler


# from django.core.mail import send_mail


@admin.register(pwr)
class pwr_admin(admin.ModelAdmin):
    """
    This class is used for admin page of website
    """



    fieldsets = excel_helper.get_fieldsets_for_admin(pwr_test_item)

    list_display = ('get_tester', 'get_test_date', 'get_test_summary')
    search_fields = ['get_tester']
    list_filter = ['test_date']

    

    def get_tester(self):
        return self.tester
    def get_test_date(self):
        return self.test_date
    def get_test_summary(self):
        return self.test_summary

    @exception_handler
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
        # for i in xrange(0, pwr_admin.test_record_line_num_for_test):
        for i in xrange(0, 2):
            temp = []
            no = excel_helper.index_list[i]
            case_name = excel_helper.test_item_list[i]
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

        # post-save operation, get entries from databases and write them to excel
        data = self.get_data(obj=obj)
        # per = request.user.user_permissions.select_related()
        # self.email_send(message=per)
        excel_helper.write_excel(record=obj, data=data)




