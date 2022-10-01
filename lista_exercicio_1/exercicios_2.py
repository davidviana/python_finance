# 4

now = float(input())
high = float(input())
low = float(input())
sup = low + (high - low) * 0.3
res = low + (high - low) * 0.6

if low <= now <= high:
    print('O preço da ação está dentro da faixa de suporte-resistência')
else:
    print('O preço da ação está fora da faixa de suporte-resistência')

# 5

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4 * (a * c)

if delta == 0:
    print(f'\nx1 = {-b/(2*a)}')
elif delta > 0:
    print(f'\nx1 = {-b + delta / (2 * a)}'
          f'\nx2 = {-b - delta/ (2 * a)}')
else:
    print('não existem raízes reais')

# 11

n = int(input())
pi = 0.0

for k in range(0, n, 1):
    if k % 2 == 0:
        pi = pi + 1 / (2 * k + 1)
    else:
        pi = pi - 1 / (2 * k + 1)

pi = 4 * pi

print(pi)