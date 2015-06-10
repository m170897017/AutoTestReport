from django.db import models

from read_excel import ReadExcel


class pwr(models.Model):
    exc = ReadExcel()
    item_list, index_list = exc.get_test_items_list()

    # test info
    tester = models.CharField(max_length=10)
    test_date = models.DateField(verbose_name='Test Date')
    test_summary = models.TextField(verbose_name='Test Summary')
    test_duration = models.CharField(max_length=20, verbose_name='Test Duration')
    # DUT info
    dut_model = models.CharField(max_length=20, blank=True, verbose_name='Model')
    dut_sample_size = models.CharField(max_length=2, verbose_name='Sample Size', blank=True)
    dut_summary = models.TextField(blank=True, verbose_name='Summary')
    dut_chipset = models.CharField(max_length=10, blank=True, verbose_name='Chipset')
    dut_power = models.CharField(max_length=10, default='9V/0.6A', blank=True, verbose_name='Power')
    dut_shell = models.CharField(max_length=10, blank=True, verbose_name='Shell')
    dut_antenna = models.CharField(max_length=10, blank=True, verbose_name='Antenna')
    dut_driver = models.CharField(max_length=10, blank=True, verbose_name='Driver')
    dut_hw_version = models.CharField(max_length=10, blank=True, verbose_name='HW Version')
    dut_sw_version = models.CharField(max_length=10, blank=True, verbose_name='SW Version')

    # SUT info
    sut_model = models.CharField(max_length=20, blank=True, verbose_name='Model')
    sut_driver = models.CharField(max_length=10, blank=True, verbose_name='Driver')
    sut_os = models.CharField(max_length=10, blank=True, verbose_name='OS')
    sut_hw_version = models.CharField(max_length=10, blank=True, verbose_name='HW Version')
    sut_sw_version = models.CharField(max_length=10, blank=True, verbose_name='SW Version')

    # Testbed info
    testbed_name = models.CharField(max_length=10, blank=True, verbose_name='Name')
    testbed_topo = models.CharField(max_length=30, blank=True, default='Topo_lan_wan', verbose_name='Topo')
    testbed_remark = models.CharField(max_length=30, blank=True, verbose_name='Remark')

    for i in xrange(0, len(item_list)):
        ii = str(i)
        test_result = 'test_result_' + ii
        test_com = 'test_comment_' + ii
        bug_level = 'bug_level_' + ii
        bug_id = 'bug_id_' + ii
        bug_sum = 'bug_summary_' + ii
        exec (test_result + "= models.CharField(max_length=20, verbose_name='Result', \
        choices=(\
        ('Pass', 'P'), \
        ('Fail', 'F'), \
        ('Not Test', 'N/T'), \
        ('Not Avaliable', 'N/A'), \
        ('Reference', 'Ref'), \
        ('Warn', 'W')\
        ))")
        exec (test_com + "= models.CharField(max_length=100,  verbose_name='Comment',  blank=True)")
        exec (bug_level + "= models.CharField(max_length=100,  verbose_name='Bug Level',  blank=True, \
                            choices=(('1', '1:Blocker'), \
                            ('2', '2:Critical'), \
                            ('3', '3:Major'), \
                            ('4', '4:Normal'), \
                            ('5', '5:Enhancement')))")
        exec (bug_id + "= models.CharField(max_length=10,  verbose_name='Bug ID',  blank=True)")
        exec (bug_sum + "= models.CharField(max_length=100,  verbose_name='Bug Summary',  blank=True)")


    def __unicode__(self):
        return self.test_summary


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    