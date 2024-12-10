


from clase.mascota import Mascota

from clase.cliente import Cliente
from clase.inventario import Inventario
from clase.mascota import Loro, Perro, Gato
from clase.producto import Producto
from clase.venta import Venta




def registrar_mascota():
    tipo=input("ingrese el tipo de mascota ").strip().lower()
    if tipo not in["perro","gato","loro"]:
        print("mascota no reconocida ")
        return None
    else:
        nombre=input("ingrese el nombre de la mascota ")
        edad=int(input("ingrese la edad de la mascota "))
        salud=input("estado de salud de la mascota ")
        precio=float(input("cual es el precio de la consulta"))
        

    if tipo=="perro":
        raza=input("ingrese la raza del perro ")
        energia=input("como esta el nivel de energia del perro ")
        mascota= Perro (nombre,edad,salud,precio,raza,energia)
    elif tipo=="Gato":
        raza= input("raza del gato ")
        independencia=input("Nivel de independencia del gato ")
        mascota= Gato(nombre, edad, salud, precio, raza, independencia)
    elif tipo=="Loro":
        mascota==Loro(nombre, edad, salud, precio)
    else:
        print("mascota no reconocida ")
        return Mascota


def registrar_cliente():
    nombre= input("nombre del cliente ")
    direccion=input("direccion del cliente ")
    telefono=input("telefono del cliente ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre=input("ingrese su producto ").strip().lower()
    categoria=input("categoria del producto ")
    precio=input("precio del prodcuto ")
    cantidad=int(input("ingrese la cantidad "))
    producto=Producto(nombre, categoria,precio,cantidad)
    return producto

def registrar_ventas(clientes,inventario):
    nombre_cliente=input("nombre del cliente que desea buscar ")
    cliente= next ((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("cliente no encontrado ")
        return 
    
    productos=[]

    while True:
        nombre_producto=input("nombre del producto (deje vacio para terminar)")
        if not nombre_producto:
            break
        producto=next((p for p in inventario.lista_de_productos if p.nombre== nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("producto no encontrado ")
    
    if productos:
        venta=Venta(cliente,producto)
        venta.registrar_venta()
        print("venta registrada")
    else:
        print("no se registraron productos ")
    


def mostrar_menu():
    print("\n --- Menu de gestion patas felices ---")
    print("1) registrar mascota")
    print("2) registrar cliente")
    print("3) registrar producto")
    print("4) registrar venta")
    print("5) Mostrar info acerca de: Mascota ")
    print("6) Mostrar info acerca de: Cliente")
    print("7) Mostrar info acerca de: Producto")
    print("8) generar alerta inventario")
    print("9) salir")


def main():
    mascotas= []
    clientes = []
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion=input("seleccione una opcion ")

        if opcion=="1":
            mascota=registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("mascota registrada ")
        elif opcion=="2":
            cliente=registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("cliente registrado con exito ")
        elif opcion=="3":
            producto=registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("producto registrado ")
        elif opcion=="4":
            registrar_ventas(clientes,inventario)
        elif opcion=="5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota,Perro) or isinstance(mascota,Gato) or isinstance(mascota,Loro):
                    print(mascota.mostrar_caracteristicas())
        elif opcion=="6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        elif opcion=="7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_info())
        elif opcion=="8":
           umbral_min= int(input("ingrese el umbral minimo del inventario "))
           print(inventario.generar_alerta(umbral_min))
        elif opcion=="9":
            print("Gracias por usar patas felices app ")
            break
        else:
            print("opcion invalida, por favor seleccione una opcion valida ")
            opcion=input("seleccione una opcion")

if __name__ == "__main__":
   main()

            



