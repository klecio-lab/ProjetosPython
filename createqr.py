import  pyqrcode 

code = pyqrcode.create("daleee")

code.png("codigo.png", scale=6)

if code != 0:
    print("Qr code foi gerado")
