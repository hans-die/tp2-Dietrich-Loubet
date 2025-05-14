from PIL import Image
import numpy as np
import random
import math
import time


start_time = time.time()
#PASO 1
image=Image.open("C:\\Users\\aula\\Documents\\TP2 LOUBET\\alonso.jpeg").convert("RGB")
pixels=np.array(image)

pixelsList=[]

pixels_height,pixels_width,_=pixels.shape #Pixel shape te da alto ancho y colores de pixeles r,g,b., lo de rgb lo omito xq siempre son 3dame 

#Recorro cada pixel
for row in range (pixels_height):
    for column in range (pixels_width):
        color=pixels[row][column] #color rgb
        pixelsList.append(color) #SE PUEDE PONER COMO LISTA DE COMPRENSION PERO ES MAS FACIL DE VERLO ASI

clusters_quantity=8 #LO PONE EL USUARIO 

centroids=random.sample(pixelsList,clusters_quantity) #DEVUELVE EN UNA LISTA LA MEZCLA DE LOS 3 COLORES RGB PARA GENERAR EL COLOR DEL CENTROIDE



#PASO 2

for i in range(100):
    list_pixelsToCentroids=[]
    for color in pixelsList:
        R1,G1,B1=map(int,color) #Convierto a int para que el unit no tenga problemas, que en vez de 16 me de -240 cuando hace 10-250
        best_distance=10000

        for h,centroid in enumerate(centroids):
            R2,G2,B2=map(int,centroid)
            #Calculo distancia entre colores
            distance=math.sqrt((R1-R2)**2 + (G1-G2)**2 + (B1-B2)**2)

            if(distance<best_distance):
                best_distance=distance
                best_index=h            #Guardo el indice del centroide, no el color

        list_pixelsToCentroids.append(best_index) #Esta lista son todos los pixeles ya con el centroide asignado y que color van a representar

    #Paso 3
    sum_r = {}
    sum_g = {}
    sum_b = {}
    quantity = {}

    for i in range(clusters_quantity): #Hago una estructura para acumular valores RGB y la cantidad de pixeles asignados a cada cluster
        sum_r[i] = 0
        sum_g[i] = 0
        sum_b[i] = 0
        quantity[i] = 0

    for m in range(len(pixelsList)):
        pixel = pixelsList[m]
        index = list_pixelsToCentroids[m]
        # Busco en los pixeles a que centroice fue asignado y sumo

        r, g, b = map(int,pixel)
        sum_r[index] += r
        sum_g[index] += g
        sum_b[index] += b
        quantity[index] += 1

    new_centroids=[]

    for j in range(clusters_quantity):
        if quantity[j]==0:
            new_centroids.append(random.choice(pixelsList))
        else:
            new_r=round(sum_r[j]/quantity[j])
            new_g=round(sum_g[j]/quantity[j])
            new_b=round(sum_b[j]/quantity[j])
            new_centroids.append([new_r,new_g,new_b])

    if np.allclose(centroids, new_centroids, atol=1): #Corta el bucle si no hay cambios significativos entre los centroides
        break

    centroids = new_centroids
    

#PASO 5 

for row in range (pixels_height):
    for column in range (pixels_width):# Voy pixel a pixel y reemplazo por el color del centroide final
        index=row*pixels_width+column
        centroid_index=list_pixelsToCentroids[index]

        pixels[row][column]=centroids[centroid_index]

Image.fromarray(pixels.astype(np.uint8)).save("imagen_resultado.png")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")




