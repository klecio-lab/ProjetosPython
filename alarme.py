import datetime

now = datetime.datetime.now()

def hora():
    hora = now.strftime('%H')
    minuto = now.strftime('%M')
    print(hora, minuto)
while True:
    hora()
    
