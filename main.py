# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import choice
from reglas.prueba_uno import *
from flask import Flask, jsonify, request
from reglas.prueba_uno import ReglasHoras
from reglas.regla_fecha import ReglasFecha
from reglas.regla_tipo_cirujia import ReglaTipoCirujia, TipoCirujia

app = Flask(__name__)




@app.route('/regla_privada', methods=['POST'])
def  regla_privada():
    #print(request.json['hora'])
    hora_inicio = int(request.json['hora'])
    fecha_date = datetime.fromisoformat(request.json['fecha'])
    day = dia_semana(fecha_date)
    numero_dias = numero_dias_reserva(fecha_date)
    engine = ReglasHoras()
    engine.reset()
    engine.declare(Hora(hora=hora_inicio), DiaCirujia(day=day), DiasReserva(numero_dias=numero_dias))
    engine.run()
    facts_return = engine.facts

    return jsonify(facts_return)

@app.route('/regla_fecha', methods=['POST'])
def regla_fecha():
    fecha_date = datetime.fromisoformat(request.json['fecha'])
    day = dia_semana(fecha_date)
    numero_dias = numero_dias_reserva(fecha_date)
    engine = ReglasFecha()
    engine.reset()
    engine.declare(DiaCirujia(day=day), DiasReserva(numero_dias=numero_dias))
    engine.run()
    facts_return = engine.facts

    return jsonify(facts_return)

@app.route('/regla_tipo_cirujia/<string:tipo_cirujia>', methods=['POST'])
def regla_tipo_cirujia(tipo_cirujia):
    tipo=tipo_cirujia
    engine = ReglaTipoCirujia()
    engine.reset()
    engine.declare(TipoCirujia(tipo=tipo))
    engine.run()
    facts_return = engine.facts

    return jsonify(facts_return)

def dia_semana(fecha):
    day = fecha.strftime('%A')
    return day

def numero_dias_reserva(fecha):
    now = datetime.now()
    delta = now - fecha
    return abs(delta.days)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")


