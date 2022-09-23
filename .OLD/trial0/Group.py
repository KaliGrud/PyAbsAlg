from abc import ABC,abstractmethod

class AbsGroup(ABC):
    @abstractmethod
    def operator(self,a,b): return

    @abstractmethod
    def inverse(self,a,b): return
