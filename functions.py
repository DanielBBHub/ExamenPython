def read_data(nombre_archivo):
    texto = open(nombre_archivo, mode="rt", encoding="utf-8")
    llaves = texto.readline().split(",")
    print(llaves)
    vinos = dict()
    long_fila = len(llaves)
    linea = texto.readline()
    i = 0

    while linea != "" :
        if len(datos:=linea.split(",")) == long_fila:
            vino = [llave:]
            vinos.setdefault("dato" + i, )
            i += 1
        linea = texto.readline()
        