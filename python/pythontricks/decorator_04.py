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

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

#run this first with these to decorator commented out and then uncomment them
@strong
@emphasis
def greet():
    return 'Hello'


if __name__ == '__main__':

   print greet()

   decorated_greet=strong(emphasis(greet))

   print decorated_greet()
