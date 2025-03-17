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

