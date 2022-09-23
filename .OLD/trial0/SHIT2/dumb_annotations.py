def f(x:int,y:float,z:str="666")->str:
    return str(y)*x

print(type(f.__annotations__))
print(f.__annotations__)
print(f(3,6.66))
