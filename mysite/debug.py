from functools import wraps
def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        print 'cache is', cache
        print 'args is', args

        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

@memo
def fib(n):
    if n < 2:
        print 'befor less 2 return'
        return n
    print 'befor return!!'
    return fib(n - 1) + fib(n - 2)

print 'fib is', fib(5)