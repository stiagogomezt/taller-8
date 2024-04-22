import numpy as np
import matplotlib.pyplot as plt
# Lista de 18 datos
Estaturas = [1.88, 1.60, 1.60, 1.60, 1.60, 1.60, 1.65, 1.59, 1.75, 1.59, 1.72, 1.74, 1.80, 1.75, 1.75, 1.75, 1.75, 1.75]

# Convertir la lista en un ndarray de dos dimensiones

arreglo_2d = np.array(Estaturas).reshape(2, 9)
print(arreglo_2d)
media=np.mean(arreglo_2d)
print("mediana=",media)
mediana=np.median(arreglo_2d)
print("mediana=",mediana)
desviacion =np.std(arreglo_2d)
print("desviacion estandar=",desviacion)

plt.imshow(arreglo_2d, cmap="brg")
plt.colorbar(label="Estaturas(m)")
