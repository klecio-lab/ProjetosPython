# coding=<UTF-8>

#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener
import pyautogui
import pyperclip

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #dicionário com as teclas a serem traduzidas
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "esc",
        "Key.cmd": "",
        "Key.caps_lock": "",
    }

    #converter a tecla pressionada para string
    keydata = str(key)

    #remover as asplas simples que delimitam os caracteres
    keydata = keydata.replace("'", "")

    for key in translate_keys:
        #key recebe a chave do dicionário translate_keys
        #substituir a chave (key) pelo seu valor (translate_keys[key])
        keydata = keydata.replace(key, translate_keys[key])

    texto = str(keydata)
    #print(texto)

    if texto == "Key.f9":
            pyperclip.copy("""
- Agradecemos a preferência por nosso diário!

Entre em nossos grupos de pré inscrição e fiquem por dentro da disponibilidade de vagas!

- Insta: https://www.instagram.com/libertadoresmobileff/

- Pré Inscrição: https://chat.whatsapp.com/Ilb0A9SN9qT38onpKXzAC1

Até a próxima! 🏆
""")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            
    if texto == "Key.f8":
        hora_atual = datetime.now()
        hora = int(hora_atual.strftime("%H"))
        
        if hora == 23:
            pyperclip.copy("*_GO ÁS 00:00 EM PONTO_*")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            
            pyperclip.copy('''
SOU O *CRIADOR*, PÊNDENCIAS NA SALA COMO SLOTS ERRRADOS, *SOMENTE* NO MEU PRIVADO DO *WHATSAPP!*

_Obs.: OS OUTROS ADM'S NÃO SÃO RESPOSAVÉIS PELA SALA ;)_
''')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        else:
            hora_mais = str(hora + 1)
            hora_mod = hora_mais + ":00"
            MENSAGEM = "*_GO ÁS {} EM PONTO_*".format(hora_mod)
            pyperclip.copy(MENSAGEM)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            
            pyperclip.copy('''
SOU O *CRIADOR*, PÊNDENCIAS NA SALA COMO SLOTS ERRRADOS, *SOMENTE* NO MEU PRIVADO DO *WHATSAPP!*

_Obs.: OS OUTROS ADM'S NÃO SÃO RESPOSAVÉIS PELA SALA ;)_
''')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()
