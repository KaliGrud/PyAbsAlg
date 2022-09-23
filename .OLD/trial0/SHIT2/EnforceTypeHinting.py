def CastTypeHinting(func):
    def _f(*args,**kwargs):
        rtype = func.__annotations__.pop("return",None)
        fargs = {t(locals()[x]) for x,t in func.__annotations__.items()}
        return rtype(func(**fargs)) if rtype is not None else func(**fargs)
    return _f

@CastTypeHinting
def one(x:int,y:int):
    return x*y

print(one(1.2,2.4))
