def multi_numeros(NumeroMayor,NumeroMenor):

    suma = 0
 
    for i in range(NumeroMenor):

        suma = suma + NumeroMayor
        
    return suma


def div_numeros(Divisor,Dividendo):

    suma = 0
    DividendoOrig = Dividendo

    if Dividendo == 0 :
        return "No se puede dividir por 0"
    
 
    while multi_numeros(Dividendo,suma+1) <= Divisor:

        suma = suma + 1
        
    
        
    return suma
 




def Potencia_numeros(Numero,Potencia):

    suma = 1
 
    for i in range(Potencia):

        suma = multi_numeros(suma,Numero)
        
    return suma


def Factorial(Numero):

    suma = 1

    while Numero != 0:

        suma = multi_numeros(suma,Numero)

        Numero  = Numero-1

        
 
    
        
    return suma





def Polinomio(K,X,N):


    Tam = len(K)
    if Tam != N+1 :
        return "El vector es menor o mayor a N+1"



    suma = 0
    polinom = " "

    for i in range(N):


        Num = multi_numeros(Potencia_numeros(X,N-i),K[i])
        suma = suma + Num
        polinom = polinom + str(K[i]) + "*" + str(X) + "^" + str(N-i)+ " + "


    polinom = polinom + str(K[N])
    suma = suma + K[N]

    print polinom
        
        
    return suma

        
 
    
        
   



print multi_numeros(2,5)
print Potencia_numeros(3,4)
print Potencia_numeros(45,0)
print Factorial(5)
print div_numeros(1,0)
print div_numeros(20,5)
print Polinomio([4,2,1,10,20],2,4)
