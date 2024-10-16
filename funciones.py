

def trozado_de_texto(texto, participantes):
    """
     Funcionalidad: Dado un texto (se da uno por defecto) y un número de participantes, el programa entrega el texto
     partido en partes iguales para cada persona
    """

    por_palabras = texto.split()

    largo_texto = len(por_palabras)

    repartija = round(largo_texto/participantes)

    for i_cadena in range(0, len(por_palabras), repartija):

        inicio_cadena = i_cadena + repartija

        retazo = (por_palabras[i_cadena:inicio_cadena])

        concatenada = " ".join(retazo)

        print(concatenada)
