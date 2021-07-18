

from experta import *
from datetime import datetime

class Hora(Fact):
    """Info about the traffic light."""
    print('llego al fact')
    pass
class Autorizar(Fact):
    pass

class HoraInicio(Fact):
    pass
class DiaCirujia(Fact):
    pass

class DiasReserva(Fact):
    pass

now = datetime.now()
hora=0
aut=False
class ReglasHoras(KnowledgeEngine):

    def __init__(self):

        KnowledgeEngine.__init__(self)


#-----------------AUTORIZAR----------------------
    @Rule(AND(
        Hora(hora=P(lambda x: x >= 14)& P(lambda x: x <= 17)),
          OR(
              DiaCirujia(day='Monday'),
              DiaCirujia(day='Tuesday'),
              DiaCirujia(day='Wednesday'),
              DiaCirujia(day='Thursday'),
              DiaCirujia(day='Friday')
          ),
         DiasReserva(numero_dias=P(lambda numero_dias: numero_dias < 9))
          ))
    def autorizar_red_uno(self):
        print("la cirujia publica es autorizada!! UNO")
        self.declare(Autorizar(autorizar_red=True))
#--------------------------AUTORIZAR-----------------------------------------------

    @Rule(AND(
        Hora(hora=P(lambda x: x >= 8) & P(lambda x: x <= 12)),
          DiaCirujia(day='Saturday'),
          DiasReserva(numero_dias=P(lambda numero_dias: numero_dias < 9))
        ))
    def autorizar_red_dos(self):
        print("la cirujia publica es autorizada!!DOS")
        self.declare(Autorizar(autorizar_red=True))

# --------------------------NO AUTORIZAR-----------------------------------------------

    @Rule(AND(Hora(hora=P(lambda x: x < 14) | P(lambda x: x > 17)),
          OR(
              DiaCirujia(day='Monday'),
              DiaCirujia(day='Tuesday'),
              DiaCirujia(day='Wednesday'),
              DiaCirujia(day='Thursday'),
              DiaCirujia(day='Friday')
          )
          ))
    def no_autorizar_red_uno(self):
        print("la cirujia publica es autorizada!! NO UNO")
        self.declare(Autorizar(autorizar_red=False))

    # ----------------------NO AUTORIZAR-------------------------------------
    @Rule(AND(Hora(hora=P(lambda x: x < 8) | P(lambda x: x > 12)),
          DiaCirujia(day='Saturday')
          ))
    def no_autorizar_red_dos(self):
        print("la cirujia publica es autorizada!! NO DOS")
        self.declare(Autorizar(autorizar_red=False))

    # ----------------------------NO AUTORIZAR-----------------------------------

    @Rule(DiaCirujia(day='Sunday'))
    def no_autorizar_red_tres(self):
        print("la cirujia publica es autorizada!! NO TRES")
        self.declare(Autorizar(autorizar_red=False))



    #---------------FIN------------------


    @Rule(HoraInicio(hora_inicio=MATCH.hora_inicio), Autorizar(autorizar_red=MATCH.autorizar_red))
    def hora_inicio(self):
        self.horas_inicio  = hora
        print("a esta hora iniciaría la  cirujía: ")
        print(self.horas_inicio )
        print('La red puede realziar cirujia?: ')
        print(aut)





    @Rule(HoraInicio(hora_inicio=MATCH.hora_inicio), Autorizar(autorizar_red=MATCH.autorizar_red))
    def hora_inicio(self):
        self.horas_inicio  = hora
        print("a esta hora iniciaría la  cirujía: ")
        print(self.horas_inicio )
        print('La red puede realziar cirujia?: ')
        print(aut)


