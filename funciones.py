import datetime


def validar(lista_postulados, estudiante,cola):
    '''Funcion que valida si el estudiante esta postulado o inscrito
    
    Parametros
    ----------
    lista_postulados : lista
    estudiante : int
    cola : cola

    Retorna
    -----------
    Retorna la cola con los estudiantes inscritos y sus datos
    '''
    if estudiante in lista_postulados:
        print('Estudiante ',estudiante,'se encuentra en la lista')
        if cola:
            if cola[0][0] == estudiante:
                print("Ya inscrito")
            else:
                cola =inscribir(estudiante,cola)
        else:
            cola = inscribir(estudiante,cola)
    else:
        print('Estudiante',estudiante,' no se encuentra en la lista')
        cola = inscribir(estudiante,cola)
    return cola


def inscribir(estudiante,cola):
    '''Funcion que inscribe a los estudiantes en un programa de la universidad

    Parametros
    ----------
    estudiante : int
    cola : cola

    Retorna
    ----------
    cola con los estudiantes inscritos
    '''
    print('Ingrese los datos del estudiante :')
    codigo = estudiante   
    print('Ingrese el codigo: ',codigo)
    identificacion = int(input('Ingrese la identificacion: '))
    nombre = input('Ingrese el nombre: ')
    edad = int(input('Ingresese la edad: '))
    print('Seleccione el programa al que desea inscribirse' )
    print('1. Ingenieria Civil')
    print('2. Ingenieria de Sistemas')
    print('3. Ingenieria Electronica')
    opcion = int(input(''))
    while opcion < 1 or opcion > 3:
        opcion = int(input('Digite un numero entre 1 y 3'))
    if opcion == 1 :
        programa = 'Ingenieria Civil'
    if opcion == 2 :
        programa = 'Ingenieria de Sistemas' 
    if opcion == 3 :
        programa = 'Ingenieria Electronica'
    fecha = datetime.datetime.today()
    fecha = fecha.strftime('%d %B %Y %H:%M:%S')
    estudiantes = [codigo,identificacion,nombre,edad,programa,fecha]
    cola.append(estudiantes)
    return cola