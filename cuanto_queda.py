#!/usr/bin/python3
from datetime import date, timedelta

fecha_inicio = date.today()
fecha_fin = date(2026, 2, 9)
festivos_unicos = {
    date(2025, 12, 8),
}

# Rango de festivos (ambos incluidos)
rango_festivo_inicio = date(2025, 12, 22)
rango_festivo_fin = date(2026, 1, 7)

# --- FUNCIÓN PARA COMPROBAR SI ES DÍA LABORABLE ---
def es_dia_laborable(d):
    # Excluir fines de semana
    if d.weekday() >= 5:  # 5 = sábado, 6 = domingo
        return False
    # Excluir festivos únicos
    if d in festivos_unicos:
        return False
    # Excluir rango de festivos
    if rango_festivo_inicio <= d <= rango_festivo_fin:
        return False
    return True

dia_actual = fecha_inicio
dias_laborables = 0

while dia_actual <= fecha_fin:
    if es_dia_laborable(dia_actual):
        dias_laborables += 1
    dia_actual += timedelta(days=1)


print(f"Días laborables entre {fecha_inicio} y {fecha_fin}: {dias_laborables}")

dia_actual = fecha_inicio
dias_totales = 0

while dia_actual <= fecha_fin:
    dias_totales += 1
    dia_actual += timedelta(days=1)


print(f"Días entre {fecha_inicio} y {fecha_fin}: {dias_totales}")

