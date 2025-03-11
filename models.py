#Definición del modelo de la tabla 'usuarios' en SQLAlchemy

from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios' #Define el nombre en la base de datos

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50), nullable = False)
    correo = Column(String(100), unique = True, nullable = False)