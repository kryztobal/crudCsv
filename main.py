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

    def save(self):
        """
        Esta funcion se encarga de guardar en el archivo csv la data modificada
        """
        with open('data.csv', 'w') as File:
            fieldnames = ['ID', 'nombre', 'apellido','edad']
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
            if id == record["ID"]:
                return {"status":True, "data":record}
        return {"status":False, "data":None}

    def getById(self):
        """
        Busca un registro a travez de su ID
        """
        id = input("Ingrese id a buscar: ")
        print("{:<5}{:<20}{:<20}{:<5}".format("Id","Nombre","Apellido","Edad"))
        for record in self.data:
            if id == record["ID"]:
                print("{:<5}{:<20}{:<20}{:<5}".format(record["ID"],record["nombre"],record["apellido"],record["edad"]))


    def getByNombre(self):
        """
        Busca un registro a travez de su ID
        """
        nombre = input("Ingrese nombre a buscar: ")
        print("{:<5}{:<20}{:<20}{:<5}".format("Id","Nombre","Apellido","Edad"))
        for record in self.data:
            if nombre == record["nombre"]:
                print("{:<5}{:<20}{:<20}{:<5}".format(record["ID"],record["nombre"],record["apellido"],record["edad"]))

    def getByApellido(self):
        """
        Busca un registro a travez de su ID
        """
        apellido = input("Ingrese apellido a buscar: ")
        print("{:<5}{:<20}{:<20}{:<5}".format("Id","Nombre","Apellido","Edad"))
        for record in self.data:
            if apellido == record["apellido"]:
                print("{:<5}{:<20}{:<20}{:<5}".format(record["ID"],record["nombre"],record["apellido"],record["edad"]))


    def printData(self):
        """
        Imprime por consola todos los registros del arvhivo csv
        """
        print("{:<5}{:<20}{:<20}{:<5}".format("Id","Nombre","Apellido","Edad"))
        for record in self.data:
            print("{:<5}{:<20}{:<20}{:<5}".format(record["ID"],record["nombre"],record["apellido"],record["edad"]))

    def delete(self):
        """
        Eliminar un registro
        """
        id = input("Ingrese id a eliminar: ")
        response = self.find(id)
        if response["status"]:
            result = []
            for record in self.data:
                if record['ID'] != str(id):
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
        apellido = input("Ingrese apellido: ")
        edad = input("Ingrese edad: ")

        lastIndex = 0
        for record in self.data:
            if lastIndex < int(record["ID"]):
                lastIndex = int(record["ID"])

        newRecord = {
            "ID":'{}'.format(lastIndex+1),
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad
        }
        self.data.append(newRecord)
        print("Creacion exitosa")

    def update(self):
        """
        Actualizar un registro
        """
        id = input("Ingrese id a modificar: ")
        response = self.find(id)
        if response["status"]:
            response = response["data"]
            print("Se va a modificar: \n")
            print("{:<5}{:<20}{:<20}{:<5}\n".format(response["ID"],response["nombre"],response["apellido"],response["edad"]))
            
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            edad = input("Ingrese edad: ")

            newRecord = {
                "ID":id,
                "nombre":nombre,
                "apellido":apellido,
                "edad":edad
            }

            data = []
            for record in self.data:
                if record["ID"] == id:
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
        newlist = sorted(self.data, key=lambda k: int(k['ID']))
        self.data = newlist
        self.printData()

    def sortByNombre(self):
        """
        Ordenar por nombre
        """
        newlist = sorted(self.data, key=lambda k:k['nombre'])
        self.data = newlist
        self.printData()

    def sortByApellido(self):
        """
        Ordenar por apellido
        """
        newlist = sorted(self.data, key=lambda k:k['apellido'])
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
        print("7. Ordenar por apellido")
        print("8. Guardar")
        print("9. Buscar por id")
        print("10. Buscar por nombre")
        print("11. Buscar por apellido")
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
            c.sortByApellido()
        elif(opc == "8"):
            c.save()
        elif(opc == "9"):
            c.getById()
        elif(opc == "10"):
            c.getByNombre()
        elif(opc == "11"):
            c.getByApellido()
        elif(opc == "12"):
            print("Adios")
        else:
            print("Opcion incorrecta\n")