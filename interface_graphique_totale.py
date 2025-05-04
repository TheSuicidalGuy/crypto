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

    elif method_name == "Analyse de fréquence":
        tk.Label(method_window, text="Analyse de fréquence", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(method_window, text="Code de César", width=20, height=2, command=lambda: open_analyse_frequence_window("Code de César")).pack(pady=5)
        tk.Button(method_window, text="Scytale", width=20, height=2, command=lambda: open_analyse_frequence_window("Scytale")).pack(pady=5)
        tk.Button(method_window, text="Chiffre de Vigenère", width=20, height=2, command=lambda: open_analyse_frequence_window("Chiffre de Vigenère")).pack(pady=5)
        
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

        # Widgets pour entrer le texte chiffré
        tk.Label(force_brute_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(force_brute_window, width=40)
        message_entry.pack(pady=5)

        # Widgets pour entrer la clé
        tk.Label(force_brute_window, text="Veuillez entrer une clé (mot) :").pack(pady=5)
        cle_entry = tk.Entry(force_brute_window, width=30)
        cle_entry.pack(pady=5)

        # Label pour afficher le résultat
        resultat_label = tk.Label(force_brute_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)

        # Fonction pour effectuer le déchiffrement du Chiffre de Vigenère
        def dechiffrer_vigenere():
            try:
                message = message_entry.get().replace(" ", "").upper()
                cle = cle_entry.get().upper()
                lg_message = len(message)
                lg_cle = len(cle)
                MessageDecrypte = ""

                if not cle:
                    resultat_label.config(text="Veuillez entrer une clé valide.")
                    return

                for i in range(lg_message):
                    lettre_message = ord(message[i]) - 65
                    lettre_cle = ord(cle[i % lg_cle]) - 65
                    lettre_decryptee = (lettre_message - lettre_cle + 26) % 26
                    MessageDecrypte += chr(lettre_decryptee + 65)

                resultat_label.config(text=f"Message déchiffré : {MessageDecrypte}")
            except Exception as e:
                resultat_label.config(text=f"Erreur : {str(e)}")

        # Bouton pour lancer le déchiffrement
        tk.Button(force_brute_window, text="Déchiffrer (Vigenère)", command=dechiffrer_vigenere).pack(pady=10)
        
    # Bouton pour fermer la fenêtre
    tk.Button(force_brute_window, text="Fermer", command=force_brute_window.destroy).pack(pady=20)

def open_analyse_frequence_window(method_name):
    """Ouvre une nouvelle fenêtre pour une méthode spécifique d'analyse de fréquence."""
    analyse_window = tk.Toplevel(root)
    analyse_window.title(f"Analyse de fréquence : {method_name}")
    analyse_window.geometry("600x400")

    tk.Label(analyse_window, text=f"Analyse de fréquence : {method_name}", font=larger_bold_font).pack(pady=10)

    if method_name == "Code de César":
        tk.Label(analyse_window, text="Analyse de fréquence pour le Code de César.", font=("Helvetica", 12)).pack(pady=10)

        # Widgets pour entrer le texte chiffré
        tk.Label(analyse_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(analyse_window, width=40)
        message_entry.pack(pady=5)

        # Label pour afficher les résultats
        resultat_label = tk.Label(analyse_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)

        # Fonction pour effectuer l'analyse de fréquence
        def analyse_frequence_cesar():
            texte = message_entry.get().upper()
            if not texte:
                resultat_label.config(text="Veuillez entrer un texte valide.")
                return

            # Fréquence des lettres en français (approximative)
            frequences_francaises = {
                'E': 14.7, 'A': 7.6, 'S': 7.9, 'I': 7.5, 'T': 7.0,
                'N': 7.0, 'R': 6.5, 'U': 6.1, 'L': 5.4, 'O': 5.2,
                'D': 3.6, 'C': 3.3, 'M': 2.9, 'P': 2.5, 'V': 1.8,
                'Q': 1.4, 'F': 1.1, 'B': 1.0, 'G': 0.9, 'H': 0.8,
                'J': 0.7, 'X': 0.4, 'Y': 0.3, 'Z': 0.1, 'K': 0.0, 'W': 0.0
            }

            # Calcul des fréquences dans le texte
            frequences_message = {}
            for lettre in texte:
                if lettre.isalpha():
                    frequences_message[lettre] = frequences_message.get(lettre, 0) + 1

            # Normalisation des fréquences
            total_lettres = sum(frequences_message.values())
            for lettre in frequences_message:
                frequences_message[lettre] = (frequences_message[lettre] / total_lettres) * 100

            # Deviner la clé en supposant que la lettre la plus fréquente = 'E'
            lettre_frequente = max(frequences_message, key=frequences_message.get)
            cle = (ord(lettre_frequente) - ord('E')) % 26

            # Déchiffrer le texte avec la clé trouvée
            def dechiffre(texte, cle):
                resultat = ""
                for c in texte:
                    if c.isalpha():
                        decal = (ord(c.upper()) - ord('A') - cle) % 26
                        resultat += chr(decal + ord('A'))
                    else:
                        resultat += c
                return resultat

            texte_dechiffre = dechiffre(texte, cle)

            # Afficher les résultats dans le label
            resultats = f"Lettre la plus fréquente : {lettre_frequente}\n"
            resultats += f"Clé estimée : {cle}\n\n"
            resultats += f"Texte déchiffré :\n{texte_dechiffre}"
            resultat_label.config(text=resultats)

        # Bouton pour lancer l'analyse de fréquence
        tk.Button(analyse_window, text="Analyser", command=analyse_frequence_cesar).pack(pady=10)

    elif method_name == "Scytale":
        tk.Label(analyse_window, text="Analyse de fréquence pour Scytale.", font=("Helvetica", 12)).pack(pady=10)
     
     # Widgets pour entrer le texte chiffré
        tk.Label(analyse_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(analyse_window, width=40)
        message_entry.pack(pady=5)

        tk.Label(analyse_window, text="Veuillez entrer le nombre de colonnes :").pack(pady=5)
        colonnes_entry = tk.Entry(analyse_window, width=10)
        colonnes_entry.pack(pady=5)

        # Label pour afficher les résultats
        resultat_label = tk.Label(analyse_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)
        # Fonction pour effectuer l'analyse de fréquence pour Scytale
        def analyse_frequence_scytale():
            try:
                # Récupérer les valeurs des champs d'entrée
                message = message_entry.get().replace(" ", "").upper()
                colonnes = int(colonnes_entry.get())

                if not message or colonnes <= 0:
                    resultat_label.config(text="Veuillez entrer un texte valide et un nombre de colonnes valide.")
                    return

                # Reconstitution du texte par lignes
                lignes = (len(message) + colonnes - 1) // colonnes
                grille = [""] * colonnes

                for i in range(len(message)):
                    grille[i % colonnes] += message[i]

                # Reconstruction du texte déchiffré
                texte_dechiffre = "".join(grille)

                # Affichage des résultats
                resultats = f"Texte déchiffré :\n{texte_dechiffre}"
                resultat_label.config(text=resultats)

            except ValueError:
                resultat_label.config(text="Erreur : Veuillez entrer un nombre valide pour les colonnes.")

        # Bouton pour lancer l'analyse de fréquence
        tk.Button(analyse_window, text="Analyser", command=analyse_frequence_scytale).pack(pady=10)

    elif method_name == "Chiffre de Vigenère":
        tk.Label(analyse_window, text="Analyse de fréquence pour le Chiffre de Vigenère.", font=("Helvetica", 12)).pack(pady=10)
        
        # Widgets pour entrer le texte chiffré
        tk.Label(analyse_window, text="Veuillez écrire une phrase chiffrée :").pack(pady=5)
        message_entry = tk.Entry(analyse_window, width=40)
        message_entry.pack(pady=5)

        # Widgets pour entrer la longueur de la clé
        tk.Label(analyse_window, text="Veuillez entrer la longueur de la clé supposée :").pack(pady=5)
        longueur_cle_entry = tk.Entry(analyse_window, width=10)
        longueur_cle_entry.pack(pady=5)

        # Label pour afficher les résultats
        resultat_label = tk.Label(analyse_window, text="", justify="left", wraplength=500)
        resultat_label.pack(pady=10)
        
        def analyse_frequence_vigenere():
            try:
                texte = message_entry.get().replace(" ", "").upper()
                longueur_cle = int(longueur_cle_entry.get())

                if not texte or longueur_cle <= 0:
                    resultat_label.config(text="Veuillez entrer un texte valide et une longueur de clé valide.")
                    return

                # Lettres les plus fréquentes en français
                lettres_frequentes_fr = ['E', 'A', 'S', 'T']

                # Étape 1 : Diviser le texte selon la longueur de la clé
                groupes = ['' for _ in range(longueur_cle)]
                j = 0
                for i, c in enumerate(texte):
                    if c.isalpha():
                        groupes[j % longueur_cle] += c.upper()
                        j += 1

                # Étape 2 : Trouver une clé probable
                cle_estimee = ''
                for groupe in groupes:
                    lettre_freq = analyse_frequence(groupe)
                    cle = (ord(lettre_freq) - ord('E')) % 26  # Supposons que 'E' est la lettre la plus fréquente
                    cle_estimee += chr(ord('A') + cle)

                # Étape 3 : Déchiffrer avec la clé estimée
                texte_dechiffre = dechiffre_vigenere(texte, cle_estimee)

                # Afficher les résultats
                resultats = f"Clé estimée : {cle_estimee}\n\n"
                resultats += f"Texte déchiffré :\n{texte_dechiffre}"
                resultat_label.config(text=resultats)

            except ValueError:
                resultat_label.config(text="Erreur : Veuillez entrer une longueur de clé valide.")
        def analyse_frequence(texte):
            frequences = {}
            for lettre in texte:
                if lettre.isalpha():
                    frequences[lettre] = frequences.get(lettre, 0) + 1
            if not frequences:
                return 'E'  # Valeur par défaut
            return max(frequences, key=frequences.get)  # Lettre la plus fréquente

        # Fonction pour déchiffrer avec le Chiffre de Vigenère
        def dechiffre_vigenere(texte, cle):
            resultat = ""
            cle = cle.upper()
            i = 0
            for c in texte:
                if c.isalpha():
                    decal = (ord(c.upper()) - ord(cle[i % len(cle)])) % 26
                    resultat += chr(decal + ord('A'))
                    i += 1
                else:
                    resultat += c
            return resultat

        # Bouton pour lancer l'analyse de fréquence
        tk.Button(analyse_window, text="Analyser", command=analyse_frequence_vigenere).pack(pady=10)
        

       

    # Bouton pour fermer la fenêtre
    tk.Button(analyse_window, text="Fermer", command=analyse_window.destroy).pack(pady=20)


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

def open_about_window():
    """Ouvre une fenêtre 'Explication des codes'."""
    about_window = tk.Toplevel(root)
    about_window.title("À propos")
    about_window.geometry("400x300")
    tk.Label(about_window, text="Explication des codes", font=larger_bold_font).pack(pady=20)
    tk.Label(about_window, text="Le code de césar :", font=large_bold_font, justify="center").pack(pady=20)
    tk.Label(about_window, text="Le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, \n" \
                                "dans l'ordre de l'alphabet. Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début. Par exemple avec un décalage de 3 vers la droite, \n" \
                                " A est remplacé par D, B devient E, et ainsi jusqu'à W qui devient Z, puis X devient A etc. ", justify="center").pack(pady=20)
    tk.Label(about_window, text="Le chiffre de Vigenère :", font=large_bold_font, justify="center").pack(pady=20)
    tk.Label(about_window, text="Le chiffre de Vigenère est un algorithme de chiffrement par substitution polyalphabétique. Il utilise une clé pour déterminer le décalage de chaque lettre du texte clair. \n" \
                                "Chaque lettre de la clé correspond à un décalage dans l'alphabet, et le texte est chiffré en appliquant ces décalages successivement.", justify="center").pack(pady=20)
    tk.Label(about_window, text="La scytale :", font=large_bold_font, justify="center").pack(pady=20)
    tk.Label(about_window, text="La scytale est un ancien dispositif de chiffrement qui consiste à enrouler un message autour d'un cylindre. \n" \
                                "Le message est ensuite lu en déroulant le cylindre, révélant ainsi le texte chiffré.", justify="center").pack(pady=20)
    tk.Label(about_window, text="La substitution monoalphabétique :", font=large_bold_font, justify="center").pack(pady=20)
    tk.Label(about_window, text="La substitution monoalphabétique est un type de chiffrement par substitution dans lequel chaque lettre du texte clair est remplacée par une autre lettre. \n" \
                                "La clé de chiffrement est une permutation de l'alphabet, et chaque lettre est remplacée par la lettre correspondante dans la clé.", justify="center").pack(pady=20)
                            
    tk.Button(about_window, text="Fermer", command=about_window.destroy).pack(pady=20)

button3 = tk.Button(root, text="Explication des codes", width=20, height=2, command=open_about_window)
button3.grid(row=1, column=1, pady=10)

root.mainloop()