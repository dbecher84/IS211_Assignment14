#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""recusrion homework week 14"""


from __future__ import division

def fib(num):
    """calc the fibonacci sequnce a specified length"""
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)


def gcd_func(x, y):
    """Euclids greatest common denominator"""
    if x < y:
        print "x must be greater that y"
    elif y == 0:
        return x
    elif x % y == 0:
        return y
    else:
        return gcd_func(y, x % y)


def compare_to(s1, s2):
    """Compares two strings"""
    if s1 == '' and s2 == '':
        return 0
    if s1 == '' and s2 != '':
        return -1
    if s1 != '' and s2 == '':
        return -1
    if s1 != '' and s2 != '':
        if ord(s1[0]) == ord(s2[0]):
            return compare_to(s1[1:], s2[1:])
        if ord(s1[0]) != ord(s2[0]):
            return -1


if __name__ == "__main__":
    NUM = int(raw_input("Enter terms in the fib sequence: "))

    print "Fibonacci sequence to the {} number is:".format(NUM)
    for item in range(NUM):
        print fib(item)

    X_NUM = int(raw_input("Enter value x for gcd: "))
    Y_NUM = int(raw_input("Enter value y for gcd: "))

    print "The GCD for the numbers entered is:"
    print gcd_func(X_NUM, Y_NUM)

    STR1 = raw_input("Enter string 1 for comparison: ")
    STR2 = raw_input("Enter string 2 for comparison: ")
    print compare_to(STR1, STR2)
