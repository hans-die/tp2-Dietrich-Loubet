import numpy as np
from PIL import Image
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

def separateChannels(image):
    imagen=Image.open(r"C:\Users\loube\Documents\TP\test_images\alonso.jpeg")
    img_array=np.array(imagen)
    R,G,B=img_array[:,:,1],img_array[:,:,1],img_array[:,:,2]

    return R,G,B

R,G,B=separateChannels()

height_red,width_red=R.shape
height_blue,width_blue=B.shape
height_green,width_green=G.shape

dot_size=5 #LO PONE EL USUARIO
angle=15 #LO PONE EL USUARIO

chords_list_red=get_grid_coords(height_red,width_red,dot_size,angle)
chords_list_blue=get_grid_coords(height_blue,width_blue,dot_size,angle)
chords_list_green=get_grid_coords(height_green,width_green,dot_size,angle)

#new_red_channel = np.ones((height_red, width_red), dtype=np.uint8) * 255 EN DUDA , ES LO DE SUBIR TODO A 255 PERO NO ENTENDI MUY BIEN

for coordenada in chords_list_red:
    columna=coordenada[0]
    fila=coordenada[1]

    pixel_intensity=R[fila,columna]

    max_radius=dot_size/2
    radius = max_radius * (1 - pixel_intensity / 255)

    #FALTA DIBUJAR EL CIRCULO
