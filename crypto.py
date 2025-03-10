Messageacrypter="le script pour décoder ne devrait pas être long a faire,  je Le donnerai sur ce même forum"
cle=24 # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)

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