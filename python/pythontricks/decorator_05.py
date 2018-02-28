#!/usr/bin/env python
# coding=utf-8
import functools

def null_decorator(func):
    return func

def proxy(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

def trace(func):
    def wrapper(*args,**kwargs):
        print('TRACE: calling {func.__name__}() with {args},{kwargs}'.format(func=func,args=args,kwargs=kwargs))
        original_result = func(*args,**kwargs)
        print('TRACE: {func.__name__}() returned {original_result!r}'.format(func=func,original_result=original_result))
        return original_result
    return wrapper


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def strong(func):
    @functools.wraps(func)
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

#run this first with these to decorator commented out and then uncomment them
@strong
@emphasis
def greet():
    " Return a friendly greeting.  "
    return 'Hello'


@trace
def say(name,line):
    return '{name}: {line}'.format(name=name,line=line)

if __name__ == '__main__':

   print greet()
   #decorated_greet=strong(emphasis(greet))
   decorated_greet=uppercase(greet)

   #print decorated_greet()
   print say('Jane', 'Hello, World')
