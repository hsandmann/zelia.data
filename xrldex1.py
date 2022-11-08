import matplotlib.pyplot as fig # plot
import statistics as st
import xlrd
import numpy as ny # np
import scipy.stats as sci
from scipy.stats import norm

wb = xlrd.open_workbook('bovespa.xlsx')
plan = wb.sheet_by_name('sheet1')
nlin = plan.nrows
ncol = plan.ncols
dados = []

for i in range(ncol):
    coluna = plan.col_values(i)
    dados.append(coluna[1:])

dias = ny.arange(0, nlin - 1)
dados = ny.array(dados)

# retorno
retorno = (dados[1, 1:] - dados[1, 0:-1])/dados[1, 0:-1]
# print(retorno)

fig.subplot(221)
fig.plot(dias, dados[1], color='black')
fig.xlabel('dias')
fig.title('BOVESPA')

fig.subplot(222)
fig.plot(dias[1:], retorno, color='black')
fig.xlabel('dias')
fig.title('RETORNO')

fig.subplot(223)
fig.hist(retorno, bins=20, color='gray', density=True, stacked=True)
fig.xlabel('classes')
fig.ylabel('frequencia')
fig.title('HISTOGRAMA - RETORNO')

xmin, xmax = fig.xlim()
# print(xmin, xmax)
media = st.mean(retorno)
desvio=st.pstdev(retorno)
eixo_x = ny.linspace(xmin, xmax, 100)
eixo_y = norm.pdf(eixo_x, media, desvio)
fig.plot(eixo_x, eixo_y, color='red')

fig.subplot(224)
sci.probplot(retorno, dist='norm', plot=fig)
fig.title('QQ-Plot BOVESPA')