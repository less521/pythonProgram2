#! /usr/bin/env python
#coding=utf-8

import sys
import os

def fileCounter(path):
    if path is not None:
        lst = os.listdir(path)
        print lst
def main(path):
    fileCounter(path)

if __name__ == "__main__":
    path=  os.getcwd()
    print len(sys.argv)
    if (len(sys.argv) > 1):
        main(sys.argv[1])
    main(path)
