# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import re
r= requests.get('https://www.tianqi.com/baoding')
result=re.search('<p class="now"><b>(\d*.\d)</b>',r.text)
c=eval(result.group(1))
f=32+1.8*c
print ('保定当前温度为：{}℃,转化为华氏度为:{:.1f}华氏度。'.format(c,f))
