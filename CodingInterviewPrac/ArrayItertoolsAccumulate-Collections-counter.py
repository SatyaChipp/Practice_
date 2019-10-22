"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the 
array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
"""
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # zerolist = [0]*n
    # for a, b, c in queries:
    #     for i in range(a-1, b):
    #         zerolist[i]+=c
    # return max(zerolist)
    from itertools import accumulate
    from collections import defaultdict
    ar = defaultdict(int)
    for p, q, k in queries:
        ar[p] += k
        ar[q + 1] -= k
    return(max(accumulate(ar[i] for i in sorted(ar))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    
    fptr.write(str(result) + '\n')

    fptr.close()
 -----------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
import sys
"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it 
occurs in the list of input strings.
For example, given input  and , we find  instances of ',  of '' and  of ''. For each query, we add an element to our return array, .
"""
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    from collections import Counter
    c = Counter(strings)#dict of counts
    return [c[strs] if strs in c else 0 for strs in queries]

   
