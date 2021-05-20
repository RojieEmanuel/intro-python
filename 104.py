# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
def listasIguais(lista1, lista2):
	a = True
	b = False
	print('As Listas são Iguais? ')
	if (lista1 != lista2):
    		print(b)
	else:
   			print(a)



#2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
def palindromes(pali, pali2):
	a = False
	b = True
	pali = pali.lower().replace(' ', '')
	pali2 = pali2.lower().replace(' ', '')

	print('As strings analisadas são palindromes perfeitas? ')

	if (pali == pali[::-1]):
			print('{} = '.format(pali) , b)	
	else:
			print('{} = '.format(pali) , a)

	if (pali2 == pali2[::-1]):
			print('{} = '.format(pali2) , b)	
	else:
			print('{} = '.format(pali2) , a)


listasIguais(['rojie', 2], ['rojie', 2, 3])
palindromes('Ovo', 'rojie lima')

