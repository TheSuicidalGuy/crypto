import tkinter as tk

def chiffrer_message():
    Messageacrypter = message_entry.get()
    cle = int(cle_entry.get())
    acrypter = Messageacrypter.upper()
    lg = len(acrypter)
    MessageCrypte = ""

    for i in range(lg):
        if acrypter[i] == ' ':
            MessageCrypte += ' '
        else:
            asc = ord(acrypter[i]) + cle
            MessageCrypte += chr(asc + 26 * ((asc < 65) - (asc > 90)))

    resultat_label.config(text=MessageCrypte)

root = tk.Tk()
root.title("Chiffrement césar")
root.geometry("400x300")

tk.Label(root, text="Veuillez ecrire une phrase:").grid(row=0, column=0, pady=10)# grid= fonction afin 
message_entry = tk.Entry(root)
message_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Veuiller entrer la clé:").grid(row=1, column=0, pady=10)
cle_entry = tk.Entry(root)
cle_entry.grid(row=1, column=1, pady=10)

button1 = tk.Button(root, text="Chiffrer", command=chiffrer_message)
button1.grid(row=2, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=3, column=1, pady=10)

root.mainloop()