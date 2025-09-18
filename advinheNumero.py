import random

usuarioNumero = int ( input ( 'Digite um valor de 1 a 20: '))

def advinheNumero (usuarioNumero):
    numeroAleatorio = random.randint (1,20)

    nomeUsuario = input ('Qual o seu nome? ')
    print(f'---- Seja BEM-VINDO {nomeUsuario}---- \nVamos jogar')
    
