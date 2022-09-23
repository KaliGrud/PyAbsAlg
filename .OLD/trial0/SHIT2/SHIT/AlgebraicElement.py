from abc import ABC,abstractmethod

class ParametericObject(object):
    def __init__(self,*pars):
        self._pars = pars

    def __getitem__(self,key):
        return self._pars[key]

class AbsAlgebraicElement(ParametericObject):
    def __init__(self,*pars):
        super(AbsAlgebraicElement,self).__init__(*pars)

    @abstractmethod
    def __flattened_pars__(self): return

    def flattened(self):
        return self.__flattened_pars__()

    def __eq__(self,othr):
        return all(self.flatten(a)==self.flattened(b) for a,b in zip(self._pars,othr._pars))
