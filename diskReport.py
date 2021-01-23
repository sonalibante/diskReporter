#!/usr/bin/python3
import sys
import os
import pandas as pd


def getSize(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += getSize(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        
        except Exception as e:
                print ("Exception: ", e)
                total += 0
        
    return total        

if __name__ == '__main___':
    path = '/home/'
    
print("Totle arguments passed: ", len(sys.argv))
path='/home/'
directory = sys.argv[1] if len(sys.argv) >= 2 else path

usage = []
paths = []

for entry in os.scandir(directory):
    print(entry.path)
    if (entry.is_dir(follow_symlinks=False)):
        # print(entry.path + " is a diredtory")
        # print(getSize(entry.path))

        total = getSize(entry.path)
        print (total)

        paths.append(entry.path)
        usage.append(total)

    usageDict = {"directory" : paths, "usage": usage}
    df = pd.DataFrame(usageDict)

    print(df)
    df.to_csv("disk_report.csv")