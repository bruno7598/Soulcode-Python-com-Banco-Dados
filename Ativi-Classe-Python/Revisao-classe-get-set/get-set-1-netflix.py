class netflix:

#O inicializador __init__ sempre receberá self, e também passaremos outros atributos: nome, email, valor, cpf, data de nascimento
    def __init__(self, nome, email, valor, cpf, data_nascimento):
        try:        
            self.nome = nome
            self.email = email
            self.valor = str(valor)
            self.cpf = str(cpf)
            self.data_nascimento = str(data_nascimento)
        except Exception as e:
            print(str(e))        
        

try:
    #Metodo setter para atribuir um novo valor ao atributo 
    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_valor(self, valor):
        self.valor = valor
    def set_cpf(self, cpf):
        self.cpf = cpf
    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
except Exception as e:
    print(str(e))        


      
try:    
    #Metodo getter para retornar o valor do atributo
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_email(self):
        return self.email
    def get_cpf (self):
        return self.cpf
    def get_data_nascimento(self):
        return self.data_nascimento
except Exception as e:
    print(str(e))           
  

  
if __name__ == "__main__":
    try:
    
        test = netflix("Bruno", "brunomirandamagalhaes@gmail.com", "R$50.00", "118.302.405-98", "06/11/1994")
        print("-="*30)
        a = str(input("Digite o seu nome: "))
        b = str(input("Digite o seu email: "))
        c = input("Digite o seu valor a pagar: ")
        d = input("Digite o seu CPF: ")
        e = input("Digite sua data de nasciment: ")
        test.__init__(a, b, c ,d , e)
        print("-="*30)
    
        print("Seu nome: {} \n"
          "Seu EMAIL: {} \n"
          "O valor a pagar: {} \n"
          "O seu CPF:{} \n"
          "Sua data de nascimento: {} \n".format(test.nome, test.email, test.valor, test.cpf, test.data_nascimento))
    
        
    except Exception as e:
        print(str(e))