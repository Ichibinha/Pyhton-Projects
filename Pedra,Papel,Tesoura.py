from random import randint

r = 0

print("Bem vindo ao jogo Pedra, Papel e Tesoura")

tent = str(input("Digite a sua jogada.\n"))


list1 = ['Pedra', 'Papel', 'Tesoura']
list2 = [0, 1, 2]

while tent != list1[r]:
    r = r + 1


aleat = randint(0,2)

print( list1[aleat])
#print(r, tent)

if aleat == r+1 or aleat == r-2:
    print('Você perdeu :( ')
    
elif aleat == r:
    print("Empatamos '-' ")
    
    
else:
    print('Você ganhou!!!!!!!')




    