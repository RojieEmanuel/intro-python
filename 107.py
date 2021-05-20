professor1 = {'id':42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla

a = dir(list)
print('=========================================== MÉTODOS DE LISTA =======================================', '\n')
print(a)
print('=========================================== FIM ====================================================', '\n')

b = dir(tuple)
print('=========================================== MÉTODOS DE TUPLA =======================================', '\n')
print(a)
print('=========================================== FIM ====================================================', '\n')

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
def Diferenca(listaA, listaB):
    print("Métodos de list: ", set(listaA) - set(listaB))
    print('\n\n')
    print("Métodos de tuple: ", set(listaB) - set(listaA))
    print('\n\n')


Diferenca(a, b)



# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py
professor1['latitude'] = '22º 27´N'
professor1['longitude'] = '113º 56´E'

professor2['latitude'] = '38º 4´N'
professor2['longitude'] = '9º 8´W'

professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
professor3['latitude'] = '22º 55´S'
professor3['longitude'] = '34º 53´W'


print(professor1,'\n')
print(professor2,'\n')
print(professor3,'\n')