#importar arquivo de outra pasta
from functions import *
#sys.exit linha 23 / função: finalizar programa
import sys

print('Olá, qual o seu nome ?')
nome = pegaNome(resposta())
resp = respondeNome(nome)
print (resp)

resp = resposta()
if resp == 'sim':
  cardapioCompleto()
else:
  print('tchau, tchau')
  sys.exit()


print('Quer fazer um pedido ? responda com sim ou não')
while True:
  resp = resposta()
  if resp == 'sim':
    pedido()
    break
  elif resp == 'não':
    sys.exit() 
    break
  else:
    print('Digite sim ou não')
   
print('Quer fazer mais algum pedido ?')
resp = resposta()
if resp == 'sim':
  cardapioCompleto()
  pedido()
else:
  sys.exit()
  

while True:
  resp = resposta()
  if resp == 'tchau':
    break
 
    
print('tchau, tchau')

