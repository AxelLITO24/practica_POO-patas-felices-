class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio
    
    def actualizar_informacion(self, edad=None, salud=None, precio=None):
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio
    
    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"
    
class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_de_energia):
        super().__init__(nombre,edad,salud,precio)
        self.raza = raza
        self.nivel_de_energia = nivel_de_energia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de Energía: {self.nivel_de_energia}"

class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre,edad,salud,precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_caracteristicas(self):
         return f"Raza: {self.raza}, Independencia: {self.independencia}"

class Loro (Mascota):
    def __init__(self, nombre, edad, salud, precio, nivel_habla):
        super().__init__(nombre, edad, salud, precio)
        self.nivel_habla = nivel_habla
    
    def mostrar_caracteristicas(self):
        return f"Nivel de Habla: {self.nivel_habla}"


