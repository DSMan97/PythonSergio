
import csv

def calcular_notas_finales():
    '''Aquí uso with open(ruta_archivo.csv) para leer su contenido'''
    with open('notas.csv') as csv_file:
        '''Aquí leo su contenido indicando el delimitador a usar'''
        csv_reader = csv.reader(csv_file, delimiter=',')
        '''Aquí inicializo el principio de lectura, linea 0'''
        line_count = 0
        '''Aquí realizo un bucle for para recorre la lineas del csv'''
        for row in csv_reader:
                '''Aquí realizo los cálculos con cada una de las notas'''
                ''' row[2] => control 1'''
                ''' row[3] => control 2'''
                ''' row[4] =>  examen'''
                '''He usado float para trata los valores obtenido como decimales'''
                '''He usado este fromato %.2f para quedarme solo con los 2 decimales '''
                control1_ponderado= float(str("%.2f" % (float(row[2])*(10/100))))
                control2_ponderado= float(str("%.2f" % (float(row[3])*(10/100))))
                examen_ponderado= float(str("%.2f" % (float(row[4])*(80/100))))
                ''' Aquí defino el examen sin ponderar para poderlo usar según las condiciones del enunciado: '''
                ''' "Si el estudiante ha suspendido el examen final, entonces la calificación final será la del examen." '''
                examen = float(row[4])

                '''Aquí se calcula la media con las notas ya ponderadas'''
                media = control1_ponderado+control2_ponderado+examen_ponderado
                '''Aquí defino el resultado aprobado o suspenso'''
                resutado = 'aprobado'

                '''Defino previamente el aprobado para tratar con los ifs los suspensos siendo de esta forma mas eficiente '''
                if (examen<5):
                        media = examen
                        resutado = 'suspenso'
                if(media<5):
                    resutado = 'suspenso'

                '''Aquí imprimo la salida por consola '''
                print(f'\t{row[0]}, {row[1]} {"%.2f" % media} {resutado}')
                '''Aquí añado 1 a la posición actual de la fila para poder recorrerlas durante el bucle for'''
                line_count += 1

if __name__ == '__main__':
    '''Aquí defino la sección main generada por el IDE (PyCharm) '''
    calcular_notas_finales()
    ''' Aquí llamo a la función'''


