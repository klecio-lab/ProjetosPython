# importando bibliotecas
import pymysql  # conectar com o bd
import cv2  # parte de leitura
import numpy as np  # parte de leitura
import pyzbar.pyzbar as pyzbar  # parte de leitura
from datetime import datetime  # para gravar os horarios
import calendar
import pygame

# criando conexão com o servidor
try:
    conexão = pymysql.connect(
        host='sql289.main-hosting.eu',
        user='u993759258_LKTech',
        password='678LKtech',
        database='u993759258_qrproject'
    )
except pymysql.err.OperationalError:
    print("conexão não foi possivel")


cursor = conexão.cursor()

# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()

def tocar_muscica():
    pygame.mixer.music.load('ponto_batido.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

def otimizada():
    resultado = cursor.fetchall()
    # buscando ids no banco de dados
    for x in resultado:
     print(x)
    t = str(resultado)
    b = ''.join(t)

    b = str(b)

    b = b.replace("(", "")
    b = b.replace(",", "")
    b = b.replace(")", "")
    b = b.replace("[", "")
    b = b.replace("]", "")
    b = b.replace(",", "")

    buscando_data = b.split()
    buscando_data = [value.replace('\n', '').strip("'") for value in buscando_data]
    dta_str = str(data)

def enviar_dados():
    valor = [(ID, nome, setor, email, telefone, R_hora, dia_da_semana, R_data)]
    cursor.execute(com_sql, valor)

    conexão.commit()  # gravar permanente as modificações

    print(cursor.rowcount, "inserida com sucesso")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN


parar = True
while True:
    parar = True
    while parar == True:
        _, frame = cap.read()
        print(frame)
        decodedObjects = pyzbar.decode(frame)

        for obj in decodedObjects:

            #pra pegar o dia da semana
            nova_data = datetime.now()

            data = nova_data.strftime('%d/%m/%Y')

            dia = int(nova_data.strftime('%d'))
            mes = int(nova_data.strftime('%m'))
            ano = int(nova_data.strftime('%Y'))
            # indice da semana(0,1,2...)
            dt = calendar.weekday(ano, mes, dia)

            weekday_name = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado", "Domingo"]

            dia_da_semana = weekday_name[dt]

            #print(dia_da_semana)
            # horarios para marcar os pontos
            data_atual = datetime.now()

            data = data_atual.strftime('%d/%m/%Y')
            R_data = str(data)

            hora_atual = data_atual.strftime("%H:%M:%S")
            R_hora = hora_atual

            hora = data_atual.strftime('%H')

            compara_hora = int(hora)

            #leitura = obj.data.decode("utf-8")  # quardando os valores
            #cv2.imshow("QrProject", frame)
            #print("Data", obj.data) #texto do qr

            a = obj.data.decode("utf-8")  # quardando os valores
            print(a)#printa os valores no console

            #a = "MECARD:N:Kemuel Lima batista;ORG:informatica;TEL:988052398;EMAIL:kemuellima20@gmail.com;ADR:1;;"

            a = a.replace(" ", "_")

            b = a.replace(";", " ")

            b = b.replace("MECARD:", "")

            b = b.replace("N:", "")

            b = b.replace("ORG:", "")

            b = b.replace("TEL:", "")

            b = b.replace("EMAIL:", "")

            b = b.replace("ADR:", "")

            b = b.replace("URL:", "")

            c = b.split()
            print(c)
            nome = c[0]

            setor = c[1]

            telefone = c[2]

            email = c[3]

            endereco = c[5]

            primary_key = str(c[4])

            ID = int(c[4])

            # verificar o tipo de batida
            #q = "SELECT ID_Func FROM funcionario"
            cursor.execute("SELECT ID_Func FROM funcionario")
            print("aqui0")
            resultado1 = cursor.fetchall()

            # buscando ids no banco de dados
            for x in resultado1:
                print(x)
            t = str(resultado1)
            b = ''.join(t)

            b = str(b)

            b = b.replace("(", "")
            b = b.replace(",", "")
            b = b.replace(")", "")

            b = b.split()

            verificao_de_id = []

            # tranformar a lista em numeros inteiros
            for val in b:
                verificao_de_id.append(int(val))
                print(verificao_de_id)

            if ID in verificao_de_id:

                # buscando o tipo de batida
                a = "SELECT batida FROM funcionario WHERE ID_Func=" + primary_key
                cursor.execute(a)
                resultado = cursor.fetchall()

                for x in resultado:
                    print(x)
                t = str(resultado)
                b = ''.join(t)

                b = str(b)

                b = b.replace("(", "")
                b = b.replace(",", "")
                b = b.replace(")", "")

                b = b.split()

                verificao = []

                # tranformar a lista em numeros inteiros
                for val in b:
                    verificao.append(int(val))
                    print(verificao)

                # separando se é de 2 batidas ou de 4 batidas
                if 2 in verificao:

                    # verificando se a data ja foi registrada'''
                    a = "SELECT data FROM entrada WHERE id=" + primary_key
                    #aqui vai uma função
                    otimizada()

                    if dta_str in buscando_data:
                        print("Ponto Já Foi Batido")

                        # verificando a data da saida
                        a = "SELECT data FROM saida WHERE id=" + primary_key
                        #aqui vai uma função
                        otimizada()

                        if dta_str in buscando_data:
                            print("Ponto Já Foi Batido")
                            # time.sleep(3) no lugar do time.sleep vou utilixar o evento de esperar a musica acabar
                            parar = False
                        else:
                            print("Novo Ponto Sendo Batido")

                            # parte de enviar para o banco de dados de entrada
                            com_sql = "INSERT INTO saida(id, nome, setor, email, telefone, horario, data) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                            #funções
                            enviar_dados()
                            tocar_muscica()
                            parar = False

                    else:
                        print("Novo Ponto Sendo Batido")

                        # parte de enviar para o banco de dados de entrada
                        com_sql = "INSERT INTO entrada(id, nome, setor, email, telefone, horario,dia_da_semana, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        
                        #funções
                        enviar_dados()
                        tocar_muscica()
                        parar = False

                if 4 in verificao:

                    # bucando datas do entrada
                    a = "SELECT data FROM entrada WHERE id=" + primary_key
                    #aqui vai uma função
                    otimizada()

                    # bucando datas do ida_almoco
                    if dta_str in buscando_data:
                        print("Ponto Já Foi Batido")

                        # verificando se a data de ida_almoco
                        a = "SELECT data FROM ida_almoco" + primary_key
                        #aqui vai uma função
                        otimizada()

                        if dta_str in buscando_data:
                            print("Ponto Já Foi Batido")

                            # verificando se a data de volta_almoco
                            a = "SELECT data FROM volta_almoco WHERE id=" + primary_key
                            #aqui vai uma função
                            otimizada()
                            tocar_muscica()
                            parar = False

                            if dta_str in buscando_data:

                                # verificando a data de saida
                                a = "SELECT data FROM saida WHERE id=" + primary_key
                                #aqui vai uma função
                                otimizada()

                                if dta_str in buscando_data:
                                    print("Ponto Já Foi Batido")
                                    # time.sleep(3) no lugar do time.sleep vou utilixar o evento de esperar a musica acabar
                                    pygame.mixer.music.load('ponto_batido.mp3')
                                    pygame.mixer.music.play()
                                    pygame.event.wait()
                                    parar = False
                                else:
                                    print("Novo Ponto Sendo Batido")

                                    # parte de enviar para o banco de dados de saida
                                    com_sql = "INSERT INTO saida(id, nome, setor, email, telefone, horario,dia_da_semana, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                                    #funções
                                    enviar_dados()
                                    tocar_muscica()
                                    parar = False
                                    print("aqui2")

                            else:
                                print("Novo Ponto Sendo Batido")

                                # parte de enviar para o banco de dados de volta_almoco
                                com_sql = "INSERT INTO volta_almoco(id, nome, setor, email, telefone, horario,dia_da_semana, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                                #funções
                                enviar_dados()
                                tocar_muscica()
                                parar = False
                        else:
                            print("Novo Ponto Sendo Batido")

                            # parte de enviar para o banco de dados de ida_almoco
                            com_sql = "INSERT INTO ida_almoco(id, nome, setor, email, telefone, horario,dia_da_semana, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                            #funções
                            enviar_dados()
                            tocar_muscica()
                            parar = False

                    else:
                        print("Novo Ponto Sendo Batido")

                        # parte de enviar para o banco de dados de entrada
                        com_sql = "INSERT INTO entrada(id, nome, setor, email, telefone, horario, dia_da_semana, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                        #funções
                        enviar_dados()
                        tocar_muscica()
                        parar = False
            else:
                print("O usuario não consta em nosso sistema")

        cv2.imshow("QrProject", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

