temperaturas = [20, 22, 19, 21]

for temp in range (len(temperaturas)-1):
    diferencia = []
    diff = temperaturas [temp+1] - temperaturas [temp]
    diferencia.append(diff)

    print(f"La diferencia entre la temperatura {temp+1} y la temperatura {temp} es: {diff}")