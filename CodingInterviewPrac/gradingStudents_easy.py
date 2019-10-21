#!/bin/python3

import math
import os
import random
import re
import sys

#Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    listg = []
    for g in grades:
        if g>=38:
            if g%5 !=0:
                if (5*(g//5 + 1) - g) <3:
                    listg.append(5*(g//5 + 1))
                else:
                    listg.append(g)
            else:
                listg.append(g)
        else:
            listg.append(g)
    return listg
#### or return [n if n < 38 or n % 5 < 3 else (n + 5 - (n % 5)) for n in grades]
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
