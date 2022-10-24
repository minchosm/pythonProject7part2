import time
from time import strftime, localtime

# Hora horaObjetivo transformada a segundos
horaObjetivo = 68400
hora = strftime("%H:%M:%S", localtime())
horaformateada = time.strptime(hora, "%H:%M:%S")
tsegundos = horaformateada.tm_hour * 3600 + horaformateada.tm_min * 60 + horaformateada.tm_sec
if tsegundos < horaObjetivo:
    segundos = horaObjetivo - tsegundos
    h = int(segundos/3600)
    m = segundos % 3600
    minutos = int(m / 60)
    s = m % 60
    print(f"Faltan {h} horas, {minutos} minutos, {s} segundos para las 19:00")
else:
    segundos = tsegundos - horaObjetivo
    h = int(segundos / 3600)
    m = segundos % 3600
    minutos = int(m / 60)
    s = m % 60
    print(f"Pasan {h} horas, {minutos} minutos, {s} segundos de las 19:00")

