import math
import statistics as st

# 1a)
x = 4 ** 3 - 2 ** 2
print('1a)', x)

# 1b)

x = math.sin(2) - math.cos(4.2)
print(f'1b) {x:.2f}')

# 1c)
z = math.cos(math.sin(3.7) - math.tan(1.3))
print(f'1c) {z:.2f}')

# 1d)
x = (26 % 4)
print(f'1d) {x}')

# 1e)
y = math.degrees(42.2)
x = math.radians(x)
print(f'1e) {x:.2f}')

# 1f)
z = math.radians(3.1)
x = math.degrees(z)
print(f'1f) {x}')

# 2

x = 3
y = 6

# 2a)
w = math.log(x) - math.log(y)
print(f'\n2a) {w}')

# 2b)
z = (x * y ** 2) + (y * math.cos(x))
print(f'2b) {z}')

# 2c)
s = math.sqrt((x / y) + math.log(x + y) + math.tan(x))
print(f'2c) {s}')

# 3
num = [3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

print(f'\n3a) {num[2:3]}')
print(f'3b) {num[4:8]}')
print(f'3c) {num[1:-1]}')
print(f'3d) {num[0:-1]}')
print(f'3e) {num[0:-1:3]}')
print(f'3f) {num[-1]}')
print(f'3g) {num[-3:]}')
print(f'3h) {num[0:4]}')
print(f'3i) {len(num)}')
print(f'3j) {num.count(1)}')

# 4
bolsa = ['dow', 'ibov', 'ftse', 'dax', 'nasdaq', 'cac']

print(f'\n4a) {bolsa[0:3]}')
bolsa.extend(['hong kong', 'merval'])
print(f'4b) {bolsa}')
x = bolsa.index('nasdaq')
print(f'4c) {x}')
bolsa.remove('cac')
print(f'4d) {bolsa}')
bolsa.insert(1, 'sp&500')
print(f'4e) {bolsa}')

# 5
print(f'\n 5) write bov.txt')
f = open('bov.txt', 'w')
lista = ['petr4', 'vale3', 'ggbr4', 28.4, 31.3, 15.76]
f.write('%s %5.2f\n%s %5.2f\n%s %5.2f' % (lista[0], lista[3], lista[1], lista[4], lista[2], lista[5]))

f.close()

# 6
print(f'\n 6) read bov.txt')
f = open('bov.txt', 'r')
print(f.read())

# 7
lista_dois = [2, 2, 3, 3, 3, -1, -1, -2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0, 2, 1, 5, 5, 7, 6, 5, 0, 0]
print(f'\n7a) {sum(lista_dois)}')
print(f'7b) {max(lista_dois)}')
print(f'7c) {min(lista_dois)}')
print(f'7d) {st.mean(lista_dois)}')
print(f'7e) {st.median(lista_dois)}')
print(f'7f) {st.mode(lista_dois)}')
print(f'7g) {st.stdev(lista_dois)}')
print(f'7h) {st.pstdev(lista_dois)}')
print(f'7i) {lista_dois.count(0)}')
print(f'7j) {lista_dois.count(5)}')
lista_dois.sort()
print(f'7k) {lista_dois}')
lista_dois.reverse()
print(f'7l) {lista_dois}')
