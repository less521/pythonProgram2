#! /usr/bin/env python
#coding = utf-8

import json

def jsonHandle():
    f = open("version.json", "r")
    if f is not None:
        lst = json.load(f)
        totalUV = 0
        totalCrash = 0
        for dic in lst:
            version=  dic["app_version"]
            uv = float(dic["uv"])
            crash = float(dic["crashTimes"])
            #print(version,uv,crash)
            totalUV += uv
            totalCrash += crash
            if uv is not 0:
                crashRate = crash / uv
                print("the crash rate of %s is %.4f") % (version, crashRate)
            else:
                print("the uv is 0")
            if totalUV is not 0:
                totalCrashRate = totalCrash / totalUV;
                print ("total crash rate is %.4f")%totalCrashRate


def main():
    jsonHandle()

if __name__ == "__main__":
    main()