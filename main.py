import json
def cargar_usuarios(biblioteca):
    try:
        with open(biblioteca, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def guardar_usuarios (biblioteca,usuarios):
    with open(biblioteca,mode="w") as file:
        json.dump(usuarios,file,indent=4)

def Agregar_usuarios (biblioteca):
    usuarios=cargar_usuarios(biblioteca)
    nuevo_usuario={
        "id":input("id:"),
        "nombre":input("nombre:"),
        "email":input("email"),
        "fecha_registro":input("fecha_registro:")
    }
    usuarios.append(nuevo_usuario)
    guardar_usuarios(biblioteca,usuarios)
    print("usuario agragado")

while True:
    
    print("*****************MUNDO LIBRO***************")
    print("1) mantenedor de usuarios")
    print("2) reportes")
    print("3) salir")
    try:    
        opc=int(input("ingrese una opcion"))
    except:
        print("ingrese una opcion valida")
        
        if opc==1:
            try:
                print("*******MANTENEDOR USUSARIO*******")
                print("1) Agregar usuario")
                print("2) editar usuario")
                print("3) eliminar usuario")
                print("4) buscar usuario")
                print("5) volver")
                opc1=int(input("ingrese una opcion"))    
            except:
                print("ingrese una opcion valida")
                
                    

                        
                    
                   
    
            

    
