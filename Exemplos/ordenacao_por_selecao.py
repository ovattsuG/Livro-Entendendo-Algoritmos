def buscarMenor(lista):
    menor = lista[0] #---------------------> 1
    for i in range(1, len(lista)): #---------> 2
        if lista[i] < menor: #--------------> 3
            menor = lista[i] #---------------> 4
    return menor #---------------------------> 5
def ordenacao_por_selecao(lista): #-----------> 6
    lista_ordenada = [] #--------------------> 7
    for i in range(len(lista)): #-------------> 8
        menor = buscarMenor(lista) #-----------> 9
        lista_ordenada.append(menor) #---------> 10
        lista.remove(menor) #-----------------> 11
    return lista_ordenada #-------------------> 12

minha_lista = [5, 3, 6, 2, 10] #---------> 13
print(ordenacao_por_selecao(minha_lista)) #-----> 14


#1  menor é o primeiro elemento da lista.
#2  percorre a lista a partir do segundo elemento.
#3  se o elemento atual for menor que o menor, atualiza o menor.
#4  atualiza o menor.
#5  retorna o menor elemento da lista.
#6  função que ordena a lista.
#7  cria uma lista vazia para armazenar os elementos ordenados.
#8  percorre a lista original.
#9  busca o menor elemento da lista original.
#10  adiciona o menor elemento à lista ordenada.
#11  remove o menor elemento da lista original.
#12  retorna a lista ordenada.
#13  lista a ser ordenada.
#14  imprime a lista ordenada.
# Saída: [2, 3, 5, 6, 10]