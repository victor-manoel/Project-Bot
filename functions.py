
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
  frase = 'Muito prazer, '
  return frase+nome