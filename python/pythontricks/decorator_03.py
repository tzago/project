#!/usr/bin/env python
# coding=utf-8
def null_decorator(func):
    return func



def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

#@null_decorator
@uppercase
def greet():
    return 'Hello'


if __name__ == '__main__':

   print greet()
