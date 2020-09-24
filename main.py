#importar arquivo de outra pasta
from functions import *

print('Olá, qual o seu nome ?')
nome = pegaNome(resposta())
resp = respondeNome(nome)
print (resp)

resp = resposta()
if resp == 'sim':
  cardapioCompleto()
  print('Escolha o código do seu pedido')
  

while True:
  resp = resposta()
  if resp == 'tchau':
    break
 
    
print('tchau, tchau')


"""
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
