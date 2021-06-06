from collections import deque
import funciones as func

lista_postulados = [11,22,33]
cola = deque()
op = 'S'

while op == 'S':
    estudiante = int(input('Ingrese el codigo del estudiante: '))
    resultado = func.validar(lista_postulados,estudiante,cola)
    op = input('Consultar otro estudiante? '+ ' Si(S) '+' No(N) ')

print('Total estudiantes inscritos: ',len(resultado))
contar_civil = 0
contar_sistemas = 0
contar_electronica = 0

for i in range(len(resultado)):
    contador = resultado[i].count('Ingenieria Civil')
    contar_civil += contador
    contador = resultado[i].count('Ingenieria de Sistemas')
    contar_sistemas += contador
    contador = resultado[i].count('Ingenieria Electronica')
    contar_electronica += contador
    contador = 0

print('Total inscritos en Ingenieria Civil: ',contar_civil)
print('Total inscritos en Ingenieria de Sistemas: ',contar_sistemas)
print('Total inscritos en Ingenieria Electronica: ',contar_electronica)
print('En promedio se inscribieron ',len(resultado)/3, ' estudiantes por programa')
