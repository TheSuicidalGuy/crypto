import tkinter as tk

root = tk.Tk()
root.title("substitution monoalphabétique")
root.geometry("300x300")

tk.Label(root, text="Veuillez ecrire une phrase:").grid(row=0, column=0, pady=10)# grid= fonction 
message_entry = tk.Entry(root)
message_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Veuiller entrer la clé: ").grid(row=1, column=0, pady=10)
cle_entry = tk.Entry(root)
cle_entry.grid(row=1, column=1, pady=10)


tk.Button.grid(row=1, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=2, column=1, pady=10)

root.mainloop()

import string
import random

def generer_clef_substitution():
    alphabet = list(string.ascii_uppercase)
    clef = alphabet[:]
    random.shuffle(clef)
    return dict(zip(alphabet, clef))

def substitution_chiffrer(text, clef):
    text = text.upper()
    encrypted_text = ''.join(clef.get(char, char) for char in text)
    return encrypted_text

def substitution_dechiffrer(encrypted_text, clef):
    inverse_clef = {v: k for k, v in clef.items()}
    decrypted_text = ''.join(inverse_clef.get(char, char) for char in encrypted_text)
    return decrypted_text

# Exemple d'utilisation
text = "Hello"
resultat_label.config(text="Vous avez écrit : " + text)  # Affiche le texte 
clef = generer_clef_substitution()
print(f"Clef de substitution : {clef}")

encrypted_text = substitution_chiffrer(text, clef)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = substitution_dechiffrer(encrypted_text, clef)
print(f"Texte déchiffré : {decrypted_text}")