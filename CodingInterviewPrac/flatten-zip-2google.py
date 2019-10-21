##flatten arbitrary dict of dicts
import collections
import itertools

def flatten(d, parent_key='', sep='_'):
    items=[]
    for k,v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
print(flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}))

##flatten dict using pandas
import pandas
##dont need to normlize if there are no nested dicts
df = pandas.io.json.json_normalize({'a': 1,
                                    'c': {'a': 2,
                                          'b': {'x': 5,
                                                'y' : 10}},
                                    'd': [1, 2, 3]})
print(df.to_dict(orient='records')[0]) ##records means list like format
#can do
dic = dict(zip(('a', 'b', 'c'), (1,2 ,3)))
for item in zip((1, 2, 3), ('a', 'b', 'c'), (23, 45, 67)):
    print(item)
zipped  = zip((1, 2, 3), ('a', 'b', 'c'), (23, 45, 67))
unzipped = zip(*zipped)
##zip produces a iterable
for item in unzipped:
    print(item)

###sort dict by key

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sortedx = sorted(x.items(), key=operator.itemgetter(1), reverse=True)

print(sortedx)
doc = dict()
for item in sortedx:
    doc[item[0]] = item[1]
print(doc)
##operations on list
import functools
lis = [ 1 , 3, 5, 6, 2, ]
print(functools.reduce(operator.add,lis)) #sumof list
print(functools.reduce(operator.mul, lis))
list23 = ['str', 'dffdg', 'abcedd']
print(functools.reduce(operator.add, list23))

