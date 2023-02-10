from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('Suas opções:')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# Input do jogador
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 15)
print('COMPUTADOR jogou {}' .format(itens[computador]))
print('JOGADOR jogou {}' .format(itens[jogador]))
print('=-' * 15)
sleep(1)


if computador == 0:
    if jogador == 0:
            print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    elif jogador == 0:
        print('COMPUTADOR VENCE!')
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
