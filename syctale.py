import tkinter as tk

root = tk.Tk()
root.title("syctale")
root.geometry("300x300")

button1 = tk.Button(root, text="Veuillez ecrire une phrase:", command=lambda: print("") ) 
button1.grid(row=1, column=1, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=2, column=1, pady=10)

def scytale_chiffrer(text, num_rails):
    encrypted_text = [''] * num_rails
    for i in range(len(text)):
        encrypted_text[i % num_rails] += text[i]
    return ''.join(encrypted_text)

def scytale_dechiffrer(encrypted_text, num_rails):
    num_cols = len(encrypted_text) // num_rails
    decrypted_text = [''] * num_cols
    for i in range(len(encrypted_text)):
        decrypted_text[i % num_cols] += encrypted_text[i]
    return ''.join(decrypted_text)

# Exemple d'utilisation
text = "HELLOSCYTALE"
num_rails = 3
encrypted_text = scytale_chiffrer(text, num_rails)
print(f"Texte chiffré : {encrypted_text}")

decrypted_text = scytale_dechiffrer(encrypted_text, num_rails)
print(f"Texte déchiffré : {decrypted_text}")