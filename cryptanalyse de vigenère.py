# test 1 #

message = "SEMAINE"
cle = "CLE"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message_code = ""

for i in range(len(message)):
    lettre_message = message[i]
    lettre_cle = cle[i % len(cle)]
    indice = (alphabet.index(lettre_message) + alphabet.index(lettre_cle)) % len(alphabet)
    message_code += alphabet[indice]
print("Message chiffré :", message_code)



