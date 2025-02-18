def pesquisa_binaria(lista, item):
    baixo = 0  #----------> 1
    alto = len(lista) - 1 #----------> 1

    while baixo <= alto: #---------> 2
        meio = (baixo + alto) //2 #-------> 3
        chute = lista[meio]
        if chute == item: #------> 4
            return meio
        if chute > item: #-------> 5
            alto = meio - 1
        else: #-------------> 6
            baixo = meio + 1
    return None #---------------> 7

minha_lista = [1, 3, 5, 7, 9] #-----> 8

print (pesquisa_binaria(minha_lista, 3)) # retorna 1  -----> 9

print (pesquisa_binaria(minha_lista, -1)) # retorna "None" -------> 10

#1  baixo e alto acompanham a parte da lista que você está procurando.

#2  enquanto ainda não conseguiu a um único elemento...

#3 ... verifica o elemento central.

#4 acha o item.

#5 chute foi muito alto

#6 chute foi muito baixo 

#7 Item não existe

#8 Lista

#9 as listas começam no indice 0. O próximo endereço tem indice 1.

#10 "None" significa nulo em python. Indica que o elemento não foi encontrado.