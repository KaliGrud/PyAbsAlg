from Base       import  Elem_t,Pars_t,Set_t,Alg_t,Magma_t
from itertools  import  product as cart_prodcuter
from abc        import  ABC,abstractmethod
from typing     import  TypeVar,NewType,\
                        Union,\
                        Sequence,Generator,Tuple,\
                        Callable,Any

# Abstract Magma Alegebra Classes

class AbsMagmaAlgebra(ABC):
    @abstractmethod
    def __operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...

    def __call__(self,a:Elem_t,b:Elem_t) -> Elem_t:
        return self.__operator__(a,b)

    def generate_from(self,*el:Elem_t) -> Tuple[Elem_t]:
        magma = list(el)
        tests = magma.copy()
        while len(tests) > 0:
            new_elements = []
            for a,b in cart_product(magma,tests):
                if (m:=self(a,b)) not in magma:
                    magma.append(m)
                    new_elements.append(m)
            tests = new_elements.copy()
        return tuple(magma)
                       
    def is_a_idempotent(self,a:Elem_t) -> bool:
        return a == self(a,a)

    def is_ab_left_absorbing(self,a:Elem_t,b:Elem_t) -> bool:
        return a == self(a,b)

    def is_ab_right_absorbing(self,a:Elem_t,b:Elem_t) -> bool:
        return b == self(a,b)

    def is_ab_communative(self,a:Elem_t,b:Elem_t) -> bool:
        return self(a,b) == self(b,a)

    def is_abc_associative(self,a:Elem_t,b:Elem_t,c:Elem_t) -> bool:
        return self(a,self(b,c)) == self(self(a,b),c)

# Example of a _strict_ magma algebra

class CrossProductAlgebra(AbsMagmaAlgebra):
    def __operator__(self,a:Elem_t,b:Elem_t) -> Elem_t:
        ai,aj,ak = a
        bi,bj,bk = b
        i = aj*bk - ak*bj
        j = ak*bi - ai*bk
        k = ai*bj - aj*bi
        return i,j,k

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __identity__(self) -> Callable[Pars_t,Elem_t]: ...

class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __leftdiv__(self,a:Elem_t,b:Elem_t) -> Elem_t: ... 

    @abstractmethod
    def __rightdiv__(self,a:Elem_t,b:Elem_t): ...

class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @abstractmethod
    def __leftinv__(self,a:Elem_t) -> Elem_t: ...

    @abstractmethod
    def __rightinv__(self,a:Elem_t) -> Elem_t: ...

# Abstract Magma Classes

class AbsMagma(ABC):
    @property
    @abstractmethod
    def alg(self) -> Alg_t: ...

    @property
    @abstractmethod
    def elements(self) -> Iterator: ...
