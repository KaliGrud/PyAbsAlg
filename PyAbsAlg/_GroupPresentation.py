from typing import TypeVar,Union,Optional,\
                    Tuple,\
                    Pars__t,Elem__t,Set__t,Oper__t,Alg__t,Struc__t,\
                    Pars__o,Elem__o,Set__o,Oper__o,Alg__o,Struc__o,\
                    Pars__e,Elem__e,Set__e,Oper__e,Alg__e,Struc__e,\
                    Pars__f,Elem__f,Set__f,Oper__f,Alg__f,Struc__f,\
                    Pars__u,Elem__u,Set__u,Oper__u,Alg__u,Struc__u
                   
class GroupPresentationParser:
    def __init__(
            self,
            expr:str,
            **pars:Pars___t
        ) -> None:
        """
        i.e. < S | R > where S is the set of group generators and R are the
        set of expressions which define their relations
        e.g. Dicyclic group of order n
        >>> expr = "<a,x|a**(2*{n}),x**2=a**{n},x'*a*x=a'>"
        """
        self.expr = expr
        self.pars = pars
        S,R = self.get_generators_and_relations(expr,**pars)
        self.generators = S
        self.relations = R

    @staticmethod
    def get_generators_and_relations(
            expr:str,
            **pars:Pars___t
        ) -> Tuple[list[str]]:
        S,R = expr.format(**pars).replace(" ","")[1:-1].split("|")
        return S.split(","),R.split(",")

    @staticmethod
    def parse_relations_for_exponential(
            rels:list[str],
            **pars:Pars___t
        ):
        
