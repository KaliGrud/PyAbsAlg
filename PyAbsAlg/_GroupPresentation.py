class GroupPresentation:
    def __init__(self,expr:str,**pars):
        """
        e.g. Dicyclic group of order n
        >>> expr = "<a,x|a**(2*{n}),x**2=a**{n},x'*a*x=a'>"
        """
        self.expr = expr
        self.pars = pars

    def get_generators(self,**kwargs):
        pars = kwargs.copy()
        pars.update(pars)
        fexp = expr.format(**pars)
        self.parse_presentation_expr(fexp)
        self.parse_for_parameters(fexp)
        self.parse_for_exp(fexp)
        self.parse_for_mul(fexp)

    def parse_presentation_expr(self,expr) -> Tuple[str]:
        S,R = expr.format(**self.pars).strip()[1:-1].split("|")
        Sm  = S.split(",")
        Rn  = [r.strip().split("=") if "=" in r else [r,"e"] for r in R.split(",")]
        return Sm,Rn

    def parse_for_parenthesis(self,expr) -> Iterable:
        for pars in expr.split("(")[1:]:
            for par in pars.split(")")[:-1]:
                yield par

    def parse_for_exp(self,expr) -> Iterable:
        for side in expr.split("**",1):
            yield side

    def parse_for_mul(self,expr) -> Iterable:
        for side in expr.split("*",1):
            yield side
