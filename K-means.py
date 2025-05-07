from PIL import Image
import numpy as np
import random
import math

#PASO 1
image=Image.open("C:\\Users\\aula\\Documents\\TP2 FRANCISCO LOUBET\\istockphoto-517188688-612x612.jpg").convert("RGB")
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

for color in pixelsList:
    R1,G1,B1=color
    best_distance=10000
    list_pixelsToCentroids=[]

    for centroid in centroids:
        R2,G2,B2=centroid
        #Calculo distancia entre colores
        distance=math.sqrt((R1-R2)**2 + (G1-G2)**2 + (B1-B2)**2)

        if(distance<best_distance):
            best_distance=distance
            best_centroid=centroid

        list_pixelsToCentroids.append(best_centroid) #Esta lista son todos los pixeles ya con el centroide asignado y que color van a representar

