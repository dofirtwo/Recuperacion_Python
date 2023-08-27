from empleado import Empleado
from negocio import Negocio
from cliente import Cliente
from datetime import datetime

negocio=Negocio()

def RegistrarCliente():
    nombre=input("Ingrese su nombre: ")
    sexo=input("Ingrese su genero(Masculino/Femenino): ").lower()
    correo=input("Ingrese su correo: ")
    celular=int(input("Ingrese su celular: "))
    cliente=Cliente(nombre,sexo,correo,celular)
    return cliente

def RegistrarEmpleado(especialidad):
    nombre=input("Ingrese el nombre del empleado: ")
    correo=input("Ingrese el correo del empleado: ")
    celular=int(input("Ingrese el celular del empleado: "))
    empleado=Empleado(nombre,correo,celular,especialidad)
    return empleado

def registrarCita():
    cliente = RegistrarCliente()
    if (cliente):
        idCita=int(input("Ingrese la Identificacion de la Cita: "))
        info=""
        listaEmpleados=[]
        listaServicios=[]
        while(info!="salir"):
            print("\t\t Ingrese el Servicio que desea Prestar")
            print("\tCorte de Cabello")
            print("\tMaquillaje y peinado")
            print("\tUñas")
            print("\tDiseño y depilado de cejas")
            print("\tTratamientos Capilares")
            print("Ingrese (Salir) si decesa Terminar de Registrar La Cita")
            info=input("Ingrese la opcion: ").lower()
            if (info=="corte de cabello"):
                listaServicios.append([info,15000])
                listaEmpleados.append(RegistrarEmpleado(info))  
            if (info=="maquillaje y peinado"):
                listaServicios.append([info,25000])
                listaEmpleados.append(RegistrarEmpleado(info))
            if (info=="uñas"):
                listaServicios.append([info,20000])
                listaEmpleados.append(RegistrarEmpleado(info))
            if (info=="diseño y depilado de cejas"):
                listaServicios.append([info,30000])
                listaEmpleados.append(RegistrarEmpleado(info))
            if (info=="tratamientos capilares"):
                listaServicios.append([info,60000])
                listaEmpleados.append(RegistrarEmpleado(info))
        negocio.registrarCitas(idCita,cliente,listaEmpleados,datetime.now(),listaServicios)
        print("Cita Agregada Correctamete")

def atenderCita():
    idCita=int(input("Ingrese la Identificacion de la Cita que desea anteder: "))
    citas = negocio.getListaCitas()
    negocio.atenderCitas(idCita)

x=0
while x!=6:
    print(f"\t\t Bienvenido a {negocio.getNombre()}")
    print("\t1. Registrar Cita")
    print("\t2. Atender Cita")
    print("\t3. Listar Citas Pendientes por Atender")
    print("\t4. Listar Citas Atendidas")
    print("\t5. Listar Citas Atendidas")
    print("\t6. salir")
    x= int(input("\tIngrese la opcion (1-6): "))
    if x==1:
        registrarCita()
    if x==2:
        atenderCita()
    if x==3:
        negocio.listarCitasPendientes()
    if x==4:
        negocio.listarCitasAtendidas()
    if x==5:
        negocio.listarClientes()