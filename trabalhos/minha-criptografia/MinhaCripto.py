import tkinter as tk

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "


# =========================
# CHAVE → NÚMEROS
# =========================
def chave_para_numeros(chave):
    numeros = []

    for c in chave:
        if c in ALFABETO:
            numeros.append(ALFABETO.index(c))

    return numeros


# =========================
# PADDING
# =========================
def adicionar_padding(texto, tamanho_bloco):
    resto = len(texto) % tamanho_bloco

    if resto != 0:
        quantidade = tamanho_bloco - resto
        texto = texto + ("X" * quantidade)

    return texto


def remover_padding(texto):
    return texto.rstrip("X")


# =========================
# VIGENERE DINÂMICO
# =========================
def vigenere(texto, chave_nums, decifrar=False):
    resultado = ""

    for i in range(len(texto)):
        letra = texto[i]

        if letra not in ALFABETO:
            resultado += letra
            continue

        indice_letra = ALFABETO.index(letra)

        indice_chave = i % len(chave_nums)
        valor_chave = chave_nums[indice_chave]

        deslocamento = valor_chave + i

        if decifrar:
            deslocamento = -deslocamento

        novo_indice = (indice_letra + deslocamento) % len(ALFABETO)

        resultado += ALFABETO[novo_indice]

    return resultado


# =========================
# INVERSÃO DE BLOCOS
# =========================
def inverter_blocos(texto, tamanho):
    resultado = ""
    i = 0

    while i < len(texto):
        bloco = texto[i:i+tamanho]
        bloco_invertido = bloco[::-1]
        resultado += bloco_invertido
        i += tamanho

    return resultado


# =========================
# RAIL FENCE
# =========================
def rail_fence(texto, trilhos):
    if trilhos <= 1:
        return texto

    linhas = [""] * trilhos
    linha = 0
    descendo = True

    for c in texto:
        linhas[linha] += c

        if linha == 0:
            descendo = True
        elif linha == trilhos - 1:
            descendo = False

        if descendo:
            linha += 1
        else:
            linha -= 1

    return "".join(linhas)


def desfazer_rail(texto, trilhos):
    if trilhos <= 1:
        return texto

    padrao = list(range(trilhos)) + list(range(trilhos-2, 0, -1))

    indices = []
    for i in range(len(texto)):
        indices.append(padrao[i % len(padrao)])

    contagem = []
    for t in range(trilhos):
        contagem.append(indices.count(t))

    linhas = []
    pos = 0

    for c in contagem:
        linhas.append(list(texto[pos:pos+c]))
        pos += c

    ponteiros = [0] * trilhos
    resultado = ""

    for idx in indices:
        resultado += linhas[idx][ponteiros[idx]]
        ponteiros[idx] += 1

    return resultado


# =========================
# PERMUTAÇÃO
# =========================
def permutar(texto, chave_nums):
    tamanho = len(chave_nums)

    ordem = list(range(tamanho))
    ordem.sort(key=lambda i: chave_nums[i])

    resultado = ""
    i = 0

    while i < len(texto):
        bloco = texto[i:i+tamanho]

        novo = [""] * tamanho

        for j in range(len(bloco)):
            pos = ordem[j]
            novo[j] = bloco[pos]

        resultado += "".join(novo)
        i += tamanho

    return resultado


def desfazer_permutacao(texto, chave_nums):
    tamanho = len(chave_nums)

    ordem = list(range(tamanho))
    ordem.sort(key=lambda i: chave_nums[i])

    resultado = ""
    i = 0

    while i < len(texto):
        bloco = texto[i:i+tamanho]

        novo = [""] * tamanho

        for j in range(len(bloco)):
            pos = ordem[j]
            novo[pos] = bloco[j]

        resultado += "".join(novo)
        i += tamanho

    return resultado


# =========================
# CIFRAR
# =========================
def cifrar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    chave = entrada_chave.get().strip()

    if not chave:
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "Erro: chave vazia")
        return

    chave_nums = chave_para_numeros(chave)

    texto = adicionar_padding(texto, len(chave_nums))

    t1 = vigenere(texto, chave_nums)
    t2 = inverter_blocos(t1, len(chave_nums))

    trilhos = (len(chave_nums) % 5) + 2
    t3 = rail_fence(t2, trilhos)

    t4 = permutar(t3, chave_nums)

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, t4)


# =========================
# DECIFRAR
# =========================
def decifrar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    chave = entrada_chave.get().strip()

    if not chave:
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "Erro: chave vazia")
        return

    chave_nums = chave_para_numeros(chave)

    t1 = desfazer_permutacao(texto, chave_nums)

    trilhos = (len(chave_nums) % 5) + 2
    t2 = desfazer_rail(t1, trilhos)

    t3 = inverter_blocos(t2, len(chave_nums))

    t4 = vigenere(t3, chave_nums, decifrar=True)

    t_final = remover_padding(t4)

    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, t_final)


# =========================
# INTERFACE SIMPLES E CLARA
# =========================
janela = tk.Tk()
janela.title("Criptografia")
janela.geometry("600x450")

tk.Label(janela, text="Texto:").pack()
entrada_texto = tk.Text(janela, height=5, width=60)
entrada_texto.pack()

tk.Label(janela, text="Chave:").pack()
entrada_chave = tk.Entry(janela, width=40)
entrada_chave.pack()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Cifrar", width=15, command=cifrar).grid(row=0, column=0, padx=10)
tk.Button(frame_botoes, text="Decifrar", width=15, command=decifrar).grid(row=0, column=1, padx=10)

tk.Label(janela, text="Resultado:").pack()
resultado = tk.Text(janela, height=5, width=60)
resultado.pack()

janela.mainloop()