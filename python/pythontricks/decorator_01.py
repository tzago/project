#!/usr/bin/env python
# coding=utf-8
def null_decorator(func):
    return func

def greet():
    return 'Hello'

if __name__ == '__main__':
   greet = null_decorator(greet)

   print greet()
