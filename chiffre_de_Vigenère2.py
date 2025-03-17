import tkinter as tk

def generer_clef(text, cle):
    cle = list(cle)
    if len(text) == len(cle):
        return cle
    else:
        for i in range(len(text) - len(cle)):
            cle.append(cle[i % len(cle)])
    return "".join(cle)

def vigenere_chiffrer(text, cle):
    encrypted_text = []
    cle = generer_clef(text, cle)
    for i in range(len(text)):
        x = (ord(text[i]) + ord(cle[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    return "".join(encrypted_text)

    resultat_label.config(text=encrypted_text)

def vigenere_dechiffrer(encrypted_text, cle):
    decrypted_text = []
    cle = generer_clef(encrypted_text, cle)
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(cle[i]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

    resultat_label2.config(text=decrypted_text)

root = tk.Tk()
root.title("Chiffre de Vigenère")
root.geometry("400x300")

tk.Label(root, text="Veuillez ecrire une phrase:").grid(row=0, column=0, pady=10)
message_entry = tk.Entry(root)
message_entry.grid(row=0, column=1, pady=10)

button1 = tk.Button(root, text="Chiffrer", command=vigenere_chiffrer)
button1.grid(row=2, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=3, column=1, pady=10)


tk.Label(root, text="Veuillez ecrire une phrase:").grid(row=0, column=0, pady=10)
message_entry2 = tk.Entry(root)
message_entry2.grid(row=4, column=1, pady=10)

button2 = tk.Button(root, text="Dechiffrer", command=vigenere_dechiffrer)
button2.grid(row=5, column=1, pady=10)

resultat_label2 = tk.Label(root, text="")
resultat_label2.grid(row=6, column=1, pady=10)

root.mainloop()
#à reparer, le code n'est pas aboutit