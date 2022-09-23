import numpy as np

class AlephNumber(object):
    def __init__(self,alpha):
        self.alpha = alpha

    def __lt__(self,othr):
        try:
            return self.alpha < othr.alpha
        except AttributeError:
            return np.inf < othr

    def __le__(self,othr):
        try:
            return self.alpha <= othr.alpha
        except AttributeError:
            return np.inf < othr

    def __gt__(self,othr):
        try:
            return self.alpha >= othr.alpha
        except AttributeError:
            return np.inf > othr

    def __ge__(self,othr):
        try:
            return self.alpha >= othr.alpha
        except AttributeError:
            return np.inf > othr

Aleph0 = AlephNumber(0)
Aleph1 = AlephNumber(1)
