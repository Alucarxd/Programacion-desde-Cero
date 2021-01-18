print ("Digiti el ano")
anio = int(input())

if(anio % 4 == 0 and anio % 100 != 0) or anio % 400 ==0:
    print ("Ano bisiento")
else:
    print ("Ano NO bisiesto")