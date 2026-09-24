# Hardware — Android como base

Repo: open-vending-snacks. Distinto de open-vending. No fusionar.

## Que controla este repo

Planogram y vencimiento (`src/planogram.py`).
Android muestra el planogram. El candado de fecha corre en Python, no en la UI.

## Hardware minimo

- Panel Android industrial 7–10", 12 V, kiosco.
- Reloj con NTP: el lockout por vencimiento depende de la hora.
- Sensor de puerta opcional (espiral / exclusa).
- UART o USB-serial al proceso Python.

Etapa calle: IP65 si hay sol. Fuente 24 V + relés para espirales.
Pago: terminal PCI aparte.

No usar tablet de vidrio de consumo como maquina.

Licencia MIT. Lee `/LEEME_LICENCIA.md`. Sin garantia.
