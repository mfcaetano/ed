class Vertex:
    def __init__(self, key):
        self.__id = key
        self.__connect_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.__connect_to[nbr] = weight

        # abaixo a forma de cadastro de mais de uma aresta
        # para um mesmo vertice destino
        #self.__connect_to.setdefault(nbr, []).append(weight)
        

    def del_neighbor(self, nbr):
        if nbr in self.__connect_to:
            return self.__connect_to.pop(nbr)
        
            #del self.__connect_to[nbr]

    def get_connections(self):
        return self.__connect_to.keys()

    def get_id(self):
        return self.__id

    def set_id(self, key):
        self.__id = key

    def get_weight(self, nbr):
        return self.__connect_to[nbr]

    def __str__(self):
        return f'{self.__id} connect_to {[x.get_id() for x in self.__connect_to]}'
    
class Graph:
    def __init__(self):
        self.__vert_list = {}
        self.__num_vert = 0

    def add_vertex(self, key):
        self.__vert_list[key] = Vertex(key)
        self.__num_vert += 1

    def del_vertex(self, key):
        pass

    def get_vertex(self, key):
        if key in self.__vert_list:
            return self.__vert_list[key]

    def add_edge(self, src, dst, cost=0):
        if src not in self.__vert_list:
            self.add_vertex(src)
        if dst not in self.__vert_list:
            self.add_vertex(dst)

        self.get_vertex(src).add_neighbor(self.get_vertex(dst), cost)


    def get_vertices(self):
        return self.__vert_list.values()

    def __contains__(self, key):
        return key in self.__vert_list.values()
        

    def __iter__(self):
        return iter(self.__vert_list.values())






g = Graph()

g.add_vertex('V0')
g.add_vertex('V1')
g.add_vertex('V2')
g.add_vertex('V3')
g.add_vertex('V4')
g.add_vertex('V5')
g.add_vertex('V6')

g.add_edge('V0', 'V1', 5)
g.add_edge('V0', 'V5', 2)
g.add_edge('V1', 'V2', 4)
g.add_edge('V2', 'V3', 9)
g.add_edge('V3', 'V5', 3)
g.add_edge('V3', 'V4', 7)
g.add_edge('V4', 'V0', 1)
g.add_edge('V5', 'V2', 1)
g.add_edge('V5', 'V4', 8)        


v1 = g.get_vertex('V1')
#v2 = Vertex('V2')

#v1.add_neighbor(v2, 4)

if v1 in g:
    print('ESTÁ')
else:
    print('Não está cadastrado')


for i in g:
    print(i)

#print(v1.del_neighbor(v2))
#print(v1.del_neighbor(v2))

g.del_vertex('V1')

#print(v1.get_connections())

print(g.get_vertices())