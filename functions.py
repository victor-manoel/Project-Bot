
def resposta():
  resp = input('>: ').lower().replace('é','e')
#nome = nome.lower()
#nome = nome.replace('é','e')
  return resp

def pegaNome(nome):
#condição para evitar erros na digitação do usuario
  if 'o meu nome e ' in nome:
     nome = nome[13: ]
     nome = nome.title()
  return nome
 
def respondeNome(nome):
  frase = 'Muito prazer '+nome
  return frase+', voce deseja ver o cardápio ? Responda com Sim ou Nao'

def mostrarCardapio(self):
  for i in range(0, len(self.cardapio)):
    print(self.cardapio[i], self.precos[i])

def cardapioCompleto(pedido):
    print('___________________________________________\n')
    print('CODIGO / HAMBURGUERES / PREÇOS\n')
    print('1-BRASIL - 10,00 R$\n')
    print('pão-carne-presunto-queijo-alface-calabresa-bacon\n')
    print('2-ALEMANHA - 15,00 R$\n')
    print('pão-carne-presunto-queijo-bacon-salada-cebola-calabresa\n')
    print('3-ARGENTINA - 16,00 R$\n')
    print('pão-carne-presunto-queijo-alface-calabresa-ovo-bacon-frango\n')
    print('4-ITALIA - 18,00 R$\n')
    print('pão-2 carnes-presunto-queijo-calabresa-salada-ovo-\n')
    print("5-BELGICA - 21,00 R$\n")
    print('pão-2 carnes-presunto-queijo-salada-calabresa-bacon-ovo-frango\n')
    print('____________________________________________\n')
    pedido()