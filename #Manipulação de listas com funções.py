#Manipulação de listas com funções

'''
1) Função para obter o tamanho da lista- tamanho_lista()
2) Função para criar uma lista - criar_lista()
3) Função para imprimir a lista - imprimir_lista()
'''

def tamanho_lista():
    print('*-TAMANHO DA LISTA -*')
    print('------------------')
    t = int(input('Tamanho: '))
    return t

def criar_lista(t):
    print('*-CRIAR UMA LISTA -*')
    print('------------------')
    lista = [] #lista vazia
    i=0
    while i < t:
        n = int(input('Numero: '))
        lista.append(n)
        i +=1
    return lista

def imprimir(lista):
    print('*-IMPRIMIR UMA LISTA -*')
    print('------------------')
    for i in lista:
        print(f'Elemento: {i}')

#Programa principal
t = tamanho_lista()
lista = criar_lista(t)
imprimir(lista)
