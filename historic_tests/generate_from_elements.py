import itertools,functools

def operator(a,b,c):
    return (a*b-c) % 20

def cross_product(u,v):
    ui,uj,uk = u
    vi,vj,vk = v
    i = uj*vk - vj*uk
    j = uk*vi - vk*ui
    k = ui*vj - vi*uj
    return i,j,k

def generate_from_elements(elems,func,n):
    out = tuple()
    new = (*elems,)
    while len(new) > 0:
        out = (*out,*new)
        combinations = itertools.combinations_with_replacement(out,n)
        permutations = map(itertools.permutations,combinations)
        unique_perms = map(list,map(set,permutations))
        perms = functools.reduce(lambda x,y: x+y,unique_perms)
        new = set(c for args in perms\
                if (c:=func(*args)) not in out)
    return out


elems = [ el for el in generate_from_elements([(1,0,0),(0,1,0)],\
                        cross_product,2) ]
print(elems) 
