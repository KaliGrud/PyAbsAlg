from abc import ABC,abstractmethod

class AbsAlgebra(ABC):
    def __init__(self,*args,**pars) -> None:
        self._args = args
        self._pars = pars

    @abstractmethod
    def __operator__(self,*args,**pars): ...

    @property
    def pars(self):
        return self._pars.copy()

    @property
    @abstractmethod
    def nargs(self): ...

    def __call__(self,*args,**pars):
        _pars = self.pars
        _pars.update(pars)
        return self.__operator__(*args,**_pars)

    def generate_from_elements(self,*elems,**pars):
        out = tuple()
        new = (*elems,)
        while len(new) > 0:
            out = (*out,*new)
            perms = itertools.permutations((*[out]*(self.nargs-1),
                                            *[new]*self.nargs),self.nargs)
            prods = sum(list(itertools.product(*perm)) for perm in perms)
            new = {c for args in prods if (c:=self(*args,**pars)) not in out}
        return out


class AbsBinaryAlgebra(AbsAlgebra):
    @abstractmethod
    def __operator__(self,a,b,**pars): ...

    @property
    def nargs(self) -> int: return 2

class AbsAlgebraicElement(ABC):
    @property
    @abstractmethod
    def __algebra__(self): ...
    
    @abstractmethod
    def __add__(self,othr): ...

    @abstractmethod
    def __mul__(self,othr): ...

    @abstractmethod
    def __matmul__(self,othr): ...

    @abstractmethod
    def __sub__(self,othr): ...

    @abstractmethod
    def __truediv__(self,othr): ...

    @abstractmethod
    def __floordiv__(self,othr): ...

    @abstractmethod
    def __pow__(self,n): ...


class AbsAlgebraicStructure(ABC):
    @abstractmethod
    def __algebra__(self): ...

    @property
    def algebra(self):
        return self.__algebra__
