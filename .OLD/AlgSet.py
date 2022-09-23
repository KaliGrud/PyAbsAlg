from abc import ABC

class AbsAlgSet(ABC):
    @abstractmethod
    def __call__(self,*args): return None

    @abstractmethod
    def __getitem__(self,key): return None

class AlgFiniteSet(AbsAlgSet):
    def __init__(self,func,elements):
        self.func = func
        self.elements = elements

    @property
    def size(self):
        return len(self)

    def __len__(self):
        return len(self.elements)
