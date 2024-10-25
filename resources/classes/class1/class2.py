num1 = 2
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
if  numero1.isnumeric() and numero2.isnumeric() :
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    print("La resta es: ", resta)
    print("La multiplicacion es: ", multiplicacion)
    print("La division es: ", division)
    print("La suma es: ", suma)
else:
    print("Los valores no son numericos")
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False