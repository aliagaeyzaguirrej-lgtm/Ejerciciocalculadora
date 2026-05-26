categoria_sucia = "  SeGuRiDaD  "
categoria = categoria_sucia.strip().upper()
print(f"Procesando el ticket de categoria: {categoria}")
match categoria:
    case "SOFWARE":
        print("ingresando al sofware")
    case "HARDWARE":
        print("ingresando al hardware")
    case "SEGURIDAD":
        print("Ingresando a seguridad")