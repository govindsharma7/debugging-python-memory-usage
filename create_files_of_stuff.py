#!/usr/bin/env python
import os.path


BYTES_PER_CHAR = 1.0


def main():
    for size_kb in range(1, 201):

        size_bytes = float(size_kb) * 1024.0
        obj_that_eats_the_memory = ' ' * int(size_bytes / BYTES_PER_CHAR)

        filepath = os.path.join('data', 'stuff_%dK.txt' % size_kb)
        with open(filepath, 'w') as f:
            f.write(obj_that_eats_the_memory)


if __name__ == '__main__':
    main()
