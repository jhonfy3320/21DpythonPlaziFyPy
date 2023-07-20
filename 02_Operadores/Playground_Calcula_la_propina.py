def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    rounded_tip_amount = round(tip_amount, 2)
    return rounded_tip_amount       # Salida: 10.0

print(calculate_tip(100, 10)) 
print(calculate_tip(1524.33, 25))
print(calculate_tip(1524.33, 25)) 
