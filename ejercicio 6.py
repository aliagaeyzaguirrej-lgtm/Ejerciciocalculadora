clima= input("¿Cómo está el clima hoy?: ")
match clima:
    case "soleado, verano":
        print("se recomienda ponerse bloqueador solar")
    case "lluvioso":
        print("se recomineda llevar paraguas")
    case "nevado":
        print("se recomienda abrigarse")
    case "nublado":
        print("se recomienda estar en casa ")
    case _: 
        print(" no es encuentra ")
                   