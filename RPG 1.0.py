#  RPG using python built-in libraries
from random import randint
from time import sleep


# Main Menu layout
def main_menu(a, b, c):
    print('RPG 1.0'
          '\n1 - Iniciar '
          '2 - Configuração da música'
          '\n3 - Sair')
    a = input('Ação: ')
    while True:
        if a not in '123':
            print('Inválido, digite novamente.')
            a = input('Ação: ')
        else:
            break
    if a == '1':
        print('Let the games begin!')
        c = True
    elif a == '2':
        print('Trabalho em progresso, volte em uma futura versão.')
    else:
        print('Obrigado pelo seu tempo!')
        b = True
    sleep(1.5)
    return a, b, c


# Card change
def random(a):  
    a = randint(0, 2)
    return a


# Function for the Battle Screen
def battle_menu(nome_inimigo, hp_inimigo, nome_player, hp_player):     
    print('{}HP {:>10}\n\n'.format('[]' * hp_inimigo, nome_inimigo))
    print('{:<10} {}HP'.format(nome_player, '[]' * hp_player))


def battle_phase_first(creature, magic, joker):
    magic_used = False
    joker_used = False
    while True:
        print(f"1. Criatura: {creature[0]} / Status: Ativo"
              f"\n2. Magia: {magic[0]} / Status: {magic_used}"
              f"\n3. Coringa: {joker[0]} / Status: {joker_used}"
              f"\n4. Continuar para batalha")
        print("Digite o número da carta para mais detalhes.")
        resp = int(input())
        if resp == 1:
            print(f"Nome: {creature[0]}"
                  f"\nHP: {creature[1]} / Resistência: {creature[2]}"
                  f"\nDano: {creature[3]} / Velocidade: {creature[4]}")
            print("Opções: 1. Voltar")
            resp = int(input())
        elif resp == 4:
            print("Que comece a batalha!")
            sleep(1.5)
            break
    return creature, magic, joker


# Initializing Variables
sair = False
opcao = 0
card = random(opcao)
batalha = False
turno = 0

# Creature Card, Name -> HP -> Resistance -> Damage -> Speed
Cmo1 = ['Mago Elfico', 3, 0, 4, 1]
Cmo2 = ['Espadachim Bestial', 4, 1, 3, 2]
Cmo3 = ['Guerreiro Anão', 5, 2, 2, 0]
Cartas_monstro = [Cmo1, Cmo2, Cmo3]

# Magic Card, Description -> Value -> (buff/nerf)_type
Cma1 = ['Aumenta o dano em 1', 1, 'buff_atk']
Cma2 = ['Aumenta a resistencia em 1', 1, 'buff_def']
Cma3 = ['Aumenta o HP em 1', 1, 'buff_hp']
Cartas_magia = [Cma1, Cma2, Cma3]

# Joker Card, Description -> Effect
Cj1 = ['Pula o turno', 'Pula_turno']
Cj2 = ['Nega a magia do oponente', 'Nega_magia']
Cj3 = ['Causa 1 de dano diretamente ao oponente', 'Dano_HP']
Cartas_joker = [Cj1, Cj2, Cj3]

# Player hp and random cards initialized
player = ['', 5, Cartas_monstro[random(card)], Cartas_magia[random(card)], Cartas_joker[random(card)]]
# Enemy hp and random cards initialized
enemy = ['Enemy', 5, Cartas_monstro[random(card)], Cartas_magia[random(card)], Cartas_joker[random(card)]]  
'''print(Cartas_monstro)  #Test
print(Cartas_magia)
print(Cartas_joker)
print(player)
'''

# Character's name with user input
player[0] = input('Qual sua graça? ').strip()
print('Tem certeza de que quer o nome {}?'.format(player[0]))
opcao = input('[S/N] ').strip()
while True:
    if opcao in 'Ss':
        print('Então vamos começar!')
        print('Fim Menu nome')
        break
    elif opcao in 'Nn':
        print('Então vamos trocar seu nome.')
        player[0] = input('Como deseja ser chamado? ')
        print('Tem certeza de que quer o nome {}?'.format(player[0]))
        opcao = input('[S/N] ').strip()
    else:
        print('Não entendi, pode digitar novamente? ')
        opcao = input('[S/N] ')

# Starting the game
while not sair:
    # print('começo menu principal')
    opcao, sair, batalha = main_menu(opcao, sair, batalha)
    # print('Fim menu principal')
    # print(opcao, sair, batalha)
    if batalha:
        print('Começando batalha')
        print('Menu de batalha')
        battle_menu(enemy[0], enemy[1], player[0], player[1])
        battle_phase_one(player[2], player[3], player[4])


print('Fim')
