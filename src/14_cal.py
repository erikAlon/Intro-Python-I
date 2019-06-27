"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


class ArgumentsError(Exception):
    __module__ = Exception.__module__


c = calendar.Calendar(6)
a = sys.argv
t = datetime.now()
tY = t.year
tM = t.month
arg_length = len(a)

try:
    if arg_length == 1:
        cal = calendar.month(tY, tM)
        print(cal)
    elif arg_length == 2:
        arg1 = int(round(float(a[1])))
        if arg1 >= 1 and arg1 <= 12:
            cal = calendar.month(tY, arg1)
            print(cal)
        else:
            raise ArgumentsError(
                "This program only takes a month between 1 and 12 as first argument")
    elif arg_length == 3:
        arg1 = int(round(float(a[1])))
        arg2 = int(round(float(a[2])))
        if arg1 >= 1 and arg1 <= 12:
            if arg2 >= 1 and arg2 <= tY:
                cal = calendar.month(arg2, arg1)
                print(cal)
            else:
                raise ArgumentsError(
                    "This program only takes a year between 1 and %d as second argument" % tY)
        else:
            raise ArgumentsError(
                "This program only takes a month between 1 and 12 as first argument")
    else:
        raise ArgumentsError("This program only uses less than 3 arguments")
except ArgumentsError:
    raise
except ValueError:
    raise ValueError("This program only uses numbers as arguments")
