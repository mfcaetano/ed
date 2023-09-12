class Pessoa:

     def __init__(self,n,i,a):
          self.nome = n
          self.idade = i
          self.altura = a
     
     def __str__(self):
         return self.nome+" , idade: "+str(self.idade)     
     
     def ehMaiorIdade(self):
         if self.idade >=18:
            return True
         return False 
         
     def maior(self,outra):
         if self.altura > outra.altura:
            return True
         return False

class Aluno(Pessoa):

     def __init__(self,n,i,a,m):
         Pessoa.__init__(self,n,i,a)
         self.matricula = m
         
     def getMatricula(self):
         return self.matricula    

class Professor(Pessoa):

     def __init__(self,n,i,a,d):
         Pessoa.__init__(self,n,i,a)
         self.disciplina = d
         
         
eduardo = Aluno("Eduardo",42,1.76,10000)
pedro = Professor ("Pedro",17, 1.80,"ED")
#l = [eduardo,pedro]
print(eduardo.nome,"é maior de idade: ",eduardo.ehMaiorIdade())
print("Pedro é maior de idade: ",pedro.ehMaiorIdade())
print("Eduardo é maior: ",eduardo.maior(pedro))
print("Eduardo possui matricula: ",eduardo.getMatricula())
print("Pedro disciplina: ",pedro.disciplina)











