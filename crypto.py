import tkinter as tk

root = tk.Tk()
root.title("Chiffrement césar")
root.geometry("300x300")

button1 = tk.Button(root, text="Veuillez ecrire une phrase:", command=lambda: print("") ) 
button1.grid(row=1, column=1, pady=10)


Messageacrypter= input("Veuillez ecrire une phrase : ")
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
#https://fraoustin.fr/old/20111222_1.html