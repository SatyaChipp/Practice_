def fibonacci(n):
    fn = [0, 1,]
    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])
    return fn
def fibnacci_generator(n):
    a, b =0, 1
    for i in range(n):
        yield a
        a = b
        b = a+b
print(fibonacci(7))
print(list(fibnacci_generator(10)))
##decorators are used for memoizing -- that is caching a slow to compute result of a function


##get nth fibonacci
def memoize(func):
    func.memo = {1:0, 2:1} ##can start from 0 or 1 the fib seq
    return func

@memoize
def fib(n):
    for i in range(3, n+1):
        fib.memo[i] = fib.memo[i-1] + fib.memo[i-2]
    return fib.memo[n]
print(fib(250))
