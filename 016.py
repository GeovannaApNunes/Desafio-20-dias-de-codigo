import math

# lendo os valores
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# calculando a distância
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# exibindo com 4 casas decimais
print(f"{distancia:.4f}")