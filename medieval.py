import

print("bem vindo ao jogo de luta medieval")
print("voce é um guerreiro enfrentando um inimigo")

vida_jogador = 100
vida_inimigo = 100
dano_base = 15

while vida_jogador > 0 and vida_inimigo > 0:
    print(f"\n sua vida é {vida_jogador} e do inimigo é {vida_inimigo}")
    input("pressione enter para atacar")

    dano_jogador = random.randint(dano_base - 5, dano_base + 5)
    vida_inimigo -= dano_jogador
    print(f"voce causou {dano_jogador} de dano")


    dano_inimigo = random.randint(dano_base - 5, dano_base + 5)
    vida_inimigo -= dano_inimigo
    print(f"voce causou {dano_inimigo} de dano ao jogador")

    if vida_inimigo


    