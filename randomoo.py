
#!/usr/bin/env python
#coding=utf-8
import random

def getRandom(n):
    lst = range(0, n)
    lst2 = random.sample(lst, n)
    print lst2

    lst3 = []
    for i in lst:
        lst3.append(random.uniform(i, i+1))
    print lst3

def main():
    getRandom(10)
if __name__ == '__main__':
    main()