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
