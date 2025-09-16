import math

def integral(expr, a, b, N=100000):
    largura = (b - a) / N # aqui eu calculo a largura de cada retangulo da soma de riemann
    # a partir daqui, calculo a soma de riemann pelo ponto médio a partir da soma das areas dos retangulos
    soma = 0.0
    for i in range(N):
        x = a + (i + 0.5) * largura
        soma += eval(expr, {"x": x, **math.__dict__}) * largura
    return soma

if __name__ == "__main__":
    expr = input("Digite a função f(x) a ser integrada, no formato adequado:\nExemplo: sin(5*x+8), x**2+3*x-1, exp(x), log(x+1)\nobs: Não utilizar frações!\n")
    a = eval(input("Digite o limite inferior a: "), {"pi": math.pi, "e": math.e})
    b = eval(input("Digite o limite superior b: "), {"pi": math.pi, "e": math.e})
    print("Integral aproximada =", integral(expr, a, b))
