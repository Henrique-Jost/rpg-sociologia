class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida 
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano > 0:
            alvo.vida -= dano

    def __str__(self) -> str:
        return f"{self.nome} - Vida: {self.vida}"