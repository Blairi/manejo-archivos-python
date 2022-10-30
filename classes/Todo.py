class Todo:
    
    id = None
    nombre = None
    completado = False

    def __init__(self, id : int|None, nombre : str, completado : bool) -> None:
        self.id = id
        self.nombre = nombre
        self.completado = completado
    
    def __str__(self) -> str:
        return f"Id: { self.id }\nNombre: { self.nombre }. { self.completado }"

    def get_id(self) -> int|None:
        return int(self.id)

    def get_nombre(self) -> str|None:
        return self.nombre

    def is_completado(self) -> bool:
        return self.completado