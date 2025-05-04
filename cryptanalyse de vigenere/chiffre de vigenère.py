def chiffre_vigenere(message,cle):
    message = message.upper()
    cle = cle.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_code = ""
    j = 0
    for i in range(len(message)):
        lettre_message = message[i]
        if lettre_message in alphabet:
            lettre_cle = cle[j % len(cle)]
            indice = (alphabet.index(lettre_message) + alphabet.index(lettre_cle)) % len(alphabet) 
            message_code += alphabet[indice]  # On chiffre la lettre du message avec la lettre de la cléb 
            j += 1
        else:
            message_code += lettre_message  # Si la lettre est dans l’alphabet, on la chiffre. Sinon on la garde telle quelle (espace, ponctuation, etc)
    return message_code





message = input("Veuillez entrer le message à chiffrer : ")
cle = input ("Veuillez entrer la clé : ")
message_code = chiffre_vigenere(message, cle)
print ("Message chiffré : ", message_code)
         



