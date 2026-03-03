alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
texto_cifrado = input("El mensaje es: ").upper()
letra_interceptada = input("La letra interceptada es: ").upper()
letra_traducida = input("La equivalencia es con la letra: ").upper()

idx_cifrada = alfabeto.find(letra_interceptada)
idx_clara = alfabeto.find(letra_traducida)
clave = (idx_cifrada - idx_clara) % len(alfabeto)

mensaje_descifrado = ""
for letra in texto_cifrado:
    if letra in alfabeto:
        indx = (alfabeto.find(letra) - clave) % len(alfabeto)
        mensaje_descifrado += alfabeto[indx]
    else:
        resultado += letra


print(mensaje_descifrado) 