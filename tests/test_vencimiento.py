"""Prueba corta que no venda vencido.

El dia del vencimiento todavia vende. Ayer no.
Sin fecha no se si vencio, entonces vende.
Todavia estoy con cursos. Si esta mal, avisen.
"""
from datetime import date
from src.planogram import Planogram, Slot

def test_no_vende_vencido():
    hoy = date(2026, 10, 19)
    p = Planogram()
    p.put(Slot("A1", "chips", 10, 3, date(2026, 10, 18), 2))
    ok, reason = p.can_vend("A1", hoy)
    assert ok is False
    assert reason == "expired"
    antes = p.slots["A1"].qty
    p.vend("A1", hoy)
    assert p.slots["A1"].qty == antes

def test_dia_de_vencimiento_si_vende():
    hoy = date(2026, 10, 19)
    p = Planogram()
    p.put(Slot("A2", "barra", 10, 3, date(2026, 10, 19), 2))
    ok, reason = p.can_vend("A2", hoy)
    assert ok is True
    assert reason == "ok"
    p.vend("A2", hoy)
    assert p.slots["A2"].qty == 2

def test_sin_fecha_si_vende():
    hoy = date(2026, 10, 19)
    p = Planogram()
    p.put(Slot("B1", "galletita", 10, 3, None, 2))
    ok, reason = p.can_vend("B1", hoy)
    assert ok is True
    assert reason == "ok"

if __name__ == "__main__":
    test_no_vende_vencido()
    test_dia_de_vencimiento_si_vende()
    test_sin_fecha_si_vende()
    print("ok")
