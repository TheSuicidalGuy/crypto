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
        def analyse_frequence(texte):
            texte = texte.upper()
            frequences = {}
            for lettre in texte:
                if lettre.isalpha():
                    if lettre in frequences:
                        frequences[lettre] += 1
                    else:
                        frequences[lettre] = 1
            total = sum(frequences.values())
            
            print("Fréquences des lettres :")
            for lettre in sorted(frequences, key=frequences.get, reverse=True):
                pourcentage = 100 * frequences[lettre] / total
                print(f"{lettre} : {pourcentage:.2f}%")

            return frequences
        
        def dechiffre(texte, cle):
            resultat = ""
            for c in texte:
                if c.isalpha():
                    decal = (ord(c.upper()) - ord('A') - cle) % 26
                    resultat += chr(decal + ord('A'))
                else:
                    resultat += c
            return resultat
#texte à trouver  = "LOIN DE MOI L'IDEE DE GRAVER DANS LE MARBRE DE TAILLER DANS UNE ECORCE D'ARBRE LOIN DE MOI L'IDEE DE SUGGERER QUE JE M'EN MOQUE QUE JE N'EN AI RIEN À FAIRE QUE GUERE JE NE M'EN SOUCIE LOIN DE MOI CES FOLIES MAIS JE M'ECHINE DEPUIS OCTOBRE ET POURQUOI DONC DEPUIS DEBUT OCTOBRE MEME ET QUI M'AIME ME SUIVE DEPUIS OCTOBRE DEPUIS CE MEME DERNIER OCTOBRE LE TROIS DU MOIS JE CROIS DEPUIS CE TEMPS-LÀ DEPUIS TROIS MOIS DEPUIS TROIS MOIS ET UNE SEMAINE JE M'ECHINE AILLEURS ET LE TRES LONG TEXTE N'A PAS AVANCE D'UN POIL PAS BEAUCOUP SANS DOUTE EST-CE MON COTE VELLEITAIRE QUI NE CESSE DE ME JOUER DES TOURS ET LES MEANDRES DU TRES LONG TEXTE SE SONT FIGES COMME UNE GELEE LE LONG DES PAROIS D'UN BOCAL DE VERRE ET JE VITUPERE CONTRE MES ESSAIS EPHEMERES MON TEMPERAMENT AFFREUSEMENT VELLEITAIRE ET CE TEINT D'ALBÂTRE QUI N'EST PAS LE MIEN COMME JE VOUDRAIS QU'IL FÛT D'ALBÂTRE OU D'EBENE OU AUTREMENT MEME SANS METAPHORE MAIS AU MOINS QU'IL AIT QUELQUE TENUE QUE MON VISAGE SANS RETENUE PUISSE SOUDAIN PASSER POUR UN TISSU UNE PIERRE UN SONGE SOIT EN QUELQUE SORTE UN TABLEAU FASSE TABLEAU MAIS CE N'EST PAS LE CAS MEME CE MOT ALBÂTRE JETE AU VISAGE JETE TOUT À TRAC SUR LA PAGE EN HAUT DE PAGE CE MOT ME DEFIGURE NE ME FIGURE PAS NE ME REPRESENTE PAS NE FIGURE RIEN DE CE QUE JE SUIS DE CE QUE JE PENSE ETRE ET JE SUIS ENCORE ET TOUJOURS CIRCONSPECT DANS LE DOUTE ET CE MOT N'APPORTE RIEN AUCUNE REPONSE ET DONC TOUJOURS JE ME JETTE À LA FIGURE CES ACCUSATIONS COMME DES BOUTEILLES NON PAS À LA MER MAIS BIEN DANS LA GUEULE OUI JE ME DONNE DES COUPS DE BOUTEILLE TESSONS EPARS SUR LE PARQUET ET MES JOUES ENSANGLANTEES ENFIN QUE CE SOIT OU NON METAPHORE QUE LE MOT D'ALBÂTRE ME FIGURE OU NON JE PRENDS CES COUPS CES REPROCHES EN PLEIN VISAGE ET JE M'ACCUSE D'ETRE VELLEITAIRE AUSSI BIEN SÛR POUR TROP ENTREPRENDRE JE LANCE CENT FEUX IL EST NORMAL QU'UN CERTAIN NOMBRE DES FOYERS MEURE ET MEME NE DEMARRE QU'À PEINE AVANT DE S'ACHEVER DANS UN BRUIT DE FEUILLES MOUILLEES DE BOIS MORT DE BOIS TROP VERT ENCORE POUR PRENDRE TOUT CELA ENCORE METAPHORE ET TOUJOURS METAPHORE PEUT-ETRE EST-CE LE MOT ALBÂTRE QUI APPELLE AUTANT DE METAPHORES OU BIEN LES CONDITIONS D'ECRITURE DU TRES LONG TEXTE QUE PAR FACETIE OU ENCORE AUTODERISION JE POURRAIS ETRE TENTE DE REBAPTISER TRES LONG TEXTE INTERROMPU ET L'ADJECTIF INTERROMPU ICI AU MILIEU DE LA LIGNE INTERROMPT MES SONGES INTERROMPT LE TORRENT DE SORNETTES LANCE D'AUTRES TIRADES PROPOSE PEUT-ETRE D'AUTRES CHARADES MAIS POUR MIEUX ME RAMENER VERS LE RIVAGE BOURBEUX OÙ JE NE CESSE DE ME LANCER CES REPROCHES À LA FIGURE VELLEITAIRE VELLEITAIRE ET ME VOICI ENCORE À NE PAS MEME ESSAYER DE ME JUSTIFIER MOI-MEME DE TOUT CELA FEUX MAL ETEINTS ET FEUX QUI N'ONT JAMAIS PRIS AUSSI ME TROUVE-JE VINGT VAINES JUSTIFICATIONS IMPROBABLES MEME SI CERTAINES SONT JUSTES PAR AILLEURS COMME DANS LE CAS DU PROJET DE TRADUIRE REGULIEREMENT ET PENSAIS-JE AU DEBUT AU MOINS UNE FOIS PAR SEMAINE UN POEME ET QUI S'EST ENLISE APRES À PEINE TROIS OU QUATRE TRACASSERIES MAIS CELA REPRENDRA PARFOIS AUSSI DEPUIS DEBUT OCTOBRE LE TROIS JE CROIS SUSPENDU À CE MOT D'ALBÂTRE DEPUIS LE TROIS OCTOBRE LE TROIS JE CROIS JE ME DISAIS QUE POUR ETRE INTERROMPU OU INACHEVE LE TRES LONG TEXTE RECELAIT DE VRAIES POSSIBILITES ET QU'IL SUFFISAIT SUFFIRAIT EÛT SUFFI DE S'Y REMETTRE ET LA MACHINE REPRENDRAIT DU GALON NON LÀ CETTE IMAGE-LÀ NE VA PAS JE MELANGE LES FORMULES CROISE LES FIGURES DE STYLE ET DONC JE PENSAIS QU'IL ME FAUDRAIT TOUTES PROPORTIONS GARDEES ENVISAGER CES CARNETS COMME PAUL VALERY TRAVAILLANT REGULIEREMENT ET SANS ESPOIR D'EN FINIR JAMAIS CHAQUE MATIN À SES CAHIERS DESORMAIS REGROUPES EN DEUX TOMES EN PLEIADE ET QUE J'AI DEVORES CONSULTES ADMIRES LUS COMPULSES LONGUEMENT NAGUERE MAIS IL FAUDRAIT DIRE JADIS OU BALANCER ENTRE LES DEUX LUS DISONS ENTRE 1993 ET 1997 ET DONC TOUTES PROPORTIONS GARDEES JE ME VERRAIS BIEN AINSI À REPRENDRE TEL CHANTIER INTERROMPU TROIS MOIS ET LE FAISANT AVANCER UN PETIT PEU MAIS ENFIN CE N'EST PAS POSSIBLE IL NE VA PAS SE COMPARER À PAUL VALERY L'AUTRE OISEUX OISIF EX-OISIEN DE SURCROÎT ANCIEN OISIEN INTO THE BARGAIN NON IL NE VA PAS SE COMPARER À PAUL VALERY TOUT DE MEME ALORS QUE SEULEMENT ET IL NOUS L'A DIT MEME AVEC METAPHORES TOUT LE TINTOUIN OUI OUI NOIR SUR BLANC DIT CE N'EST RIEN D'AUTRE QU'UN AFFREUX VELLEITAIRE COMME LA PLUIE COMME LES PIERRES S'ATTARDANT TRAÎNANT SON ABSENCE D'INSPIRATION AU COURS DE DEUX LONGUES SEMAINES UN TEXTE SE MEUT OU SE MEURT SANS LE MOUVEMENT DES LIGNES OU DES DOIGTS SUR LA PAGE OU DES DOIGTS SUR LE CLAVIER OU DU MERCURE DANS LA CABOCHE PAS MOYEN D'AVANCER UN TEXTE SE MEUT OU SE MEURT RETENEZ BIEN CELA RENTIERS DE L'ECRITURE RETENEZ BIEN CELA DIEUX DE PLATINE DIEUX DE MARBRE DIEUX D'IVOIRE DIEUX D'AIRAIN RETENEZ CELA UN TEXTE SE MEUT OU SE MEURT UNE PROFANATION ET C'EST LA VIE LE SILENCE GLISSANT DE L'ONDE IMMOBILE ET PLUS UN CLAPOTIS VOUS VOYEZ LENTEMENT AGONISER LE TEXTE DIEUX D'AIRAIN J'EN APPELLE À VOS RICTUS J'EN APPELLE MEME À VOS SOCLES J'EN APPELLE À ESCHYLE À EURIPIDE J'EN APPELLE AUX ASTRONOMES AVEC LEURS LUNETTES J'EN APPELLE AUX BOURGEOIS DE VAUDEVILLE AVEC LEURS MONOCLES OUI J'EN APPELLE À SOPHOCLE SURTOUT DIEUX D'AIRAIN J'EN APPELLE AUX HEMICYCLES DES AMPHITHEÂTRES TOUT AUTANT QU'AUX HEMISTICHES ABSOLUS DU VIEUX PERE CORNEILLE UN TEXTE SE MEUT OU SE MEURT ET SUR LA SCENE AUCUN ACTEUR NE MEURT VRAIMENT TANT QU'UN TEXTE LATENT OU DIT LE PORTE OU QUE LE DIABLE L'EMPORTE UN ACTEUR PORTE SON TEXTE PLUS QU'IL NE LE DIT IL LE PORTE EN-DEDANS AU-DEDANS DE SOI ET CELA N'A RIEN À VOIR AVEC UN CHIEN MORT NI UN TRAJET EN AUTOBUS JUSQU'AUX CONFINS D'UNE VILLE POUSSIEREUSE D'AFRIQUE AFIN D'ENTERRER UN ENFANT MORT NON CELA NE PORTE PAS DE NOM C'EST SEULEMENT LA VIE PROPRE LA DYNAMIQUE INTROUVABLE DE TOUT TEXTE ET SI L'ON VOUS DIT DE TISSER FILEUSES TISSEZ SI L'ON VOUS DIT DE TISSER DIEUX D'AIRAIN NE DORMEZ PAS DANS L'HERBE CAR LE CHEMIN EST LONG ET IL Y AURA ENCORE DES CARREFOURS DES DOUANES DES PASSAGES ETROITS DES FOURCHES CAUDINES DES DICTATEURS"
# Exemple avec clé 3
        texte = "ORLQ GH PRL O'LGHH GH JUDYHU GDQV OH PDUEUH GH WDLOOHU GDQV XQH HFRUFH G'DUEUH ORLQ GH PRL O'LGHH GH VXJJHUHU TXH MH P'HQ PRTXH TXH MH Q'HQ DL ULHQ D IDLUH TXH JXHUH MH QH P'HQ VRXFLH ORLQ GH PRL FHV IROLHV PDLV MH P'HFKLQH GHSXLV RFWREUH HW SRXUTXRL GRQF GHSXLV GHEXW RFWREUH PHPH HW TXL P'DLPH PH VXLYH GHSXLV RFWREUH GHSXLV FH PHPH GHUQLHU RFWREUH OH WURLV GX PRLV MH FURLV GHSXLV FH WHPSV-OD GHSXLV WURLV PRLV GHSXLV WURLV PRLV HW XQH VHPDLQH MH P'HFKLQH DLOOHXUV HW OH WUHV ORQJ WHAWH Q'D SDV DYDQFH G'XQ SRLO SDV EHDXFRXS VDQV GRXWH HVW-FH PRQ FRWH YHOOHLWDLUH TXL QH FHVVH GH PH MRXHU GHV WRXUV HW OHV PHDQGUHV GX WUHV ORQJ WHAWH VH VRQW ILJHV FRPPH XQH JHOHH OH ORQJ GHV SDURLV G'XQ ERFDO GH YHUUH HW MH YLWXSHUH FRQWUH PHV HVVDLV HSKHPHUHV PRQ WHPSHUDPHQW DIIUHXVHPHQW YHOOHLWDLUH HW FH WHLQW G'DOEDWUH TXL Q'HVW SDV OH PLHQ FRPPH MH YRXGUDLV TX'LO IXW G'DOEDWUH RX G'HEHQH RX DXWUHPHQW PHPH VDQV PHWDSKRUH PDLV DX PRLQV TX'LO DLW TXHOTXH WHQXH TXH PRQ YLVDJH VDQV UHWHQXH SXLVVH VRXGDLQ SDVVHU SRXU XQ WLVVX XQH SLHUUH XQ VRQJH VRLW HQ TXHOTXH VRUWH XQ WDEOHDX IDVVH WDEOHDX PDLV FH Q'HVW SDV OH FDV PHPH FH PRW DOEDWUH MHWH DX YLVDJH MHWH WRXW D WUDF VXU OD SDJH HQ KDXW GH SDJH FH PRW PH GHILJXUH QH PH ILJXUH SDV QH PH UHSUHVHQWH SDV QH ILJXUH ULHQ GH FH TXH MH VXLV GH FH TXH MH SHQVH HWUH HW MH VXLV HQFRUH HW WRXMRXUV FLUFRQVSHFW GDQV OH GRXWH HW FH PRW Q'DSSRUWH ULHQ DXFXQH UHSRQVH HW GRQF WRXMRXUV MH PH MHWWH D OD ILJXUH FHV DFFXVDWLRQV FRPPH GHV ERXWHLOOHV QRQ SDV D OD PHU PDLV ELHQ GDQV OD JXHXOH RXL MH PH GRQQH GHV FRXSV GH ERXWHLOOH WHVVRQV HSDUV VXU OH SDUTXHW HW PHV MRXHV HQVDQJODQWHHV HQILQ TXH FH VRLW RX QRQ PHWDSKRUH TXH OH PRW G'DOEDWUH PH ILJXUH RX QRQ MH SUHQGV FHV FRXSV FHV UHSURFKHV HQ SOHLQ YLVDJH HW MH P'DFFXVH G'HWUH YHOOHLWDLUH DXVVL ELHQ VXU SRXU WURS HQWUHSUHQGUH MH ODQFH FHQW IHXA LO HVW QRUPDO TX'XQ FHUWDLQ QRPEUH GHV IRBHUV PHXUH HW PHPH QH GHPDUUH TX'D SHLQH DYDQW GH V'DFKHYHU GDQV XQ EUXLW GH IHXLOOHV PRXLOOHHV GH ERLV PRUW GH ERLV WURS YHUW HQFRUH SRXU SUHQGUH WRXW FHOD HQFRUH PHWDSKRUH HW WRXMRXUV PHWDSKRUH SHXW-HWUH HVW-FH OH PRW DOEDWUH TXL DSSHOOH DXWDQW GH PHWDSKRUHV RX ELHQ OHV FRQGLWLRQV G'HFULWXUH GX WUHV ORQJ WHAWH TXH SDU IDFHWLH RX HQFRUH DXWRGHULVLRQ MH SRXUUDLV HWUH WHQWH GH UHEDSWLVHU WUHV ORQJ WHAWH LQWHUURPSX HW O'DGMHFWLI LQWHUURPSX LFL DX PLOLHX GH OD OLJQH LQWHUURPSW PHV VRQJHV LQWHUURPSW OH WRUUHQW GH VRUQHWWHV ODQFH G'DXWUHV WLUDGHV SURSRVH SHXW-HWUH G'DXWUHV FKDUDGHV PDLV SRXU PLHXA PH UDPHQHU YHUV OH ULYDJH ERXUEHXA RX MH QH FHVVH GH PH ODQFHU FHV UHSURFKHV D OD ILJXUH YHOOHLWDLUH YHOOHLWDLUH HW PH YRLFL HQFRUH D QH SDV PHPH HVVDBHU GH PH MXVWLILHU PRL-PHPH GH WRXW FHOD IHXA PDO HWHLQWV HW IHXA TXL Q'RQW MDPDLV SULV DXVVL PH WURXYH-MH YLQJW YDLQHV MXVWLILFDWLRQV LPSUREDEOHV PHPH VL FHUWDLQHV VRQW MXVWHV SDU DLOOHXUV FRPPH GDQV OH FDV GX SURMHW GH WUDGXLUH UHJXOLHUHPHQW HW SHQVDLV-MH DX GHEXW DX PRLQV XQH IRLV SDU VHPDLQH XQ SRHPH HW TXL V'HVW HQOLVH DSUHV D SHLQH WURLV RX TXDWUH WUDFDVVHULHV PDLV FHOD UHSUHQGUD"

        frequences = analyse_frequence(texte)

# Devine la clé en supposant que la lettre la plus fréquente = 'E'
        lettre_frequente = max(frequences, key=frequences.get)
        cle = (ord(lettre_frequente) - ord('E')) % 26
        print(f"\nLettre la plus fréquente : {lettre_frequente}")
        print(f"Clé estimée : {cle}")

# Déchiffre avec la clé trouvée
        texte_dechiffre = dechiffre(texte, cle)
        print("\nTexte déchiffré :")
        print(texte_dechiffre)

    elif method_name == "Scytale":
        tk.Label(analyse_window, text="Analyse de fréquence pour Scytale.", font=("Helvetica", 12)).pack(pady=10)
     

    elif method_name == "Chiffre de Vigenère":
        tk.Label(analyse_window, text="Analyse de fréquence pour le Chiffre de Vigenère.", font=("Helvetica", 12)).pack(pady=10)
       

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

root.mainloop()