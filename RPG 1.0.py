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
def random():
    a = randint(0, 2)
    return a


def creature_card_change(card):
    card = creatureCards[random()]
    return card


def magic_card_change(card):
    card = magicCards[random()]
    return card


def joker_card_change(card):
    card = jokerCards[random()]
    return card


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


def enemy_prepare_phase(creature, magic, joker):
    a = randint(0, 1)
    if a == 0:
        magic_used = True
        joker_used = False
    elif a == 1:
        magic_used = False
        joker_used = True
    else:
        magic_used = True
        joker_used = True
    return magic_used, joker_used


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
            sleep(0.75)
            break
    return magic_used, joker_used


def battle(player_actions, enemy_actions):
    skip = False
    enemy_win = False
    player_win = False

    # Joker interactions
    if player_actions[1]:
        if player['joker'][2] == 'pula_turno':
            skip = True
            nome = player['nome']
            print(f'Você gastou seu coringa para evitar esse turno!')
        if player['joker'][2] == 'nega_magia':
            enemy_actions[0] = False
            print(f'Você negou a magia do oponente!')
        if player['joker'][2] == 'dano_hp':
            enemy['hp'] -= 1
            print(f'Isso deve ter doído... Seu oponente perdeu 1 ponto de vida!')
        else:
            print(f'Você decidiu guardar seu coringa.')

    print("Esperando oponente...")
    sleep(1)

    if not skip:
        if enemy_actions[1]:
            if enemy['joker'][2] == 'pula_turno':
                skip = True
                print(f'O jogador {enemy["nome"]} gastou seu coringa para evitar esse turno!')
            if enemy['joker'][2] == 'nega_magia':
                player_actions[0] = False
                print(f'O jogador {enemy["nome"]} gastou seu coringa para negar sua magia!')
            if enemy['joker'][2] == 'dano_hp':
                player['hp'] -= 1
                print(f'O jogador {enemy["nome"]} gastou seu coringa para te dar 1 de dano. Espero que não tenha '
                      f'doído... ')
        else:
            print(f'O jogador {enemy["nome"]} decidiu guardar seu coringa.')

    if not skip:
        # Magics interactions
        if player_actions[0]:
            if player['magic'][2] == 'buff_atk':
                player['creature'][3] += 1
                print(f'{player["creature"][0]} se sente inspirado. Seu ataque foi aprimorado em 1 ponto')
            if player['magic'][2] == 'buff_def':
                player['creature'][2] += 1
                print(f'{player["creature"][0]} se sente confiante. Sua defesa foi aprimorada em 1 ponto')
            if player['magic'][2] == 'buff_hp':
                player['creature'][1] += 1
                print(f'{player["creature"][0]} se sente revigorado. Sua vida foi aprimorada em 1 ponto')

        if enemy_actions[0]:
            if enemy['magic'][2] == 'buff_atk':
                enemy['creature'][3] += 1
                print(f'O {enemy["creature"][0]} do oponente se preparou para um ataque. Seu ataque foi aprimorado em '
                      f'1 ponto')
            if enemy['magic'][2] == 'buff_def':
                enemy['creature'][2] += 1
                print(f'O {enemy["creature"][0]} do oponente sente confiante. Sua defesa foi aprimorada em 1 ponto')
            if enemy['magic'][2] == 'buff_hp':
                enemy['creature'][1] += 1
                print(f'O {enemy["creature"][0]} do oponente foi curado. Sua vida foi aprimorada em 1 ponto')

        # Battle interaction
        if player['creature'][4] > enemy['creature'][4]:
            print(f'{player["creature"][0]} toma a dianteira e se prepara para atacar!')
            print(f'{enemy["creature"][0]} tomou {player["creature"][3]} de dano...', end=' ')
            if enemy["creature"][1] == 0:
                print(f"e não sobreviveu... Vitória para {player['creature'][0]}")
                player_win = True
            else:
                print(f'e sobreviveu com {enemy["creature"][1]} pontos de vida.')
                print(f'Agora {enemy["creature"][0]} se prepara para atacar!')
                print(f'{player["creature"][0]} tomou {enemy["creature"][3]} de dano...', end=' ')
                if player["creature"][1] == 0:
                    print(f"e não sobreviveu... Vitória para {enemy['creature'][0]}")
                    enemy_win = True

        elif player['creature'][4] < enemy['creature'][4]:
            print(f'{enemy["creature"][0]} toma a dianteira e se prepara para atacar!')
            print(f'{player["creature"][0]} tomou {enemy["creature"][3]} de dano...', end=' ')
            if enemy["creature"][1] == 0:
                print(f"e não sobreviveu... Vitória para {enemy['creature'][0]}")
                player_win = True
            else:
                print(f'e sobreviveu com {player["creature"][1]} pontos de vida.')
                print(f'Agora {player["creature"][0]} se prepara para atacar!')
                print(f'{enemy["creature"][0]} tomou {player["creature"][3]} de dano...', end=' ')
                if enemy["creature"][1] == 0:
                    print(f"e não sobreviveu... Vitória para {player['creature'][0]}")
                    enemy_win = True

        if player_win:
            print(f'Parabéns! Você ganhou a batalha e seu oponente tomou 1 de dano')
            enemy["hp"] -= 1
        elif enemy_win:
            print(f'Mais sorte da próxima vez... O {enemy["nome"]} ganhou dessa vez.')
            print(f'Você tomou 1 de dano.')
            player["hp"] -= 1
        else:
            print("Ninguém morreu dessa vez, se prepare para a próxima batalha!")

        if player_action[0]:
            player_action[0] = not player_action[0]
            player["magic"] = magic_card_change(player["magic"])
        if player_action[1]:
            player_action[1] = not player_action[1]
            player["joker"] = joker_card_change(enemy["joker"])
        if enemy_action[0]:
            player_action[0] = not player_action[0]
            player["magic"] = magic_card_change(enemy["magic"])
        if enemy_action[1]:
            enemy_action[1] = not player_action[1]
            enemy["joker"] = joker_card_change(enemy["joker"])


# Initializing Variables
leave = False
option = 0
# card = 0
battle_ = False
turn = 0

# Checks if the magic or Joker Card is being used
# 0 - Magic | 1 - Joker
player_action = [False, False]
enemy_action = [False, False]


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
cj1 = ['Pula o turno', 'pula_turno']
cj2 = ['Nega a magia do oponente', 'nega_magia']
cj3 = ['Causa 1 de dano diretamente ao oponente', 'dano_hp']
jokerCards = [cj1, cj2, cj3]


# Player hp and random cards initialized
# Name -> HP -> Creature Card -> Magic Card -> Joker Card
player = {
    "nome": '',
    "hp": 5,
    "creature": creatureCards[random()],
    "magic": magicCards[random()],
    "joker": jokerCards[random()]
}

enemy = {
    "nome": 'Enemy',
    "hp": 5,
    "creature": creatureCards[random()],
    "magic": magicCards[random()],
    "joker": jokerCards[random()]
}

# player = ['', 5, creatureCards[random(card)], magicCards[random(card)], jokerCards[random(card)]]
# Enemy hp and random cards initialized
# Name -> HP -> Creature Card -> Magic Card -> Joker Card
# enemy = ['Enemy', 5, creatureCards[random(card)], magicCards[random(card)], jokerCards[random(card)]]


# Starting the game
player[0] = new_name(player[0])

while not leave:
    # print('começo menu principal')
    option, leave, battle = main_menu(option, leave, battle)
    # print('Fim menu principal')
    # print(opcao, sair, batalha)
    if battle_:
        # print('Começando batalha')
        # print('Menu de batalha')
        battle_menu(enemy['nome'], enemy['hp'], player['nome'], player['hp'])
        player_action[0], player_action[1] = prepare_phase(player['creature'], player['magic'], player['joker'])
        enemy_action[0], enemy_action[1] = enemy_prepare_phase(enemy['creature'], enemy['magic'], player['joker'])
        battle(player_action, enemy_action)

print('Fim')
