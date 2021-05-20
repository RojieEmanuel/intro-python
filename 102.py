weekdays = ['mon','tues','wed','thurs','fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

weekdays

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

print(all_days)

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))
print('\n\t')
# list.reverse()
# print(list)

#########
print('#############################################################################################################################')
print( 'Exercicios - Listas')
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
print('\n1')
print(days_list[2])

# Como verificar o tipo de 'mon'?
print('\n2')
print(type(days_list[0]))

# Como separar 'wed' até 'fri'?
print('\n3')
print(days_list[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print('\n4')
print(days_list[4])
print(days_list[4:5])

# Qual eh o tamanho dos dias e days_list?
print('\n5')
dias = len(days)
listaD= len(days_list)
print('tamanho de dias: ', dias)
print('tamanho de days_list: ', listaD)

# Como inverter a ordem dos dias?
print('\n6')
print(weekdays[::-1])

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
print('\n 10')
ultimo_elemento = list[-1]
print(ultimo_elemento)
list.remove(list[-1])
print(list)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
print('\n7')
list.insert(1,'zero')
print(list)

# Como limpar list?
print('\n8')
print(list.clear())

# Como deletar list?
print('\n9')
print()



print('######################################### FIM ##############################################################################')

