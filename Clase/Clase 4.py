#
#import os
#os.path()
#os.getcwd()

#import glob
#path = os.getcwd()
#path
#glob.glob(path+'/*')

# def division(numero, divisor):
#   try:
#       return(numero/divisor)
#   except:
#       print("Mal ahi bro")

# Desafio 1
import re
with open(r"C:\Users\Mateo Sceia\Documents\Facultad Mateo\2do Año\1er Cuatri\Fundamentos de Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt","r") as myfile:
    print (myfile.read)
texto = (myfile.read)
print(re.search("-(.*)-", texto))

# Desafio 2
open(r"C:\Users\Mateo Sceia\Documents\Facultad Mateo\2do Año\1er Cuatri\Fundamentos de Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt","a")