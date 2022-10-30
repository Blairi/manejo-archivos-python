import random

import sys
sys.path.insert(0,"..")
from database.TodosFile import TodosFile
from classes.Todo import Todo


class TodosService:

    def __init__(self) -> None:
        self.repositorio = TodosFile()

    
    def nuevo_todo(self, nombre : str, completado: bool) -> None:

        id = random.randint(0, 999999999)
        todo_nuevo = Todo(id, nombre, completado)
        self.repositorio.guardar_todo( todo_nuevo )

    
    def listar_todos(self) -> list[Todo]:

        resp = self.repositorio.listar_todos()

        todos = []
        for todo in resp:

            id, nombre, completado = todo

            todos.append( Todo( id, nombre, completado ) )

        return todos

    
    def actualizar_todo( self, id : int, nombre : str, completado : bool ) -> None:
        self.repositorio.actualizar_todo( Todo( id, nombre, completado ) )

    
    def borrar_todo(self, id : int) -> None:
        self.repositorio.eliminar_todo( id )
    