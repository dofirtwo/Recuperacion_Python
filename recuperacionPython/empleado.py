class Empleado():
    def __init__(self,nombre,correo,celular,especialidad):
        self.__nombre=nombre
        self.__correo=correo
        self.__celular=celular
        self.__especialidad=especialidad
        
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    def getCelular(self):
        return self.__celular
    def getEspecialidad(self):
        return self.__especialidad