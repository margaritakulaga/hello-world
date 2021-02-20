#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Это стартовая программа, поэтому тут не учитан стучай,
# когда день больше 31, а месяц больше 12. Если что, могу исправить.

y = int(input('Enter year: '))
m = int(input('Enter month: '))
d = int(input('Enter day: '))

b = bool(y%4==0 and (y%400==0 or y%100!=0))

if ((not b) and (m == 2) and (d >= 29)):
    print('There are 28 days in February in ' + str(y))
else:
    y1 = y - (14 - m) // 12
    x = y1 + y1 // 4 - y1 // 100 + y1 // 400
    m1 = m + 12 * ((14 - m) // 12) - 2
    d1 = (d + x + 31 * m1 // 12) % 7

    print('\nSun' + '\t' + str(bool(d1==0)))
    print('Mon' + '\t' + str(bool(d1==1)))
    print('Tue' + '\t' + str(bool(d1==2)))
    print('Wed' + '\t' + str(bool(d1==3)))
    print('Thu' + '\t' + str(bool(d1==4)))
    print('Fri' + '\t' + str(bool(d1==5)))
    print('Sat' + '\t' + str(bool(d1==6)))