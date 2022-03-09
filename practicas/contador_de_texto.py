def cambiar_hora(tiempo):

    hora = int(tiempo[:2])
    minutos = int(tiempo[3:5])
    segundos = int(tiempo[6:8])
    ampm = tiempo[-2:]

    if hora < 12 and ampm == 'PM':
        hora = hora + 12
    else:
        hora = hora
    tiempo_12 = f'{hora:02d}:{minutos:02d}:{segundos:02d}'

    return tiempo_12

if __name__ == '__main__':
    print('Escribe la hora en este formato')
    print('Ejemplo: 07:05:23 PM/AM')
    tiempo = input('Dame la hora en el formato requerido: ')
    resultado = cambiar_hora(tiempo)
    print(resultado)


def contador(texto):

    vocales = 0
    consonantes = 0
    signos = 0
    numeros = 0
    cont_vocales = 'aeiou'
    cont_consonantes = 'bcdfghjklmnpqrstvwxyz'
    cont_signos = ',.-;:_!¡?¿#$%&/()=+*}{]['
    cont_numeros = '1234567890'

    for i in texto.lower():
        if i in cont_vocales:
            vocales += 1
        elif i in cont_consonantes:
            consonantes += 1
        elif i in cont_signos:
            signos += 1
        elif i in cont_numeros:
            numeros += 1
        else:
            pass

    return (vocales, consonantes, signos, numeros)

if __name__ == '__main__':
    palabra = input('dame un texto: ')
    resultado = contador(palabra)
    print('El total de vocales es: %i, el total de consonantes es: %i, el total de signos son: %i, el total de numero es: %i' % resultado)
    print(resultado)
