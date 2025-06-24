data = {
    "usuarios": []
}

def buscar_usuario_por_nombre(nombre):
    for usuario in data["usuarios"]:
        if usuario["nombre"].lower() == nombre.lower():
            return None 
        
def buscar_usuario_por_clave(clave):
    for usuario in data  ["usuarios"]:
        if usuario ["clave"] == clave :
            return usuario 


def registrar_usuario():
    nombre = input("Nombre:").strip()
    if buscar_usuario_por_nombre(nombre):
        print("Nombre ya registrado en la base de datos.")
        return 
    try:
        edad = int(input("edad : "))
        if not (1 <= edad <= 100):
            print("Edad fuera de rango.")
            return 
    except ValueError:
        print("Edad inválida.")
        return
    genero = input("Genero (F/M):").strip().upper()
    if genero not in ("F", "M"):
        print("Genero Invalido.")
    clave = input("clave (8 caracteres alfanumericos):").strip().upper()
    if len (clave) != 8 or not clave.isalnum():
        print("clave invalida")
        return
    if buscar_usuario_por_clave(clave):
        print("clave ya registrada en la base de datos.")
        return 
    data ["usuarios"].append({
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "clave": clave
    })
    print("Usuario Registrado.")


def buscar_usuario():
    datos_usuario= input("Ingrese nombre o clave:").strip()
    usuario = buscar_usuario_por_clave(datos_usuario) or buscar_usuario_por_nombre(datos_usuario)
    if usuario:
        print(f"Nombre: {usuario['nombre']} Edad: {usuario['edad']} Genero: {usuario['genero']} Clave: {usuario['clave']}")
    else:
        print("Usuario no encontrado.") 



def eliminar_usuario():
    clave = input("Clave de usuario a eliminar:").strip()
    [usuarios] = buscar_usuario_por_clave(clave.lower()) or buscar_usuario_por_nombre(clave.lower())  
    if usuarios:
        data["usuarios"].remove(usuarios)
        print("Usuario eliminado con exito")
    else:
        print("No se pudo eliminar. No existe el usuario o se equivoco en la clave, vuelva a intentarlo")





    
def menu():
    while True:
        print("--- Menú ---")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir ") 
        
        
        opcion = (input("Ingrese una opcion entre (1-4):").strip())
        if opcion == "1":
          registrar_usuario()
        elif opcion == "2":
           buscar_usuario()    
        elif opcion == "3":
           eliminar_usuario()
        elif opcion == "4":
          print("Saliendo de la aplicacion !!")
          break
        else:
          print("Opcion no valida.(Ingrese una opcion entre (1-4))")   



menu() 