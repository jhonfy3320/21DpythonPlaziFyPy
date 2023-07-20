def find_set_intersection(sets):
    if not sets:
        return set()  # Retorna un conjunto vacío si la lista está vacía
    
    intersection = sets[0]  # Inicializa la intersección con el primer conjunto
    
    for s in sets[1:]:
        intersection = intersection.intersection(s)  # Realiza la intersección con cada conjunto
    
    return intersection

sets = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

result = find_set_intersection(sets)
print(result)
# Salida: {3, 4}