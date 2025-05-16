import numpy as np
import random
import math

# Kmeans functions

def get_all_pixels(image:np.ndarray):  #Paso 1
    """
    Recorre una imagen representada como un array NumPy y convierte cada píxel en una lista de colores RGB.
    ------
    Entrada:
    -La imagen para luego recorrerla
    ------
    Returns:
    - pixels_height (int): Alto de la imagen.
    - pixels_width (int): Ancho de la imagen.
    - pixels_list (list): Lista de todos los colores RGB en la imagen, en orden fila por fila.
    """
    pixels = np.array(image)
    pixels_list = []
    pixels_height, pixels_width,_ = pixels.shape #Pixel shape te da alto ancho y colores de pixeles r,g,b., lo de rgb lo omito xq siempre son 3dame 
    #Recorremos cada pixel
    for row in range (pixels_height):
        for column in range (pixels_width):
            color=pixels[row][column] #color rgb
            pixels_list.append(color) #SE PUEDE PONER COMO LISTA DE COMPRENSION PERO ES MAS FACIL DE VERLO ASI
    return pixels_height, pixels_width, pixels_list, pixels

def find_centroids(pixels_list:list,clusters_quantity:int): #Paso 2
    '''
    Ejecuta el algoritmo de K-Means para agrupar colores de una imagen en un número fijo de clusters.
    -------
    Entrada:
    -La lista de pixeles y la cantidad de clusters, el ultimo ingresado por el usuario.
    -------
    Returns:
    - centroids (list): Lista final de centroides optimizados tras iterar.
    - list_pixels_centroids (list): Lista de índices de centroides asignados a cada píxel de la imagen.'''
    centroids = random.sample(pixels_list, clusters_quantity) #DEVUELVE EN UNA LISTA LA MEZCLA DE LOS 3 COLORES RGB PARA GENERAR EL COLOR DEL CENTROIDE
    for i in range(100):
        list_pixels_centroids = []
        for color in pixels_list:
            R1, G1, B1 = map(int,color) #Convierto a int para que el unit no tenga problemas, que en vez de 16 me de -240 cuando hace 10-250
            best_distance = 10000

            for h, centroid in enumerate(centroids):
                R2, G2, B2 = map(int,centroid)
                #Calculo distancia entre colores
                distance = math.sqrt((R1-R2)**2 + (G1-G2)**2 + (B1-B2)**2)

                if (distance<best_distance):
                    best_distance = distance
                    best_index = h            #Guardo el indice del centroide, no el color

            list_pixels_centroids.append(best_index) #Esta lista son todos los pixeles ya con el centroide asignado y que color van a representar
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

        for m in range(len(pixels_list)):
            pixel = pixels_list[m]
            index = list_pixels_centroids[m]
            # Busco en los pixeles a que centroice fue asignado y sumo

            r, g, b = map(int,pixel)
            sum_r[index] += r
            sum_g[index] += g
            sum_b[index] += b
            quantity[index] += 1

        new_centroids=[]

        for j in range(clusters_quantity):
            if quantity[j]==0:
                new_centroids.append(random.choice(pixels_list))
            else:
                new_r = round(sum_r[j]/quantity[j])
                new_g = round(sum_g[j]/quantity[j])
                new_b = round(sum_b[j]/quantity[j])
                new_centroids.append([new_r,new_g,new_b])

        if np.allclose(centroids, new_centroids, atol=1): #Corta el bucle si no hay cambios significativos entre los centroides
            break
        centroids = new_centroids
    return centroids, list_pixels_centroids
    
def join_pixels(pixels:np.ndarray, pixels_height:int, pixels_width:int, list_pixels_centroids:list, centroids:list):
    """
    Asigna a cada píxel de la imagen el color de su centroide correspondiente.
    ------
    Entrada:
    -Los pixeles, su ancho y alto, la lista de centroides 
    ------
    Returns:
    - pixels (np.ndarray): Imagen modificada con colores reemplazados por sus centroides."""
    for row in range (pixels_height):
        for column in range (pixels_width):# Voy pixel a pixel y reemplazo por el color del centroide final
            index = row * pixels_width + column
            centroid_index = list_pixels_centroids[index]

            pixels[row][column] = centroids[centroid_index]
    return pixels
