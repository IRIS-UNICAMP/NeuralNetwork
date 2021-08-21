entradas = [1, 0 , 1, 0]
pesos = [1, 1, -2, 1]
bias = 2
feedforward = []

for n in range(len(entradas)):
  elemento_pesado = entradas[n]*pesos[n]
  feedforward.append(elemento_pesado)

soma = 0
for elemento in feedforward:
  soma += feedforward[elemento]

soma += bias

if soma>=0:
  resposta = 1
else:
  resposta = 0

print(resposta)

///melhorando
def feedforward(entradas, pesos):
  iteracoes = len(entradas)
  pre_bias = 0
  for n in iteracoes:
    pre_bias += entradas[n]+pesos[n]

  return pre_bias

def f(valor):
  if valor >= 0:
    saida = 1
  else:
    saida = 0 

  return saida

def main():
  num_entradas = int(input())
  entradas = []
  for n in range(len(num_entradas)):
    entrada = input()
    entradas.append(entrada)

  num_pesos = int(input())
  pesos []
  for i in range(len(num_pesos)):
    peso = []
    pesos.append(peso)

  pre_bias = feedforward(entradas, pesos)
  entrada_ativ = pre_bias + bias
  saida = ativacao(entrada_ativ)

  print(saida)

