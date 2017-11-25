#!/usr/bin/env python
# -*- coding: utf-8 -*-

def high_and_low(numbers):
	'''
	на входе строка ['3','4','0','100']
	на выходе строка вида '100 0' - максимальное и минимальное число
	'''
    str_n = numbers.split(" ")
    n = list(map(int, str_n))
    return "%s %s" % (max(n), min(n))