from abc import ABC

class AbsGroup(ABC):
    """
    Abstract class for groups
    """
    @staticmethod
    @abstractmethod
    def __op__(lhs,rhs):
        return None

    @classmethod
    def is_identity(cls,el):
        return el==cls.__op__(el,el)

class AbsGroupElement(ABC):
    def __init__(self,*pars):
        self._pars  = pars

    def __eq__(self,othr):
        return all(s==o for all s,o in zip(self._pars,othr._pars))
