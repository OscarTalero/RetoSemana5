import datetime

def validar(lista_postulados, estudiante):
    for i in lista_postulados:
        if i == estudiante:
            print('Estudiante se encuentra en la lista')

def inscribir(lista_postulados):
    estudiantes = {}
    for i in range(len(lista_postulados)):
        print('Ingrese los datos del estudiante :')
        codigo = lista_postulados[i]     
        print('Codigo: ',codigo)
        identificacion = int(input('Ingrese la identificacion'))
        nombre = input('Ingrese el nombre')
        edad = input('Ingresese la edad; ')
        op = True
        while not False:
            print('Seleccione el programa al que desea inscibirse')
            print('1. Ingenieria Civil')
            print('2. Ingenieria de Sistemas')
            print('3. Ingenierlia Electronica')
            opcion = int(input())
            if opcion == 1 :
                programa = 'Ingenieria Civil'
            if opcion == 2 :
                programa = 'Ingenieria de Sistemas' 
            if opcion == 3 :
                programa = 'Ingenieria Electronica'
            if op > 0 or op < 4 :
                op = False
            fecha = datetime.datetime.today()
        estudiantes[codigo] = (identificacion,nombre,edad,programa,fecha)
        print(estudiantes)
    return estudiantes
