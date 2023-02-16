class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome_profissional = nome
        self.__especialidade = especialidade
        self.__sala = sala


    def get_nomep(self):
        return self.__nome_profissional

    def get_sala(self):
        return self.__sala

    def __str__(self):
        return f"Nome: {self.__nome_profissional} - {self.__especialidade} {self.__sala}"



class visitante:
    def __init__(self, nome, documento):
        self.__nome_visitante = nome
        self.__documento = documento


    def get_nomev(self):
        return self.__nome_visitante

class Visita:
    def __init__(self, visitante, profissional, data):
        self.visitante = visitante
        self.profissional = profissional
        self.data = data

    def __str__(self):
        return f"Dr(a).{self.profissional.get_nomep()} - Visitante: {self.visitante.get_nomev()} - Data: {self.data}"



def cadastrar_profissional():
    nome = input("Nome: ")
    especialidade = input("especialidade: ")
    sala = input("Sala: ")
    profissional = Profissional(nome, especialidade, sala)
    lista_profissional.append(profissional)



def localizar_profissional():
    selecionar = input("Digite o nome do profissional: ")
    cont = False
    for Profissional in lista_profissional:
        if selecionar == Profissional.get_nomep():
            cont = True
            print(f"{Profissional.get_nomep()} - sala: {Profissional.get_sala()}")
            break
    if cont == False:
            print("profissional não encontrado")

def cadastrar_visitante():
    nome = input("Nome: ")
    documento = input("documento: ")
    objvisitante = visitante(nome, documento)
    lista_visitante.append(objvisitante)

def registrador_visita():
    print(f"\nVisitantes Cadastrados: ")
    for pos, visitante in enumerate(lista_visitante):
        print(f"{pos+1}. {visitante.get_nomev()}")
    escolha_visitante = input(f"\nDigite o nome do visitante cadastrado: ")
    existe_visitante = False
    for visitante in lista_visitante:
        if escolha_visitante == visitante.get_nomev():
            existe_visitante = True
            print(f"Profissionais Cadastrados: ")
            for pos, profissional in enumerate(lista_profissional):
                print(f"{pos+1}. {profissional.get_nomep()}")
            escolha_profissional = input("Digite o nome do profissional cadastrado: ")
            existe_profissional = False
            for profissional in lista_profissional:
                if escolha_profissional == profissional.get_nomep():
                    existe_profissional = True
                    data = input("Digite a data da visita (dd/mm/aa): ")
                    lista_visita.append(Visita(visitante, profissional, data))
                    print("Visita cadastrada")
            if existe_profissional == False:
                print("Profissional não cadastrado")
    if existe_visitante == False:
        print("Visitante não cadastrado")

def relatorio():
    print("Escolha um profissional: ")
    for pos, profissional in enumerate(lista_profissional):
            print(f"{pos+1}. {profissional.get_nomep()}")
    escolha_profissional = input("Digite o nome do profissional desejado: ")
    print("******* RELATÓRIO PRONTO*******")
    for visitas in lista_visita:
        if visitas.profissional.get_nomep() == escolha_profissional:
            print(visitas)

def menu():
    while True:
        escolha = input(
            """
            1- Cadastrar Profissional
            2- Localizar Profissional
            3- Cadastrar Visitante
            4- Registrar Visita
            5- Relatório de Conferência
            Escolha: """)

        if escolha == "1":
            cadastrar_profissional()
        if escolha == "2":
            localizar_profissional()
        if escolha == "3":
            cadastrar_visitante()
        if escolha == "4":
            registrador_visita()
        if escolha == "5":
            relatorio()

lista_profissional = []
lista_visitante = []
lista_visita = []

menu()


