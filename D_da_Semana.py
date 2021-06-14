import calendar
from datetime import datetime  # para gravar os horarios

data_atual = datetime.now()

data = data_atual.strftime('%d/%m/%Y')

dia = int(data_atual.strftime('%d'))
mes = int(data_atual.strftime('%m'))
ano = int(data_atual.strftime('%Y'))
#indice da semana(0,1,2...)
dt = calendar.weekday(ano, mes, dia)

weekday_name = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

dia_da_semana = weekday_name[dt]

print(dia_da_semana)
