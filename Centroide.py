# Ejercicio de Centroides
def calcular_centroide(coordenadas):  # Define una función que recibe una lista de coordenadas (x, y)
    
    A = 0      # Inicializa el área del polígono
    Cx = 0     # Inicializa la suma parcial para la coordenada x del centroide
    Cy = 0     # Inicializa la suma parcial para la coordenada y del centroide

    for i in range(len(coordenadas) - 1):  # Itera sobre cada par de puntos consecutivos
        xi, yi = coordenadas[i]            # Coordenadas del punto actual
        xi1, yi1 = coordenadas[i + 1]      # Coordenadas del siguiente punto
        paso = (xi * yi1 - xi1 * yi)  # Cálculo del determinante parcial (parte del área)
        A = A + paso                  # Acumula el área parcial
        Cx += (xi + xi1) * paso      # Acumula la suma para coordenada x del centroide
        Cy += (yi + yi1) * paso      # Acumula la suma para coordenada y del centroide

    A *= 0.5                          # Multiplica el área acumulada por 1/2 según la fórmula (A = A/2)

    #if A == 0:                        # Si el área resulta cero, el polígono no es válido
        #raise ValueError("El área es cero, revisa las coordenadas.")  # Lanza un error

    Cx /= (6 * A)                     # Calcula la coordenada x del centroide usando la fórmula
    Cy /= (6 * A)                     # Calcula la coordenada y del centroide usando la fórmula
    #return (Cx, Cy)
    return round(Cx, 2), round(Cy, 2)  

# Ejemplo de uso
coordenadas = [(0, 0), (4.35, 0), (4.35, 0.7), (1.38, 0.7), (1.38, 6), (1.13, 6), (0.6, 0.7), (0, 0.7), (0,0)]
centroide = calcular_centroide(coordenadas)
print(f"Centroide: {centroide}")
