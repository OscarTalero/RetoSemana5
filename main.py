from collections import deque
import funciones as func

lista_postulados = [11,22,33]
cola = deque()
op = 'S'
while op == 'S':
    estudiante = int(input('Ingrese estudiante: '))
    resultado = func.validar(lista_postulados,estudiante,cola)
    op = input('Consultar otro estudiante? '+ ' S '+' N  ')
print(resultado)
print('Total estudiantes inscritos: ',len(resultado))
for i in range(len(resultado)):
    contar_civil = resultado[i].count('Ingenieria Civil')
    contar_sistemas = resultado[i].count('Ingenieria de Sistemas')
    contar_electronica = resultado[i].count('Ingenieria Electronica')
print('Total postulados en Ingenieria Civil: ',contar_civil)
print('Total postulados en Ingenieria de Sistemas: ',contar_sistemas)
print('Total postulados en Ingenieria Electronica: ',contar_electronica)
print()
