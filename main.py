import csv

print("Por favor logueese para ingresar al menu:\n") 
user = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

print(user,password)

def getAll():
    return 1

def getOne():
    return 1

def searchBy():
    return 1

def delete():
    return 1

def update():
    return 1

def create():
    return 1

def sortBy():
    return 1

results = []
with open('data.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print (results)


