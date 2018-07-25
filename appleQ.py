"""
>How large file can be on HDFS distributed file system?
>Given busy slots as a data-set in a person's outlook calendar (eg: {(1000, 1200), (1415, 1530),...}) and the time required for a meeting (eg: 45 mins) write a method to find an open available slot for scheduling a meeting.
"""
from collections import OrderedDict, defaultdict

def split_string(string):
    length = len(string)
    strs = []
    for i in range(length):
        for j in range(i+1, length):
            if string[i] != string[j]:
                print(string[i:j])
                print(i, j)
                strs.append(string[i:j])
                i=j
                if j==length-1:

    print(strs)


print(split_string('xxxyyzx'))
