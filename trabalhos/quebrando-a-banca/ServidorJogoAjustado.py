from fastapi import FastAPI, HTTPException
import random
import time
import secrets

app = FastAPI()

# Banco de dados em memória para gerenciar as sessões 
db_sessoes = {}

def obter_semente():
    return int(time.time() * 1000)

@app.get("/iniciar/{nome_jogador}")
def iniciar(nome_jogador: str):
    # Identifica se o jogador já tinha um jogo e avisa sobre o reinício
    aviso = None
    if nome_jogador in db_sessoes:
        aviso = f"Jogo reiniciado para o jogador {nome_jogador}."
      

    semente = obter_semente()
    random.seed(semente)
    
    # Estrutura do Baralho Padrão 
    naipes = ['O', 'E', 'C', 'P'] # O(uro)  E(spadas) C(opa) P(aus)
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [f"{v}{n}" for v in valores for n in naipes]
    
    # Embaralhamento que não é mais determinístico
    secrets.SystemRandom().shuffle(baralho)
    
    # Distribuição: 9 cartas para o jogador 
    # E 9 cartas ocultas para a casa 9
    mao_jogador = [baralho.pop(0) for _ in range(9)]
    mao_casa = [baralho.pop(0) for _ in range(9)]
    
    # Salva o estado da partida do jogador
    db_sessoes[nome_jogador] = {
        "jogador": mao_jogador,
        "casa": mao_casa,
        "ativa": True
    }
    
    return {
        "status": aviso or "Partida Iniciada",
        "jogador": nome_jogador,
        "suas_cartas": mao_jogador
    }
    
@app.get("/conferir_resultado/{nome_jogador}")
def finalizar(nome_jogador: str):
    if nome_jogador not in db_sessoes:
        raise HTTPException(status_code=404, detail="Jogador não encontrado. Inicie um jogo primeiro.")
    
    # Recupera a mão da casa e finaliza a partida
    resultado = db_sessoes[nome_jogador]["casa"]
    del db_sessoes[nome_jogador] # Finaliza a sessão
    
    return {
        "mensagem": f"Partida de {nome_jogador} finalizada.",
        "mao_da_casa": resultado
    }