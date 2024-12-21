def caching_fibonacci():
    cache = {}
    def fibonacci(num):
        if num < 2:
            cache[num] = num
        if num in cache:
            return cache[num]
        
        cache[num] = fibonacci(num - 1) + fibonacci(num -2)
        return cache[num]
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))