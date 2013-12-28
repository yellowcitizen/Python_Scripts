#! /usr/bin/env python3.3
# -*- coding: utf-8 -*-

#fibonacci series

def fibonacci(x):
    a, b = 0, 1
    print('the fibonacci sequence is: '),
    while b < x:
        print(b),
        a, b = b, a + b

x = input('type a number great than 0 and 1\n')
print(fibonacci(x))
