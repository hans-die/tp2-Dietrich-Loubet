import numpy as np
from PIL import Image
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

large,height=R.shape()
dot_size=5 #LO PONE EL USUARIO
angle=15 #LO PONE EL USUARIO
chords_R=get_grid_coords(large,height,dot_size,angle)
