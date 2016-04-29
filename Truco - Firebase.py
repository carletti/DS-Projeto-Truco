# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:22:38 2016

@author: dell
"""

import firecall

my_firebase = firecall.Firebase("https://amber-inferno-9126.firebaseio.com/")

data = eval(my_firebase.get_sync(point="/"))

print(data)
print(type(data))