import tkinter as tk
from tkinter import font
import string
import random


def open_new_window(action):
    """Ouvre une nouvelle fenêtre en fonction de l'action choisie."""
    new_window = tk.Toplevel(root)
    new_window.title(f"Action : {action}")
    new_window.geometry("400x300")  # Taille de la nouvelle fenêtre

    tk.Label(new_window, text=f"Vous avez choisi de {action}.", font=large_bold_font).pack(pady=50)
    if action == "chiffrer":
        tk.Label(new_window, text="Choisir une méthode de chiffrement :", font=larger_bold_font).pack(pady=20)

        tk.Button(new_window, text="Code de césar", width=20, height=2, command=lambda: open_method_window("Code de césar")).pack(pady=7)
        tk.Button(new_window, text="Chiffre de Vigenère", width=20, height=2, command=lambda: open_method_window("Chiffre de Vigenère")).pack(pady=7)
        tk.Button(new_window, text="Scytale", width=20, height=2, command=lambda: open_method_window("Scytale")).pack(pady=5)
        tk.Button(new_window, text="Substitution monoalphabétique", width=20, height=2, command=lambda: open_method_window("Substitution monoalphabétique")).pack(pady=7)
    
    elif action == "dechiffrer":
        tk.Label(new_window, text="Choisir une méthode de déchiffrement :", font=large_bold_font).pack(pady=20)
        tk.Button(new_window, text="Force brute", width=25, height=2, command=lambda: open_method_window("Force brute")).pack(pady=7)
        tk.Button(new_window, text="Analyse de fréquence", width=25, height=2, command=lambda: open_method_window("Analyse de fréquence")).pack(pady=7)
        tk.Button(new_window, text="Cryptanalyse de Vigenère", width=25, height=2, command=lambda: open_method_window("Cryptanalyse de Vigenère")).pack(pady=7)
    
    tk.Button(new_window, text="Fermer", command=new_window.destroy).pack(pady=20)


def open_method_window(method_name):
    """Ouvre une nouvelle fenêtre pour une méthode spécifique."""
    method_window = tk.Toplevel(root)
    method_window.title(f"Méthode : {method_name}")
    method_window.geometry("400x300")

    if method_name == "Code de césar":
        tk.Label(method_window, text="Code de César", font=larger_bold_font).pack(pady=10)
        tk.Label(method_window, text="Veuillez écrire une phrase :").pack(pady=5)
        message_entry = tk.Entry(method_window, width=30)
        message_entry.pack(pady=5)

        tk.Label(method_window, text="Veuillez entrer la clé :").pack(pady=5)
        cle_entry = tk.Entry(method_window, width=10)
        cle_entry.pack(pady=5)
        
        resultat_label = tk.Label(method_window, text="", font=larger_bold_font)
        resultat_label.pack(pady=10)

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

        tk.Button(method_window, text="Chiffrer", command=chiffrer_message).pack(pady=10)

    elif method_name == "Chiffre de Vigenère":
        tk.Label(method_window, text="Chiffre de Vigenère", font=larger_bold_font).pack(pady=10)

        tk.Label(method_window, text="Veuillez écrire une phrase :").pack(pady=5)
        message_entry = tk.Entry(method_window, width=30)
        message_entry.pack(pady=5)

        tk.Label(method_window, text="Veuillez entrer une clé (mot) :").pack(pady=5)
        cle_entry = tk.Entry(method_window, width=30)
        cle_entry.pack(pady=5)

        resultat_label = tk.Label(method_window, text="", font=larger_bold_font)
        resultat_label.pack(pady=10)

        def chiffrer_vigenere():
            message = message_entry.get().replace(" ", "").upper()
            cle = cle_entry.get().upper()
            lg_message = len(message)
            lg_cle = len(cle)
            MessageCrypte = ""

            for i in range(lg_message):
                lettre_message = ord(message[i]) - 65
                lettre_cle = ord(cle[i % lg_cle]) - 65
                lettre_cryptee = (lettre_message + lettre_cle) % 26
                MessageCrypte += chr(lettre_cryptee + 65)

            resultat_label.config(text=MessageCrypte)

        tk.Button(method_window, text="Chiffrer", command=chiffrer_vigenere).pack(pady=10)

    elif method_name == "Scytale":
        tk.Label(method_window, text="Scytale", font=larger_bold_font).pack(pady=10)

        tk.Label(method_window, text="Veuillez écrire une phrase :").pack(pady=5)
        message_entry = tk.Entry(method_window, width=30)
        message_entry.pack(pady=5)

        tk.Label(method_window, text="Veuillez entrer le nombre de colonnes :").pack(pady=5)
        colonnes_entry = tk.Entry(method_window, width=10)
        colonnes_entry.pack(pady=5)

        resultat_label = tk.Label(method_window, text="", font=larger_bold_font)
        resultat_label.pack(pady=10)

        def chiffrer_scytale():
            message = message_entry.get().replace(" ", "").upper()
            colonnes = int(colonnes_entry.get())
            lignes = (len(message) + colonnes - 1) // colonnes
            grille = [""] * colonnes

            for i in range(len(message)):
                grille[i % colonnes] += message[i]

            resultat_label.config(text="".join(grille))

        tk.Button(method_window, text="Chiffrer", command=chiffrer_scytale).pack(pady=10)

    elif method_name == "Substitution monoalphabétique":
        tk.Label(method_window, text="Substitution Monoalphabétique", font=larger_bold_font).pack(pady=10)

        tk.Label(method_window, text="Veuillez écrire une phrase :").pack(pady=5)
        message_entry = tk.Entry(method_window, width=30)
        message_entry.pack(pady=5)

        tk.Label(method_window, text="Veuillez entrer une clé (facultatif) :").pack(pady=5)
        cle_entry = tk.Entry(method_window, width=30)
        cle_entry.pack(pady=5)

        resultat_label = tk.Label(method_window, text="", font=larger_bold_font)
        resultat_label.pack(pady=10)

        def generer_clef_substitution():
            alphabet = list(string.ascii_uppercase)
            clef = alphabet[:]
            random.shuffle(clef)
            return dict(zip(alphabet, clef))

        def substitution_chiffrer():
            text = message_entry.get()
            clef = generer_clef_substitution()
            encrypted_text = ''.join(clef.get(char.upper(), char) for char in text)
            resultat_label.config(text=f"Texte chiffré : {encrypted_text}")
            print(f"Clef de substitution : {clef}")

        tk.Button(method_window, text="Chiffrer", command=substitution_chiffrer).pack(pady=5)

    elif method_name == "Force brute":
        tk.Label(method_window, text="Force brute", font=larger_bold_font).pack(pady=10)

        tk.Button(method_window, text="Code de César", width=20, height=2, command=lambda: open_force_brute_window("Code de César")).pack(pady=5)
        tk.Button(method_window, text="Scytale", width=20, height=2, command=lambda: open_force_brute_window("Scytale")).pack(pady=5)
        tk.Button(method_window, text="Chiffre de Vigenère", width=20, height=2, command=lambda: open_force_brute_window("Chiffre de Vigenère")).pack(pady=5)

    else:
        tk.Label(method_window, text=f"Vous avez sélectionné la méthode : {method_name}", font=larger_bold_font).pack(pady=50)
    
    tk.Button(method_window, text="Fermer", command=method_window.destroy).pack(pady=20)


def open_force_brute_window(method_name):
    """Ouvre une nouvelle fenêtre pour une méthode spécifique de force brute."""
    force_brute_window = tk.Toplevel(root)
    force_brute_window.title(f"Force brute : {method_name}")
    force_brute_window.geometry("400x300")

    tk.Label(force_brute_window, text=f"Force brute : {method_name}", font=larger_bold_font).pack(pady=10)

    if method_name == "Code de César":
        tk.Label(force_brute_window, text="Déchiffrement par force brute pour le Code de César.", font=("Helvetica", 12)).pack(pady=10)
    # Widgets pour entrer le texte
        tk.Label(force_brute_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(force_brute_window, width=40)
        message_entry.pack(pady=5)

        # Label pour afficher le résultat
        resultat_label = tk.Label(force_brute_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)

        # Fonction pour effectuer le déchiffrement par force brute
        def dechiffrer_force_brute():
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

        # Bouton pour lancer le déchiffrement
        tk.Button(force_brute_window, text="Déchiffrer (Force Brute)", command=dechiffrer_force_brute).pack(pady=10)

    
    elif method_name == "Scytale":
        tk.Label(force_brute_window, text="Déchiffrement par force brute pour Scytale.", font=("Helvetica", 12)).pack(pady=10)

        # Widgets pour entrer le texte
        tk.Label(force_brute_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(force_brute_window, width=40)
        message_entry.pack(pady=5)

        tk.Label(force_brute_window, text="Veuillez entrer le nombre de colonnes :").pack(pady=5)
        colonnes_entry = tk.Entry(force_brute_window, width=10)
        colonnes_entry.pack(pady=5)

        # Label pour afficher le résultat
        resultat_label = tk.Label(force_brute_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)

        # Fonction pour effectuer le déchiffrement de la Scytale
        def dechiffrer_scytale():
            message = message_entry.get().replace(" ", "").upper()
            colonnes = int(colonnes_entry.get())
            lignes = (len(message) + colonnes - 1) // colonnes
            grille = [""] * lignes

            for i in range(len(message)):
                grille[i % lignes] += message[i]

            decrypted_message = "".join(grille)
            resultat_label.config(text=f"Message déchiffré : {decrypted_message}")

        # Bouton pour lancer le déchiffrement
        tk.Button(force_brute_window, text="Déchiffrer (Scytale)", command=dechiffrer_scytale).pack(pady=10)

    elif method_name == "Chiffre de Vigenère":
        tk.Label(force_brute_window, text="Déchiffrement par force brute pour le Chiffre de Vigenère.", font=("Helvetica", 12)).pack(pady=10)

    tk.Button(force_brute_window, text="Fermer", command=force_brute_window.destroy).pack(pady=20)


# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Cryptanalyse de chiffrements")
root.attributes("-fullscreen", True)

root.columnconfigure(0, weight=1) 
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)  
root.rowconfigure(0, weight=1)    
root.rowconfigure(1, weight=1)     
root.rowconfigure(2, weight=1)   

large_bold_font = font.Font(family="Helvetica", size=24, weight="bold")
larger_bold_font = font.Font(family="Helvetica", size=20)

tk.Label(root, text="Bonjour, nous avons créé des algorithmes pour chiffrer et déchiffrer des chiffrements anciens.", font=large_bold_font).grid(row=0, column=0, columnspan=3, pady=50, sticky="n")
tk.Label(root, text="Voulez-vous chiffrer ou déchiffrer ?", font=larger_bold_font).grid(row=0, column=0, columnspan=3, pady=150, sticky="n")

button1 = tk.Button(root, text="Chiffrer", width=20, height=2, command=lambda: open_new_window("chiffrer"))
button1.grid(row=0, column=0, pady=10)

button2 = tk.Button(root, text="Déchiffrer", width=20, height=2, command=lambda: open_new_window("dechiffrer"))
button2.grid(row=0, column=2, pady=10)

root.mainloop()