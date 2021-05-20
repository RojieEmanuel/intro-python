import csv

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a
# clausula else no loop implementado.
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Santa Catarina',
              'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I',
                          'Programação para Internet II']}

def define_default_city(state):
    """ Define a capital do estado de origem como city_origin para um professor existente no arquivo.
    Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.
    Keyword arguments:
        state -- O estado de origem do professor
    """
    with open('capitais-BR.csv', mode='r', encoding="utf-8") as capitais:
        reader = csv.reader(capitais, delimiter=";")
        for row in reader:
            if state == row[0]:
                professor1['city_origin'] = row[1]
                return True
        else:
            return False


if define_default_city(professor1['state_origin']):
    print(professor1['city_origin'])

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o
# suficiente.

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva
# em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.


def leCPF():
    set_cpfs = set()
    with open('lista-cpf.txt','r') as arquivo_cpfs:
        with open('lista-cpf-unicos.txt', 'w') as arquivo_cpfs_unicos:
            for cpf in arquivo_cpfs:
                if cpf not in set_cpfs:
                    arquivo_cpfs_unicos.write(cpf)
                    set_cpfs.add(cpf)
    return len(set_cpfs)


print(leCPF())