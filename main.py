pessoas = []
resposta = 0

def Menu():
  print('1 - Mostrar pessoas')
  print('2 - Adicionar pessoas')
  resposta = input('-> ')
  return resposta

def MostrarPessoas():
  print(pessoas)

def AdicionarPessoas():
  resposta = 1
  while resposta != '0':
    if(resposta == '1'):
      nome = input('Nome: ')
      idade = input('idade: ')

      pessoas.append({'Nome': nome, 'idade': idade})
    resposta = input('Quer adicionar uma pessoa nova? 1 - sim | 0 - não -> ')
  
while resposta != 'exit':
  resposta = Menu()
  if resposta == '1':
    MostrarPessoas()
  if resposta == '2':
    AdicionarPessoas()


