import time
from datetime import datetime
data = datetime(2027, 1, 9)

agora = datetime.now()
tempo_restante = data - agora

dias = tempo_restante.days
segundos = tempo_restante.seconds

horas, resto = divmod(segundos, 3600)
minutos, segundos = divmod(resto, 60)

print(
    f"Faltam: {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
