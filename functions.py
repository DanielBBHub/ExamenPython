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
            print(llaves)
            vino = {llaves[indice]: list(vinoDict.values())[indice] for indice in range(1,len(vinoDict))}
            vino_blanco.setdefault("dato" + str(nDatoW), vino)
            nDatoW += 1
            print(vino_blanco.items())
        if vinoDict.get(llaves[0])== "red": 
            print(llaves)
            vino = {llaves[indice]: list(vinoDict.values())[indice] for indice in range(1,len(vinoDict))}
            vino_rosa.setdefault("dato" + str(nDatoR), vino)
            nDatoR += 1
            print(vino_rosa.items())
    
    return vino_blanco, vino_rosa
