from PIL import Image

def interaction():
    print("--- Edicion de Imagenes ---")
    while True:
        imagen = input("Ingrese la ruta de la imagen: ")
        try:
            imagen_open = Image.open(imagen)
            break
        except FileNotFoundError:
            print("")
            continue
    while True:
        metodo = input("Seleccione el método de cuantización (halftone/kmeans): ")
        if metodo.upper() == "HALFTONE" or metodo.upper() == "KMEANS":
            break
        else:
            print("-Ingrese Halftone o Kmeans. Intente denuevo")
            continue
    if metodo.upper() == "HALFTONE":
        while True:
            dot_size_input = input("Ingrese el tamaño de los puntos (Aprieta enter para elegir el default): ").strip() #.strip para borrar postibles espacios
            if dot_size_input != "":
                try:
                    dot_size = int(dot_size_input)
                    if dot_size > 0:
                        print("-El numero tiene que ser mayor que 0. Intente otra vez.")
                        break
                    else:
                        continue
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
    return dot_size, angle_r, angle_g, angle_b, metodo.upper()