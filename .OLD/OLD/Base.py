from typing import  TypeVar,NewType,Union,\
                    Iterable,Iterator,Generator,Tuple,List,Dict,\
                    Callable,Any

# TypeVars defined for clarity of use and purpose
Pars_t  = TypeVar("Pars_t") # Unpacked *tuple elements
Elem_t  = TypeVar("Elem_t") # Element of an algebraic set
Set_t   = TypeVar("Set_t",bound=Iterator) # Algebraic set
Alg_t   = TypeVar("Alg_t",bound=Callable) # An algebra
Magma_t = TypeVar("Magma_t",bound=Iterator) # A 
Group_t = TypeVar("Group_t",bound=Magma_t) # A 
