"""Crea un programa que pida al usuario ingresar dos números y luego le permita elegir una operación 
(suma, resta, multiplicación, división). Realiza la operación seleccionada e imprime el resultado."""



def opciones (): 
    num1 = int (input ("Ingresa el primer número:"))
    num2 = int (input ("Ingresa el segundo número:"))
    menu = int(input ("""Elige la operación: 
1) Suma 
2) Resta 
3) Multiplicación 
4) Division
5) Exit 
>>>""" ))
       
    if menu == 1:
        suma = (num1) + (num2)
        print ("El resultado de la suma es:", suma)

    elif menu == 2:
        resta = (num1) - (num2)
        print ("El resultado de la resta es:", resta)

    elif menu == 3:
        multiplicacion = (num1) * (num2)
        print ("El resultado de la multiplicació es:", multiplicacion)

    elif menu == 4:
        division = (num1) / (num2)
        print ("El resultado de la division es:", division)

    elif menu == 5:
        print ("Hasta pronto")
        exit ()

    else:
        print ("Opción inválida")

while True:
    opciones ()
