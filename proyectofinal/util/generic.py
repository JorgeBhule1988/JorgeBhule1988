def centrar_ventana(ventana, ancho, largo):
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenwidth()
    x = int((pantalla_ancho/2) - (ancho/2))
    y = int((pantalla_largo/2) - (largo/2))
    return ventana.geometry(f"{ancho}x{largo}+{x}+{y}")


def mod(x):

    return x.value_counts().index[0]


def cm_to_pixel(value):

    return value/96
