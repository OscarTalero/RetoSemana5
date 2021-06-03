from collections import deque
import funciones as func

cola = deque([11,22,33,44])
lista_postulados = [11,22,33,44]
estudiante = int(input('Ingresese estudiante: '))
resultado = func.validar(lista_postulados,estudiante)
func.inscribir(lista_postulados)

