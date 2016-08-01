#! /usr/bin/env python
# coding=utf-8

import sys
import os


def fileCounter(path):
    if path is not None:
        lst = os.listdir(path)
        print lst
        for item in lst:
            fullpath = os.path.join(path, item)
            print fullpath
            if os.path.isdir(fullpath):
                print "%s is a dir" % item
            elif os.path.isfile(fullpath):
                print "%s is a file" % item


def main( path):
    fileCounter(path)


if __name__ == "__main__":
    path = os.getcwd()
    if len(sys.argv) > 1:
        path = sys.argv[1]
    main(path)
