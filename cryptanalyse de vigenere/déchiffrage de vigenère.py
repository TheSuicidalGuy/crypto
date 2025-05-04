def dechiffre_vigenere(message_code,cle):
    message_code = message_code.upper()
    cle = cle.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_reel = ""
    j = 0
    for i in range(len(message_code)):
        lettre_message_code = message_code[i]
        if lettre_message_code in alphabet:
            lettre_cle = cle[j % len(cle)]
            indice = (alphabet.index(lettre_message_code) - alphabet.index(lettre_cle)) % len(alphabet) 
            message_reel += alphabet[indice]  # On chiffre la lettre du message avec la lettre de la cléb 
            j += 1
        else:
            message_reel+= lettre_message  # Si la lettre est dans l’alphabet, on la chiffre. Sinon on la garde telle quelle (espace, ponctuation, etc)
    return message_reel





message_code = input("Veuillez entrer le message codé : ")
cle = input ("Veuillez entrer la clé en lien avec le message codé : ")
message_reel = dechiffre_vigenere(message_code, cle)
print (" Le message réel est : ", message_reel)