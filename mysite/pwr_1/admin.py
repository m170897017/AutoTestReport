# /usr/bin/env python
# coding:utf-8

from django.contrib import admin
from django.core.mail.message import EmailMessage

from pwr_1.models import pwr
from excel_helper import excel_helper


# from django.core.mail import send_mail


@admin.register(pwr)
class pwr_admin(admin.ModelAdmin):
    """
    This class is used for admin page of website
    """

    fieldsets = excel_helper.get_fieldsets_for_admin()

    list_display = ('get_tester', 'get_test_date', 'get_test_summary')
    search_fields = ['get_tester']
    list_filter = ['test_date']


    def get_tester(self):
        return self.tester
    def get_test_date(self):
        return self.test_date
    def get_test_summary(self):
        return self.test_summary

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
        :param obj: DB instance.
        """
        #        data = [[1,'WPS Button test.............','Pass','N/A',12345,'None','None'],
        #            [2,'Power Button test','Pass','N/A',12345, 'None', 'None'],]

        data = []
        result = None
        bug_level = None
        comment = None
        bug_id = None
        bug_summary = None
        pwr_test_item_all = excel_helper.get_test_items_list_from_db()
        # pwr_test_item_all will look like: ((1L, '1.1.1', 'C-15551:power_cycle_func_wps_button_long_press'), ...)

        test_items_num = len(pwr_test_item_all)

        # use 2 here for debug only
        # for i in xrange(test_items_num):
        for i in xrange(2):
            no = pwr_test_item_all[i][1]
            case_name = pwr_test_item_all[i][2]
            i = str(i)
            # to dynamically get test item info from database
            commands = [
                ''.join(['result = obj.', 'test_result_', i, ]),
                ''.join(['comment = obj.', 'test_comment_', i, ]),
                ''.join(['bug_level = obj.', 'bug_level_', i, ]),
                ''.join(['bug_id = obj.', 'bug_id_', i, ]),
                ''.join(['bug_summary = obj.', 'bug_summary_', i, ]),

            ]
            for cmd in commands:
                exec cmd
            # this order is strictly required
            # bug id should be bug summary position minus 2
            # bug summary should be the last one to be added because of
            # it's to be the bottom of the sheet
            data.append([no, case_name, result, bug_level, bug_id, comment, bug_summary])
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