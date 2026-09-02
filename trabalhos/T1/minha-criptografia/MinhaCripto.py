import tkinter as tk
from tkinter import messagebox
import random
import string

ALFABETO = string.ascii_uppercase + string.ascii_lowercase + " "
TAM = len(ALFABETO)

seed = random.randint(5, 50)
shift_inicial = random.randint(0, TAM - 1)

def validar_texto(texto):
    for ch in texto:
        if ch not in ALFABETO:
            messagebox.showerror("Erro", "Texto contém caracteres inválidos! Somente letras do alfabeto (A-Z, a-z) e espaços são permitidos.")
            return False
    return True

def cifrar(texto):
    desloc = shift_inicial
    ultimo = 0
    resultado = []

    for pos, ch in enumerate(texto):
        idx = ALFABETO.index(ch)
        novo = (idx + desloc + ultimo + seed * (pos + 1)) % TAM
        resultado.append(ALFABETO[novo])
        ultimo = novo
        desloc = novo

    return ''.join(resultado)

def decifrar(texto):
    desloc = shift_inicial
    ultimo = 0
    resultado = []

    for pos, ch in enumerate(texto):
        idx = ALFABETO.index(ch)
        original = (idx - desloc - ultimo - seed * (pos + 1)) % TAM
        resultado.append(ALFABETO[original])
        ultimo = idx
        desloc = idx

    return ''.join(resultado)

def encrypt():
    texto = entry_text.get().strip()

    if not texto:
        messagebox.showwarning("Aviso", "Digite um texto primeiro!")
        return

    if not validar_texto(texto):
        return

    encrypted_text.set(cifrar(texto))
    decrypted_text.set("")

def decrypt():
    texto = entry_text.get().strip()

    if not texto:
        messagebox.showwarning("Aviso", "Digite um texto primeiro!")
        return

    if not validar_texto(texto):
        return

    decrypted_text.set(decifrar(texto))

root = tk.Tk()
root.title("Minha Criptografia")

tk.Label(root, text="Texto:").grid(row=0, column=0, padx=10, pady=5)

entry_text = tk.Entry(root, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Criptografar", command=encrypt)\
    .grid(row=2, column=0, padx=10, pady=5)

tk.Button(root, text="Descriptografar", command=decrypt)\
    .grid(row=2, column=1, padx=10, pady=5)

encrypted_text = tk.StringVar()
decrypted_text = tk.StringVar()

tk.Label(root, text="Texto Criptografado:")\
    .grid(row=3, column=0, padx=10, pady=5)

tk.Entry(root, textvariable=encrypted_text, width=40, state='readonly')\
.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Texto Descriptografado:")\
    .grid(row=4, column=0, padx=10, pady=5)

tk.Entry(root, textvariable=decrypted_text, width=40, state='readonly')\
.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()