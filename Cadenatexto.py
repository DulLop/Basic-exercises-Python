#Pedir al usuario que ingrese una cadena de texto y contar cuántos caracteres tiene (sin contar espacios).

cadena = input ( "Ingrese una cadena de texto: ")

contador = 0

for caracter in cadena:
    if caracter != "" :
        contador += 1
 
print (contador)       