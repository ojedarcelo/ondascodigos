#!/usr/bin/env python
# coding: utf-8

# # Lab 4 OyO

# In[1]:


import matplotlib.pyplot as plt

# Valores obtenidos de las mediciones
do = [25, 60.5, 59, 24.5, 44]  # Reemplaza con tus valores de do
di = [64, 28, 29.2, 68.5, 37]  # Reemplaza con tus valores de di

# Cálculo de 1/do y 1/di
inv_do = [1 / valor for valor in do]
inv_di = [1 / valor for valor in di]

# Gráfico de 1/di vs 1/do
plt.plot(inv_do, inv_di, 'o')
plt.xlabel('1/do')
plt.ylabel('1/di')
plt.title('Gráfico: 1/di vs 1/do')
plt.grid(True)
plt.show()


# In[2]:


# Valores obtenidos de las mediciones
do = [25, 60.5, 59, 24.5, 44]  # Reemplaza con tus valores de do
di = [64, 28, 29.2, 68.5, 37]  # Reemplaza con tus valores de di
hi = [-3,-2.5, -2.4, -3, -2.1]  # Reemplaza con tus valores de hi

# Cálculo de di/do y hi
di_do = [di[i] / do[i] for i in range(len(do))]
altura_objeto = [hi[i] * di_do[i] for i in range(len(do))]

# Gráfico de hi vs di/do
plt.plot(di_do, hi, 'o')
plt.xlabel('di/do')
plt.ylabel('hi')
plt.title('Gráfico: hi vs di/do')
plt.grid(True)
plt.show()

# Cálculo de la altura del objeto
altura_promedio = sum(altura_objeto) / len(altura_objeto)
print("Altura promedio del objeto:", altura_promedio)


# ## Parte 2

# In[3]:


# Valores obtenidos de las mediciones
d1 = [23.5, 23.5, 47, 55, 41, 18.5]  # Reemplaza con tu valor de d1
d = [17.5, 13, 17, 17, 3, 60.5]  # Reemplaza con tu valor de d
d2 = [31.2, 55.5, 26, 27, 38, 14.5]  # Reemplaza con tu valor de d2

# Cálculo de la distancia focal f
f_minus = (1 / d1) - (1 / d) + (1 / d2)

# Cálculo de las posiciones de las imágenes reales y virtuales
posicion_imagen_real = 1 / (1 / d - 1 / f_minus)
posicion_imagen_virtual = 1 / (1 / d + 1 / f_minus)

# Imprime los resultados
print("Distancia focal f-:", f_minus)
print("Posición de la imagen real:", posicion_imagen_real)
print("Posición de la imagen virtual:", posicion_imagen_virtual)


# ## Parte 3

# In[12]:


def calcular_magnificacion(f_1, f_2, d_oo, d_o):
    magnificacion_exp = - (f_1 * d_oo) / (d_o * f_1) * f_2
    magnificacion_esperada = - f_1 / f_2
    return magnificacion_exp, magnificacion_esperada


# Valores:
f_1 = 300  # Distancia focal de la lente 1 (en cm)
f_2 = 125  # Distancia focal de la lente 2 (en cm)
d_oo = (274+3+42.5)  # Distancia entre el objeto y el ojo (en cm)
d_o = 274  # Distancia entre el objeto y la lente 1 (en cm)

magnificacion_exp, magnificacion_esperada = calcular_magnificacion(f_1, f_2, d_oo, d_o)

# Cálculo de la diferencia porcentual
diferencia_porcentual = abs((magnificacion_esperada - magnificacion_exp) / magnificacion_esperada) * 100

print("Magnificación experimental: ", magnificacion_exp)
print("Magnificación esperada: ", magnificacion_esperada)
print("Diferencia porcentual:", diferencia_porcentual)


# ## Parte 4

# In[13]:


def calcular_magnificacion_galileo(f_1, f_2, d_oo, d_o):
    magnificacion = - ((f_1 * d_oo) / ((d_o - f_1) * f_2))
    return magnificacion

magnificacion_real_4 = - (f_1 / f_2)

# Valores de ejemplo
f_1 = 300  # Distancia focal de la lente positiva (en cm)
f_2 = -50  # Distancia focal de la lente negativa (en cm)
d_oo = (297+3+25)  # Distancia entre el objeto y el ojo (en cm)
d_o = 297  # Distancia entre el objeto y la lente 1 (en cm)

magnificacion = calcular_magnificacion_galileo(f_1, f_2, d_oo, d_o)

print("Magnificación del telescopio de Galileo: ", magnificacion)


# ## Parte 5

# In[21]:


def calcular_magnificacion_microscopio(f_1, f_2, d_oo, d_o, d_i):
    magnificacion = - ((f_1 * d_oo) / ((d_o - f_1) * f_2))
    magnificacion_real = - ((L * d_oo) / (f_1 * f_2))
    return magnificacion, magnificacion_real


f_1 = 15  # Distancia focal del objetivo (en cm)
f_2 = 125  # Distancia focal del ocular (en cm)
d_oo = (2+2+8.5)  # Distancia entre el objeto y el ojo (en cm)
d_o = 2  # Distancia entre el objeto y el objetivo (en cm)
d_i = 2  # Distancia entre el ocular y la imagen final (en cm)
L = 8.5

magnificacion = calcular_magnificacion_microscopio(f_1, f_2, d_oo, d_o, d_i)

print("Magnificación del microscopio: ", magnificacion)
print("Magnificación esperada del microscopio: ", magnificacion_real)

