import os
os.system('clear')
bienvenida = """ 

    /--------------------------------------/
   /                                      /
  / Bienvenido a la tienda de bicicletas /
 /                                      /
/--------------------------------------/

"""

# Diccionario para usuarios
usuarios = {
    "christian": "12345678",
    "carlos": "12345678",
    "jordy": "123456abc"
}
# Funcion para inicio de sesion
def login(usuario, contrasena):
    if usuario in usuarios:
        if usuarios[usuario] == contrasena:
            return True
        else:
            return False
    else:
        return False

salir = False

# Funcion para registrar usuario
def registrar_usuario():
    nuevo_usuario = input("Ingrese un nombre de usuario: ").lower()
    if nuevo_usuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro")
    else:
        nueva_contrasena = input("Ingrese una nueva contrasena: ")
        usuarios[nuevo_usuario] = nueva_contrasena
        print(f"Usuario {nuevo_usuario} registrado exitosamente")

# Listar usuarios
def listar_usuarios():
    os.system('clear')
    print("Lista de todos los usuarios registrados")
    for usuario in usuarios:
        print(f"- {usuario}")

def gestion_articulos():
    while True:
        print("\nGestion de articulos (Bicicletas):\n")
        print("(1) Ingresar nueva bicicleta")
        print("(2) Modificar bicicleta")
        print("(3) Listar todas las bicicletas")
        print("(4) Eliminar bicicleta")
        print("(5) Buscar nueva bicicleta")
        print("(6) Volver al menú principal")
        
        opcion_articulo = int(input("\nSeleccione una opcion: "))
        
        if opcion_articulo == 1:
            ingresar_bicicleta()

        elif opcion_articulo == 6:
            break
        else:
            print("Opción no válida")

bicicletas = {}
""" 
        elif opcion_articulo == 2:
            modificar_bicicleta()
        elif opcion_articulo == 3:
            listar_bicicleta()
        elif opcion_articulo == 4:
            eliminar_articulo()
        elif opcion_articulo == 5:
            buscar_articulo()
"""
def ingresar_bicicleta():
    id_bicicleta = input("Ingresa un ID para la bicicleta: ")
    if id_bicicleta in bicicletas:
        print("El id de la bicicleta ya existe. Intenta con otro")
    else:
        atributos = {
            "marca": input("Ingrese la marca: "),
            "modelo": input("Ingrese el modelo: "),
            "tipo": input("Ingrese el tipo: "),
            "tamano": input("Ingrese el tamano: "),
            "color": input("Ingrese el color: "),
            "material": input("Ingrese el material: "),
            "precio": input("Ingrese el precio: "),
            "cantidad": input("Ingrese la cantidad: "),
            "velocidades": input("Ingrese las velocidades: "),
            "accesorios": input("Ingrese la marca de accesorios: ")
        }
        bicicletas[id_bicicleta] = atributos
        print(f"Bicicleta {id_bicicleta} ingresada exitosamente.")
            

while not salir:
    print(bienvenida)
    print("Menú de opciones:\n")
    print("(1) Gestión de usuarios")
    print("(2) Salir del sistema")
    opcion = int(input("\nSeleccione una opción: "))
    # Simulación de login
    if opcion == 1:
        print("\nGestión de Usuarios:\n")
        print("(1) Iniciar sesión")
        print("(2) Registrarse")
        print("(3) Modificar usuario o contraseña")
        print("(4) Buscar usuario")
        print("(5) Listar todos los usuarios")
        print("(6) Volver al menú principal")
        
        
        opcion_usuario = int(input("\nSeleccione una opción: "))
        
        if opcion_usuario == 1:
            usuario_input = input("Ingrese su nombre de usuario: ")
            contrasena_input = input("Ingrese su contraseña: ")
            
            if login(usuario_input, contrasena_input):
                print("Bienvenido al sistema")
                #incluir mas opciones del menu una vez autenticado
                gestion_articulos()
                continue
            else:
                print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
                
        elif opcion_usuario == 2:
            registrar_usuario()
            
        elif opcion_usuario == 5:
            listar_usuarios()
            
        elif opcion_usuario == 6:
            continue
            
        else:
            print("Opción no válida.")
    
    elif opcion == 2:
        print("Ha elegido salir del sistema...")
        break
    else:
        print("Debe elegir una opcion válida: ")