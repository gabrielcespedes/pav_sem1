from crud import *

salir = ''
while salir != 's':
    print("Ingrese datos del usuario a agregar:\n")
    nombre = input("Ingrese nombre de usuario: ")
    correo = input("Ingrese correo de usuario: ")
    agregar_usuario(nombre, correo)
    salir = input("Ingrese s si desea dejar de agregar usuarios, de lo contrario ENTER: ")

usuarios = obtener_usuario()

print("Lista de usuarios: ")

for usuario in usuarios:
    print(f'ID: {usuario.id}, nombre: {usuario.nombre}, correo: {usuario.correo}')

print("Actualización de usuario: ")

id_usuario = input("Ingrese id de usuario a actualizar")
nuevo_nombre = input("Ingrese nuevo nombre: ")
nuevo_correo = input("Ingrese nuevo correo: ")

actualizar_usuario(int(id_usuario), nuevo_nombre, nuevo_correo)

usuarios = obtener_usuario()

id_usuario_eliminar = input("Ingrese Id usuario a eliminar: ")

if id_usuario_eliminar.isdigit():
    eliminar_usuario(int(id_usuario_eliminar))
else:
    print("No se eliminó ningún usuario")

usuarios = obtener_usuario()

print("Usuarios después de los cambios:")

for usuario in usuarios:
    print(f'ID: {usuario.id}, nombre: {usuario.nombre}, correo: {usuario.correo}')