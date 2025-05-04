import tkinter as tk
import string
import random

# Fonction pour générer une clé de substitution
def generer_clef_substitution():
    alphabet = list(string.ascii_uppercase)
    clef = alphabet[:]
    random.shuffle(clef)
    return dict(zip(alphabet, clef))

# Fonction pour chiffrer un texte avec la substitution
def substitution_chiffrer():
    text = message_entry.get()  # Récupérer le texte de l'entrée
    clef = generer_clef_substitution()  # Générer une clé aléatoire
    encrypted_text = ''.join(clef.get(char.upper(), char) for char in text)  # Chiffrer le texte
    resultat_label.config(text=f"Texte chiffré : {encrypted_text}")  # Afficher le résultat
    print(f"Clef de substitution : {clef}")  # Afficher la clé dans la console

# Fonction pour déchiffrer un texte avec la substitution
def substitution_dechiffrer():
    text = message_entry.get()  # Récupérer le texte de l'entrée
    clef = eval(cle_entry.get())  # Récupérer la clé entrée par l'utilisateur
    inverse_clef = {v: k for k, v in clef.items()}  # Inverser la clé
    decrypted_text = ''.join(inverse_clef.get(char.upper(), char) for char in text)  # Déchiffrer le texte
    resultat_label.config(text=f"Texte déchiffré : {decrypted_text}")  # Afficher le résultat

# Création de la fenêtre principale
root = tk.Tk()
root.title("Substitution Monoalphabétique")
root.geometry("400x300")

# Widgets pour entrer le texte et la clé
tk.Label(root, text="Veuillez écrire une phrase :").grid(row=0, column=0, pady=10)
message_entry = tk.Entry(root, width=30)
message_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Veuillez entrer la clé (facultatif) :").grid(row=1, column=0, pady=10)
cle_entry = tk.Entry(root, width=30)
cle_entry.grid(row=1, column=1, pady=10)

# Boutons pour chiffrer et déchiffrer
chiffrer_button = tk.Button(root, text="Chiffrer", command=substitution_chiffrer)
chiffrer_button.grid(row=2, column=0, pady=10)

dechiffrer_button = tk.Button(root, text="Déchiffrer", command=substitution_dechiffrer)
dechiffrer_button.grid(row=2, column=1, pady=10)

# Label pour afficher le résultat
resultat_label = tk.Label(root, text="", font=("Helvetica", 12))
resultat_label.grid(row=3, column=0, columnspan=2, pady=10)

# Lancer la boucle principale
root.mainloop()