#Exercício 1
#Suponha uma listacom 15 valores inteiros.
# Mostre a soma de todos esses valores,
#média desses valores e quanto valores são
#acima de 10.
valores = []
maior10 = []
soma = 0
i = 0
while i < 14:
    valor = int(input('Digite 15 valores: '))
    if valor>= 10:
        maior10.append(valor)
    valores.append(valor)
    i+=1
i = 0
print('Valores inserido:')
while i < 14:
    soma += valores[i]
    
    i+=1
media = soma / 14
print('\n Entrada de valores :',valores)
print('\nMédia de valores é : ', media)
print('\nValores maiores que 10 :',maior10)

