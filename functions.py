#importar arquivo de outra pasta
from functions import *
#sys.exit linha 23 / função: finalizar programa
import sys
total = 0

print('Olá, qual o seu nome ?')
nome = pegaNome(resposta())
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


print('Quer fazer um pedido ? responda com sim ou nao')
while True:
  resp = resposta()
  if resp == 'sim':
    total += pedido()
    break
  elif resp == 'nao':
    sys.exit() 
    break
  else:
    print('Digite sim ou não')
   

while True:
  print('Quer fazer mais algum pedido ? Responda com sim ou nao')
  resp = resposta()
  if resp == 'sim':
    cardapioCompleto()
    total += pedido()
  elif resp == 'nao':
    valor_total(total)
    break
  else:
    print('Digite sim ou não')
    
corrigirPedido()
solicitaEndereco()

  
while True:
  resp = resposta()
  if resp == 'tchau':
    break
 
    
print('tchau, tchau')

