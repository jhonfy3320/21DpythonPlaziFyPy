def get_packages_info(packages):
    total_weight = 0
    destinations = {}

    for package in packages:
        weight = package[1]
        destination = package[2]
        total_weight += weight

        if destination in destinations:
            destinations[destination] += 1
        else:
            destinations[destination] = 1

    rounded_total_weight = round(total_weight, 2)

    return {"total_weight": rounded_total_weight, "destinations": destinations}

packages = [
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
]

result = get_packages_info(packages)
print(result)
# Salida:
# {
#   "total_weight": 171.50,
#   "destinations": {
#     "Mexico": 3,
#     "Colombia": 4,
#     "Argentina": 3
#   }
# }
#Resultados en consola 
