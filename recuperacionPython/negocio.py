from cita import Cita
class Negocio():
    def __init__(self):
        self.__nombre="Glam-House"
        self.__ListaCitas=[]
        
    def getNombre(self):
        return self.__nombre
    def getListaCitas(self):
        return self.__ListaCitas
    
    def registrarCitas(self,idCita,cliente,empleado,fechaCita,servicios):
        cita = Cita(idCita,cliente,empleado,fechaCita,servicios)
        self.__ListaCitas.append(cita)
        
    def atenderCitas(self,idCita):
        for c in self.__ListaCitas:
            if (c.getIdCita()==idCita):
                c.setEstado()
                print("Persona Atendida Correctamente")
                
    def listarCitasPendientes(self):
        print("Lista de Citas Pendientes")
        for c in self.__ListaCitas:
            if (c.getEstado()=="PENDIENTE"):
                print("----------------------------------------")
                print("Nombre del Cliente:",c.getCliente().getNombre())
                for s in c.getServicios():
                    print("Servicios que Requiere:",s[0]," Costo:",s[1])
                for e in c.getEmpleado():
                    print("Empleados que lo Atenderan:",e.getNombre()," Especialidad:",e.getEspecialidad())
                print("Estado:",c.getEstado())
                print("----------------------------------------")

    def listarCitasAtendidas(self):
        print("Lista de Citas Atendidas")
        for c in self.__ListaCitas:
            if (c.getEstado()=="ATENDIDO"):
                print("----------------------------------------")
                print("Nombre del Cliente:",c.getCliente().getNombre())
                for e in c.getEmpleado():
                    print("Atendido por:",e.getNombre()," Especialidad:",e.getEspecialidad())
                print("Estado:",c.getEstado())
                print("----------------------------------------")
    
    def listarClientes(self):
        print("Lista de Clientes")
        for c in self.__ListaCitas:
            print("----------------------------------------")
            print("Nombre del Cliente:",c.getCliente().getNombre())
            print("Genero del Cliente:",c.getCliente().getSexo())
            print("Correo del Cliente:",c.getCliente().getCorreo())
            print("Celular del Cliente:",c.getCliente().getCelular())
            print("Estado:",c.getEstado())
            print("----------------------------------------")