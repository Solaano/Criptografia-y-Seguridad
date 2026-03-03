alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje_cifrado = input("Mensaje Cifrado: ")

for clave in range(len(alfabeto)):
    mensaje_descifrado = ""
    
    for letra in mensaje_cifrado.upper():
        if letra in alfabeto:
            indice = alfabeto.find(letra)
            nuevo_indice = (indice - clave) % len(alfabeto)
            mensaje_descifrado += alfabeto[nuevo_indice]
        else:
            mensaje_descifrado += letra
    
    print(f"Clave {clave:02d}: {mensaje_descifrado}")