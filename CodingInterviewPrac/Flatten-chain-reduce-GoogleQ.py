from collections import OrderedDict, Counter

##chain to flatten list
import itertools
list1 = [[1, 3], [[5, 6, 7], [3, 45]] ]
list2 = [[1, 3], [[5, 6, 7], [3, 45]], (2, (3, 4)) ]
list3 = [[1, 3], [[5, 6, 7], [3, 45]], (2, (3, 4)), 'er', 8, 9 ]

print(list(itertools.chain(*list1))) #only one lvel flattening
# print(list(itertools.chain(*[1, 2, 3, [4, 5, 6]])))
list_of_lists = [[range(4), range(7)]]

#flatten the lists
flattened_list = [y for x in list2 for y in x] #one level unnesting only
print(flattened_list)

import operator
from functools import reduce
print(reduce(operator.concat, list1))
##or
print(reduce(lambda x, y:x+y, list1))
import numpy
print(list(numpy.concatenate(list1)))


##prog to flatten arbitary structs in lists-- nested lists
from collections import Iterable
def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
print(list(flatten(list3)))

string = 'xxyyyzzx'
