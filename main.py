
def resposta():
  resp = input('>: ').lower().replace('é','e')
  return resp

print('Olá, qual o seu nome ?')
nome = resposta()


#nome = nome.lower()
#nome = nome.replace('é','e')
#condição para evitar erros na digitação do usuario
if 'o meu nome e ' in nome:
  nome = nome[13: ]

  nome = nome.title()

print('Muito prazer, '+nome)
print('Voce deseja fazer um pedido ?')
simnao = resposta()

if simnao == 'sim':
  print('O que voce deseja ?')


while True:
  resp = resposta()
  if resp == 'tchau':
    print('tchau, tchau')
    break
  else:
    print('O que voce deseja ?')


"""class pedido():
    def _init_(self):
        self.nomeC = ""
        self.nomeP = ""
        self.precoP = 0
        self.precos = [12, 22, 32]
        self.cardapio = ["sanduiche1","sanduiche2","sanduiche3"]

    def gerarnota(self):
        print(self.nomeC)
        print(self.nomeP)
        print(self.precoP)
    
    def gerarpedido(self):
        self.nomeC = raw_input("Digite seu nome:\n")
        self.mostrarcardapio()
        n = int(raw_input("Digite o numero do pedido\n")) - 1
        self.nomeP = self.cardapio[n]
        self.precoP = self.precos[n]

    def mostrarcardapio(self):
        for i in range(0, len(self.cardapio)):
            print(self.cardapio[i], self.precos[i])
    
pedido1 = pedido()
pedido1.gerarpedido()
pedido1.gerarnota()"""
