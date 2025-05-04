import tkinter as tk

def transformer_en_majuscules():
    texte = entree.get("1.0", tk.END)     # lit le texte entré par l'utilisateur
    texte_maj = texte.upper()             # transforme le texte en MAJUSCULES
    sortie.delete("1.0", tk.END)          # vide la zone de sortie (ancienne valeur)
    sortie.insert(tk.END, texte_maj)      # écrit le texte majuscule dans la sortie

fenetre = tk.Tk()
fenetre.title("Transforme en MAJUSCULES")

label1 = tk.Label(fenetre, text="Écris ton texte :")
label1.pack()

entree = tk.Text(fenetre, height=4, width=50)
entree.pack()

bouton = tk.Button(fenetre, text="Mettre en majuscules", command=transformer_en_majuscules)
bouton.pack()

label2 = tk.Label(fenetre, text="Résultat :")
label2.pack()

sortie = tk.Text(fenetre, height=4, width=50)
sortie.pack()

fenetre.mainloop()