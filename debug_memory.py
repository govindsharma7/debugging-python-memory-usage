#!/usr/bin/env python

import sys
import time


class MyObj(object):
    def __init__(self, size_kb):
        self.att = ' ' * int(size_kb) * 1024


def myfunc(size_kb):
    mylist = [MyObj(size_kb) for x in xrange(100)]
    len(mylist)
    return []


def main():
    size_kb = sys.argv[1]
    myfunc(size_kb)
    time.sleep(3600)


if __name__ == '__main__':
    main()
