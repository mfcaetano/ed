
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def set_nome(self, nome):

        self.nome = nome
    
    def get_nome(self):
        return self.nome

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.altura}' 

    def __gt__(self, outro):
        return self.altura > outro.altura
            
class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        Pessoa.__init__(self, nome, idade, altura)
        self.matricula = matricula

    def __str__(self):
        return super().__str__() + f', {self.matricula}'

pessoa_1 = Pessoa("Caetano", 18, 1.76)
pessoa_2 = Pessoa("João", 32, 2.76)

aluno = Aluno("Joazinho", 17, 2.00, 123)
aluno_1 = Aluno("Pedrinho", 22, 2.95, 223)
print(type(aluno))

print(pessoa_1)
print(pessoa_2)

pessoa_1.nome = 2.3
pessoa_1.set_nome(2.3)

print(pessoa_1.get_nome())


if aluno > aluno_1:
    print(f'{aluno} é maior que {aluno_1}')
elif aluno_1 > aluno:
    print(f'{aluno_1} é maior que {aluno}')
