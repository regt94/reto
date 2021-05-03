from json import load, decoder, dump
from time import sleep
from uuid import uuid4
from docente import Docente

data = {
    'alumnos_creados': [],
    'docentes_creados': []
}
      

class Alumno:
    def __init__(self, nombrealumno, maximanota, minimanota, promedio):
        self.nombrealumno = nombrealumno
        self.maximanota = maximanota
        self.minimanota = minimanota
        self.promedio = promedio

        

    def interfaz(self): # metodo de instancia
        while True:
            print('''
                Bienvenido al creador de Alumnos/Docentes : 
                ¿Que deseas hacer?
                1) Registrar notas de un Alumno o registrar un Docente
                2) Ver Alumnos/Docentes creados
                3) Salir del programa\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.configurar_Persona()
            elif opcion == "2": # else if
                pass
            elif opcion == "3":
                print("\nGracias por usar la aplicacion")
                sleep(1)
                quit()
            else:
                print("\nIntroduciste una opcion incorrecta")

################################Cargas#############################
    def cargar_Alumnos(self):
        try:
            archivo = open("Alumnos.json", "r")
            data["Alumnos_creados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de Alumnos...")
            sleep(1)
            archivo = open("Alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay Alumnos creados, se puede crear desde ahora")
    
    def cargar_Docentes(self):
        try:
            archivo = open("Docentes.json", "r")
            data["docentes_creados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de Docentes...")
            sleep(1)
            archivo = open("Docentes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay Docentes creados, se puede crear desde ahora")

##############################################################################

    def configurar_Persona(self):
        print('''\n¿Que deseas registrar?\n
            1) Nota de Alumno
            2) Docentes''')
        tipo = input("> ")
        if tipo == "1":
            self.clase_Alumno()
        elif tipo == "2":
            nombre = input('Ingrese el nombre del Docente \n')
            edad = input('Ingrese la edad del Docente \n')
            dni = input('Ingrese el DNI del Docente \n')
            self.registrar_Docente(nombre,edad,dni)

        else:
            print("\nHas introducido una raza erronea")

    def clase_Alumno(self):
        try:
            nombre=input('Ingrese el Nombre del alumno  \n')
            lista=[]
            for x in range(4):
                valor=int(input("Ingrese valor:"))
                lista.append(valor)

            mayor=lista[0]
            for x in range(1,4):
                if lista[x]>mayor:
                    mayor=lista[x]
            print(f"El número mayor es {mayor}")

            menor=lista[0]
            for y in range(1,4):
                if lista[y]<menor:
                    menor=lista[y]
            print(f"El número menor es {menor}")

            promedio = sum(lista) / len(lista)
            print(f"El promedio es {promedio}")

            self.registrar_Alumno(nombre, mayor, menor, promedio)


        except Exception as e:
            print(e.__class__.__name__)
            print(f"Ocurrion un problema {e}")


######################################Registro######################################
    def registrar_Alumno(self,  nombrealumno, maximanota, minimanota, promedio):
        try:
            
            nuevo_rg = Alumno(nombrealumno, maximanota, minimanota, promedio)
            datos = {
            
                "nombre": nuevo_rg.nombrealumno,
                "maximanota": nuevo_rg.maximanota,
                "minimanota": nuevo_rg.minimanota,
                "promedio": nuevo_rg.promedio
            }
            self.guardar_Alumno(datos)
            print(f"\nSe Registro el Alumno {nombrealumno} con exito")
        except Exception as e:
            print(e.__class__.__name__)
            print(f"Ocurrion un problema {e}")

    def registrar_Docente(self,  nombre,edad, dni):
        try:
            
            nuevo_rg = Docente(nombre,edad, dni)
            datos1 = {
            
                "nombre": nuevo_rg.nombre,
                "edad": nuevo_rg.edad,
                "dni": nuevo_rg.dni
                
            }
            self.guardar_Docente(datos1)
            print(f"\nSe Registro el Docente {nombre} con exito")
        except Exception as e:
            print(e.__class__.__name__)
            print(f"Ocurrion un problema {e}")
################################Guardar#############################################
    def guardar_Alumno(self, datos):
        data['alumnos_creados'].append(datos)
        alu = data['alumnos_creados']
        archivo = open("Alumnos.json", "w")
        dump(alu, archivo, indent=4)
        archivo.close()

    def guardar_Docente(self, datos):
        data['docentes_creados'].append(datos)
        alu = data['docentes_creados']
        archivo = open("Docentes.json", "w")
        dump(alu, archivo, indent=4)
        archivo.close()
    
#############################################################################################


class Start(Alumno):
    def __init__(self):
        try:
            self.cargar_Alumnos()
            self.cargar_Docentes()
            self.interfaz()
            
        except KeyboardInterrupt:
            print('\nAplicacion interrumpida')

Start()

