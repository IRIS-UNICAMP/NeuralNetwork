def main():
  entrada = list(map(int, input("Entradas: ").split()))
  pesos = list(map(int, input("Pesos: ").split()))
  bias = int(input("Bias: "))

  def func_ativação(parametro):
    if parametro > 0:
      return 1
    elif parametro < 0:
      return 0

  soma = 0
  for valor1, peso1 in zip(entrada, pesos):
    soma += valor1 * peso1

  soma += bias
  output = func_ativação(soma)
  print("Output: " + str(output))

main()