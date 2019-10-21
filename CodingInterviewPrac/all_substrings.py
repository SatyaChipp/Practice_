###generate all substrings for a given string

def get_all_substrings_continuous(string):
    ##write a generator instead to save memory
    #use yelid instead instead of saving all of them in memory
    length=len(string)
    for i in range(length):
        for j in range(i+1, length+1):
            yield (string[i:j])
# for item in get_all_substrings_continuous("abcdefgghija"):
#     print(item)


from collections import Counter, OrderedDict
def get_counts_strings(string):
    length = len(string)
    c = Counter(string)
    print(c)

class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return '%s(%r)'%(self.__class__.__name__, OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
# print(OrderedCounter("aabccdeddfeaa"))
#OrderedCounter(OrderedDict([('a', 4), ('b', 1), ('c', 2), ('d', 3), ('e', 2), ('f', 1)]))

def string_count_maintain_order(string):
    length = len(string)
    lis = []
    for i in range(length):
        for j in range(i+1, length+1):
            print(i, j)
            if string[i] != string[j]:
                yield string[i:j]

for item in string_count_maintain_order('zzyyyyxx'):
    print(item)




# ##print all possible rearrangements of a string --stanford
# ##using backtracking: choose a char, explore, then unchoose char
# ## how do we keep track of the choices? - use an auxilary string
# def permute_helper(string,  chosen): # c is whats chosen so far
#     ##using recurse --be more lazy:
#     ##basic recurse - base condition : least amount of work to compute ""
#     #empty string
#     print("permute_helper( {} , {} )".format( string, chosen))
#     if string == "": #empty string
#         print(chosen)
#     else:
#         #choose/explore/unchoose
#         for i in range(len(string)):
#             #choose
#             c = string[i]
#             chosen+=c
#             string.replace(c,'',1)
#             ##explore
#             permute_helper(string, chosen )##pass diff state to the nextcall
#             ##unchoose
#             string = string[:i] + c + string[i:]
#             ch = list(chosen).pop(i)
#             chosen = "".join(ch)
#
#
# def permute(string):
#     ##choose c to  be first/permute/then unchoose c
#     permute_helper(string, "")
#
#
# permute("abcdefgh")
