#!/usr/bin/env python

import gc
import sys
import time


def main():
    size_kb = sys.argv[1]

    mylist = []
    for x in xrange(100):
        mystr = ' ' * int(size_kb) * 1024
        mylist.append(mystr)

    del mylist

    gc.collect()

    mylist = []
    for x in xrange(100):
        mystr = ' ' * int(size_kb) * 1024
        mylist.append(mystr)

    del mylist

    gc.collect()

    time.sleep(3600)


if __name__ == '__main__':
    main()
