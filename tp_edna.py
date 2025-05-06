from PIL import Image
import numpy as np
import math

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

#DEFINIMOS LA IMAGEN Y SEPARAMOS EN CANALES
r, g, b = separar_rgb("/Users/hansdietrich/Documents/VS/UDESA/TP2/soccer.png")
height_red, width_red, height_blue, width_blue, height_green, width_green = height_width(r,g,b)

dot_size = 5 #LO PONE EL USUARIO
angle = 15,45,0 #here go there

#CONSEGUIMOS LAS COORDENADAS DONDE ESTAN LOS PUNTOS CENTRALES PARA DIBUJAR EL CIRCULO
chords_list_red = get_grid_coords(height_red ,width_red ,dot_size ,angle)
chords_list_blue = get_grid_coords(height_blue ,width_blue ,dot_size ,angle)
chords_list_green = get_grid_coords(height_green ,width_green ,dot_size ,angle)


array_white_r = np.full((height_red, width_red),255, dtype = np.uint8)  #Fondo blanco
array_white_g = np.full((height_green, width_green),255, dtype = np.uint8)
array_white_b = np.full((height_blue, width_blue),255, dtype = np.uint8)

for chord in chords_list_red:
    column = int(chord[0])
    row = int(chord[1])

    pixel_intensity = r[row,column]

    max_radius = dot_size/2
    radius = int(max_radius * (1 - pixel_intensity / 255))

    #RECORRO UNA CUADRICULA CERCA DEL CIRCULO QUE SE FIJE QUE PUNTOS ESTAN DENTRO DEL CIRCULO
    for i in range((row - radius),(row + radius)+1):  
        for j in range((column - radius),(column + radius)+1):
            if 0 <= i < height_red and 0 <= j < width_red: #SE FIJA SI ESTAMOS EN LA MATRIZ
                if (i - row)**2 + (j - column)**2 <= radius**2: #CHEQUEO ESTO DE ECUACION DADA
                    array_white_r[i, j] = 0 

for chord in chords_list_green:
    column = int(chord[0])
    row = int(chord[1])

    pixel_intensity = g[row,column]

    max_radius = dot_size/2
    radius = int(max_radius * (1 - pixel_intensity / 255))

    #RECORRO UNA CUADRICULA CERCA DEL CIRCULO QUE SE FIJE QUE PUNTOS ESTAN DENTRO DEL CIRCULO
    for i in range((row - radius),(row + radius)+1):  
        for j in range((column - radius),(column + radius)+1):
            if 0 <= i < height_green and 0 <= j < width_green: #SE FIJA SI ESTAMOS EN LA MATRIZ
                if (i - row)**2 + (j - column)**2 <= radius**2: #CHEQUEO ESTO DE ECUACION DADA
                    array_white_g[i, j] = 0 

for chord in chords_list_blue:
    column = int(chord[0])
    row = int(chord[1])

    pixel_intensity = b[row,column]

    max_radius = dot_size/2
    radius = int(max_radius * (1 - pixel_intensity / 255))

    #RECORRO UNA CUADRICULA CERCA DEL CIRCULO QUE SE FIJE QUE PUNTOS ESTAN DENTRO DEL CIRCULO
    for i in range((row - radius),(row + radius)+1):  
        for j in range((column - radius),(column + radius)+1):
            if 0 <= i < height_blue and 0 <= j < width_blue: #SE FIJA SI ESTAMOS EN LA MATRIZ
                if (i - row)**2 + (j - column)**2 <= radius**2: #CHEQUEO ESTO DE ECUACION DADA
                    array_white_b[i, j] = 0 
print("Forma R:", array_white_r.shape)
print("Forma G:", array_white_g.shape)
print("Forma B:", array_white_b.shape)
final_array = np.stack([array_white_r, array_white_g , array_white_b], axis=2)
nueva_imagen = Image.fromarray(final_array.astype(np.uint8))
nueva_imagen.save("imagen_invertida4.png")
print("Forma final_array:", final_array.shape)
