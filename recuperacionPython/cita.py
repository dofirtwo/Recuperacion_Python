class Cita():
    def __init__(self,idCita,cliente,empleado,fechaCita,servicios):
        self.__idCita=idCita
        self.__cliente=cliente
        self.__empleado=empleado
        self.__estado="PENDIENTE"
        self.__fechaCita=fechaCita
        self.__servicios=servicios
    
    def getIdCita(self):
        return self.__idCita   
    def getCliente(self):
        return self.__cliente
    def getEmpleado(self):
        return self.__empleado
    def getFechaCita(self):
        return self.__fechaCita
    def getServicios(self):
        return self.__servicios
    def getEstado(self):
        return self.__estado
    
    def setEstado(self):
        if(self.__estado=="PENDIENTE"):
            self.__estado="ATENDIDO"
        else:
            self.__estado="PENDIENTE"
