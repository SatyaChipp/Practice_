"""
print positive integer solutions for a3 +b3 = c3 +d3
a,b,c,d between 1to1000
"""

import math
import logging
import timeit
import sys


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger.setLevel(logging.INFO)

class EvaluateExpression(object):
    def __init__(self, results=[]):
        self.results = results
        self.start = 1
        self.end = 100
        self.hashTable = {}
        self.ListValues = []

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

    def method2(self):
        try:
            ##remove duplicated work from method1 and further optimize
            for a in range(self.start,self.end):
                for b in range(self.start,self.end):
                    result = a**3 + b**3
                    self.hashTable[result] = []
                    self.hashTable[result].append((a,b))
                    # print(self.hashTable)
            for c in range(self.start,self.end):
                for d in range(self.start,self.end):
                    result = c**3 + d**3
                    self.ListValues.append(self.hashTable.get(result))
                    # print(self.hashTable.get(result))
                    # for pair in self.ListValues:
                    #     print(c,d, pair[0])

        except Exception as er:
            logger.error("Exception occurred: {}".format(er))
            raise er

    def cal_bigOtimes(self):
        from code_imports_timeit import imports1, code1, imports2, code2
        print ("Time: %s"%timeit.timeit(setup=imports1, stmt=code1, number=10000))
        ##runtime for method1 is O(N3)
        print ("Time: %s"%timeit.timeit(setup=imports2, stmt=code2, number=10000))


if __name__ == '__main__':
    evalExp = EvaluateExpression()
    evalExp.method1()
    # for item in evalExp.results:
    #     print(item)
    logger.info("Number of positive integer solutions : {}".format(len(evalExp.results)))
    logger.info(evalExp.cal_bigOtimes())
    logger.info("Implementing hash table to lookup (a,b) tuple cubes")
    logger.info(evalExp.method2())
