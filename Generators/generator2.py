#1. Fibonacci series using Generators
def generateFibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a+b)

f = generateFibonacci()
counter = 0
for x in f:
    print(x, " ")
    counter +=1
    if(counter > 10):
        break


#2. Another implementation
def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
list(islice(fib(),10))