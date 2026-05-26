clave_real= "python123"
contraseña=(input("ingrese contraseña: "))
if contraseña == clave_real:
    print("contraseña correcta ")
    print("ingresando...")
elif contraseña != clave_real:
    print("contraseña incorrecta")
    print("vuelva a intentarlo")