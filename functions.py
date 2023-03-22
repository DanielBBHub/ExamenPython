def read_data(nombre_archivo):
    texto = open(nombre_archivo, mode="rt", encoding="utf-8")
    llaves = texto.readline().split(",")
    vinos = dict()
    long_fila = len(llaves)
    linea = texto.readline()
    i = 0

    while linea != "" :
        if len(datos:=linea.split(",")) == long_fila:
            for indice in range(len(datos)):
                vino = {llave: datos[indice] for llave in llaves }
                #print(vino)
            vinos.setdefault("dato" + str(i), vino)
            i += 1
        linea = texto.readline()
    
    print(vinos)