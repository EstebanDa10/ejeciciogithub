import random

def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1, 10)
    
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número del 1 al 10.")
    
    while True:
      
        try:
            numero_usuario = int(input("Introduce tu adivinanza: "))
            
           
            if numero_usuario < 1 or numero_usuario > 10:
                print("Por favor, introduce un número entre 1 y 10.")
                continue
            
            
            if numero_usuario == numero_aleatorio:
                print("¡Ganaste! Adivinaste el número.")
                break
            else:
                print("Sigue intentando...")
        
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 10.")


juego_adivinanza()
