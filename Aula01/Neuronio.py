class Neuronio:

  def __init__(self, pesos, bias):
    self.pesos = pesos
    self.bias = bias

  def ativacao(valor):
    if valor >= 0:
      return 1
    return 0

  def resultado(self,entrada):
    total = self.bias
    for i in range(len(entrada)):
      total += entrada[i]*self.pesos[i]
    return Neuronio.ativacao(total)


neu = Neuronio([1,1,-2,1],2)
print(neu.resultado([1,0,1,0]))