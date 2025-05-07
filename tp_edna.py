from PIL import Image
import numpy as np
import math
dot_size = 5 #LO PONE EL USUARIO
angle_r = 15
angle_g = 45
angle_b = 10
def get_grid_coords(h, w, dot_size, angle_deg):
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

def separar_rgb(imagen:str): #SEPARAMOS EN CANALES LA IMAGEN, ROJO VERDE, AZUL, Y RETORNAMOS LOS CANALES EN FORMA DE ARRAY
    imagen_open = Image.open(imagen)
    imagen_array = np.array(imagen_open)
    rojo = imagen_array[:,:,0]
    verde = imagen_array[:,:,1]
    azul = imagen_array[:,:,2]
    return rojo, verde, azul

def height_width(r,g,b): #ACA CONSEGUIMOS EL ANCHO Y ALTO DE CADA CANAL, PARA LUEGO PONERLO EN GET GRID COORDS
    height_red , width_red = r.shape
    height_blue , width_blue= g.shape
    height_green , width_green= b.shape
    return height_red, width_red, height_blue, width_blue, height_green, width_green

def draw_circle(chords_list:list, dot_size:float, height, width, array_white, color):
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

#DEFINIMOS LA IMAGEN Y SEPARAMOS EN CANALES
r, g, b = separar_rgb("/Users/hansdietrich/Documents/VS/UDESA/TP2/soccer.png")
height_red, width_red, height_blue, width_blue, height_green, width_green = height_width(r,g,b)



#CONSEGUIMOS LAS COORDENADAS DONDE ESTAN LOS PUNTOS CENTRALES PARA DIBUJAR EL CIRCULO
chords_list_red = get_grid_coords(height_red ,width_red ,dot_size ,angle_r)
chords_list_blue = get_grid_coords(height_blue ,width_blue ,dot_size ,angle_g)
chords_list_green = get_grid_coords(height_green ,width_green ,dot_size ,angle_b)

#Fondo blanco
array_white_r = np.full((height_red, width_red),255, dtype = np.uint8)  
array_white_g = np.full((height_green, width_green),255, dtype = np.uint8)
array_white_b = np.full((height_blue, width_blue),255, dtype = np.uint8)

#Dibujo el circulo para cada color
new_array_white_r = draw_circle(chords_list_red, dot_size, height_red, width_red, array_white_r, r)
new_array_white_g = draw_circle(chords_list_green, dot_size, height_green, width_green, array_white_g, g)
new_array_white_b = draw_circle(chords_list_blue, dot_size, height_blue, width_blue, array_white_b, b)

#Se unen los tres canales y se guarda la imagen
final_array = np.stack([new_array_white_r, new_array_white_gn , new_array_white_bn], axis=2)
nueva_imagen = Image.fromarray(final_array.astype(np.uint8))
nueva_imagen.save("imagen_invertida7.png")
