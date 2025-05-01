# test 1 #

message =  input("Veuillez ecrire un message : ")  # Message à chiffrer
cle = input("Veuillez entrer la clé : ")  # Clé de chiffrement
message = message.upper()  # Convertir le message en majuscules
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alphabet utilisé pour le chiffrement
message_code = "" # Initialiser le message chiffré

for i in range(len(message)): # Parcourir chaque lettre du message
    lettre_message = message[i] # Lettre du message
    lettre_cle = cle[i % len(cle)]
    indice = (alphabet.index(lettre_message) + alphabet.index(lettre_cle)) % len(alphabet)
    message_code += alphabet[indice]
print("Message chiffré :", message_code)



