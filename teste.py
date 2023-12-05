from google.colab import drive
import os
drive.mount('/content/drive')
os.chdir("/content/drive/MyDrive/")
!ls

import pandas as pd # clássicas
import numpy as np  # clássicas
import matplotlib.pyplot as plt  # clássicas
import datetime
from random import randrange, seed

# criando um objeto datetime com a data e hora atual
agora = datetime.datetime.now()
print("Data e hora atual:", agora)

# criando um objeto date com a data de hoje
hoje = datetime.date.today()
print("Data de hoje:", hoje)

# criando dois objetos date com datas diferentes
data_1 = datetime.date(2022, 1, 1)
data_2 = datetime.date(2023, 1, 1)
# calculando a diferença entre as duas datas
diferenca = data_2 - data_1
print("Diferença entre as duas datas:", diferenca)

# listando tipos diferentes de variáveis
lista = ['int', False, True, '18', 2020]
for elemento in lista:
    print(type(elemento))

# criando lista de nostas aleatórias
seed(10)
notas = []
for nota in range(0, 18):
    notas.append([randrange(0,11)])
print(notas)
print(len(notas))
print(type(randrange))

# visualização gráfica (dados aleatórios)
x = list(range(1,100))
y = list(range(1,100))
plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
