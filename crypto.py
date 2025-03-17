import tkinter as tk

root = tk.Tk()
root.title("Chiffrement césar")
root.geometry("300x300")

button1 = tk.Button(root, text="Veuillez ecrire une phrase:", command=lambda: print("") ) 
button1.grid(row=1, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=2, column=1, pady=10)


#######################
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

def vigenere_dechiffrer(encrypted_text, cle):
    decrypted_text = []
    cle = generer_clef(encrypted_text, cle)
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(cle[i]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

# Exemple d'utilisation
text = "BONJOUR"
cle = "KEY"
encrypted_text = vigenere_chiffrer(text, cle)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = vigenere_dechiffrer(encrypted_text, cle)
print(f"Texte déchiffré : {decrypted_text}")
#https://www.thepingouin.com/2024/10/15/chiffre-de-vigenere-en-python-guide-complet-pour-le-chiffrement-polyalphabetique/






def scytale_chiffrer(text, num_rails):
    encrypted_text = [''] * num_rails
    for i in range(len(text)):
        encrypted_text[i % num_rails] += text[i]
    return ''.join(encrypted_text)

def scytale_dechiffrer(encrypted_text, num_rails):
    num_cols = len(encrypted_text) // num_rails
    decrypted_text = [''] * num_cols
    for i in range(len(encrypted_text)):
        decrypted_text[i % num_cols] += encrypted_text[i]
    return ''.join(decrypted_text)

# Exemple d'utilisation
text = "HELLOSCYTALE"
num_rails = 3
encrypted_text = scytale_chiffrer(text, num_rails)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = scytale_dechiffrer(encrypted_text, num_rails)
print(f"Texte déchiffré : {decrypted_text}")



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



