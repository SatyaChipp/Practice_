#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def rotateList(n, d, a):
    de = deque(a) #use deque lib
    de.rotate(d*-1)##for right rotate use positive numbers
    return [str(i) for i in list(de)]

def rotateList2(n, d, a):
    ##slicing technique
    listleftRotate = a[d:] + a[:d] #left rotate 
    rotateRight = a[-d:] + a[:-d]
    return rotateRight


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    print(' '.join(rotateList(n, d, a)))
    print(' '.join(map(str, rotateList2(n, d, a))))
