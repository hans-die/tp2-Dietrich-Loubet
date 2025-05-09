from PIL import Image
import numpy as np
import math
import halftone_func as hf
import user_interaction as ui
#import K-means_func as kf

if __name__ == "__main__":
    while True:
        metodo, imagen_open = ui.interaction() # El usuario carga la imagen y decide que metodo usar
        if metodo == "HALFTONE":
            dot_size, angle_r, angle_g, angle_b, name_photo = ui.interaction_halftone()
            #DEFINIMOS LA IMAGEN Y SEPARAMOS EN CANALES
            r, g, b = hf.split_rgb(imagen_open)
            height, width = hf.height_width(r)

            #CONSEGUIMOS LAS COORDENADAS DONDE ESTAN LOS PUNTOS CENTRALES PARA DIBUJAR EL CIRCULO
            chords_list_red = hf.get_grid_coords(height ,width ,dot_size ,angle_r)
            chords_list_blue = hf.get_grid_coords(height ,width ,dot_size ,angle_g)
            chords_list_green = hf.get_grid_coords(height ,width ,dot_size ,angle_b)

            #Fondo blanco
            array_white_r = np.full((height, width),255, dtype = np.uint8)  
            array_white_g = np.full((height, width),255, dtype = np.uint8)
            array_white_b = np.full((height, width),255, dtype = np.uint8)

            #Dibujo el circulo para cada color
            new_array_white_r = hf.draw_circle(chords_list_red, dot_size, height, width, array_white_r, r)
            new_array_white_g = hf.draw_circle(chords_list_green, dot_size, height, width, array_white_g, g)
            new_array_white_b = hf.draw_circle(chords_list_blue, dot_size, height, width, array_white_b, b)

            #Se unen los tres canales y se guarda la imagen
            final_array = np.stack([new_array_white_r, new_array_white_g , new_array_white_b], axis=2)
            nueva_imagen = Image.fromarray(final_array.astype(np.uint8))
            both_images = np.concatenate((final_array,imagen_open), axis=1)
            muestra = Image.fromarray(both_images.astype(np.uint8))
            muestra.show("Concatenada.png")
            nueva_imagen.save(f"/Users/hansdietrich/Documents/VS/UDESA/TP2/imagenes_generadas/{name_photo}.png")
            decision = input('Si desea editar otra imagen presione enter, sino escriba "No": ')
            if decision == "":
                print("Recuerde no guardar la nueva imagen con el mismo nombre que la anterior.")
                continue
            else:
                print("Gracias por usar nuestro editor de imagenes.")
                break
        else:
            colors = ui.interaction_kmeans()
            break
