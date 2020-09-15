print('Olá, qual o seu nome ?')
nome = input('>: ').lower().replace('é','e')

#nome = nome.lower()
#nome = nome.replace('é','e')
#condição para evitar erros na digitação do usuario
if 'o meu nome e ' in nome:
  nome = nome[13: ]

  nome = nome.title()

print('Muito prazer, '+nome)

while True:
  resposta = input('>: ')
  if resposta == 'tchau':
    break
  else:
    print('O que voce deseja ?')
print('tchau, tchau')
