def cuadrado_de_polibio_cifrado(texto_claro):
    texto_claro = texto_claro.replace(" ", "").upper()

    cuadrado = [
        ["A","B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U","V", "W", "X", "Y"],
    ]

    texto_cifrado = []

    for letra in texto_claro:
        if letra.isalpha():
            for i, fila in enumerate(cuadrado):
                for j, letra_cuadrado in enumerate(fila):
                    if letra == letra_cuadrado:
                        texto_cifrado.append(str(i + 1) + str(j + 1))
        else:
            texto_cifrado.append(letra)

    return " ".join(texto_cifrado)  # Separa cada par con un espacio (aqui si use IA porque no supe como separarlo)

texto = input("Texto a cifrar: ")
print("El texto cifrado es:", cuadrado_de_polibio_cifrado(texto))