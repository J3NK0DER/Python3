### lógica de programação da calculadora
while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite o método de operação (+-/*): ')
  numeros_validos = None
  num_1_float = 0
  num_2_float = 0
  operadores_permitidos = '+-/*'


  try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True 
  except:
        numeros_validos = None

## Checagem das condições númericas ##

  if numeros_validos is None:
      print('Um ou ambos os números digitados são inválidos.')
      continue

  if operador not in operadores_permitidos:
      print('Operador Inválido.')
      continue
  
  if len(operador) > 1:
      print('Digite apenas um operador.')
      continue
  
## Fim da checagem ##

  print('Realizando sua conta. Confira o resultado abaixo:')
  if operador == '+':
       print(f'{num_1_float} +{num_2_float}=', num_1_float + num_2_float)
  elif operador == '-':
       print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
  elif operador == '/':
       print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
  elif operador == '*':
       print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
  else:
      print('Erro interno')
  
  
  while True:
   sair = input('Quer sair? [s]im:').lower()
   if sair.startswith('s'):
       break
   else:
       continue


