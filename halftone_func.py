from PIL import Image
import numpy as np
import math

#Functions Halftone

def get_grid_coords(h:int, w:int, dot_size:int, angle_deg:int):
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

def split_rgb(imagen:str): #SEPARAMOS EN CANALES LA IMAGEN, ROJO VERDE, AZUL, Y RETORNAMOS LOS CANALES EN FORMA DE ARRAY
    imagen_open = Image.open(imagen)
    imagen_array = np.array(imagen_open)
    rojo = imagen_array[:,:,0]
    verde = imagen_array[:,:,1]
    azul = imagen_array[:,:,2]
    return rojo, verde, azul

def height_width(r:list,g:list,b:list): #ACA CONSEGUIMOS EL ANCHO Y ALTO DE CADA CANAL, PARA LUEGO PONERLO EN GET GRID COORDS
    height_red , width_red = r.shape
    height_blue , width_blue= g.shape
    height_green , width_green= b.shape
    return height_red, width_red, height_blue, width_blue, height_green, width_green

def draw_circle(chords_list:list, dot_size:float, height:int, width:int, array_white:list, color:list):
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