#importar arquivo de outra pasta
from functions import *
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


print('Quer fazer um pedido ? responda com sim ou não')
resp = resposta()
if resp == 'sim':
  pedido()
else:
  sys.exit()
  

while True:
  resp = resposta()
  if resp == 'tchau':
    break
 
    
print('tchau, tchau')

