import math

import numpy as np
import openpyxl as op
import matplotlib.pyplot as fig
import statistics as st

lista_cot = []
wb = op.load_workbook('PETR4.xlsx')
plan = wb['dados']

for i in range(0, len(plan['A'])):
    i += 1
    x = plan[f'A{i}'].value
    lista_cot.append(x)

lista_cot.reverse()

array_cot = np.array(lista_cot)

retorno = (array_cot[1:len(array_cot)] - array_cot[0:(len(array_cot) - 1)]) / array_cot[0:(len(array_cot) - 1)]

t = np.arange(0, 22)

# Cenários
# Otimista = media do retorno + 2 * (desvpad(retorno))/ raiz(n)
# Pessimista = media do retorno - 2 * (desvpad(retorno))/ raiz(n)

desvio = st.pstdev(retorno)

otimista = st.mean(retorno) + 2 * (desvio/math.sqrt(len(array_cot)))
pessimista = st.mean(retorno) - 2 * (desvio/math.sqrt(len(array_cot)))


print(f'O cenário otimista possui: {otimista:.4f}% \n'
      f'O cenário pessimista possui: {pessimista:.4f}%')

tempo = np.arange(0, len(array_cot))

fig.subplot(211), fig.plot(tempo, array_cot)
fig.subplot(212), fig.plot(t, retorno)

fig.show()
