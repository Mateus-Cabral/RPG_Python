#  RPG using only built-in libraries in Python
from random import randint
from time import sleep


def action():
    a = input("Ação: ")
    while True:
        if a in "1234":
            b = int(a)
            break
        else:
            print("Por favor, digite uma opção válida")
            a = input("Ação: ")
    return b


# Card change
def random(a):
    a = randint(0, 2)
    return a


# Player's name with user input
def new_name(a):

    a = input('Qual a sua graça? ').strip()
    print('Tem certeza de que quer o nome {}?'.format(a))
    opcao = input('[S/N] ').strip()

    while True:
        if opcao in 'Ss':
            print('Então vamos começar!')
            # print('Fim Menu nome')
            break

        elif opcao in 'Nn':
            print('Então vamos trocar seu nome.')
            a = input('Como deseja ser chamado? ')
            print(f'Tem certeza de que quer o nome {a}?')
            opcao = input('[S/N] ').strip()
        else:
            print('Não entendi, pode digitar novamente? ')
            opcao = input('[S/N] ')
    return a


# Main Menu layout
def main_menu(a, b, c):
    print('RPG 1.0'
          f'\nSaudações, {player[0]}'
          '\n1 Iniciar '
          '\n2 Configuração da música'
          '\n3 Renomear'
          '\n4 Sair')

    a = action()
    if a == 1:
        print('Let the games begin!')
        c = True
    elif a == 2:
        print('Trabalho em progresso, volte em uma futura versão.')
    elif a == 3:
        player[0] = new_name(player[0])
    else:
        print('Obrigado pelo seu tempo!')
        b = True
    sleep(1.5)
    return a, b, c


# Function for the Battle Screen
def battle_menu(nome_inimigo, hp_inimigo, nome_player, hp_player):     
    print('{}HP {:>10}\n\n'.format('[]' * hp_inimigo, nome_inimigo))
    print('{:<10} {}HP'.format(nome_player, '[]' * hp_player))


def prepare_phase(creature, magic, joker):
    magic_used = False
    joker_used = False
    while True:
        print(f"1 Criatura: {creature[0]} / Status: Batalhando")
        print(f"2 Magia: {magic[0]} / Status: Ativo" if magic_used else f"2. Magia: {magic[0]} / Status: Guardar")
        print(f"3 Coringa: {joker[0]} / Status: Ativo" if joker_used else f"3. Coringa: {joker[0]} / Status: Guardar")
        print("4 Continuar para batalha\n")
        print("Digite o número da carta para mais detalhes.")
        resp = int(input("Ação: "))
        if resp == 1:
            print(f"Nome: {creature[0]}"
                  f"\nHP: {creature[1]} | Resistência: {creature[2]}"
                  f"\nDano: {creature[3]} | Velocidade: {creature[4]}")
            print("1 Voltar")
            resp = int(input("Ação: "))

        elif resp == 2:
            print(f"Descrição: {magic[0]}")
            print("Usar essa magia fará com que ela desapareca e seja reposta por outra.")
            print("1 Guardar \n2 Voltar" if magic_used else "1 Usar  \n2 Voltar")
            resp = int(input("Ação: "))
            if resp == 1:
                magic_used = not magic_used

        elif resp == 3:
            print(f"Descrição: {joker[0]}")
            print("Usar esse coringa fará com que ela desapareca e seja reposta por outra.")
            print("1 Guardar \n2 Voltar" if joker_used else "1 Usar  \n2 Voltar")

            resp = int(input("Ação: "))
            if resp == 1:
                joker_used = not joker_used

        elif resp == 4:
            print("Que comece a batalha!")
            sleep(1.5)
            break
    return creature, magic, joker


# Initializing Variables
leave = False
option = 0
card = 0
battle = False
turn = 0


# Creature Card, Name -> HP -> Resistance -> Damage -> Speed
cr1 = ['Mago Elfico', 3, 0, 4, 1]
cr2 = ['Espadachim Bestial', 4, 1, 3, 2]
cr3 = ['Guerreiro Anão', 5, 2, 2, 0]
creatureCards = [cr1, cr2, cr3]


# Magic Card, Description -> Value -> (buff/nerf)_type
cma1 = ['Aumenta o dano em 1', 1, 'buff_atk']
cma2 = ['Aumenta a resistencia em 1', 1, 'buff_def']
cma3 = ['Aumenta o HP em 1', 1, 'buff_hp']
magicCards = [cma1, cma2, cma3]


# Joker Card, Description -> Effect
cj1 = ['Pula o turno', 'Pula_turno']
cj2 = ['Nega a magia do oponente', 'Nega_magia']
cj3 = ['Causa 1 de dano diretamente ao oponente', 'Dano_HP']
jokerCards = [cj1, cj2, cj3]


# Player hp and random cards initialized
# Name -> HP -> Creature Card -> Magic Card -> Joker Card
player = ['', 5, creatureCards[random(card)], magicCards[random(card)], jokerCards[random(card)]]
# Enemy hp and random cards initialized
# Name -> HP -> Creature Card -> Magic Card -> Joker Card
enemy = ['Enemy', 5, creatureCards[random(card)], magicCards[random(card)], jokerCards[random(card)]]
'''print(Cartas_monstro)  #Test
print(Cartas_magia)
print(Cartas_joker)
print(player)
'''

# Starting the game
player[0] = new_name(player[0])

while not leave:
    # print('começo menu principal')
    option, leave, battle = main_menu(option, leave, battle)
    # print('Fim menu principal')
    # print(opcao, sair, batalha)
    if battle:
        # print('Começando batalha')
        # print('Menu de batalha')
        battle_menu(enemy[0], enemy[1], player[0], player[1])
        prepare_phase(player[2], player[3], player[4])


print('Fim')
