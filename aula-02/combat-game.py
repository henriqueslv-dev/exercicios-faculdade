import random
tank_vida = 2000
tank_resistencia_fisica = 20
tank_resistencia_fogo = 20
tank_resistencia_raio = 5

atacante_dano_fisico = 100
atacante_dano_fogo = 150
atacante_dano_raio = 500

atacante_vida = 1000

atacante_resistencia_fisico = 200
atacante_resistencia_fogo = 150
atacante_resistencia_pedra = 150

tank_ataque_soco = 300
tank_ataque_fogo = 300
tank_ataque_espada = 300

#_______________________________________________________________________________________________________________________

print("Digite 1 para fisico 2 para fogo 3 para raio")

while tank_vida > 0 or atacante_vida > 0:
    escolha_do_ataque = int(input("escolha seu ataque: "))

    if escolha_do_ataque == 1:
        tank_vida = tank_vida - (atacante_dano_fisico - tank_resistencia_fisica)
        print("Atacante usou dano fisico")

    elif escolha_do_ataque == 2:
        tank_vida = tank_vida - (atacante_dano_fogo - tank_resistencia_fogo)
        print("Atacante usou dano fogo")

    elif escolha_do_ataque == 3:
        tank_vida = tank_vida - (atacante_dano_raio - tank_resistencia_raio)
        print("atacante usou raio")
    else:
        print("escolha inválida")
    escolha_do_tank = random.randint(1, 3)

    if escolha_do_tank == 1:
        print("tank atacou com soco")
        atacante_vida = atacante_vida - (tank_ataque_soco - atacante_resistencia_fisico)

    elif escolha_do_tank == 2:
        print("tank atacou com fogo")
        atacante_vida = atacante_vida - (tank_ataque_fogo - atacante_resistencia_fogo)

    else:
        print("tank atacou com espada")
        atacante_vida = atacante_vida - (tank_ataque_espada - atacante_resistencia_pedra)

    print("vida do atacante", atacante_vida)
    print("vida do tank",tank_vida)


    if tank_vida <= 0:
        print("tank abatido")

    else:
        print("atacante abatido")

