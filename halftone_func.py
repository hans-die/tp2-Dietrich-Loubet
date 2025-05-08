from PIL import Image
import numpy as np
import math

#Functions Halftone

def get_grid_coords(h:int, w:int, dot_size:int, angle_deg:int):
    """
    Calcula las coordenadas de una grilla rotada que cubre una imagen. Genera una lista de coordenadas que representan
    los centros de una grilla de puntos.
    ------
    Returns:
    -Lista de coordenadas (x,y): List of tuple
    """
    positions = []
    angle_rad = math.radians(angle_deg)
    cx, cy = w / 2, h / 2 # centro de la imagen

    # calcular la dimension de la grilla
    diag = int(math.hypot(w, h))
    num_x = diag // dot_size + 3
    num_y = diag // dot_size + 3

    # alinear el centro de la grilla con el centro de la imagen
    offset_x = cx - (num_x * dot_size) / 2
    offset_y = cy - (num_y * dot_size) / 2

    # recorrer la grilla y calcular las posiciones (geometría 👻) 
    for i in range(num_y):
        for j in range(num_x):
            gx = offset_x + j * dot_size + dot_size / 2 - cx
            gy = offset_y + i * dot_size + dot_size / 2 - cy
            rx = gx * math.cos(angle_rad) - gy * math.sin(angle_rad) + cx
            ry = gx * math.sin(angle_rad) + gy * math.cos(angle_rad) + cy

            ix, iy = int(round(rx)), int(round(ry))
            if 0 <= iy < h and 0 <= ix < w:
                positions.append((ix, iy))
    return positions

def split_rgb(imagen:str): 
    """
    Separa en 3 canales (R,G,B) a la imagen.
    ------
    Returns:
    -Canales RGB: int
    """
    imagen_array = np.array(imagen)
    rojo = imagen_array[:,:,0]
    verde = imagen_array[:,:,1]
    azul = imagen_array[:,:,2]
    return rojo, verde, azul

def height_width(r:list): #ACA CONSEGUIMOS EL ANCHO Y ALTO DE CADA CANAL, PARA LUEGO PONERLO EN GET GRID COORDS
    """
    Devuelve el alto y ancho de la imagen.
    ------
    Returns:
    Height: int
    Width: int
    """
    height , width = r.shape
    return height, width

def draw_circle(chords_list:list, dot_size:float, height:int, width:int, array_white:list, color:list):
    """
    Dibuja circulos negros en una matriz blanca segun la intensidad de un canal de color.
    Para cada coordenada calula el radio y dibuja un circulo
    ------
    Return:
    Array white: np.ndarray
    """
    for chord in chords_list:
        column = int(chord[0])
        row = int(chord[1])

        pixel_intensity = color[row,column]

        radius = ((1 - pixel_intensity / 255)* dot_size *0.7)

        #RECORRO UNA CUADRICULA CERCA DEL CIRCULO QUE SE FIJE QUE PUNTOS ESTAN DENTRO DEL CIRCULO
        for i in range(int(row - radius),int(row + radius)+1):  
            for j in range(int(column - radius),int(column + radius)+1):
                if 0 <= i < height and 0 <= j < width: #SE FIJA SI ESTAMOS EN LA MATRIZ
                    if (i - row)**2 + (j - column)**2 <= radius**2: #CHEQUEO ESTO DE ECUACION DADA
                        array_white[i, j] = 0
    return array_white
