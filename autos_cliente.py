import json
from autos import Autos
from concesionarias import Concesionaria 
from config import concesionarias
ARCHIVO = "autos.json"


def agregar_auto():
    print("=== Agregar Auto ===")
       
    marca = input("Ingrese la marca del auto: ").lower()     
    modelo = input("Ingrese el modelo: ")
    año = int(input("Ingrese el año del auto: "))
    
    while True:
        condicion_input = input("¿El auto es 0 km? (si/no): ").lower()
        if condicion_input in ["si", "no"]:
            break
        print("Error: solo se permite 'si' o 'no'. Intenta de nuevo.")

    condicion = condicion_input == "si"
    
    id_nuevo = siguiente_id(concesionarias)
    auto = Autos(id_nuevo, marca, modelo, año, condicion)

    if marca.lower() in concesionarias:
        concesionaria = concesionarias[marca]
        concesionaria.agregar_autos(auto)
        print(f"Auto agregado a {concesionaria.nombre}")
        guardar_autos(ARCHIVO)
    else:
        print("Esa marca no tiene concesionaria registrada.")

def listar_autos():
    print("\n=== Listado de autos ===")
    for concesionaria in concesionarias.values():
        concesionaria.listar_autos()
        
def buscar_autos():
    nombre = input("Ingrese el nombre de la concesionaria del vehículo: ").lower()
    
    # Buscar la concesionaria que coincide con el nombre ingresado
    seleccionada = None
    for marca, concesionaria in concesionarias.items():
        if nombre in concesionaria.nombre.lower() :
            seleccionada = concesionaria
            break
    
    if not seleccionada:
        print("⚠️ Esa concesionaria no está registrada.")    
        return
    
    modelo = input("Ingrese el modelo a buscar (o presione Enter para ver todos): ").lower()
    
    autos = []
    for marca, lista_autos in seleccionada.marca_auto.items():
        for auto in lista_autos:
            if modelo == "" or auto.modelo.lower() == modelo:
                autos.append(auto)
    
    if autos:
        print(f"\nAutos en {seleccionada.nombre}:")
        for auto in autos:
            auto.mostrar_info()
    else:
        print("No se encontraron autos que coincidan con la búsqueda.")


def siguiente_id(concesionarias):
    ids = []
    
    #ids_existentes = sorted(auto['id'] for auto in concesionarias)
    #nuevo_id = 1
    for concesionaria in concesionarias.values():
        for lista_autos in concesionaria.marca_auto.values():
            for auto in lista_autos:
                try:
                    ids.append(int(auto.id))
                except Exception:
                    pass
    ids = sorted(set(ids))
    nuevo = 1
    for id_actual in ids:
        if id_actual == nuevo:
            nuevo += 1
        elif id_actual > nuevo:
            break
    return nuevo
                        
def guardar_autos(archivo):

    datos = []
    for concesionaria in concesionarias.values():
        for marca, lista_autos in concesionaria.marca_auto.items():
            for auto in lista_autos:
                datos.append({
                    "id": int(auto.id),
                    "concesionaria": concesionaria.nombre,
                    "marca": auto.marca.lower(),
                    "modelo": auto.modelo,
                    "año": auto.año,
                    "estado": bool(auto.condicion)
                })
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos,f, indent=4, ensure_ascii=False)                
    
def cargar_autos(archivo):
    try:
        with open(archivo,"r", encoding="utf-8") as f:
            datos = json.load(f)
            for d in datos:
                a = Autos(d["id"] ,d["marca"], d["modelo"], d["año"], d["estado"])
                for cons in concesionarias.values():
                    if cons.nombre.strip().lower() == d["concesionaria"].strip().lower():
                        cons.agregar_autos(a)
                        break
    except FileNotFoundError:
        print("No se encontró autos.json ")                
                    
def eliminar_auto():
    try:
        id_busqueda = int(input("Ingrese Id a eliminar: "))
    except ValueError:
        print("❌ Id no encontrado.")
    for concesionaria in concesionarias.values():
        for lista_autos in concesionaria.marca_auto.values():
            for a in list(lista_autos):
                if int(a.id) == id_busqueda:
                    lista_autos.remove(a)
                    print(f"El auto de id: {id_busqueda}, marca: {a.marca}. Ha sido eliminado de {concesionaria.nombre}")
                    guardar_autos(ARCHIVO)
                    return
    print("No se encontró ningún auto con ese ID.")
        
def editar_auto():    
    try:
        id_editar = int(input("Ingrese Id del auto a editar: "))
    except ValueError:
        return print("❌ Id mo encontrado. ") 
         
    for concesionaria in concesionarias.values():
        for lista_autos in concesionaria.marca_auto.values():
            for a in lista_autos:
                if int(a.id) == id_editar:
                    print("\n=== Editar Auto ===")
                    a.mostrar_info()
                    marca_original = a.marca.lower()
                    nueva_marca = input(f'Nueva marca (ENTER PARA MANTENER {a.marca}): ').strip()
                    if nueva_marca:
                        lista_autos.remove(a)
                        a.marca = nueva_marca
                        if nueva_marca in concesionarias:
                            concesionarias[nueva_marca].agregar_autos(a)                 
                            print(f'Auto movido a {concesionarias[nueva_marca].nombre} ')
                        else:
                            print("Esa marca no tiene concesionaria registrada, el auto queda sin registrar")    
                    
                    nuevo_modelo = input(f'Nuevo modelo (ENTER PARA MANTENER {a.modelo}): ').strip()
                    if nuevo_modelo:
                        a.modelo = nuevo_modelo 
                    try:
                        nuevo_año = input(f'Nuevo año (ENTER PARA MANTENER {a.año}): ').strip()               
                        if nuevo_año:
                            a.año = int(nuevo_año)
                    except ValueError:
                      print("⚠️ Año inválido, se mantiene el actual.")
                    
                    while True:
                        nueva_condicion = input(f"¿Es 0 km? (si/no, Enter para mantener '{'si' if a.condicion else 'no'}'): ").lower()               
                        if nueva_condicion in ["si", "no"]:
                            a.condicion = (nueva_condicion == "si")
                            break
                        elif nueva_condicion == "":
                            break
                        else: 
                            print("Error: sólo se permite 'si', 'no' o ENTER.")
                            
                    guardar_autos(ARCHIVO)
                    print("Auto editado con éxito.")        
                    return
    print("No se encontró ningún auto con ese ID.")            
        

def menu():
    while True:
        print("\n=== Menú Concesionarias ===")
        print("1. Agregar auto")
        print("2. Listar autos")
        print("3. Buscar autos por concesionaria")
        print("4. Eliminar auto")
        print("5. Editar auto")
        print("6. Salir")
        
        

        opcion = input("Elija una opción: ")
        

        if opcion == "1":
            agregar_auto()
        elif opcion == "2":
            listar_autos()
        elif opcion == "3":
            buscar_autos()
        elif opcion == "4":
            eliminar_auto()
        elif opcion == "5":
            editar_auto()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break            
        else:
            print("Opción inválida. Vuelva a intentarlo")
            
cargar_autos(ARCHIVO)
menu()            
       
            