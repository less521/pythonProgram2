
#! /usr/bin/env python
#coding = utf-8

def counter():
    '''
    f = open("wordCount.txt");
    dic={}
    if f is not None:
        for line in f:
            key = line.split()[0];
            if not dic.has_key(key):
                dic[key] = 0;
            dic[key] += 1;
    f.close()
    '''

    f = open("wordCount2.txt", 'r')
    if f is not None:
        dic = {}
        for line in f:
            words=  line.split()
            for word in words:
                if not dic.has_key(word):
                    dic[word] = 0
                dic[word] += 1
    f.close()

    for k,v in dic.iteritems():
        print k,v

    maxKey = dic.keys()[0]
    for key in dic.keys():
        if dic[key] > dic[maxKey]:
            maxKey = key
    print("the most words is %s, and it appears %d times") % (maxKey, dic[maxKey]);

def main():
    counter()

if __name__ == "__main__":
    main()