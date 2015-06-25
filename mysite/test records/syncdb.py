#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'eccglln'

from django.conf import settings
from pwr_1.models import test_item

settings.configure()
t = test_item(test_case_id='1.1.1', test_case_description='tc1')
t.save()