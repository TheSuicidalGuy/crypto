def dechiffre_scytale(texte, cle):
    texte = texte.upper()  #met en majuscules
    longueur = len(texte)
    colonnes = (longueur + cle - 1) // cle  # Nombre de colonnes (arrondi supérieur)
    lignes = cle  # Nombre de lignes dans la grille
    grille = [''] * lignes  # Grille pour stocker les lignes

    index = 0
    for col in range(colonnes):  # Parcourt chaque colonne
        for row in range(lignes):  # Parcourt chaque ligne
            if index < longueur:
                grille[row] += texte[index]
                index += 1

    return ''.join(grille)  # Concatène les lignes pour reconstruire le texte


# Exemple
#texte_chiffre = "HLOEORLWD"  # HELLOWORLD transposé avec clé 3
texte_chiffre = "HLOEORLWD"
cle = 3

texte_dechiffre = dechiffre_scytale(texte_chiffre, cle)
print("Texte déchiffré :", texte_dechiffre)

