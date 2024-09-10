def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fi=fib()
for _ in range(10):
    print(next(fi))