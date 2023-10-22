from personagem.jogador import Jogador
from personagem.inimigo import Inimigo

jogador = Jogador("Herói", 100, 15, 10, ["Espada", "Poção"])
inimigo = Inimigo("Dragão", 200, 20, 5)

# Loop principal do jogo
while jogador.vida > 0:
    print(jogador)
    print(inimigo)
    acao = input("O que você deseja fazer? (atacar/inventário/sair): ")

    # Resto do código do jogo...
