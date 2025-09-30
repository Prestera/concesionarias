from autos import Autos

class Concesionaria:
    def __init__(self,nombre):
        self.nombre = nombre
        self.marca_auto = {}
        
    def agregar_autos(self, auto):
        if auto.marca not in self.marca_auto:
            self.marca_auto[auto.marca] = []
        self.marca_auto[auto.marca].append(auto)    
    
    
    def listar_autos(self):
        """Muestra todos los autos disponibles"""
        print(f"\nAutos en {self.nombre}:")
        if not self.marca_auto:
            print("No hay autos cargados todavía.")
        else:
            for  marca ,auto in self.marca_auto.items():
                #print(f"\nMarca: {marca}")
                for autos in auto:
                    autos.mostrar_info()           

    def buscar_autos(self, marca):
        return self.marca_auto.get(marca,[])
       
       
