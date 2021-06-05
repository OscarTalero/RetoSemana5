from collections import deque
import funciones as func

cola = deque([11,22,33,44])
lista_postulados = [11,22,33]
lista_est = []
op = 'S'
while op == 'S':
    estudiante = int(input('Ingrese estudiante: '))
    resultado = func.validar(lista_postulados,estudiante,lista_est)
    print(resultado)
    op = input('Consultar otro estudiante? '+ 'S '+'N')

