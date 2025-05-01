from collections import Counter

def analyse_frequence(texte):
    texte = texte.upper()
    lettres = [c for c in texte if c.isalpha()]
    return Counter(lettres)

def construire_substitution(freq_texte, freq_fr="EASNTIRULODCMPVQGBHFJZXWY"):
    # Associe chaque lettre du texte à une lettre fréquente française
    lettres_texte_triees = [l for l, _ in freq_texte.most_common()]
    mapping = {}
    for i, lettre in enumerate(lettres_texte_triees):
        if i < len(freq_fr):
            mapping[lettre] = freq_fr[i]
        else:
            mapping[lettre] = '?'  # si plus de lettres que dans freq_fr
    return mapping

def dechiffre_substitution(texte, mapping):
    resultat = ""
    for c in texte:
        if c.isalpha():
            maj = c.isupper()
            lettre = c.upper()
            subst = mapping.get(lettre, '?')
            resultat += subst if maj else subst.lower()
        else:
            resultat += c
    return resultat

# Exemple de texte chiffré (clé de César -3 : A→X, B→Y, etc.)
texte = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

# Étape 1 : analyse de fréquence
freq = analyse_frequence(texte)

# Étape 2 : création d’un mapping de substitution basé sur la fréquence
mapping = construire_substitution(freq)

# Étape 3 : tentative de déchiffrement
texte_dechiffre = dechiffre_substitution(texte, mapping)

# Résultat
print("Mapping estimé :", mapping)
print("Texte déchiffré :", texte_dechiffre)