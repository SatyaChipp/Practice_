import pandas as pd
import numpy as np
from multiprocessing import Pool
import multiprocessing
cores = multiprocessing.cpu_count()
partitions = 5#give a number <=cores

def parallelize(data, dfunc):
    data_split = np.array_split(data, partitions)
    print(data_split)
    pool = Pool(cores)
    data = pd.concat(pool.map(dfunc, data_split))
    pool.close()
    pool.join()
    return data

def square(x):
    return x*x

def func_test(data):
    # print("process owrking on {}".format(data))
    data['square'] = data['col'].apply(square)
    return data
if __name__=='__main__':
    df = pd.DataFrame({'col': [0,1,2,3,4,5,6,7,8,9]})
    data = parallelize(df, func_test)
    print(data)
