arquivo= open("teste.txt", "a")

rua = 0
bairro= 0
numero= 0
zona = 0

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



def cardapioCompleto():
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


def pedido():
  print('Escolha o codigo do seu pedido')
  lanche = input ()
  valor_lanche = 0

  q = float(input("Quantos ???\n"))

  if lanche=="1":
    valor_lanche = 10 * q
    nome = "Brasil"
  elif lanche=="2":
    valor_lanche = 15 * q
    nome = "Alemanha"
  elif lanche=="3":
    valor_lanche = 16 * q
    nome = "Argentina"
  elif lanche == "4":
    valor_lanche = 18 * q
    nome = "Italia"
  elif lanche == "5":
    valor_lanche = 21 * q
    nome = "Belgica"
  else:
    nome = None
    print ('Valor invalido')
  if nome:
    print (nome,"custa",valor_lanche,"Reais, por",q,"hamburguer(s)")
    
  return valor_lanche


def corrigirPedido():
    total = 0
    print("Deseja trocar o pedido?")
    res = input()
    if 'nao' in res:
        print("\nCerto")
    else:
        print('___________________________________________\n')
        cardapioCompleto()
        print('___________________________________________\n')
        print("Escolha o código do seu novo pedido:\n")
        lanche = input ()
        valor_lanche = 0

        q = float(input("Quantos ???\n"))

        if lanche=="1":
          valor_lanche = 10 * q
          nome = "Brasil"
        elif lanche=="2":
          valor_lanche = 15 * q
          nome = "Alemanha"
        elif lanche=="3":
          valor_lanche = 16 * q
          nome = "Argentina"
        elif lanche == "4":
          valor_lanche = 18 * q
          nome = "Italia"
        elif lanche == "5":
          valor_lanche = 21 * q
          nome = "Belgica"
        else:
          nome = None
          print ('Valor invalido')
        if nome:
          print (nome,"custa",valor_lanche,"Reais, por",q,"hamburguer(s)")

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

            #faltando ajeitar o loop
                

def valor_total(valor_lanche):
  total = valor_lanche
  print('o valor total é',total)


def solicitaEndereco():
    print("\nInforme seu endereço")
    print("Rua.................:")
    print("Numero................:")
    print("Bairro................:")
    print("Zona..................:\n")
    informaEndereco()

def informaEndereco():
    global rua
    print("Rua :")
    rua = input()
    arquivo.write("\nRua: " + rua)
    global numero
    print("Numero :")
    n = input()
    arquivo.write("\nNumero: " + numero)
    global bairro
    print("Bairro :")
    bairro = input()
    arquivo.write("\nBairro: " + bairro)
    global zona
    print("Zona :")
    zona = input()
    arquivo.write("\nZona: " + zona)
   

    if rua == "":
        print("Preencha a rua")
        rua = input()
        arquivo.write("\nRua: " + rua)
    if n == "":
        print("Preencha o numero")
        n = input()
        arquivo.write("\nNumero: " + numero)
    elif bairro == "":
        print("Preencha o bairro")
        bairro = input()
        arquivo.write("\nBairro: " + bairro)
    elif zona == "":
        print("Preencha a zona")
        zona = input()
        arquivo.write("\nZona: " + zona)


def nota(nome):
  print('*******************************')
  print('Dados do cliente: ' + nome)
  print('*******************************')
  print('Rua: ' + rua)  
  print('Numero: ' + numero)
  print('Bairro: ' + bairro)
  print('Zona: ' + zona)
  print('*******************************')
  print('Dados do Pedido')
  print('*******************************')
  