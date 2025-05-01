# test codage de vegenère # :

message = input("Veuillez écrire un message : ")
cle = input("Veuillez entrer la clé : ")
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
        message_code += alphabet[indice]
        j += 1  # On avance dans la clé seulement si on chiffre une lettre
    else:
        message_code += lettre_message  # Si la lettre est dans l’alphabet, on la chiffre. Sinon on la garde telle quelle (espace, ponctuation, etc)

print("Message chiffré :", message_code)

