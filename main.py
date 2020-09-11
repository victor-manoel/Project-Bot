print('Olá, qual o seu nome ?')
nome = input('>: ')

#condição para evitar erros na digitação do usuario
if 'O meu nome e ' in nome:
  nome = nome[13: ]

print('Muito prazer, '+nome)

while True:
  resposta = input('>: ')
  if resposta == 'tchau':
    break
  else:
    print('O que voce deseja ?')
print('tchau, tchau')
