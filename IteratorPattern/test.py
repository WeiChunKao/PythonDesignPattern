# use () to define generator
gen = (x * x for x in range(10))

# use yield to define generator function
def fibonacci(maxNum):
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print("use () to define generator")
    for e in gen:
        print(e, end='\t')
    print()
    print("use yield to define generator function")
    fib = fibonacci(10)
    for n in fib:
        print(n, end='\t')
    print()
