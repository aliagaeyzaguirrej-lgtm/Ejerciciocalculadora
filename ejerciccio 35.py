bodega = [
    {"nombre": "Mouse", "precio": 15000, "stock": 10},
    {"nombre": "Teclado", "precio": 25000, "stock": 0},
    {"nombre": "Monitor", "precio": 120000, "stock": 5},
    {"nombre": "Cable HDMI", "precio": 8000, "stock": 0}
]
print("informe de la bodega")
total_invercion= 0
for item in bodega:
    if item ["stock"] == 0:
        print(f"alerta el {item["nombre"]} esta agotado, pedir mas ")
    else:
        valor_en_stock = item ["precio"] * item["stock"]
        total_invercion += valor_en_stock
        print(f"{item["nombre"]}: hay {item["stock"]} unidades disponibles")
print("-"*30)
print(f"total capital invertido en stock: ${total_invercion}")
