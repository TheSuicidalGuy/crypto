
message_codé = input("Veuillez insérer le message codé : ")
cle = input("Veuillez entrer la clé : ")
message_codé = message_codé.upper()
cle = cle.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message_reel = ""
j = 0

for i in range(len(message_codé)):
    lettre_message_codé = message_codé[i]
    if lettre_message_codé in alphabet:
        lettre_cle = cle[j % len(cle)]
        indice = (alphabet.index(lettre_message_codé) - alphabet.index(lettre_cle)) % len(alphabet)
        message_reel += alphabet[indice]
        j += 1  # On avance dans la clé seulement si on chiffre une lettre
    else:
        message_reel += lettre_message_codé  # Si la lettre est dans l’alphabet, on la chiffre. Sinon on la garde telle quelle (espace, ponctuation, etc)

print("Message chiffré :", message_reel)