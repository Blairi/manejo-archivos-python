import sys

sys.path.insert(0,"..")
from services.TodosService import TodosService

def menu():

    todos_service = TodosService()

    opc = -1
    while True:

        print("===================")
        todos = todos_service.listar_todos()
        for todo in todos:
            print(todo)
            print("---------------")
        print("===================")

        opc = int(input("0. Salir\n1. Agregar otro todo\n2. Actualizar todo\n3. Borrar todo\n"))

        if opc == 0:
            break

        elif opc == 1:
            nombre = input("Nombre del todo: ")
            todos_service.nuevo_todo( nombre, False )

        elif opc == 2:
            id = int(input("Id del todo a actualizar: "))
            nombre = input("Nuevo nombre del todo: ")
            completa = input("¿Ya esta completa?\n s : n ")

            todos_service.actualizar_todo( id, nombre, completa == "s" )

        elif opc == 3:
            id = int(input("Id del todo a borrar: "))
            todos_service.borrar_todo( id )

        else:
            print("No soportado")
    
menu()