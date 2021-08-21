class Neuronio:
  def __init__(self, wheights: list, bias: float):
    self.wheights = wheights
    self.bias = bias

  def relu(self, value: float):
    return 1 if(value > 0) else 0

  def calculate_result(self, input_values: list):
    result: int = 0
    for w, v in zip(self.wheights, input_values):
      result += w*v
    return self.relu(result + self.bias)


def main():
  input_values = [float(x) for x in input().split()]
  wheights = [float(x) for x in input().split()]
  bias = float(input())
  
  n = Neuronio(wheights, bias)
  print(n.calculate_result(input_values))

if __name__ == '__main__':
  main()