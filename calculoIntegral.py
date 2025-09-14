import math

# número de subdivisões (quanto maior, mais preciso)
N = 100000 

# Entrada do usuário
expr = input("Digite a função f(x) a ser integrada, no formato adequado:\nExemplo: sin(5*x+8), x**2+3*x-1, exp(x), log(x+1)\n obs: Não utilizar frações!\n")
a = eval(input("Digite o limite inferior a: "), {"pi": math.pi, "e": math.e})
b = eval(input("Digite o limite superior b: "), {"pi": math.pi, "e": math.e})

# largura de cada retângulo
largura = (b - a) / N  
soma = 0.0

# Soma de Riemann pelo ponto médio
for i in range(N):
    x = a + (i + 0.5) * largura
    soma += eval(expr, {"x": x, **math.__dict__}) * largura

print(f"Integral aproximada = {soma}")
