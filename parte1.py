def main():
    
    print("ingrese el nombre del archivo de cartas:")
    filename = input()
    file = open(filename,"r")
    
    linea = file.readline()
    cartas = linea.split(",")
    
    n = 0
    for i,carta in enumerate(cartas):
        cartas[i] = int(carta)
        n += 1

    opt = [[0]*n for i in range(n)]
    elecciones = [[0]*n for i in range(n)]

    k = 0
    while k < n:
        izq=0
        der=k
        while(der < n):

            if izq == der:
                opt[izq][der] = cartas[izq]
                elecciones[izq][der] = izq
            else:
            
                elijo_izq = (opt[izq][izq] - opt[izq+1][der])
                elijo_der = (opt[der][der] - opt[izq][der-1])

                if elijo_izq > elijo_der:
                    elecciones[izq][der] = izq
                    opt[izq][der] = elijo_izq
                else:
                    elecciones[izq][der] = der
                    opt[izq][der] = elijo_der
            izq += 1
            der += 1
        k += 1


    izq = 0
    der = n-1
    jugador = 0
    resultado = [[],[]] #cartas que eligió cada jugador
    puntajes = [0,0] #puntos de cada jugador

    while izq<=der:
        
        eleccion = elecciones[izq][der] #lado que elije
        carta_elegida = cartas[eleccion] #la carta que estaba en ese lado
        resultado[jugador].append(str(carta_elegida))
        puntajes[jugador] += carta_elegida
        jugador = (jugador+1)%2 #cambio de jugador
        
        if eleccion == izq:
            izq+=1
        else:
            der-=1
        
    for i in range(0,2):
        print("Jugador",i + 1,":")
        print("Cartas elegidas: " + ",".join(resultado[i]))
        print("Puntos sumados",puntajes[i])
    
        

    


main()
        