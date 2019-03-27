import csv

class CsvManager:
    def __init__(self): 
        """
        Constructor de la clase, esta se encarga de cargar la data
        del archivo csv en un diccionario para poder manejarlo facilmente
        """
        self.data = []
        with open('data.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                self.data.append(row)
                print(row)

    def save(self):
        """
        Esta funcion se encarga de guardar en el archivo csv la data modificada
        """
        with open('data.csv', 'w') as File:
            fieldnames = ['nombre', 'ci', 'edad','estado', 'nacionalidad', 'hora', 'fecha']
            writer = csv.DictWriter(File, fieldnames=fieldnames)
        
            writer.writeheader()
            for record in self.data:
                writer.writerow(record)
   
        print("save complete")

    def find(self, id):
        """
        Busca un registro a travez de su ID
        """
        for record in self.data:
            if id == record["ci"]:
                return {"status":True, "data":record}
        return {"status":False, "data":None}

    def getById(self):
        """
        Busca un registro a travez de su ID
        """
        id = input("Ingrese ci a buscar: ")
        print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format('NOMBRE', 'CI', 'EDAD','ESTADO', 'NACIONALIDAD', 'HORA', 'FECHA'))
        print("-------------------------------------------------------------------------------------------------------------------")
        for record in self.data:
            if id == record["ci"]:
                print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format(record["nombre"],record["ci"],record["edad"],record["estado"],record["nacionalidad"],record["hora"],record["fecha"]))


    def getByNombre(self):
        """
        Busca un registro a travez de su ID
        """
        nombre = input("Ingrese nombre a buscar: ")
        print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format('NOMBRE', 'CI', 'EDAD','ESTADO', 'NACIONALIDAD', 'HORA', 'FECHA'))
        print("-------------------------------------------------------------------------------------------------------------------")
        for record in self.data:
            if nombre in record["nombre"]:
                print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format(record["nombre"],record["ci"],record["edad"],record["estado"],record["nacionalidad"],record["hora"],record["fecha"]))

    def getByNacionalidad(self):
        """
        Busca un registro a travez de su ID
        """
        nacionalidad = input("Ingrese nacionalidad a buscar: ")
        print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format('NOMBRE', 'CI', 'EDAD','ESTADO', 'NACIONALIDAD', 'HORA', 'FECHA'))
        print("-------------------------------------------------------------------------------------------------------------------")
        for record in self.data:
            if nacionalidad in record["nacionalidad"]:
                print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format(record["nombre"],record["ci"],record["edad"],record["estado"],record["nacionalidad"],record["hora"],record["fecha"]))


    def printData(self):
        """
        Imprime por consola todos los registros del arvhivo csv
        """
        print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format('NOMBRE', 'CI', 'EDAD','ESTADO', 'NACIONALIDAD', 'HORA', 'FECHA'))
        print("-------------------------------------------------------------------------------------------------------------------")
        for record in self.data:
            print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format(record["nombre"],record["ci"],record["edad"],record["estado"],record["nacionalidad"],record["hora"],record["fecha"]))

    def delete(self):
        """
        Eliminar un registro
        """
        ci = input("Ingrese ci a eliminar: ")
        response = self.find(ci)
        if response["status"]:
            result = []
            for record in self.data:
                if record['ci'] != str(ci):
                    result.append(record)
            self.data = result
            print("Eliminacion exitosa")
        else:
            print("Eliminacion fallida")

    def create(self):
        """
        Crear un registro
        """
        nombre = input("Ingrese nombre: ")
        ci = input("Ingrese ci: ")
        edad = input("Ingrese edad: ")
        estado = input("Ingrese estado: ")
        nacionalidad = input("Ingrese nacionalidad: ")
        hora = input("Ingrese hora: ")
        fecha = input("Ingrese fecha: ")

        newRecord = {
            "nombre":nombre,
            "ci":ci,
            "edad":edad,
            "estado":estado,
            "nacionalidad":nacionalidad,
            "hora":hora,
            "fecha":fecha
        }
        self.data.append(newRecord)
        print("Creacion exitosa")

    def update(self):
        """
        Actualizar un registro
        """
        ci = input("Ingrese ci a modificar: ")
        response = self.find(ci)
        if response["status"]:
            response = response["data"]
            print("Se va a modificar: \n")
            print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format('NOMBRE', 'CI', 'EDAD','ESTADO', 'NACIONALIDAD', 'HORA', 'FECHA'))
            print("-------------------------------------------------------------------------------------------------------------------")
            print("|{:<32}|{:<10}|{:<5}|{:<15}|{:<20}|{:<15}|{:<15}".format(response["nombre"],response["ci"],response["edad"],response["estado"],response["nacionalidad"],response["hora"],response["fecha"]))

            nombre = input("Ingrese nombre: ")
            edad = input("Ingrese edad: ")
            estado = input("Ingrese estado: ")
            nacionalidad = input("Ingrese nacionalidad: ")
            hora = input("Ingrese hora: ")
            fecha = input("Ingrese fecha: ")

            newRecord = {
                "nombre":nombre,
                "ci":ci,
                "edad":edad,
                "estado":estado,
                "nacionalidad":nacionalidad,
                "hora":hora,
                "fecha":fecha
            }

            data = []

            for record in self.data:
                if record["ci"] == ci:
                    data.append(newRecord)
                else:
                    data.append(record)
            self.data = data
            print("Actualizacion exitosa")

        else:
            print("No se encontro ese ID")

    def sortById(self):
        """
        Ordenar por ID
        """
        newlist = sorted(self.data, key=lambda k: int(k['ci']))
        self.data = newlist
        self.printData()

    def sortByNombre(self):
        """
        Ordenar por nombre
        """
        newlist = sorted(self.data, key=lambda k:k['nombre'])
        self.data = newlist
        self.printData()

    def sortByNacionalidad(self):
        """
        Ordenar por nacionalidad
        """
        newlist = sorted(self.data, key=lambda k:k['nacionalidad'])
        self.data = newlist
        self.printData()
    
    def sortByEdad(self):
        """
        Ordenar por edad
        """
        newlist = sorted(self.data, key=lambda k:k['edad'])
        self.data = newlist
        self.printData()  
     
print("Por favor logueese para ingresar al menu:\n") 
user = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if(user != 'admin'):
    print("usuario incorrecto")
elif(password != 'admin'):
    print("contraseña incorrecta")
else:
    c = CsvManager()
    opc = 0

    while (opc != '12'):
        print("\nMENU\n")
        print("1. Ver data")
        print("2. Crear registro")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Ordenar por id")
        print("6. Ordenar por nombre")
        print("7. Ordenar por nacionalidad")
        print("8. Guardar")
        print("9. Buscar por ci")
        print("10. Buscar por nombre")
        print("11. Buscar por nacionalidad")
        print("12. Salir")

        opc = input("Seleccione una opcion: ")
        print("\n")
        if(opc == "1"):
            c.printData()
        elif(opc == "2"):
            c.create()
        elif(opc == "3"):
            c.update()
        elif(opc == "4"):
            c.delete()
        elif(opc == "5"):
            c.sortById()
        elif(opc == "6"):
            c.sortByNombre()
        elif(opc == "7"):
            c.sortByNacionalidad()
        elif(opc == "8"):
            c.save()
        elif(opc == "9"):
            c.getById()
        elif(opc == "10"):
            c.getByNombre()
        elif(opc == "11"):
            c.getByNacionalidad()
        elif(opc == "12"):
            print("Adios")
        else:
            print("Opcion incorrecta\n")