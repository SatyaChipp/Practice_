imports1 = """
import math
import logging
import timeit
import sys
"""

code1 = """
def method1(self):
        try:
            for a in range(self.start,self.end):
                for b in range(self.start,self.end):
                    for c in range(self.start,self.end):
                        d = int((a**3 + b**3 - c**3) ** 1/3)
                        if d in range(self.start,self.end):
                            self.results.append((a, b, c, d))
                            break
        except ValueError as er:
            logger.error("Value error.. recheck expression and limits")
"""

imports2 = """
import math
import logging
import timeit
import sys
"""

code2 = """
def method2(self):
        try:
            ##remove duplicated work from method1 and further optimize
            for a in range(self.start,self.end):
                for b in range(self.start,self.end):
                    result = a**3 + b**3
                    self.hashTable[result] = []
                    self.hashTable[result].append((a,b))
                    print(self.hashTable)
            for c in range(self.start,self.end):
                for d in range(self.start,self.end):
                    result = c**3 + d**3
                    self.ListValues.append(self.hashTable.get(result))
                    print(self.hashTable.get(result))
                    # for pair in self.ListValues:
                    #     print(c,d, pair[0])

        except Exception as er:
            logger.error("Exception occurred: {}".format(er))
            raise er
"""