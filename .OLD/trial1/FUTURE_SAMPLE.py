class CyclicGroupAlgebra(AbsGroupAlgebra):
    def __init__(self,ordered_elements):
        self.elements = ordered_elements

    def __operation__(self,a,b):
        return (a+b) % (self.get_n_elements() + 1)

class CyclicGroup(CyclicGroupAlgebra,AbsGroup):
    def __init__(self,elements):
        self.elements = elements
