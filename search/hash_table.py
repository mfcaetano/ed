class keyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'key: {self.key} value:{self.value}'

    def __repr__(self):
        return str(self)

class HashMap:
    def __init__(self, lenght=11):
        self.items = [[] for _ in range(lenght)]
        self.lenght = lenght
        self.elements_cout = 0

    def put(self, key, value):
        hash = self.hash(key)

        for item in self.items[hash]:
            if item.key == key:
                item.value = value
                break
        else:
            self.items[hash].append(keyValue(key, value))
            self.elements_cout += 1

    def get(self, key):
        pass

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        pass

    def hash(self, key):
        return key % self.lenght





hm = HashMap()
hm.put(11, 'numero onze')
hm.put(22, 'numero vinte e dois')
hm.put(9, 'numero nove')

hm[11] = "numero ONZE"

print(hm.get(11))

print('oi')


#v = keyValue(11, 'numero onze')

#print(v)