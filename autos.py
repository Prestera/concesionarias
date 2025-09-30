class Autos:
    def __init__(self, id ,marca, modelo, año, condicion=False,):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.condicion = condicion
        
             
    def mostrar_info(self):
        estado = "Nuevo" if self.condicion else "Usado"
        print(f"Id: {self.id} Marca: {self.marca}, Modelo: {self.modelo }, Año: {self.año}, Estado: {estado}")
       
         

            
        