class Producto:
    def __init__(self,nombre, categoria,precio,cantidad):
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.cantidad=cantidad
    
    def actualizar_cant(self,cantidad):
        self.cantidad=cantidad
    
    def mostrar_info(self):
        return f"Producto{self.nombre}, Categoria{self.categoria}, precio{self.precio}, cantidad{self.cantidad} "