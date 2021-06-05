from collections import deque
import funciones as func

lista_postulados = [11,22,33]
cola = deque()
lista_est = []
op = 'S'
while op == 'S':
    estudiante = int(input('Ingrese estudiante: '))
    resultado = func.validar(lista_postulados,estudiante,cola)
    print(resultado)
    op = input('Consultar otro estudiante? '+ 'S '+'N')


