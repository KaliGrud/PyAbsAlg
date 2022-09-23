class Group(object):
    

    def __call__(self,*args):
        return self._func(*args)
