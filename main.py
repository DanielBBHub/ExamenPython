import functions
dict_sol = dict()

try:
    dict_sol = functions.read_data("ExamenPython/winequality.csv")
except ValueError as err:
    print("Ha ocurrido la excepcion: " + str(err))

blanco, rosado = functions.split(dict_sol)

try:
    functions.reduce(blanco, "fixed acidity")
except(ValueError) as err:
    print("Ha ocurrido la excepcion: " + str(err))