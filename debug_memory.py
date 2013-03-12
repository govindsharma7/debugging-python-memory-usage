#!/usr/bin/env python

import sys
import time


def myfunc(size_kb):
    mylist = [
        {'mykey': ' ' * int(size_kb) * 1024}
        for x in xrange(100)
    ]
    len(mylist)
    return []


def main():
    size_kb = sys.argv[1]
    myfunc(size_kb)
    time.sleep(3600)


if __name__ == '__main__':
    main()
