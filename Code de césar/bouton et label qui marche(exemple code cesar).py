import tkinter as tk

def chiffrer_message():
    """Chiffre un message avec le Code de César."""
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

    resultat_label.config(text=f"Message chiffré : {MessageCrypte}")

def dechiffrer_force_brute():
    """Déchiffre un message avec le Code de César en utilisant la force brute."""
    MessageCrypte = message_entry.get().upper()
    lg = len(MessageCrypte)
    resultats = []

    for cle in range(1, 26):  # Essayer toutes les clés possibles (1 à 25)
        MessageDecrypte = ""
        for i in range(lg):
            if MessageCrypte[i] == ' ':
                MessageDecrypte += ' '
            else:
                asc = ord(MessageCrypte[i]) - cle
                MessageDecrypte += chr(asc + 26 * ((asc < 65) - (asc > 90)))
        resultats.append(f"Clé {cle}: {MessageDecrypte}")

    # Afficher tous les résultats dans le label
    resultat_label.config(text="\n".join(resultats))

root = tk.Tk()
root.title("Code de César - Déchiffrement par Force Brute")
root.geometry("600x400")

# Widgets pour entrer le texte
tk.Label(root, text="Veuillez écrire une phrase :").grid(row=0, column=0, pady=10)
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=0, column=1, pady=10)

# Widgets pour entrer la clé (pour le chiffrement uniquement)
tk.Label(root, text="Veuillez entrer la clé :").grid(row=1, column=0, pady=10)
cle_entry = tk.Entry(root, width=10)
cle_entry.grid(row=1, column=1, pady=10)

# Bouton pour chiffrer
button1 = tk.Button(root, text="Chiffrer", command=chiffrer_message)
button1.grid(row=2, column=0, pady=10)

# Bouton pour déchiffrer par force brute
button2 = tk.Button(root, text="Déchiffrer (Force Brute)", command=dechiffrer_force_brute)
button2.grid(row=2, column=1, pady=10)

# Label pour afficher le résultat
resultat_label = tk.Label(root, text="", justify="left", wraplength=500)
resultat_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()