# Função da Esfera
def func1(x) -> int:
    total = 0
    for i in range(0,len(x)):
        total = total + x[i] ** 2
    return total