import random

# Arcanos Maiores
arcanos_maiores = [
    "O Mago",
    "A Sacerdotisa",
    "A Imperatriz",
    "O Imperador",
    "O Hierofante",
    "Os Amantes",
    "O Carro",
    "A Força",
    "O Eremita",
    "A Roda da Fortuna",
    "A Justiça",
    "O Enforcado",
    "A Morte",
    "A Temperança",
    "O Diabo",
    "A Torre",
    "A Estrela",
    "A Lua",
    "O Sol",
    "O Julgamento",
    "O Mundo"
]

# Arcanos Menores
naipes = ["Paus", "Copas", "Espadas", "Ouros"]
valores = [
    "Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Pajem", "Cavaleiro", "Rainha", "Rei"
]

arcanos_menores = [f"{valor} de {naipe}" for naipe in naipes for valor in valores]

# Todos os arcanos juntos
tarot_completo = arcanos_maiores + arcanos_menores


nivel_caos = 0.30 #pode ser mudado de acordo com a tiragem, quanto maior o nivel de caos, maior a probabilidade da carta vier invertida.


def gerar_cartas():
    def escolher_carta():
        carta = random.choice(tarot_completo)
        return [carta]  # mantém no formato de lista

    carta1 = escolher_carta()
    carta2 = escolher_carta()
    carta3 = escolher_carta()

    print(carta1)
    print(carta2)
    print(carta3)



def gerar_carta_sim_ou_nao(): #gera apenas para uma tiragem de cartas de sim, ou não
    def escolher_carta():
        carta = random.choice(tarot_completo)
        return [carta] 

    carta1 = escolher_carta()

    print(carta1)

