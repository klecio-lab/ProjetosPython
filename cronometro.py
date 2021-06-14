nada = "00:45:45"

nada = nada.replace(":", " ")

nada = nada.split()

print(nada)

hora_nada = int(nada[0])
minuto_nada = int(nada[1])
segundo_nada = int(nada[2])

# fim 

soma = "02:45:45"

soma = soma.replace(":", " ")

soma = soma.split()

print(soma)

hora_soma = int(soma[0])
minuto_soma = int(soma[1])
segundo_soma = int(soma[2])

# fim


''' Parte logica '''

soma_dos_segundos = segundo_nada + segundo_soma
print(soma_dos_segundos)
soma_dos_minutos = minuto_soma + minuto_nada
print(soma_dos_minutos)
soma_das_horas = hora_soma + hora_nada
print(soma_das_horas)

if soma_dos_segundos > 60:
    soma_dos_segudos = soma_dos_segundos - 60
    Resto_segundos = 1
    soma_dos_minutos += Resto_segundos
    print(soma_dos_minutos)
    print("aqui")
    
if soma_dos_minutos > 60:
    soma_dos_minutos = soma_dos_minutos - 60
    resto_minutos = 1
    soma_das_horas = soma_das_horas + resto_minutos
    print(soma_das_horas)
    print("aqui1----")
    
print("A soma das  Horas são: {}:{}:{}".format(soma_das_horas, soma_dos_minutos, soma_dos_segudos))






    
