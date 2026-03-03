def limpiar_texto(texto):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            resultado += letra.upper()
    return resultado

def obtener_factores(numero):
    factores = []
    for i in range(2, numero + 1):
        if numero % i == 0:
            factores.append(i)
    return factores

def kasiski_trigramas(texto_cifrado):
    texto = limpiar_texto(texto_cifrado)

    # Guardar posiciones de cada trigrama
    posiciones_trigramas = {}
    for i in range(len(texto) - 2):
        trigrama = texto[i:i+3]
        if trigrama in posiciones_trigramas:
            posiciones_trigramas[trigrama].append(i)
        else:
            posiciones_trigramas[trigrama] = [i]

    # Filtrar trigramas repetidos
    trigramas_repetidos = {}
    for t in posiciones_trigramas:
        if len(posiciones_trigramas[t]) > 1:
            trigramas_repetidos[t] = posiciones_trigramas[t]

    if len(trigramas_repetidos) == 0:
        print("No hay trigramas repetidos")
        return

    print("Trigramas repetidos y posiciones:")
    for t in trigramas_repetidos:
        print(t, ":", trigramas_repetidos[t])

    # Calcular distancias
    distancias = []
    for t in trigramas_repetidos:
        pos = trigramas_repetidos[t]
        for i in range(len(pos)-1):
            distancias.append(pos[i+1] - pos[i])

    # Obtener todos los factores
    todos_los_factores = []
    for d in distancias:
        f = obtener_factores(d)
        for num in f:
            todos_los_factores.append(num)

    # Contar frecuencia
    conteo = {}
    for f in todos_los_factores:
        if f in conteo:
            conteo[f] += 1
        else:
            conteo[f] = 1

    # Convertir a lista para ordenar
    ordenado = []
    for f in conteo:
        ordenado.append((f, conteo[f]))

    # Ordenar manualmente por frecuencia (mayor a menor)
    for i in range(len(ordenado)):
        for j in range(i+1, len(ordenado)):
            if ordenado[j][1] > ordenado[i][1]:
                temp = ordenado[i]
                ordenado[i] = ordenado[j]
                ordenado[j] = temp

    # Mostrar resultados
    print("Posibles longitudes de clave:")
    for i in range(min(5, len(ordenado))):
        print("Longitud:", ordenado[i][0], "Aparece:", ordenado[i][1], "veces")

if __name__ == "__main__":
    texto = input("Ingresa texto cifrado: ")
    if texto.strip() == "":
        print("Error, no ingresaste texto")
    else:
        kasiski_trigramas(texto)