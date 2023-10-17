
class Item:
    def __init__(self, dado, prox=None):
        self.dado = dado
        self.prox = prox

def len_lista(lista):
    if lista:
        return 1 + len_lista(lista.prox)
    
    return 0


def insere_inicio(item, lista):
    if lista:
        item.prox = lista
    
    return item
    

def insere_final(item, lista):
    if not lista:
        return item
    
    lista.prox = insere_final(item, lista.prox)
    return lista

def insere(item, lista, pos):
    if pos == 0:
        return insere_inicio(item, lista)
    
    if lista:
        lista.prox = insere(item, lista.prox, pos-1 )
        return lista

    raise ValueError('posição inválida')




def insere_ordenado(item, lista):
    pass




lista = None 
lista = insere_inicio(Item(2), lista)
lista = insere_inicio(Item(3), lista)
lista = insere(Item(10), lista, 0)
lista = insere(Item(200), lista, 1)
lista = insere(Item(1000), lista, 100)

print(len_lista(lista))
insere
print('oi')