# decrypte un texte avec le chiffre de Vigenere


  # remplace les caracteres accentues, supprime les espaces et la ponctuation
    # renvoie une chaine de lettres majuscules
    # Par défaut, il ajoute un espace tous les 5 caractères (utile pour la lisibilité).
def que_des_majuscules(texte,taille_bloc=5):
    chaine = ""
    i=0  # tient le compte des lettres du message transforme
    texte = texte.lower() # on passe tout en minuscules pour commencer
    for c in texte:
     # si c'est une lettre minuscule standarde, on la transforme en majuscule
        if 97 <= ord(c) <= 122:
            chaine += chr(ord(c)-32) # on la transforme en majuscule
        # si c'est un espace, on ne fait rien
        # traitement manuel de quelques caractères accentués (encodés ici façon bizarre)
        elif c in ("Ã¤","Ã ","Ã¢"):
            chaine += "A"
        elif c in ("Ã©","Ã¨","Ã«","Ãª"):
            chaine += "E"
        elif c in ("Ã®","Ã¯"):
            chaine += "I"
        elif c in ("Ã´","Ã¶"):
            chaine += "O"
        elif c in ("Ã¼","Ã»","Ã¹"):
            chaine += "U"
        elif c == "Ã§":
             chaine += "C"
        else:   # on ne tient pas compte du caractere lu
            i -= 1
        i+=1
        if taille_bloc>0 and i%taille_bloc==0 and i>0 and chaine[-1] != " ":
            chaine+=" "  # ajoute une espace tous les "taille_bloc" caracteres pour la lisibilite 
    return chaine

# Calcule l’indice de coïncidence d’un texte.
# C’est une statistique qui mesure la probabilité que deux lettres prises au hasard soient identiques.
# Si le texte est en français (ou langue naturelle), cet indice sera autour de 0.07
def ic(texte):
    chaine = que_des_majuscules(texte,0)
    frequences = [0]*26
    n = len(chaine)
    for c in chaine:
        frequences[ord(c)-65] += 1
    indice = 0.0
    for ni in frequences:
        indice += ni*(ni-1)
    return indice/(n*(n-1))  # formule de l’indice de coïncidence


# Essaie de trouver la longueur probable de la clé de Vigenère
# Il teste différentes longueurs de clés et isole les lettres en fonction de ces longueurs
# Si l’indice de coïncidence dépasse un certain seuil (0.06) on suppose que la longueur est bonne
def longueur_cle(texte):
    # devine la longueur de la cle avec l'indice de coincidence (tq k correspond à la longueur de la clé)
    seuil = 0.06
    ok = False
    k = 0
    while not ok and k<20:  # on teste jusqu'à 20 lettres de clé maximum
        partiel = ""
        k += 1
        j = 0
        while j < len(texte):
            partiel += texte[j] # on prend une lettre sur k (1ère, k+1, 2k+1, ...)
            j += k
        ok = ic(partiel)>seuil  # si l’indice est suffisant, on arrête
    return k # retourne la longueur probable de la clé


# decale une lettre majuscule  vers la droite ou la gauche de k positions dans l’alphabet 
 # Les autres caracteres ne sont pas modifies
def decalage(c,k):
    car = ord(c.upper()) # on convertit en code ASCII
    car += k # on decale de k
    while car>90:
        car -= 26
    while car<65:
        car += 26
    return chr(car) # on retransforme en lettre majuscule


def cesar(message,d):
    # effectue le decalage d sur les caracteres de message
    chiffre=''
    for c in message:
        chiffre += decalage(c,-d) # on applique le décalage inverse pour "tester"
    return chiffre

# Calcule les fréquences de chaque lettre dans un texte
def freq(texte):
    chaine = que_des_majuscules(texte,0)
    frequences = [0]*26 # initialisation de la liste des frequences tq:  frequences[0] = A, frequences[1] = B, ..., frequences[25] = Z
    n = len(chaine)
    for c in chaine:
        frequences[ord(c)-65] += 1 # on compte le nombre de lettres
    return frequences

# À partir de la longueur de clé estimée, essaie de deviner la clé exacte
# en comparant les fréquences de lettres aux fréquences standards du français
def cle_probable(texte,longueur_cle):
    cle = ""
    k = 0
    for k in range(longueur_cle):
        partiel = ""
        j = 0
     # extrait une "sous-chaîne" qui correspond à une seule lettre de la clé
        while k+j < len(texte):
            partiel += texte[k+j]
            j += longueur_cle
        long_message = len(partiel)
        ecart_min = 100000000
        for d in range(26):
            ecart = 0.0
            chiffre = cesar(partiel,d)
            frequences = freq(chiffre)
            for i in range(26):
                ecart += abs(frequences[i]/long_message-histogramme[i])
            if ecart<ecart_min:
                ecart_min = ecart
                decalage = d
        cle += chr(decalage+65)
    return cle


# Applique le chiffrement ou le déchiffrement de Vigenère avec la clé trouvée
def vigenere(message,cle,crypte):
    # effectue le decalage en fonction de la cle sur les caracteres de message
    n = 0
    chiffre=''
    for c in message:
        k = ord(cle[n%len(cle)])-65 # on récupère la bonne lettre de la clé
        if crypte:
            chiffre += decalage(c,k)
        else:
            chiffre += decalage(c,-k)
        n+=1
    return chiffre


# Fréquences approximatives des lettres en français (A à Z)
# Utilisé pour comparer lors de la cryptanalyse
histogramme = [0.084,0.0106,0.0303,0.0418,0.1726,0.0112,0.0127,0.0092,0.0734,0.0031,0.0005,0.0601,0.0296,0.0713,0.0526,0.0301,0.0099,0.0655,0.0808,0.0707,0.0574,0.0132,0.0004,0.0045,0.0030,0.0012]




    # tests
texte= "KWHBIFB, CUYJ ANSYKME, RIK PBSQWA QÉWYAXNMIHZRTRWVG JIK IYHELZBY, ZSAGKW GQFKEMF QKW EMEY,UMQ FAMNMAZ, MFLBRIFBF ISEXNMRGVF JI NWLGKW,TR TENQEK KDQFYEFB FAV DMF MSMNSXIK IZKVK.I CKMFM YKW GVG-OPK LÉCUWÉK AHX PWA CREFKUKW,ICR IIK ZBOW VM YGDMZ, ZGPSLEUMLA RZ LGVGKYP,TNOWKMAZ TABRAWWURTX DMHXW YZNTHWA NOPWA OREFKUKWUWZSI VMF GZAZBTW LZNÎTIJ À KÔGÉ JIMF."
texte_maj = que_des_majuscules(texte,0)
longueur = longueur_cle(texte_maj)
if longueur==0:
    print("la longueur de la clÃ© n'a pas pu Ãªtre dÃ©terminÃ©e")
else:
    print("longueur probable de la clÃ© :",longueur)
    cle = cle_probable(texte_maj,longueur)
    print(cle)
    texte_decode = vigenere(texte_maj,cle,False)
    print(texte_decode)

    # SOURCE : https://www.apprendre-en-ligne.net/crypto/python/vigenere/decrypt-vigenere.py
    # Ce programme n'a evidemment pas été fait par nous mais par un proffesseur qui a choisit de laisser public ce code.
    