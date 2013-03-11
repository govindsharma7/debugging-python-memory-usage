#!/usr/bin/env python

import sys
import time


class MyObj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.att = f.read()


def myfunc(filename):
    mylist = [MyObj(filename) for x in xrange(100)]
    len(mylist)
    return []


def main():
    filename = sys.argv[1]
    myfunc(filename)
    time.sleep(3600)


if __name__ == '__main__':
    main()
