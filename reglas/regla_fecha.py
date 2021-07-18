
from experta import *
from datetime import datetime

class Fecha(Fact):
    pass

class DiasReserva(Fact):
    pass

class Autorizar(Fact):
    pass

class ReglasFecha(KnowledgeEngine):

    def __init__(self):

        KnowledgeEngine.__init__(self)
    #-----------------------------AUTORIZAR RED-------------------------
    @Rule(DiasReserva(numero_dias=P(lambda numero_dias: numero_dias < 9)))
    def regla_dias_antelacion(self):
        print("la red está autorizada")
        self.declare(Autorizar(autorizar_red=True))

    #-----------------