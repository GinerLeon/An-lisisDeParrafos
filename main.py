codigo = [['A', 'ALFA'], ['B', 'BRAVO'], ['C', 'CHARLIE'], ['D', 'DELTA'], ['E', 'ECHO'], ['F', 'FOXTROT'], 
          ['G', 'GOLF'], ['H', 'HOTEL'], ['I', 'INDIA'], ['J', 'JULIETT'], ['K', 'KILO'], ['L', 'LIMA'], 
          ['M', 'MIKE'], ['N', 'NOVEMBER'], ['O', 'OSCAR'], ['P', 'PAPA'], ['Q', 'QUEBEC'], ['R', 'ROMEO'], 
          ['S', 'SIERRA'], ['T', 'TANGO'], ['U', 'UNIFORM'], ['V', 'VICTOR'], ['W', 'WHISKEY'], ['X', 'XRAY'], 
          ['Y', 'YANKEE'], ['Z', 'ZULU']]

# Función para buscar el codigo de lo que hayamos ingresado dentro de la lista codigo
def buscar(letra):
    for codigo_letra in codigo:
        if codigo_letra[0] == letra:
            return codigo_letra[1]
    

# Solicitar al usuario que ingrese el código
codigo_ingresado = input("Ingrese el código: ").upper() #El método devuelve una cadena donde todos los caracteres están en mayúsculas
#ignora las minisculas y los numeros

# Lista para almacenar el codigo de la lsita que corresponda a cada letra
codigo_earonautico = []

# Convertir cada letra del código ingresado a su código aronautico y agregarlo a la lista
for letra in codigo_ingresado:
    codigo_earonautico.append(buscar(letra))
    #El método anexa un elemento al final de la lista

# Unir los códigos en una sola cadena con espacios entre ellos utilizando el join que significa unir.
codigo_extendido = " ".join(codigo_earonautico)

# Mostrar el código extendido
print("Código extendido:")
print(codigo_extendido)