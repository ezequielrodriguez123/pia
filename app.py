# ============================================
# PIA - Programación Avanzada
# Sistema de Gestión de Muebles de Oficina
# ============================================

# -------- CLASE COMENTARIO --------
class Comentario:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

    def mostrar(self):
        return self.autor + ": " + self.texto


# -------- CLASE PRODUCTO --------
class Producto:
    def __init__(self, id_producto, descripcion, marca):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.marca = marca
        self.comentarios = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def mostrar_producto(self):
        print("\nID:", self.id_producto)
        print("Descripción:", self.descripcion)
        print("Marca:", self.marca)

        print("Comentarios:")
        if len(self.comentarios) == 0:
            print("Sin comentarios")
        else:
            i = 0
            while i < len(self.comentarios):
                print("-", self.comentarios[i].mostrar())
                i += 1


# -------- FUNCIONES ARCHIVOS --------
def guardar_productos(lista_productos):
    archivo = open("productos.txt", "w", encoding="utf-8")

    i = 0
    while i < len(lista_productos):

        producto = lista_productos[i]

        linea = producto.id_producto + "|"
        linea += producto.descripcion + "|"
        linea += producto.marca

        archivo.write(linea + "\n")

        j = 0
        while j < len(producto.comentarios):

            comentario = producto.comentarios[j]

            linea_com = "COM|" + comentario.autor + "|"
            linea_com += comentario.texto

            archivo.write(linea_com + "\n")

            j += 1

        archivo.write("FIN\n")

        i += 1

    archivo.close()


def cargar_productos():
    productos = []

    try:
        archivo = open("productos.txt", "r", encoding="utf-8")

        lineas = archivo.readlines()

        archivo.close()

        producto_actual = None

        i = 0
        while i < len(lineas):

            linea = lineas[i].strip()

            partes = linea.split("|")

            if partes[0] == "COM":

                autor = partes[1]
                texto = partes[2]

                comentario = Comentario(autor, texto)

                producto_actual.agregar_comentario(comentario)

            elif linea == "FIN":

                productos.append(producto_actual)

            else:

                id_producto = partes[0]
                descripcion = partes[1]
                marca = partes[2]

                producto_actual = Producto(
                    id_producto,
                    descripcion,
                    marca
                )

            i += 1

    except:
        print("No existe archivo previo. Se creará uno nuevo.")

    return productos


# -------- FUNCIONES DEL SISTEMA --------
def buscar_producto(lista_productos, id_producto):

    i = 0

    while i < len(lista_productos):

        if lista_productos[i].id_producto == id_producto:
            return lista_productos[i]

        i += 1

    return None


def agregar_producto(lista_productos):

    print("\n--- AGREGAR PRODUCTO ---")

    id_producto = input("ID del producto: ")

    existe = buscar_producto(lista_productos, id_producto)

    if existe != None:
        print("Ese ID ya existe.")
        return

    descripcion = input("Descripción: ")
    marca = input("Marca: ")

    producto = Producto(id_producto, descripcion, marca)

    lista_productos.append(producto)

    guardar_productos(lista_productos)

    print("Producto agregado correctamente.")


def agregar_comentario(lista_productos):

    print("\n--- AGREGAR COMENTARIO ---")

    id_producto = input("ID del producto: ")

    producto = buscar_producto(lista_productos, id_producto)

    if producto == None:
        print("Producto no encontrado.")
        return

    autor = input("Nombre del autor: ")
    texto = input("Comentario: ")

    comentario = Comentario(autor, texto)

    producto.agregar_comentario(comentario)

    guardar_productos(lista_productos)

    print("Comentario agregado.")


def ver_producto(lista_productos):

    print("\n--- VER PRODUCTO ---")

    id_producto = input("ID del producto: ")

    producto = buscar_producto(lista_productos, id_producto)

    if producto == None:
        print("Producto no encontrado.")
    else:
        producto.mostrar_producto()


def ver_productos(lista_productos):

    print("\n--- TODOS LOS PRODUCTOS ---")

    if len(lista_productos) == 0:
        print("No hay productos registrados.")
    else:

        i = 0

        while i < len(lista_productos):

            lista_productos[i].mostrar_producto()

            print("----------------------")

            i += 1


def eliminar_producto(lista_productos):

    print("\n--- ELIMINAR PRODUCTO ---")

    id_producto = input("ID del producto: ")

    producto = buscar_producto(lista_productos, id_producto)

    if producto == None:
        print("El producto no existe.")
        return

    lista_productos.remove(producto)

    guardar_productos(lista_productos)

    print("Producto eliminado correctamente.")


def modificar_producto(lista_productos):

    print("\n--- MODIFICAR PRODUCTO ---")

    id_producto = input("ID del producto: ")

    producto = buscar_producto(lista_productos, id_producto)

    if producto == None:
        print("Producto no encontrado.")
        return

    nueva_descripcion = input("Nueva descripción: ")
    nueva_marca = input("Nueva marca: ")

    producto.descripcion = nueva_descripcion
    producto.marca = nueva_marca

    guardar_productos(lista_productos)

    print("Producto modificado correctamente.")


# -------- PROGRAMA PRINCIPAL --------
productos = cargar_productos()

opcion = ""

while opcion != "7":

    print("\n========== MENÚ ==========")
    print("1.- Agregar Producto")
    print("2.- Agregar Comentario")
    print("3.- Ver Producto")
    print("4.- Ver Productos")
    print("5.- Eliminar Producto")
    print("6.- Modificar Producto")
    print("7.- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto(productos)

    elif opcion == "2":
        agregar_comentario(productos)

    elif opcion == "3":
        ver_producto(productos)

    elif opcion == "4":
        ver_productos(productos)

    elif opcion == "5":
        eliminar_producto(productos)

    elif opcion == "6":
        modificar_producto(productos)

    elif opcion == "7":
        print("Saliendo del programa...")

    else:
        print("Opción inválida.")