x = (i for i in range(10))

def f(x):
    print(x)
    return x

y = next(f(a) for i,a in enumerate(x) if i==0)
print(y)
