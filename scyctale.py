import tkinter as tk

def scytale_chiffrer(text, num_rails):
    encrypted_text = [''] * num_rails
    for i in range(len(text)):
        encrypted_text[i % num_rails] += text[i] #Chaque caractère du texte est ajouté à un rail en fonction de son index modulo
    return ''.join(encrypted_text)

def scytale_dechiffrer(encrypted_text, num_rails):
    num_cols = len(encrypted_text) // num_rails
    decrypted_text = [''] * num_cols
    for i in range(len(encrypted_text)):
        decrypted_text[i % num_cols] += encrypted_text[i]
    return ''.join(decrypted_text)

def chiffrer_message():
    # Récupérer les valeurs des champs d'entrée
    text = message_entry.get()
    try:
        num_rails = int(cle_entry.get())
        if num_rails <= 0:
            raise ValueError("La clé doit être un entier positif.")
    except ValueError:
        resultat_label.config(text="Erreur : clé invalide.")
        return

    encrypted_text = scytale_chiffrer(text, num_rails)
    resultat_label.config(text=f"Texte chiffré : {encrypted_text}")

root = tk.Tk()
root.title("Chiffrement scytale")
root.geometry("400x300")

tk.Label(root, text="Veuillez ecrire une phrase :").grid(row=0, column=0, pady=10)
message_entry = tk.Entry(root)
message_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Veuiller entrer la clé :").grid(row=1, column=0, pady=10)
cle_entry = tk.Entry(root)
cle_entry.grid(row=1, column=1, pady=10)

button1 = tk.Button(root, text="Chiffrer", command=chiffrer_message)
button1.grid(row=2, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=3, column=1, pady=10)

root.mainloop()



# Exemple d'utilisation
text = "HELLOSCYTALE"
num_rails = 3
encrypted_text = scytale_chiffrer(text, num_rails)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = scytale_dechiffrer(encrypted_text, num_rails)
print(f"Texte déchiffré : {decrypted_text}")