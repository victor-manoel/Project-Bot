arquivo= open("teste.txt", "w")

#importar arquivo de outra pasta
from functions import *
#sys.exit linha 23 / função: finalizar programa
import sys
total = 0

bem_vindo = input()
print(bem_vindo +', qual o seu nome ?')
nome = pegaNome(resposta())
arquivo.write("Nome: " + nome)
resp = respondeNome(nome)
print (resp)

while True:
  resp = resposta()
  if resp == 'sim':
    cardapioCompleto()
    break
  elif resp == 'nao':
      sys.exit()
  else:
    print('Digite sim ou nao')

   
pedidos = 0
while True:
  while True:
    if pedidos == 0:
      print('Quer fazer um pedido ? Responda com sim ou nao')
    else:
      print('Quer fazer mais algum pedido ? Responda com sim ou nao')

    resp = resposta()
    if resp == 'sim':
      cardapioCompleto()
      total += pedido()
      pedidos += 1
    elif resp == 'nao':
      if pedidos == 0:
        sys.exit()
      else:
        valor_total(total)
      break
    else:
      print('Digite sim ou não')

  print('Deseja corrigir o seu pedido ?')
  resp = resposta()
  if resp == 'sim':
    cardapioCompleto()
    total = pedido()
    pedidos = 1
    continue
  else:
    break

solicitaEndereco()
print('Aguarde enquanto processamos o seu pedido...\n')
nota(nome, total)

confirmarpedido()
  
while True:
  resp = resposta()
  if resp == 'tchau':
    break
 
    
print('tchau, tchau')

