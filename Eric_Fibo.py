import sys
def fibonacci(nombre):
    a = 0
    b = 1
    if nombre == 0:
        print (nombre)
    while True:
        result = a + b
        if result > nombre:
            sys.exit(1)
        else:
            print (result)
            a = b
            b = result
            
def main ():

    nombre = raw_input("Jusqu'à quel nombre pour la suite de fibonacci: ")
    try:
        nombre=int(nombre)
    except:
        print("Erreur lors de la conversion du nombre.")
        main()
    fibonacci(nombre)
main()
