class Cliente():
    def __init__(self,nombre,sexo,correo,celular):
        self.__nombre=nombre
        self.__sexo=sexo
        self.__correo=correo
        self.__celular=celular
        
    def getNombre(self):
        return self.__nombre
    def getSexo(self):
        return self.__sexo
    def getCorreo(self):
        return self.__correo
    def getCelular(self):
        return self.__celular