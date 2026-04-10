def descifrar_cuadrado_de_polibio(texto_cifrado):

    cuadrado = [
        ["A","B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U","V", "W", "X", "Y"],
    ]

    # Separar el texto cifrado en pares 
    pares = texto_cifrado.split() 
    texto_descifrado = ""

    for par in pares:
        if par.isdigit() and len(par) == 2:
            fila = int(par[0]) - 1  
            columna = int(par[1]) - 1
            texto_descifrado += cuadrado[fila][columna]
        else:
            texto_descifrado += par  

    return texto_descifrado

print("Ingresa el mensaje cifrado con espacios entre las letras")
texto_cifrado = input("Texto cifrado: ")
print("Texto descifrado:", descifrar_cuadrado_de_polibio(texto_cifrado))