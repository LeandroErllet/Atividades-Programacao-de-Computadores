import datetime
import time

ativado = True
while ativado:
    now = datetime.datetime.now()
    hora, minuto, segundo = now.hour, now.minute, now.second
    print(hora, minuto, segundo, sep=':')
    time.sleep(1)

