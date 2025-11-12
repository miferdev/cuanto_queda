from datetime import date, timedelta

# festivos = {
#     date(2025, 12, 8),  
#     date(2025, 12, 22),  
#     date(2025, 12, 23),  
#     date(2025, 12, 24),  
#     date(2025, 12, 25),  
#     date(2025, 12, 26),  
#     date(2025, 12, 27),  
#     date(2025, 12, 28),  
#     date(2025, 12, 29),  
#     date(2025, 12, 30),  
#     date(2025, 12, 31),  
#     date(2026, 1, 1),
#     date(2026, 1, 2),
#     date(2026, 1, 3),
#     date(2026, 1, 4),
#     date(2026, 1, 5),
#     date(2026, 1, 6),
#     date(2026, 1, 7),
# }

fecha_final = date(2026, 2, 13)

hoy = date.today()

dias_totales = fecha_final - hoy

dias_de_clase = 0

for i in range(dias_totales.days + 1):
    dia = hoy + timedelta(days = i)

    finde = dia.weekday() < 5
    #festivo = dia in festivos
    if not finde: #or not festivo:
        dias_de_clase+=1




print(f"{dias_totales.days} días naturales quedan para las prácticas\n")

print(f"{dias_de_clase} días de clase quedan para las prácticas")
