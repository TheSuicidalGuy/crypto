import tkinter as tk

Messageacrypter= input("Veuillez ecrire une phrase: ")
cle=int(input("Veuiller entrer la clé: "))

acrypter=Messageacrypter.upper()
lg=len(acrypter)
MessageCrypte=""

for i in range(lg):
    if acrypter[i]==' ':
        MessageCrypte+=' '
    else:
        asc=ord(acrypter[i])+cle
        MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

print(MessageCrypte)