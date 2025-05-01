

# Pour un texte lonnnnnnng

def analyse_frequence(texte):
    texte = texte.upper()
    frequences = {}

    for lettre in texte:
        if lettre.isalpha():
            if lettre in frequences:
                frequences[lettre] += 1
            else:
                frequences[lettre] = 1

    total = sum(frequences.values())

    print("Fréquences des lettres :")
    for lettre in sorted(frequences, key=frequences.get, reverse=True):
        pourcentage = 100 * frequences[lettre] / total
        print(f"{lettre} : {pourcentage:.2f}%")

    return frequences

def dechiffre(texte, cle):
    resultat = ""
    for c in texte:
        if c.isalpha():
            decal = (ord(c.upper()) - ord('A') - cle) % 26
            resultat += chr(decal + ord('A'))
        else:
            resultat += c
            return resultat
texte = "comme la pluie comme les pierres s'attardant traînant son absence d'inspiration au cours de deux longues semaines un texte se meut ou se meurt sans le mouvement des lignes ou des doigts sur la page ou des doigts sur le clavier ou du mercure dans la caboche pas moyen d'avancer un texte se meut ou se meurt retenez bien cela rentiers de l'écriture retenez bien cela dieux de platine dieux de marbre dieux d'ivoire dieux d'airain retenez cela un texte se meut ou se meurt une profanation et c'est la vie le silence glissant de l'onde immobile et plus un clapotis vous voyez lentement agoniser le texte dieux d'airain j'en appelle à vos rictus j'en appelle même à vos socles j'en appelle à Eschyle à Euripide j'en appelle aux astronomes avec leurs lunettes j'en appelle aux bourgeois de vaudeville avec leurs monocles oui j'en appelle à Sophocle surtout dieux d'airain j'en appelle aux hémicycles des amphithéâtres tout autant qu'aux hémistiches absolus du vieux père Corneille un texte se meut ou se meurt et sur la scène aucun acteur ne meurt vraiment tant qu'un texte latent ou dit le porte ou que le diable l'emporte un acteur porte son texte plus qu'il ne le dit il le porte en-dedans au-dedans de soi et cela n'a rien à voir avec un chien mort ni un trajet en autobus jusqu'aux confins d'une ville poussiéreuse d'Afrique afin d'enterrer un enfant mort non cela ne porte pas de nom c'est seulement la vie propre la dynamique introuvable de tout texte et si l'on vous dit de tisser fileuses tissez si l'on vous dit de tisser dieux d'airain ne dormez pas dans l'herbe car le chemin est long et il y aura encore des carrefours des douanes des passages étroits des fourches caudines des dictateurs en puissance de vrais dictateurs aussi oui ceux qui veulent dicter le sens la direction à prendre le sens d'un texte se meut ou se meurt et la garde qu'en faites-vous oh je ne m'en préoccupe si l'on vous dit de tisser c'est votre boulot pas le mien n'est-ce pas dieux d'airain dieux de marbre dieux d'albâtre dieux d'ivoire je savais bien que je réussirais à placer le mot albâtre dans un texte un jour en allant de l'avant à force d'aller de l'avant et peut-être mon seul et unique but en écrivant même en tenant ces carnets était de parvenir au texte qui me permettrait d'écrire le mot albâtre de le graver comme qui dirait métaphoriquement dans le marbre et cela évidemment se produit aujourd'hui où il pleut à pierre fendre ou pas vraiment un goutte-à-goutte à peine accéléré mais qui mouille détrempe tout et même la grande poubelle grise ouverte depuis hier afin d'en laver le fond noirâtre mot qui rime avec albâtre dans tous les cas cette pluie est une aubaine et justement ce jour de pluie infinie ténue mais tenace j'écris enfin le mot albâtre et ne sais qu'en faire ne sais que faire après d'autres doués d'un sens de l'honneur plus aiguisé que le mien ici se feraient hara-kiri c'est à n'en pas douter et tandis que la pluie humecte puis humidifie puis mouille puis inonde la grande poubelle grise ouverte dans la cour je ne sais ce qui me pousse à écrire encore et toujours albâtre comme si ce mot soudainement prenait la forme d'une incantation le dernier ressort le dernier battement des veines le dernier sursaut artériel qui permette d'aller de l'avant un texte se meut ou se meurt l'ai-je dit je crois l'avoir écrit mais l'ai-je dit toujours est-il qu'un texte oui tu l'as dit merci l'acteur se porte un texte se meut ou se meurt et sans un mot même désuet ou inutile auquel se raccrocher parfois les textes les plus parfaits s'enlisent se figent dans une immobilité d'onde gélifiée un désert de racines et de vieux bois de flottaison échoué desséché au point de ne plus pouvoir écrire même une phrase qui tienne debout et qui suis-je pour parler de phrase qui tienne debout moi qui assis pianotant tapotant clapotant comme l'eau vive d'une pluie fine mais farouche ténue mais tenace ne sais rien dire d'autre ne sais rien écrire d'autre non ne sait dire non ne sait pas écrire d'autre mot"  # Exemple avec clé 3

frequences = analyse_frequence(texte)

# Devine la clé en supposant que la lettre la plus fréquente = 'E'
lettre_frequente = max(frequences, key=frequences.get)
cle = (ord(lettre_frequente) - ord('E')) % 26
print(f"\nLettre la plus fréquente : {lettre_frequente}")
print(f"Clé estimée : {cle}")

# Déchiffre avec la clé trouvée
texte_dechiffre = dechiffre(texte, cle)
print("\nTexte déchiffré :")
print(texte_dechiffre)







# Pour essayer toutes les clés possibles

def dechiffre(texte, cle):
    resultat = ""
    for c in texte:
        if c.isalpha():
            decal = (ord(c.upper()) - ord('A') - cle) % 26
            resultat += chr(decal + ord('A'))
        else:
            resultat += c
    return resultat

texte = "hello"
print("Essai de toutes les clés possibles :\n")
for cle in range(26):
    texte_dechiffre = dechiffre(texte, cle)
    print(f"Clé {cle:2d} : {texte_dechiffre}")