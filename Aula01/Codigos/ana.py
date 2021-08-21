def ativacao(valor):
    if valor > 0:
        return 1
    else:
        return 0

def neuronio(entradas, bias, pesos, qtd_entradas):
    soma = 0
    for i in range(qtd_entradas):
        soma += entradas[i] * pesos[i]
    
    return ativacao(soma + bias)

qtd_entradas = 4
entradas = [1, 0, 2, 3]
pesos = [1, -2, 1, 2]
bias = 8

print(neuronio(entradas, bias, pesos, qtd_entradas))