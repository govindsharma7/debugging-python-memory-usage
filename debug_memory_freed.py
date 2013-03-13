#!/usr/bin/env python

import sys
import time


def main():
    size_kb = sys.argv[1]

    mylist = []
    for x in xrange(100):
        mylist.append(' ' * int(size_kb) * 1024)

    del mylist

    time.sleep(3600)


if __name__ == '__main__':
    main()
