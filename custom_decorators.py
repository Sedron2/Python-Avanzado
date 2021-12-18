def with_custom_message(message: str):
    def with_message(function):
        print(message)
        def wrapper(*args):
            function(*args) 
        return wrapper
    return with_message
#los args se ponen porque el wrapper es el que va a hacer de la funcion, y necesita los parametros de multiply, aunque se recomienda tambien ponerle un **kwargs
#esta funcion esta funcionando como cualquier otra pero necesita una funcion encima que necesita oto parametro
@with_custom_message("Hello")
def multiply(a, b):
    return a * b

multiply(10, 2)