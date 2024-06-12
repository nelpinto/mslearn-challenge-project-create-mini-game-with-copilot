# write 'hello world' to the console
print('hello world')

# la piedara le gana a las tijeras
# las tijeras le ganan al papel
# el papel le gana a la piedra
# si ambos jugadores eligen lo mismo es un empate
# el judador debe elegir entre piedra, papel o tijeras
# el programa debe elegir entre piedra, papel o tijeras
# el programa debe imprimir el resultado del juego
# el programa debe preguntar si se quiere jugar de nuevo
# si el jugador elige si, se debe repetir el juego
# si el jugador elige no, el programa debe terminar
# si el jugador elige una opcion invalida, el programa debe pedirle que ingrese una opcion valida
# el programa debe llevar un registro de los juegos ganados por el jugador y por el programa
# el programa debe imprimir el registro de juegos ganados al final del juego
# el programa debe preguntar si se quiere jugar de nuevo

def juego():
    import random
    opciones = ['piedra', 'papel', 'tijeras']
    jugador = input('ingrese piedra, papel o tijeras: ')
    while jugador not in opciones:
        jugador = input('ingrese una opcion valida: ')
    programa = random.choice(opciones)
    if jugador == programa:
        print('empate')
    elif jugador == 'piedra' and programa == 'tijeras':
        print('jugador gana')
    elif jugador == 'tijeras' and programa == 'papel':
        print('jugador gana')
    elif jugador == 'papel' and programa == 'piedra':
        print('jugador gana')
    else:
        print('programa gana')
    jugar_nuevo = input('jugar de nuevo? si/no: ')
    while jugar_nuevo not in ['si', 'no']:
        jugar_nuevo = input('ingrese una opcion valida: ')
    if jugar_nuevo == 'si':
        juego()
    else:
        print('gracias por jugar')

juego()        