#Input layer:
entradas = [float(x) for x in input("Entrada:").split(" ")]

#Informações do neuronio:
pesos = []
for i in range(1, len(entradas)+1):
  pesos.append(float(input(f"Entre com o peso para a entrada {i}:")))
bias = float(input("Entre com o bias:"))

#Cálculo do produto interno de pesos e entradas + bias:
saida = bias
for i in range(len(pesos)):
  saida += pesos[i]*entradas[i]

#Aplicação da função de ativação:
if saida > 0:
  print("A saida do neuronio é 1")
else:
  print("A saida do neuronio é 0")