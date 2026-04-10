def limpiar_texto(texto):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            resultado += letra.upper()
    return resultado

def obtener_factores(numero):
    factores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            factores.append(i)
    return factores

def kasiski_trigramas(texto_cifrado):
    texto = limpiar_texto(texto_cifrado)

    posiciones_trigramas = {}
    for i in range(len(texto) - 2):
        trigrama = texto[i:i+3]
        if trigrama in posiciones_trigramas:
            posiciones_trigramas[trigrama].append(i)
        else:
            posiciones_trigramas[trigrama] = [i]

    trigramas_repetidos = {}
    for t, posiciones in posiciones_trigramas.items():
        if len(posiciones) > 1:
            trigramas_repetidos[t] = posiciones

    if len(trigramas_repetidos) == 0:
        print("No hay trigramas repetidos")
        return

    print("Trigramas repetidos y posiciones:")
    for t, posiciones in trigramas_repetidos.items():
        print(f"{t} : {posiciones}")

    distancias = []
    for posiciones in trigramas_repetidos.values():
        for i in range(len(posiciones) - 1):
            distancias.append(posiciones[i+1] - posiciones[i])

    todos_los_factores = []
    for d in distancias:
        factores = obtener_factores(d)
        for f in factores:
            todos_los_factores.append(f)

    conteo = {}
    for f in todos_los_factores:
        if f in conteo:
            conteo[f] += 1
        else:
            conteo[f] = 1

    def obtener_frecuencia(elemento):
        return elemento[1]

    ordenado = list(conteo.items())
    ordenado.sort(key=obtener_frecuencia, reverse=True)

    print("\nPosibles longitudes de clave:")
    for i in range(min(5, len(ordenado))):
        print(f"Longitud: {ordenado[i][0]} | Aparece: {ordenado[i][1]} veces")

if __name__ == "__main__":
    texto = input("Ingresa texto cifrado: ")
    if texto.strip() == "":
        print("Error, no ingresaste texto")
    else:
        kasiski_trigramas(texto)
