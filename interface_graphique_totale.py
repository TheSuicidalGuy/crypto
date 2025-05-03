import tkinter as tk
from tkinter import font

def open_new_window(action):
    """Ouvre une nouvelle fenêtre en fonction de l'action choisie."""
    new_window = tk.Toplevel(root)
    new_window.title(f"Action : {action}")
    new_window.geometry("400x300")  # Taille de la nouvelle fenêtre

    if action == "chiffrer":
        tk.Label(root, text="Choisir une méthode de chiffrement :", font=larger_bold_font).pack(pady=20)
    elif action == "dechiffrer":
        tk.Label(new_window, text="Choisir une méthode de déchiffrement.", font=large_bold_font).pack(pady=20)
    
    tk.Label(new_window, text=f"Vous avez choisi de {action}.", font=large_bold_font).pack(pady=50)
    tk.Button(new_window, text="Fermer", command=new_window.destroy).pack(pady=20)

root = tk.Tk()
root.title("Cryptanalyse de chiffrements")
root.attributes("-fullscreen", True)

root.columnconfigure(0, weight=1) 
root.rowconfigure(1, weight=1)
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