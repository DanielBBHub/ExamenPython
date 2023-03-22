def read_data(nombre_archivo):
    texto = open(nombre_archivo, mode="rt", encoding="utf-8")
    llaves = texto.readline().split(",")
    vinos = dict()
    long_fila = len(llaves)
    linea = texto.readline()
    nDato = 0

    while linea != "" :
        if len(datos:=linea.split(",")) == long_fila:
            vino = {llaves[indice]: datos[indice] for indice in range(len(datos))}
            vinos.setdefault("dato" + str(nDato), vino)
            nDato += 1
        linea = texto.readline()
    
    if nDato < 10:
        raise ValueError("Hay menos de 10 muestras con la informacion")
    
    return vinos


def split(diccionario):
    vino_blanco = dict()
    vino_rosa = dict()
    nDatoW = 0
    nDatoR = 0

    for llave, vinoDict in diccionario.items():
        llaves=list(vinoDict.keys())
        vino = {llaves[indice]: list(vinoDict.values())[indice] for indice in range(1,len(vinoDict))}

        if vinoDict.get(llaves[0])  == "white":

            vino_blanco.setdefault("Vino blanco nº:" + str(nDatoW), vino)
            nDatoW += 1

        if vinoDict.get(llaves[0])== "red": 

            vino_rosa.setdefault("Vino rosado nº:" + str(nDatoR), vino)
            nDatoR += 1

    return vino_blanco, vino_rosa

def reduce(dict, string):
    lista_valores = list()

    for llave, vino in dict.items():
        llaves = list(vino.keys())
        if string in llaves:
            lista_valores.append(vino.get(string))
        else:
            raise(ValueError("No existe tal propiedad"))

    return lista_valores


def silhouette(lista1, lista2):
    coef  = 0


    return coef