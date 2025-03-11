#Funciones para realizar operaciones CRUD en la base de datos

from database import session
from models import Usuario

from sqlalchemy.exc import IntegrityError

def inicializar_bd():
    from database import Base, engine
    Base.metadata.create_all(engine)

def agregar_usuario(nombre, correo):
    try:
        nuevo_usuario = Usuario(nombre = nombre, correo = correo)
        session.add(nuevo_usuario)
        session.commit()
    except IntegrityError:
        session.rollback() #deshace cambios si hay error por clave única
        print(f"Error: El correo '{correo}' ya está registrado.")

def obtener_usuario():
    session.expire_all() #forzar actualizacion desde la Base de Datos
    return session.query(Usuario).all()

def buscar_usuario_correo(correo):
    return session.query(Usuario).filter_by(correo = correo).first()

def actualizar_usuario(id_usuario, nuevo_nombre, nuevo_correo):
    try:
        usuario = session.query(Usuario).filter_by(id = id_usuario).first()
        if usuario:
            #verificación si el nuevo correo ya está registrado por otro usuario
            if session.query(Usuario).filter(Usuario.correo == nuevo_correo, Usuario.id != id_usuario).first():
                print(f'Error: el correo "{nuevo_correo}" ya lo utiliza otro usuario.')
                return

            usuario.nombre = nuevo_nombre
            usuario.correo = nuevo_correo
            session.commit()
            session.refresh(usuario) #asegura que SQLAlchemy recargue los datos desde la base de datos

            print(f"Usuario con ID {id_usuario} actualizado correctamente")

        else:
            print(f'Usuario con Id {id_usuario} no encontrado.')
    except IntegrityError:
        session.rollback()
        print("No se pudo actualizar el usuario debido a una restricción de clave única.")

def eliminar_usuario(id_usuario):
    usuario = session.query(Usuario).filter_by(id = id_usuario).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        session.close() #Para liberar la sesión y evitar inconsistencias
    else:
        print(f'Usuario con Id {id_usuario} no encontrado.')
