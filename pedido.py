def calcular_total(subtotal):
    descuento_estudiante = subtotal * 0.10
    costo_delivery = 5.00
    total = subtotal - descuento_estudiante + costo_delivery
    return total

subtotal = 30.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")