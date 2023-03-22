import functions

#dict_prueba = functions.read_data("ExamenPython/winequality.csv")

dict_prueba = {
    "dato1": {
        "type": "white",
        "pfna": 1231,
        "ae": 448
    },
    "dato2": {
        "type": "red",
        "pfna": 111,
        "ae": 4888
    },
    "dato3": {
        "type": "white",
        "pfna": 0000,
        "ae": 111
    },
}

blanco, rosado = functions.split(dict_prueba)
functions.reduce(blanco, "ae")
try:
    functions.reduce(blanco, "hola")
except(ValueError):
    print("No se ha encontrado una ")