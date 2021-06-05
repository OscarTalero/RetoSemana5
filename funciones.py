import datetime

def validar(lista_postulados, estudiante,lista_est):
    if estudiante in lista_postulados:
        print('Estudiante ',estudiante,'se encuentra en la lista')
        if lista_est:
            if lista_est[0][0] == estudiante:
                print("Ya inscrito")
            else:
                lista_est =inscribir(estudiante,lista_est)
        else:
            lista_est = inscribir(estudiante,lista_est)
    else:
        print('Estudiante',estudiante,' no se encuentra postulado')
    print(lista_est)
    return lista_est

def inscribir(estudiante,lista_est):
    print('Ingrese los datos del estudiante :')
    codigo = estudiante   
    print('Codigo: ',codigo)
    identificacion = int(input('Ingrese la identificacion: '))
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingresese la edad: ')
    op = True
    while op == True:
        print('Seleccione el programa al que desea inscibirse')
        print('1. Ingenieria Civil')
        print('2. Ingenieria de Sistemas')
        print('3. Ingenieria Electronica')
        opcion = int(input(':'))
        if opcion == 1 :
            programa = 'Ingenieria Civil'
        if opcion == 2 :
            programa = 'Ingenieria de Sistemas' 
        if opcion == 3 :
            programa = 'Ingenieria Electronica'
        if opcion > 0 or opcion < 4 :
            op = False
        fecha = datetime.datetime.today()
    estudiantes = [codigo,identificacion,nombre,edad,programa,fecha]
    lista_est.append(estudiantes)
    return lista_est
