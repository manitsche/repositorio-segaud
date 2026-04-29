import requests
import time
import random

NOME = "Marco_Antonio_Nitsche"
URL_BASE = "http://127.0.0.1:8000"

def gerar_baralho():
    naipes = ['O', 'E', 'C', 'P']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f"{v}{n}" for v in valores for n in naipes]

def prever_mao_casa(minhas_cartas, tempo_aprox):
    # janela de busca (em milissegundos)
    for delta in range(-5000, 5000):
        semente = int((tempo_aprox * 1000) + delta)
        random.seed(semente)


        baralho = gerar_baralho()
        random.shuffle(baralho)

        jogador = [baralho.pop(0) for _ in range(9)]

        if jogador == minhas_cartas:
            casa = [baralho.pop(0) for _ in range(9)]
            return casa, semente

    return None, None

def quebrar_banca():
    global betQuebrada

    print(f"[*] Iniciando partida para: {NOME}...")
    tempo_antes = time.time()

    res = requests.get(f"{URL_BASE}/iniciar/{NOME}")
    dados = res.json()

    minhas_cartas = dados["suas_cartas"]
    print(f"[+] Minhas cartas: {minhas_cartas}")

    tempo_depois = time.time()
    tempo_aprox = (tempo_antes + tempo_depois) / 2

    print("[*] Tentando prever a mão da casa...")

    casa_prevista, semente = prever_mao_casa(minhas_cartas, tempo_aprox)

    if casa_prevista:
        print(f"[+] Semente encontrada: {semente}")
        print(f"[+] Mão prevista da casa: {casa_prevista}")

        betQuebrada = casa_prevista

        # Conferindo
        res_final = requests.get(f"{URL_BASE}/conferir_resultado/{NOME}")
        real = res_final.json()["mao_da_casa"]

        print("\n----- RESULTADO -----")
        print(f"Previsto: {casa_prevista}")
        print(f"Real:     {real}")

        if casa_prevista == real:
            print("\nBANCA QUEBRADA!")
        else:
            print("\nAlgo deu errado")

    else:
        print("[-] Não foi possível encontrar a semente")

if __name__ == "__main__":
    quebrar_banca()