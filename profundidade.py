"""
Encontra a profundidade de uma queda usando o tempo medido entre a soltura de um objeto e a escuta do som de impacto.

Parâmetros:
- tm: tempo medido em segundos
- n: número máximo de iterações que o código deve executar
- p: quantidade de casas decimais no resultado

Constantes:
- v: velocidade do som
- g: aceleração da gravidade

Retorna:
- Tupla (h, abs(tc-tm)) arredondados em p casas decimais
"""

from math import sqrt

def profundidade(tm: float, iteracoes: int = 1000, precisao: int = 3):

    # Constantes da natureza
    v = 330.0 # Velocidade do som
    g = 9.8 # Aceleração da gravidade

    h = (g * tm**2)/2 # Altura inicialmente estimada assumindo o som como instantâneo

    # Loop para achar a raiz da função t(h) = tc(h) - tm
    for i in range(iteracoes):

        tc = (h/v) + sqrt(2*h/g) # Tempo que seria observado se h real fosse igual ao estimado
        dtc = (1/v) + 1/sqrt(2*g*h) # Derivada dtc/dh
        h = h - (tc - tm)/dtc # Nova estimativa do valor de h conforme método de Newton-Raphson

    return round(h, precisao), round(abs(tc-tm), precisao)
