# Projeto-Consultório
Projeto realizado durante o segundo semestre de ADS.
Enunciado:
Tarefa 1
Competências avaliadas:
Saber interpretar o que foi solicitado
Desenvolver uma solução viável para o problema
Saber utilizar classes e objetos

'''
Faça um algoritmo que controle o acesso de pessoas a
um estabelecimento comercial.

Para isso você deverá utilizar as seguintes classes:

Crie uma classe Profissional com os atributos:
        - nome
        - especialidade
        - sala
    Todos atributos devem ser privados e string.

crie uma classe Visitante com os atributos:
        - nome
        - documento
    Todos atributos devem ser privados e string.

crie a classe Visita com os atributos:
        - visitante
        - profissional
        - data_visita
    O atributo visitante deverá ser um objeto da
        classe Visitante escolhido de lista_visitantes.
    O atributo profissional deverá ser um objeto da
        classe Profissional escolhido de lista_profissionais.

Crie os métodos que forem necessários para acessar os
atributos das classes.


Desenvolva seu código a partir do menu abaixo:

======================
MENU
======================
1- Cadastrar Profissional
2- Localizar Profissional
3- Cadastrar Visitante
4- Registrar Visita
5- Relatório de Conferência
Escolha:


Na opção 1 do menu cadastre o nome, especialidade e sala
    onde o profissional atende. Armazene esses dados em
    lista_Profissionais (como objetos).

Na opção 2 do menu é possível localizar um profissional
    pelo nome ou pela profissão. Isso serve para o caso
    do visitante não saber a sala do profissional.
    (Apenas mostrar na tela o nome e a sala do profissional)

Na opção 3 do menu será cadastrado o visitante com nome,
    documento. Armazene esses dados em lista_visitantes
    (como objetos).

Na opção 4 do menu será registrado a visita.
    Escolha o visitante (da lista de visitantes) e o
    profissional (da lista_profissionais), entre com a
    data e armazene a visita em lista_visitas
    (como objeto).

Na opção 5 do menu apenas crie um relatório de conferência.
    Selecione o Profissional e mostre todos os visitantes
    e a data da visita.

Obs. Em todas as listas serão armazenados as instâncias
de suas classes.

'''
