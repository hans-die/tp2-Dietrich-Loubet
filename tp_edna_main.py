from PIL import Image
import math
import numpy as np
import halftone_func as hf
import user_interaction as ui
import k_means_func as kf
import time
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta donde está el script
save_dir = os.path.join(BASE_DIR, "generated_photos")   #Solucion para guardar la imagen nueva en una carpeta sin margen de error.

counter = 0
while True:
    metodo, imagen_open, imagen  = ui.interaction() # El usuario carga la imagen y decide que metodo usar
    real_format = imagen.format
    #Halftone
    if metodo == "HALFTONE":
        dot_size, angle_r, angle_g, angle_b = ui.interaction_halftone()
        name = input("Ingrese el nombre para guardar la imagen: ").strip()
        start_time = time.time()
        print("🧬 Halftone Filter en ejecucion...")
        #Definimos la imagen y separamos en canales (RGB)
        r, g, b = hf.split_rgb(imagen_open)
        height, width = r.shape

        #CONSEGUIMOS LAS COORDENADAS DONDE ESTAN LOS PUNTOS CENTRALES PARA DIBUJAR EL CIRCULO
        chords_list_red = hf.get_grid_coords(height ,width ,dot_size ,angle_r)
        chords_list_green = hf.get_grid_coords(height ,width ,dot_size ,angle_g)
        chords_list_blue = hf.get_grid_coords(height ,width ,dot_size ,angle_b)

        #Dibujo el circulo para cada color
        new_r = hf.draw_circle(chords_list_red, dot_size, r)
        new_g = hf.draw_circle(chords_list_green, dot_size, g)
        new_b = hf.draw_circle(chords_list_blue, dot_size, b)

        #Se unen los tres canales y se guarda la imagen
        final_array = np.stack([new_r, new_g, new_b], axis = 2)
        new_image_h = Image.fromarray(final_array.astype(np.uint8))
        both_images = np.concatenate((imagen_open, final_array), axis = 1)

        elapsed = time.time() - start_time
        print(f"\n✅ Imagen guardada exitosamente en {elapsed:.2f} segundos.")

        preview_ht = Image.fromarray(both_images.astype(np.uint8))
        preview_ht.show()
        elapsed = time.time() - start_time
        counter += 1  #Para que no se sobre escriba en el caso que el usuario use el mismo nombre 2 veces.
        path_h = os.path.join(save_dir, f"{name}{counter}.{real_format.lower()}")
        new_image_h.save(path_h, format=real_format)
        #Continuar?
        if ui.ask_continue():
            continue
        else:
            break
    #K-means            
    else:
        clusters_quantity = ui.interaction_kmeans()
        name = input("Ingrese el nombre para guardar la imagen: ").strip()
        start_time = time.time() #Time
        print("🧠 K-Means quantization en ejecucion...")

        pixels_height, pixels_width, pixels_list, pixels = kf.get_all_pixels(imagen_open) 
        centroids, list_pixels_centroids = kf.find_centroids(pixels_list,clusters_quantity)
        pixels = kf.join_pixels(pixels, pixels_height, pixels_width, list_pixels_centroids, centroids)

        new_image_k = Image.fromarray(pixels.astype(np.uint8))
        both_images = np.concatenate((imagen_open,pixels), axis = 1)
       
        elapsed = time.time() - start_time
        print(f"\n✅ Imagen guardada exitosamente en {elapsed:.2f} segundos.")
        
        preview_km = Image.fromarray(both_images.astype(np.uint8))
        preview_km.show()
        counter += 1
        path_k = os.path.join(SAVE_DIR, f"{name}{counter}.{real_format.lower()}")
        new_image_k.save(path_k, format=real_format)
        #Continuar?
        if ui.ask_continue():
            continue
        else:
            break
