def neuronio(vies, pesos, parametros):
  saida=0
  for peso, parametro in zip(pesos, parametros):
    saida+=peso*parametro
  saida+=vies
  return saida

print("insira o valor do vies:")
vies=float(input())
print("insira o numero de parametros:")
num_param=int(input())
pesos=[]
parametros=[]
print("insira os valores dos pesos:\n")
for i in range(num_param):
  pesos.append(float(input()))
print("insira os valores dos parametros:\n")
for i in range(num_param):
  parametros.append(float(input()))

print(neuronio(vies, pesos, parametros))