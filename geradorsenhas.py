import random

tamanho = int( input('Quantos caracteres você deseja que tenha sua senha? '))
if tamanho < 9:
    print ('Insuficiência de caracteres. \nTente novamente.')
    exit()
if tamanho > 15:
    print ('Excesso de caracteres. \nTente novamente.')
    exit()

caracter = str( input('Deseja que tenha caracteres especiais? ')).strip().lower()

especial = ['!', '@', '#', '$', '%', '&', '*', ',', '+', '=']
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
número = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

if caracter == 'sim':
    espalnum = especial + número + alfabeto
    senha = random.choices(espalnum, k=tamanho)
    senhatext = ''.join(senha)
    print ('Sua senha será: {}. ' .format(senhatext))

elif caracter == 'não' or caracter == 'nao':
    alfabeto = alfabeto + número
    senha2 = random.choices(alfabeto, k=tamanho)
    senhatext2 = ''.join(senha2)
    print ('Sua senha será: {}. ' .format(senhatext2))

else:
    print ('Responda apenas com sim ou não.')
    exit()
