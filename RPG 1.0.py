#  RPG using python built-in libraries
from random import randint
from time import sleep


def menu_principal(a, b, c):  # Menu principal
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



def random(a):  # Randomiza a carta
    a = randint(0, 2)
    return a


def menu_batalha(nome_inimigo, hp_inimigo, nome_player, hp_player):  # Menu de batalha
    print('{}HP {:>10}\n\n\n\n'.format('[]' * hp_inimigo, nome_inimigo))
    print('{:<10} {}HP'.format(nome_player, '[]' * hp_player))


# Inicializando variáveis
sair = False
opcao = 0
card = random(opcao)
batalha = False
turno = 0

# Carta de monstro, Nome -> HP -> Resistencia -> Dano
Cmo1 = ['Mago', 3, 0, 4]
Cmo2 = ['Espadachim', 4, 1, 3]
Cmo3 = ['Tanque', 5, 2, 2]
Cartas_monstro = [Cmo1, Cmo2, Cmo3]

# Carta de magia, Descrição -> Valor -> (buff/nerf)_tipo
Cma1 = ['Aumenta o dano em 1', 1, 'buff_atk']
Cma2 = ['Aumenta a resistencia em 1', 1, 'buff_def']
Cma3 = ['Aumenta o HP em 1', 1, 'buff_hp']
Cartas_magia = [Cma1, Cma2, Cma3]

# Carta Joker, Descrição -> Efeito
Cj1 = ['Pula o turno', 'Pula_turno']
Cj2 = ['Nega a magia do oponente', 'Nega_magia']
Cj3 = ['Causa 1 de dano diretamente ao oponente', 'Dano_HP']
Cartas_joker = [Cj1, Cj2, Cj3]

player = ['', 5, Cartas_monstro[random(card)], Cartas_magia[random(card)], Cartas_joker[random(card)]]  # Player
inimigo = ['Enemy', 5, Cartas_monstro[random(card)], Cartas_magia[random(card)], Cartas_joker[random(card)]]  # Inimigo
'''print(Cartas_monstro)  # Teste dos jogadores
print(Cartas_magia)
print(Cartas_joker)
print(player)
'''

# Pegando nome do jogador
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

# Começo menu
while not sair:
    while True:
        print('começo menu_principal')
        opcao, sair, batalha = menu_principal(opcao, sair, batalha)
        print('Fim menu principal')
        print(opcao, sair, batalha)
        if batalha:
            print('Começando batalha')
            break
    print('Menu de batalha')
    menu_batalha(inimigo[0], inimigo[1], player[0], player[1])
    break

print('Fim')
