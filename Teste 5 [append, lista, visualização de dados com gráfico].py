#!/usr/bin/env python
# coding: utf-8

# In[28]:


import matplotlib
import matplotlib.pyplot as plt
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
print('/\/\/\/\/ Análise de Desempenho /\/\/\/\/'.upper())
print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n')
d = {'Português':1,'Matemática':2,'Geografia':3,'História':4,'Ciências':5 }
notas = []
bim = [1,2,3,4]
perg = int(input('Selecione a matéria:\n(1)Português\n(2)Matemática\n(3)Geografia\n(4)História\n(5)Ciências\n'))
bim1 = float(input('Qual foi a sua nota no 1º bimestre?\n'))
bim2 = float(input('Qual foi a sua nota no 2º bimestre?\n'))
bim3 = float(input('Qual foi a sua nota no 3º bimestre?\n'))
bim4 = float(input('Qual foi a sua nota no 4º bimestre?\n'))
notas.append(bim1) #adicionar dados na lista "nota"
notas.append(bim2)
notas.append(bim3)
notas.append(bim4)
plt.bar(bim,notas,color='black') #elaboração de um gráfico de colunas
plt.title('Desempenho')
plt.xlabel('Bimestre')
plt.xticks(bim)
plt.ylabel('Nota')
plt.axis([0.25,4.75,0,11])
a = len(notas) #informação da média simples do aluno
b = sum(notas)
media = b/a
print('Sua média na disciplina é {:.2f}.'.format(media))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




