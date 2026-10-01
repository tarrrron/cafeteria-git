def calcular_total(subtotal):
    costo_delivery = 5.00
    total = subtotal + costo_delivery
    return total

subtotal = 30.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")