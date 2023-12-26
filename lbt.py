#Luis Simón Albarrán DNI: 48804855M

import sys

class Usuario:
    def __init__(self, nombre, contraseña, isAdmin=False):
        self.nombre = nombre
        self.contraseña = contraseña
        self.isAdmin = isAdmin

class Fallos:
    def __init__(self, usuario, nombre, descripcion, estado="abierto"):
        self.usuario = usuario
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.comentarios = []

    def cambiarEstado(self):
        if self.estado == "abierto":
            self.estado = "cerrado"
        else:
            self.estado = "abierto"

    def añadirComentario(self, usuarioComentario, comentario):
        self.comentarios.append(Comentario(usuarioComentario, comentario))
        print("Comentario añadido con éxito.")

class Comentario:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

def menuUsuario():
    global lista_fallos, usuario_logueado

    while True:
        print()
        print("\n** Menú de Usuario **")
        print("1. Crear un nuevo aviso de fallo")
        print("2. Seguir un aviso de fallo")
        print("3. Ver lista de avisos de fallo")
        print("4. Ver mis avisos de fallo")
        print("5. Buscar avisos de fallo")
        print("6. Cerrar sesión")
        print()

        if usuario_logueado:
            if usuario_logueado.isAdmin:
                print("\n** Funciones de Administrador **")
                print("7. Abrir/Cerrar un aviso de fallo como administrador")
                print("8. Borrar un aviso de fallo como administrador")

        opcion = input("Selecciona una opción: ")
"""
        if opcion == "1":
            nombre_fallo = input("Nombre del fallo: ")
            descripcion_fallo = input("Descripción del fallo: ")
            nuevo_fallo = Fallos(usuario_logueado, nombre_fallo, descripcion_fallo)
            lista_fallos.append(nuevo_fallo)
            print("Fallo creado con éxito.")

        elif opcion == "2":
            if usuario_logueado:
                id_fallo = input("Ingrese el ID del fallo que desea seguir: ")
                try:
                    id_fallo = int(id_fallo)
                    if 1 <= id_fallo <= len(lista_fallos):
                        fallo = lista_fallos[id_fallo - 1]

                        print("\nComentarios del fallo:")
                        for comentario in fallo.comentarios:
                            print(f"{comentario.usuario}: {comentario.texto}")

                        if fallo.estado == "cerrado":
                            print("Este aviso está cerrado, no puedes comentar en él.")
                        else:
                            agregar_comentario = input("¿Deseas agregar un comentario? (S/N): ").lower()
                            if agregar_comentario == "s":
                                comentario = input("Añade un comentario: ")
                                fallo.añadirComentario(usuario_logueado.nombre, comentario)
                    else:
                        print("ID de fallo fuera de rango.")
                except ValueError:
                    print("ID de fallo no válido.")

        elif opcion == "3":
            print("\nLista de Avisos de Fallo:")
            for index, fallo in enumerate(lista_fallos):
                print(f"ID: {index + 1}, Fallo: {fallo.nombre}, Estado: {fallo.estado}, Usuario: {fallo.usuario.nombre}")

        elif opcion == "4":
            print("\nTus Avisos de Fallo:")
            for index, fallo in enumerate(lista_fallos):
                if fallo.usuario.nombre == usuario_logueado.nombre:
                    print(f"ID: {index + 1}, Fallo: {fallo.nombre}, Estado: {fallo.estado}")

        elif opcion == "5":
            texto_busqueda = input("Introduce el texto a buscar en los avisos de fallo: ")
            resultados = buscarAvisosPorTexto(texto_busqueda)
            if not resultados:
                print("No se encontraron avisos que coincidan con la búsqueda.")
            else:
                print("\nAvisos de fallo que coinciden con la búsqueda:")
                for aviso in resultados:
                    print(f"ID: {aviso[0]}, Fallo: {aviso[1].nombre}, Estado: {aviso[1].estado}, Usuario: {aviso[1].usuario.nombre}")

        elif opcion == "6":
            print("Cerrando sesión...")
            usuario_logueado = None
            break

        elif opcion == "7" and usuario_logueado and usuario_logueado.isAdmin:
            id_fallo = input("Ingrese el ID del fallo que desea abrir/cerrar como administrador: ")
            try:
                id_fallo = int(id_fallo)
                if 1 <= id_fallo <= len(lista_fallos):
                    fallo = lista_fallos[id_fallo - 1]
                    fallo.cambiarEstado()
                    print(f"El estado del fallo '{fallo.nombre}' ha sido cambiado a '{fallo.estado}'.")
                else:
                    print("ID de fallo fuera de rango.")
            except ValueError:
                print("ID de fallo no válido.")

        elif opcion == "8" and usuario_logueado and usuario_logueado.isAdmin:
            id_fallo = input("Ingrese el ID del fallo que desea borrar como administrador: ")
            try:
                id_fallo = int(id_fallo)
                if 1 <= id_fallo <= len(lista_fallos):
                    fallo = lista_fallos[id_fallo - 1]
                    lista_fallos.pop(id_fallo - 1)  # Eliminar el fallo de la lista
                    print(f"El aviso de fallo '{fallo.nombre}' ha sido borrado.")
                else:
                    print("ID de fallo fuera de rango.")
            except ValueError:
                print("ID de fallo no válido.")

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
"""
def buscarAvisosPorTexto(texto):
    resultados = []
    for index, fallo in enumerate(lista_fallos):
        if texto.lower() in fallo.nombre.lower() or texto.lower() in fallo.descripcion.lower():
            resultados.append((index + 1, fallo))
    return resultados

def main():
    global usuario_logueado, lista_usuarios, lista_fallos
    lista_usuarios = [Usuario("usuario", "usuario"), Usuario("Lsa50", "ua"), Usuario("Pepe", "Phone"), Usuario("administrador", "administrador", True)]
    lista_fallos = [Fallos(Usuario("Lsa50", "ua"), "Problema al reportar un fallo", "No se incluye mi reporte a la lista", "cerrado"),
                    Fallos(Usuario("Pepe", "Phone"), "Error en los comentarios", "No me deja añadir comentarios en la sección de fallos")]
    lista_comentarios1 = [Comentario("usuario", "A mí sí me aparece tu reporte del fallo, refresca la aplicación"), Comentario("administrador", "Tu reporte sí que aparece en nuestra BBDD")]
    for comentario in lista_comentarios1:
        lista_fallos[0].comentarios.append(comentario)

    usuario_logueado = None

    op = ""
    while op != "3":
        print()
        print("******************************************************************")
        print("Bienvenido al Local Bug Tracker, escoja una opción del menú")
        print("******************************************************************")
        print()
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Salir")
        print()
        op = input("Opcion: ")
        print()
        print("******************************************************************")
        print()

        if op == "1":
            nombre = input("Introduce nombre usuario: ")
            contraseña = input("Introduce contraseña: ")
            logueado = False

            for user in lista_usuarios:
                if user.nombre == nombre and user.contraseña == contraseña:
                    usuario_logueado = user
                    print("Inicio de sesión correcto, Hola " + user.nombre + "!!")
                    logueado = True
                    menuUsuario()
                    break

            if not logueado:
                print("Inicio de Sesión incorrecto")

        elif op == "2":
            nombre = input("Introduce nombre usuario: ")
            contraseña = input("Introduce contraseña: ")
            registrado = False
            for user in lista_usuarios:
                if user.nombre == nombre:
                    print("Registro Incorrecto: El nombre de usuario introducido ya existe, elija otro")
                    registrado = True
                    break
            if not registrado:
                usuario_logueado = Usuario(nombre, contraseña)
                print("Registro correcto, Hola " + usuario_logueado.nombre + "!!")
                lista_usuarios.append(usuario_logueado)
                menuUsuario()

        elif op == "3":
            print("Hasta la próxima!!")
            sys.exit()
        else:
            print("Introduzca una opción válida del menú")

if __name__ == "__main__":
    main()
