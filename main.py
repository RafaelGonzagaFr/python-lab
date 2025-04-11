pessoas = []
resposta = 0

def Menu():
  print('1 - Mostrar pessoas')
  print('2 - Adicionar pessoas')
  print('3 - Editar pessoas')
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

      pessoas.append({'nome': nome, 'idade': idade})
    resposta = input('Quer adicionar uma pessoa nova? 1 - sim | 0 - não -> ')

def EditarPessoas():
  contador = 1
  for pessoa in pessoas:
    print(contador, '-', pessoa)
  posicao = int(input('-> '))
  print('ALTERAR')
  try:
    pessoas[posicao]['nome'] = input(pessoas[posicao]['nome'] + '-> ')
    pessoas[posicao]['idade'] = input(pessoas[posicao]['idade'] + '-> ')
  except IndexError as error:
    print('Usuário inexistente')
  
while resposta != 'exit':
  resposta = Menu()
  if resposta == '1':
    MostrarPessoas()
  if resposta == '2':
    AdicionarPessoas()
  if resposta == '3':
    EditarPessoas()


