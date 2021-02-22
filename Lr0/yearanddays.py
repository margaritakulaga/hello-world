#!/usr/bin/env python3
# -*- coding: utf-8 -*-

y = int(input('Enter year: '))
m = int(input('Enter month: '))
d = int(input('Enter day: '))

b = bool(y%4==0 and (y%400==0 or y%100!=0))

if ((not b) and (m == 2) and (d >= 29)):
    print('\nThere are 28 days in February in ' + str(y))
else:
    if (((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)
        and (d > 0 and d <= 31)) or ((m == 4 or m == 6 or m == 9 or m == 11)
            and (d > 0 and d <= 30)) or (m == 2 and d <= 29) and (y >= 0)):

        y1 = y - (14 - m) // 12
        x = y1 + y1 // 4 - y1 // 100 + y1 // 400
        m1 = m + 12 * ((14 - m) // 12) - 2
        d1 = (d + x + 31 * m1 // 12) % 7

        if (d1 == 0):
            print('\nSunday')
        elif (d1 == 1):
            print('\nMonday')
        elif (d1 == 2):
            print('\nThuesday')
        elif (d1 == 3):
            print('\nWednesday')
        elif (d1 == 4):
            print('\nThursday')
        elif (d1 == 5):
            print('\nFriday')
        elif (d1 == 6):
            print('\nSaturday')
    else:
        print('\nError')
