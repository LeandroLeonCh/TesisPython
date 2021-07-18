from experta import *
from datetime import datetime

class TipoCirujia(Fact):
    pass

class HoraInicio(Fact):
    pass

class HoraFin(Fact):
    pass

class DiasReserva(Fact):
    pass

class Domingo(Fact):
    pass

class ReglaTipoCirujia(KnowledgeEngine):
    def __init__(self):
        KnowledgeEngine.__init__(self)




    @Rule(TipoCirujia(tipo='rpis'))
    def regla_tipo_red(self):

        self.declare(HoraInicio(hora_inicio=14),HoraFin(hora_fin=17),DiasReserva(numero_dias=8))

    @Rule(TipoCirujia(tipo='privada'))
    def regla_tipo_privada(self):
        self.declare(HoraInicio(hora_inicio=0), HoraFin(hora_fin=24), DiasReserva(numero_dias=31))