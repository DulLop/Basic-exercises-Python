import random

def adivina ():
    numero_secreto = random.randint (1,100)
    intentos = 0

    print ("Adivina el número secreto del 1 al 100:"  )

    while True:
    
        num = int (input())
        intentos +=1

        if numero_secreto < num:
            print ("Demasiado alto, intenta de nuevo")

        elif numero_secreto > num:
            print ("Demasiado bajo, intenta de nuevo")

        else:
            print ("Corrrecto, adivinaste en", intentos, "Intentos")
            break

adivina ()

    
    
