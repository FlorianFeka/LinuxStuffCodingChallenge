# Implement a job scheduler which takes in a
# function f and an integer n, and calls f after n milliseconds.

import time

def scheduler(func, n, *args):
    milliseconds = n / 1000
    while(True):
        func(*args)
        time.sleep(milliseconds)

def test(t, e):
    print(t)
    print(e)
    print(time.time())

scheduler(test, 500, 'one', 'two')


