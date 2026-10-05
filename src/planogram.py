"""Donde va cada snack y cuando vence.

Si esta vencido no lo vendo. Eso lo saque de un tutorial de inventario.
"""
from dataclasses import dataclass
from datetime import date

@dataclass
class Slot:
    id: str
    sku: str
    capacity: int
    qty: int
    expiry: date | None
    par: int

def is_expired(expiry: date | None, today: date) -> bool:
    # sin fecha no se si vencio; el dia del vencimiento todavia vende
    if expiry is None:
        return False
    return expiry < today

class Planogram:
    def __init__(self):
        self.slots = {}

    def put(self, slot: Slot):
        self.slots[slot.id] = slot

    def can_vend(self, slot_id: str, today: date) -> tuple[bool, str]:
        s = self.slots.get(slot_id)
        if not s:
            return False, "unknown slot"
        if s.qty <= 0:
            return False, "empty"
        if is_expired(s.expiry, today):
            return False, "expired"
        return True, "ok"

    def vend(self, slot_id: str, today: date) -> tuple[bool, str]:
        ok, reason = self.can_vend(slot_id, today)
        if not ok:
            return False, reason
        self.slots[slot_id].qty -= 1
        return True, "vended"

    def restock_list(self):
        # cosas que hay que reponer
        return [s.id for s in self.slots.values() if s.qty <= s.par]


if __name__ == "__main__":
    # tres fechas: ayer no vende, hoy si, manana si
    hoy = date(2026, 10, 5)
    p = Planogram()
    p.put(Slot("A1", "chips", 10, 3, date(2026, 10, 4), 2))
    p.put(Slot("A2", "barra", 10, 3, date(2026, 10, 5), 2))
    p.put(Slot("B2", "gaseosa", 8, 5, date(2026, 12, 1), 2))
    print("ayer", p.can_vend("A1", hoy))   # False expired
    print("hoy", p.can_vend("A2", hoy))    # True ok
    print("futuro", p.can_vend("B2", hoy))  # True ok
    # si esta vencido, vend no tiene que tocar el stock
    antes = p.slots["A1"].qty
    print("vend vencido", p.vend("A1", hoy), "qty", p.slots["A1"].qty)
    assert p.slots["A1"].qty == antes
