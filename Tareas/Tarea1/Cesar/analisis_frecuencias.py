alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
texto_cifrado = input("Mensaje cifrado: ").upper()

# Función para contar frecuencia de letras
def frecuencia_de_letras(texto):
    frec = {}
    for letra in texto:
        if letra in alfabeto:  
            frec[letra] = frec.get(letra, 0) + 1
    return frec

# Función para encontrar la letra más frecuente
def letra_mas_frecuente(frec):
    return max(frec, key=frec.get)

# Calcular desplazamiento
def calcular_desplazamiento(letra_cifrada, letra_clara='E'):
    i_cif = alfabeto.index(letra_cifrada)
    i_cla = alfabeto.index(letra_clara)
    return (i_cif - i_cla) % len(alfabeto)

# Descifrar 
def descifrar_cesar(texto, clave):
    resultado = ""
    for c in texto:
        if c in alfabeto:
            i = alfabeto.index(c)
            resultado += alfabeto[(i - clave) % len(alfabeto)]
        else:
            resultado += c 
    return resultado

def romper_cesar_por_frecuencia(texto_cifrado):
    frec = frecuencia_de_letras(texto_cifrado)
    letra_freq = letra_mas_frecuente(frec)
    clave = calcular_desplazamiento(letra_freq)
    texto_descifrado = descifrar_cesar(texto_cifrado, clave)
    return clave, letra_freq, texto_descifrado

desp, letra, claro = romper_cesar_por_frecuencia(texto_cifrado)

print("Letra más frecuente:", letra)
print("Clave encontrada:", desp)
print("Texto descifrado:")
print(claro)
