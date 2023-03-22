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
    
    return vinos


def split(diccionario):
    vino_blanco = dict()
    vino_rosa = dict()
    nDatoW = 0
    nDatoR = 0

    for llave, vinoDict in diccionario.items():
        llaves=list(vinoDict.keys())
        if vinoDict.get(llaves[0])  == "white":
            vino = {llaves[indice]: list(vinoDict.values())[indice] for indice in range(1,len(vinoDict))}
            vino_blanco.setdefault("Vino blanco nº:" + str(nDatoW), vino)
            nDatoW += 1
        if vinoDict.get(llaves[0])== "red": 
            vino = {llaves[indice]: list(vinoDict.values())[indice] for indice in range(1,len(vinoDict))}
            vino_rosa.setdefault("Vino rosado nº:" + str(nDatoR), vino)
            nDatoR += 1
    
    return vino_blanco, vino_rosa

def reduce(dict, string):
    lista_valores = list()

    for llave, vino in dict.items():
        llaves = list(vino.keys())
        print()
        for llave, valor in vino.items():
            
            if  string == list(valor.keys()):
                lista_valores.append(valor.get(string))
            else:
                raise(ValueError("No existe tal propiedad"))
    return lista_valores