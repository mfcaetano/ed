def busca_sequencial(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found
 
def busca_binaria_iterativa(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found

def busca_binaria_recursiva_1(alist, item):

    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return busca_binaria_recursiva_1(alist[:midpoint], item)
        else:
            return busca_binaria_recursiva_1(alist[midpoint+1:], item)

def busca_binaria_recursiva_2(alist, item, inf, sup):
    if sup <= inf:
        return False

    midpoint = (inf + sup) // 2
    if alist[midpoint] > item:
        return busca_binaria_recursiva_2(alist, item, inf, midpoint)
    if alist[midpoint] < item:
        return busca_binaria_recursiva_2(alist, item, midpoint + 1, sup)

    return True    





lista = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]

print(busca_sequencial(lista, 44))
print(busca_sequencial(lista, 40))

print(busca_binaria_iterativa(lista, 44))
print(busca_binaria_iterativa(lista, 40))

print(busca_binaria_recursiva_1(lista, 44))
print(busca_binaria_recursiva_1(lista, 40))

print(busca_binaria_recursiva_2(lista, 44, 0, len(lista)))
print(busca_binaria_recursiva_2(lista, 40, 0, len(lista)))