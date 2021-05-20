book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
titulo1 = book1.split('by')
titulo2 = book2.split('by')
titulo3 = book3.split('by')

# 3) Quantos caracteres cada título tem?
print(titulo1[0], 'Numero de caracteres = ' ,len(titulo1[0]))
print(titulo2[0], 'Numero de caracteres = ' ,len(titulo2[0]))
print(titulo3[0], 'Numero de caracteres = ' ,len(titulo3[0]))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
print('\n String na formatação solicitada fica: \" {0}{1} \" \n'.format(titulo1[0], titulo1[1]))


# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
palindrome_generico = str(input('Digite uma palavra: ')).lower().replace(' ', '')

palindrome_one = 'ovo'.lower().replace(' ', '')
palindrome_two = 'Natan'.lower().replace(' ', '')
palindrome_three = 'luz azul'.lower().replace(' ', '')
palindrome_four = 'caneta azul'.lower().replace(' ', '')


if (palindrome_generico == palindrome_generico[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_generico))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_generico))

if (palindrome_one == palindrome_one[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_one))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_one))

if (palindrome_two == palindrome_two[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_two))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_two))

if (palindrome_three == palindrome_three[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_three))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_three))		

if (palindrome_four == palindrome_four[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_four))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_four))	
