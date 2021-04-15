import re
ruta = r"C:\Users\Mateo Sceia\Documents\Facultad Mateo\2do Año\1er Cuatri\Fundamentos de Informatica\practica 4\verso1" 
with open(ruta, "r") as Versos1:
    for linea in Versos1:
        if not (re.search("^P",linea)):
            contador=1
print(contador)
