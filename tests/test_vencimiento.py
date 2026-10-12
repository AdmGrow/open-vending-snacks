"""Prueba corta que no venda vencido.

Todavia estoy con cursos. Si esta mal, avisen.
"""
from datetime import date
from src.planogram import Planogram, Slot

def test_no_vende_vencido():
    hoy = date(2026, 10, 12)
    p = Planogram()
    p.put(Slot("A1", "chips", 10, 3, date(2026, 10, 11), 2))
    ok, reason = p.can_vend("A1", hoy)
    assert ok is False
    assert reason == "expired"
    antes = p.slots["A1"].qty
    p.vend("A1", hoy)
    assert p.slots["A1"].qty == antes

if __name__ == "__main__":
    test_no_vende_vencido()
    print("ok")
