nombre = input("Ingresa su nombre: ")
edad = input("Ingresa su edad: ")

cal1 = int(input("Ingresa su calificacion 1: "))
cal2 = int(input("Ingresa su calificacion 2: "))
cal3 = int(input("Ingresa su calificacion 3: "))

resultado = cal1 + cal2 + cal3
total = resultado/3

print (nombre , " Su resultado es: " , total)

if total >= 72:
     print("Aprobado")
else:
     print("Reprobaste")    
