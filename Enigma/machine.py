import tkinter as tk

def enigma_machine():
    """Codez avec la machine Enigma"""
    import enigma
    import argparse
    import re

    machine = enigma.Enigma(["I", "II", "III"], [0, 15, 3], [3, 25, 12], "B", "AB CD EF GH IJ KL MN OP")

    plaintext = message_entry.get()
    ciphertext = machine.encrypt(plaintext)

    resultat_label.config(text=f"Resultat : {ciphertext}")

root = tk.Tk()
root.title("Machine Enigma")
root.geometry("600x400")

# Widgets pour entrer le texte
tk.Label(root, text="Veuillez écrire une phrase :").grid(row=0, column=0, pady=10)
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=0, column=1, pady=10)

# Bouton pour chiffrer
button1 = tk.Button(root, text="Chiffrer", command=enigma_machine)
button1.grid(row=2, column=0, pady=10)

# Label pour afficher le résultat
resultat_label = tk.Label(root, text="", justify="left", wraplength=500)
resultat_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()