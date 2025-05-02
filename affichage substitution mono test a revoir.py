import tkinter as tk
from collections import Counter

# Fonctions existantes
def analyse_frequence(texte):
    texte = texte.upper()
    lettres = [c for c in texte if c.isalpha()]
    return Counter(lettres)

def construire_substitution(freq_texte, freq_fr="EASNTIRULODCMPVQGBHFJZXWY"):
    lettres_texte_triees = [l for l, _ in freq_texte.most_common()]
    mapping = {}
    for i, lettre in enumerate(lettres_texte_triees):
        if i < len(freq_fr):
            mapping[lettre] = freq_fr[i]
        else:
            mapping[lettre] = '?'
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

# Interface Tkinter
def dechiffrer():
    texte = entree.get("1.0", tk.END)
    freq = analyse_frequence(texte)
    mapping = construire_substitution(freq)
    texte_dechiffre = dechiffre_substitution(texte, mapping)

    # Affichage
    resultat_mapping.set(str(mapping))
    sortie.delete("1.0", tk.END)
    sortie.insert(tk.END, texte_dechiffre)

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Déchiffreur par fréquence")

# Champ d'entrée
tk.Label(fenetre, text="Texte chiffré :").pack()
entree = tk.Text(fenetre, height=5, width=60)
entree.pack()

# Bouton
tk.Button(fenetre, text="Déchiffrer", command=dechiffrer).pack(pady=5)

# Mapping affiché
resultat_mapping = tk.StringVar()
tk.Label(fenetre, text="Mapping estimé :").pack()
tk.Label(fenetre, textvariable=resultat_mapping).pack()

# Sortie
tk.Label(fenetre, text="Texte déchiffré :").pack()
sortie = tk.Text(fenetre, height=5, width=60)
sortie.pack()

# Lancement de l'interface
fenetre.mainloop()