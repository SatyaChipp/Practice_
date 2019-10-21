##given length and sum
#find length of longest subarr having elements that sum to anumber les than or euql to k


def window_sublists(lists_, w):
    for i in range(len(lists_)-w+1):
        yield lists_[i:i+w]
def get_all_contiguous_sublists(lists_):
    for w in range(1, len(lists_)+1): #so that we get lists of len == len of parent list
        ##start with one above so that we dont get empty sublists
        yield from window_sublists(lists_, w)
# for item in get_all_contiguous_sublists([1, 2, 4, 5, 6, 7, 7]):
#     print(item)

##one liner for this
L = [1, 2, 3]
def subs(L):
    return [L[i:i+j] for i in range(0, len(L)) for j in range(1, len(L)-i+1)]
print(subs(L))
lengths_  = []
def sums_leng(item, max_):
    if sum(item) <= max_:
        lengths_.append((sum(item), len(item)))

ds = list(map(lambda x: sums_leng(x, 3), subs(L)))
print(lengths_)
from operator import itemgetter
print(max(lengths_, key=itemgetter(1))[0])#voilaa!!!

def subarr_more_than_k(a, k):
    head, tail = 0, 0
    current_sum = 0
    while(tail<len(a)):
        if current_sum + a[tail]<=k:
            current_sum += a[tail]
            tail += 1
            yield tail - head
        else:
            current_sum -= a[head]
            head += 1

def maxLength(a, k):
    return max(subarr_more_than_k(a, k))

#############################################################
"""
Students and departments
 
SELECT
    d.DEPT_NAME,
    COUNT(s.STUDENT_ID)
FROM
    Departments d 
    LEFT JOIN Students s ON d.DEPT_ID = s.DEPT_ID
GROUP by
    d.DEPT_ID
ORDER by
    COUNT(s.STUDENT_ID) DESC, 
    d.DEPT_NAME ASC
"""
#################################################################
##below buying show tickets

def waitingTime(tickets, p):
    total_ = tickets[p]
    first_half = tickets[:p]
    second_half = tickets[p+1:]

    for num in first_half:
        if num < tickets[p]:
            total_ += num
        else:
            total_ += tickets[p]

    for num in second_half:
        if num < tickets[p]:
            total_ += num
        else:
            total_ += tickets[p] - 1

    return total_
