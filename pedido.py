def calcular_total(subtotal):
    descuento_estudiante = subtotal * 0.10
    total = subtotal - descuento_estudiante
    return total

subtotal = 30.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")