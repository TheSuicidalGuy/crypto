def num(c):
    return ord(c) - ord('A')

def lettre(n):
    return chr(n + ord('A'))

def chiffrement(message) :
    chiffre = ""
    for c in message : # c comme ...
        x = (num(c) + 3) % 26
        chiffre = chiffre + lettre (x)
    return chiffre
