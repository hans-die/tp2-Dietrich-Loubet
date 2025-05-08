from PIL import Image

def interaction():
    print("--- Edicion de Imagenes ---")
    while True:
        imagen = input("Ingrese la ruta de la imagen: ")
        try:
            imagen_open = Image.open(imagen)
            break
        except FileNotFoundError:
            print("-La ruta de la imagen es invalida. Intente denuevo.")
            continue
    while True:
        metodo = input("Seleccione el método de cuantización (halftone/kmeans): ")
        if metodo.upper() == "HALFTONE" or metodo.upper() == "KMEANS":
            break
        else:
            print("-Ingrese Halftone o Kmeans. Intente denuevo")
            continue
    return metodo.upper(),imagen_open
def interaction_halftone():
    while True:
        dot_size_input = input("Ingrese el tamaño de los puntos (Aprieta enter para elegir el default): ").strip() #.strip para borrar postibles espacios
        if dot_size_input != "":
            try:
                dot_size = int(dot_size_input)
                if dot_size <= 0:
                    print("-El numero tiene que ser mayor que 0. Intente otra vez.")
                    continue
                else:
                    break
            except ValueError:
                print("-El numero es invalido. Intente denuevo.")
                continue
        else:
            dot_size = 5
            break
    while True:
        angles = input("Ingrese los ángulos de rotación para los canales RGB (Ej: 15,45,60. Si desea el default, presione enter): ").strip()
        if angles != "":
            try:
                angle_r, angle_g, angle_b = [x.strip() for x in angles.split(",")]
                break
            except ValueError:
                print("-El formato es invalido. Intente denuevo.")
                continue
        else:
            angle_r, angle_g, angle_b = 15, 45, 0
            break
    name = input("Ingrese el nombre para guardar la imagen: ")
    return dot_size, angle_r, angle_g, angle_b, name
def interaction_kmeans():
    while True:
        colors_input = input("Ingrese el numero de colores deseados (Ingrese enter para elegir el default): ").strip()
        if colors_input != "":
            try:
                colors = int(colors_input)
                if colors <= 0:
                    print("-El numero tiene que ser mayor que 0. Intente otra vez.")
                    continue
                else:
                    break
            except ValueError:
                print("-El numero es invalido. Intente denuevo.")
                continue
        else:
            colors = 8
            break
    return colors
