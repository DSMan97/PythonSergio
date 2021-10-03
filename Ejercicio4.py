# Pregunta del sistema al usuario para introducir valores
def tipo_triangulo (a,b,c):
    '''La función toma tres valores (a,b,c) como las caraas del triángulo.
    Posteriormente analiza si los datos aportados por el programa principal
    forman un triangulo aplicando la formula del triangulo;
    a continuación la función evalua que tipo de triangulo es (de serlo)
    y le aplica su tipología'''
    if c < (a+b) and (b+c)>a and a+c>b:
        if a == b and a == c:
            print('Equilatero')
        elif a == b or b == c or a == c:
            print('Isósceles')
        else:
            print('Escaleno')
    else:
        print('No es un triángulo')
'''Programa principal'''
tipo_triangulo(1, 1, 1)
tipo_triangulo(1, 3, 3)
tipo_triangulo(2, 4, 5)
tipo_triangulo(1, 2, 3)
tipo_triangulo(2, 1, 3)
tipo_triangulo(3, 2, 1)