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
        if s.expiry and s.expiry < today:
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
