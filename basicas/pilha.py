
class Stack:
    def __init__(self):
        self.__items = []

    def pop(self):
        return self.__items.pop()

    def push(self, item):
        self.__items.append(item)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


pilha = Stack()

#pilha.__items.append(1)

if pilha.is_empty():
    print('Pilha Vazia!')
else:
    print('Pilha não vazia!')


for i in range(10):
    pilha.push(i)

print(pilha.peek())

for i in range(10):
    print(pilha.pop())