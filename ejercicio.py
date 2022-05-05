#ingrese 3 notas y debe evaluar si aprueba o reprueba
notaUno = int(input("Ingrese primera nota porfavor: "))
notaDos = int(input("Ingrese segunda nota porfavor: "))
notaTres = int(input("Ingrese tercera nota porfavor: "))

notaTres = (notaUno + notaDos + notaTres)/3
if(notaTres>4): 
    print("aprobaste el ramo con nota: ",notaTres," Felicidades!!!!")
else:
    print("Reprobaste el ramo con nota: ",notaTres, "Mas suerte para la proxima campeón")