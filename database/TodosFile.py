import sys
sys.path.insert(0,"..")
from classes.Todo import Todo


class TodosFile:

    FILE_PATH = "./database/todos.txt"
    
    def guardar_todo(self, todo : Todo) -> None:

        file = open( self.FILE_PATH, "a" )
        file.write(f"{todo.id}|{todo.nombre}|{todo.completado}\n")
        file.close()


    def listar_todos(self) -> list:

        file = open( self.FILE_PATH, "r" )

        todos = list()
        for line in file:
            todos.append(tuple( line.rstrip().split("|") ))

        file.close()

        return todos


    def actualizar_todo( self, todo : Todo ) -> None:
        
        # Guardar los todos diferentes
        file = open( self.FILE_PATH, "r" )
        copia_todos = list()
        for line in file:

            todo_id = int( line.rstrip().split("|")[0] )
            
            if todo_id != todo.id:
                copia_todos.append( line.rstrip() )

        file.close()

        # escribir el nuevo todo
        file = open( self.FILE_PATH, "w" )
        file.write(f"{todo.id}|{todo.nombre}|{todo.completado}\n")
        file.close()

        # escribir la copia de los todos
        file = open( self.FILE_PATH, "a" )
        for copia_todo in copia_todos:
            id, nombre, completado = tuple( copia_todo.split("|") )
            file.write(f"{id}|{nombre}|{completado}\n")

        file.close()

    def eliminar_todo( self, id : int ) -> None:

        # Guardar los todos diferentes
        file = open( self.FILE_PATH, "r" )
        copia_todos = list()
        for line in file:

            todo_id = int( line.rstrip().split("|")[0] )

            if todo_id != id:
                copia_todos.append( line.rstrip() )

        file.close()

        # Reiniciar todos
        file = open( self.FILE_PATH, "w" )
        file.write("")
        file.close()

        # escribir la copia de los todos
        file = open( self.FILE_PATH, "a" )

        for copia_todo in copia_todos:

            id, nombre, completado = tuple( copia_todo.split("|") )
            file.write(f"{id}|{nombre}|{completado}\n")

        file.close()
