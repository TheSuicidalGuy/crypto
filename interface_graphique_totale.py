import tkinter as tk
from tkinter import font


def open_new_window(action):
    """Ouvre une nouvelle fenêtre en fonction de l'action choisie."""
    new_window = tk.Toplevel(root)
    new_window.title(f"Action : {action}")
    new_window.geometry("400x300")  # Taille de la nouvelle fenêtre

    tk.Label(new_window, text=f"Vous avez choisi de {action}.", font=large_bold_font).pack(pady=50)
    if action == "chiffrer":
        tk.Label(new_window, text="Choisir une méthode de chiffrement : ", font=larger_bold_font).pack(pady=20)

        tk.Button(new_window, text="Code de césar", width=20, height=2, command=lambda: open_method_window("Code de césar")).pack(pady=7)
        tk.Button(new_window, text="Chiffre de Vigenère", width=20, height=2, command=lambda: open_method_window("Chiffre de Vigenère")).pack(pady=7)
        tk.Button(new_window, text="Scytale", width=20, height=2, command=lambda: open_method_window("Scytale")).pack(pady=5)
        tk.Button(new_window, text="Substitution monoalphabétique", width=20, height=2, command=lambda: open_method_window("Substitution monoalphabétique")).pack(pady=7)
    
    elif action == "dechiffrer":
        tk.Label(new_window, text="Choisir une méthode de déchiffrement : ", font=large_bold_font).pack(pady=20)
    
    tk.Button(new_window, text="Fermer", command=new_window.destroy).pack(pady=20)

def open_method_window(method_name):
    """Ouvre une nouvelle fenêtre pour une méthode spécifique."""
    method_window = tk.Toplevel(root)
    method_window.title(f"Méthode : {method_name}")
    method_window.geometry("400x300")

    if method_name == "Code de césar":
        tk.Label(method_window, text="Veuillez ecrire une phrase:").pack(pady=5)
        message_entry = tk.Entry(method_window, width=30)
        message_entry.pack(pady=5)

        tk.Label(method_window, text="Veuiller entrer la clé:").pack(pady=5)
        cle_entry = tk.Entry(method_window, width=10)
        cle_entry.pack(pady=5)
        
        resultat_label = tk.Label(method_window, text="", font=larger_bold_font)
        resultat_label.pack(pady=10)

        def chiffrer_message():
            Messageacrypter = message_entry.get()
            cle = int(cle_entry.get())
            acrypter = Messageacrypter.upper()
            lg = len(acrypter)
            MessageCrypte = ""

            for i in range(lg):
                if acrypter[i] == ' ':
                    MessageCrypte += ' '
                else:
                    asc = ord(acrypter[i]) + cle
                    MessageCrypte += chr(asc + 26 * ((asc < 65) - (asc > 90)))

            resultat_label.config(text=MessageCrypte)

        tk.Button(method_window, text="Chiffrer", command=chiffrer_message).pack(pady=10)
        
    else:
        tk.Label(method_window, text=f"Vous avez sélectionné la méthode : {method_name}", font=large_bold_font).pack(pady=50)
    
    tk.Button(method_window, text="Fermer", command=method_window.destroy).pack(pady=20)

root = tk.Tk()
root.title("Cryptanalyse de chiffrements")
root.attributes("-fullscreen", True)

root.columnconfigure(0, weight=1) 
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)  
root.rowconfigure(0, weight=1)    
root.rowconfigure(1, weight=1)     
root.rowconfigure(2, weight=1)   

large_bold_font = font.Font(family = "Helvetica", size = 24, weight = "bold")
larger_bold_font = font.Font(family="Helvetica", size=20)

tk.Label(root, text="Bonjour, nous avons créé des algorithmes pour chiffrer et déchiffrer des chiffrements anciens.", font = large_bold_font).grid(row=0, column=0, columnspan=3, pady=50, sticky="n")
tk.Label(root, text="Voulez-vous chiffrer ou déchiffrer ?", font=larger_bold_font).grid(row=0, column=0, columnspan=3, pady=150, sticky="n")

button1 = tk.Button(root, text="Chiffrer", width=20, height=2, command=lambda: open_new_window("chiffrer"))
button1.grid(row=0, column=0, pady=10)

button2 = tk.Button(root, text="Dechiffrer", width=20, height=2, command=lambda: open_new_window("dechiffrer"))
button2.grid(row=0, column=2, pady=10)



root.mainloop()