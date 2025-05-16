from PIL import Image

def interaction():
    """
    Pide al usuario la ruta de la imagen y el metodo de cuantizacion.
    -------
    Returns: 
    -Metodo selecionado: str 
    -Imagen cargada: Image
    -Imagen sin convertida en rgb: Image
    """
    print("--- 🎨 Edicion de Imagenes 🎨 ---")
    while True:
        imagen = input("Ingrese la ruta de la imagen: ")
        try:
            imagen = Image.open(imagen)
            imagen_rgb = imagen.convert("RGB")
            break
        except FileNotFoundError:
            print("🚫 No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
            continue
    while True:
        metodo = input("Seleccione el método de cuantización (halftone/kmeans): ")
        if metodo.upper() == "HALFTONE" or metodo.upper() == "KMEANS":
            print(f"------ {metodo.upper()} ------\n")
            break
        else:
            print("Ingrese Halftone o Kmeans. Intente denuevo")
            continue
    return metodo.upper(), imagen_rgb, imagen
def interaction_halftone():
    """
    Pide al usuario el tamaño de los puntos y los angulos de rotacion para los canales RGB
    -------
    Returns:
    -Dot Size: int
    -Angles: int
    """
    while True:
        dot_size_input = input("Ingrese el tamaño de los puntos (Presione Enter para usar el valor por defecto): ").strip() #.strip para borrar postibles espacios
        if dot_size_input != "":
            try:
                dot_size = int(dot_size_input)
                if dot_size <= 0:
                    print("🚫 El numero tiene que ser mayor que 0. Intente otra vez.")
                    continue
                else:
                    print(f"✅ Dot size: {dot_size}")
                    break
            except ValueError:
                print("🚫 El numero es invalido. Intente denuevo.")
                continue
        else:
            dot_size = 5
            print("✅ - Dot Size default seleccionado: 5")
            break
    while True:
        angles = input("Ingrese los ángulos de rotación para los canales RGB (Ej: 15,45,60. Presione Enter para usar el valor por defecto): ").strip()
        if angles != "":
            try:
                angle_r, angle_g, angle_b = [int(x.strip()) for x in angles.split(",")]
                print(f"✅ Angulos: ({angle_r},{angle_g},{angle_b})")
                break
            except ValueError:
                print("🚫 El formato es invalido. Intente denuevo.")
                continue
        else:
            angle_r, angle_g, angle_b = 15, 45, 0
            print("✅ - Angulos default seleccionados: (15,45,60)")
            break
    return dot_size, angle_r, angle_g, angle_b
def interaction_kmeans():
    """
    Pide al usuario el numero de colores deseados.
    -------
    Return:
    -Colors: int
    """
    while True:
        colors_input = input("Ingrese el numero de colores deseados (Presione Enter para usar el valor por defecto): ").strip()
        if colors_input != "":
            try:
                colors = int(colors_input)
                if colors <= 0:
                    print("🚫 El numero tiene que ser mayor que 0. Intente otra vez.")
                    continue
                else:
                    print(f"✅ - Cantidad de colores default seleccionados: {colors}")
                    break
            except ValueError:
                print("🚫 El numero es invalido. Intente denuevo.")
                continue
        else:
            colors = 8
            print("✅ - Cantidad de colores default seleccionados: 8")
            break
    return colors

def ask_continue():
    """
    Pregunta al usuario si desea continuar editando otra imagen.
    ------
    Returns:
    - bool: True si quiere continuar, False si no.
    """
    decision = input('Presione Enter para volver a usar el editor, sino escriba "No": ')
    if decision == "":
        return True
    else:
        print("🥳 Gracias por usar nuestro editor de imagenes 🥳")
        return False
