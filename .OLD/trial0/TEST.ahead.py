# Goals for implementation

class AbsMagma(ABC): pass
class AbsUnitalMagma(AbsMagma): pass
class AbsQuasigroup(AbsMagma): pass
class AbsLoop(AbsUnitalMagma,AbsQuasigroup): pass

class AbsMagmaElement(ABC): pass
#class AbsUnitalMagmaElement(AbsMagmaElement): pass
#class AbsQuasigroupElement(AbsMagmaElement): pass
#class AbsLoopElement(AbsUnitalMagmaElement,AbsQuasigroupElement): pass
