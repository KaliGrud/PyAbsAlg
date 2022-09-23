from abc import ABC

class AbsMagma(ABC):
    @staticmethod
    @abstractmethod
    def __op__(lhs,rhs): return None

    @classmethod
    def commutator(cls,lhs,rh): return cls.__op__(lhs,rhs) - cls.__op__(rhs,lhs)

    @abstractmethod
    def __call__(self,*args): return None

    
