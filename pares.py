import tarjetas

"""
    Manos ganadoras en orden descendente:
    1 -> poker + 1 tercia
    2 -> poker + 1 par
    3 -> poker (cuatro del mismo simbolo)
    4 -> full + 1par
    5 -> full (tercia + 1 par)
    6 -> color (todas cartas mismo palo)
    7 -> 2 tercias
    8 -> 3 pares
    9 -> 1 tercia
    10 -> 2 pares
    11 -> 1 par
    12 -> carta más alta
"""

def ganador(A,B):
    winner=""
    jugada1=comprobar_jugada(A)
    jugada2=comprobar_jugada(B)
    winner=definir_ganador(jugada1,jugada2,A,B)
    return winner

def definir_ganador(jugada1,jugada2,A,B):
    dic={"carta más alta":1,"1 par":2,"2 pares":3,"1 tercia":4,"3 pares":5,"2 tercias":6,
        "color":7,"full":8,"full + 1 par":9,"poker":10,"poker + 1 par":11,"poker + 1 tercia":12}
    jugador1=dic[jugada1]
    jugador2=dic[jugada2]
    winner=""
    if jugador1>jugador2:
        winner="El ganador es el jugador 1 con la jugada de "+jugada1
    if jugador2>jugador1:
        winner="El ganador es el jugador 2 con la jugada de "+jugada2
    if jugador1==jugador2:
        winner=definir_ganador_por_puntos(jugada1,A,B)
    return winner

def definir_ganador_por_puntos(jugada,A,B):
    winner=""
    puntos1=0
    puntos2=0
    if jugada=="carta más alta":
        winner=mayor(A.mano,B.mano,jugada)
    if jugada=="1 par":
        winner=mayor(A.pares,B.pares,jugada)
    if jugada=="2 pares":
        winner=mayor(A.pares,B.pares,jugada)
    if jugada=="1 tercia":
        winner=mayor(A.tercias,B.tercias,jugada)
    if jugada=="3 pares":
        winner=mayor(A.pares,B.pares,jugada)
    if jugada=="2 tercias":
        winner=mayor(A.tercias,B.tercias,jugada)
    if jugada=="color":
        winner=mayor(A.color,B.color,jugada)
    if jugada=="full":
        puntos1,puntos2=mayor(A.tercias,B.tercias,jugada)
        p1=puntos1
        p2=puntos2
        puntos1,puntos2=mayor(A.pares,B.pares,jugada)
        p1+=puntos1
        p2+=puntos2
    if jugada=="full + 1 par":
        puntos1,puntos2=mayor(A.tercias,B.tercias,jugada)
        p1=puntos1
        p2=puntos2
        puntos1,puntos2=mayor(A.pares,B.pares,jugada)
        p1+=puntos1
        p2+=puntos2
        if p1>p2:
            winner="Gana jugador 1 con un total de "+str(p1)+" puntos"
        if p2>p1:
            winner="Gana jugador 2 con un total de "+str(p2)+" puntos"
    if jugada=="poker":
        winner=mayor(A.poker,B.poker,jugada)
    if jugada=="poker + 1 par":
        puntos1,puntos2=mayor(A.poker,B.poker,jugada)
        p1=puntos1
        p2=puntos2
        puntos1,puntos2=mayor(A.pares,B.pares,jugada)
        p1+=puntos1
        p2+=puntos2
        if p1>p2:
            winner="Gana jugador 1 con un total de "+str(p1)+" puntos"
        if p2>p1:
            winner="Gana jugador 2 con un total de "+str(p2)+" puntos"
    if jugada=="poker + 1 tercia":
        puntos1,puntos2=mayor(A.poker,B.poker,jugada)
        p1=puntos1
        p2=puntos2
        puntos1,puntos2=mayor(A.tercias,B.tercias,jugada)
        p1+=puntos1
        p2+=puntos2
        if p1>p2:
            winner="Gana jugador 1 con un total de "+str(p1)+" puntos"
        if p2>p1:
            winner="Gana jugador 2 con un total de "+str(p2)+" puntos"
    return winner

def mayor(lista1,lista2,jugada):
    may=""
    puntos1=0
    puntos2=0
    for n in lista1:
        a=n.replace("JK","")
        puntos1+=tarjetas.Carta.diccionario[a]

    for n in lista2:
        a=n.replace("JK","")
        puntos2+=tarjetas.Carta.diccionario[a]

    if jugada=="full" or jugada=="full + 1 par" or jugada=="poker + 1 par" or jugada=="poker + 1 tercia":
        return puntos1,puntos2
    else:    
        if puntos1>puntos2:
            may="Gana jugador 1 con un total de "+str(puntos1)+" puntos"
        if puntos2>puntos1:
            may="Gana jugador 2 con un total de "+str(puntos2)+" puntos"
        return may

def comprobar_jugada(jugador):
    jugada=""
    carta_mas_alta=len(jugador.mano)
    pares=len(jugador.pares)
    tercias=len(jugador.tercias)
    poker=len(jugador.poker)
    color=len(jugador.color)
    if carta_mas_alta==7:
        jugada="carta más alta"
    if pares==1:
        jugada="1 par"
    if pares==2:
        jugada="2 pares"
    if tercias==1:
        jugada="1 tercia"
    if pares==3:
        jugada="3 pares"
    if tercias==2:
        jugada="2 tercias"
    if color==7:
        jugada="color"
    if tercias==1 and pares==1:
        jugada="full"
    if tercias==1 and pares==2:
        jugada="full + 1 par"
    if poker==4:
        jugada="poker"
    if poker==4 and pares==1:
        jugada="poker + 1 par"
    if poker==4 and tercias==1:
        jugada="poker + 1 tercia"
    return jugada

def main(jugador_1,jugador_2):
    b=tarjetas.Baraja()
    A=tarjetas.Jugador(jugador_1)
    B=tarjetas.Jugador(jugador_2)

    for i in range(0,7):
        A.mano.append(tarjetas.Baraja.cartas[i])
        B.mano.append(tarjetas.Baraja.cartas[i+7])
    print("Jugador 1")
    print(A.mano)
    comprobar_pares(A)
    desplegar_mano(A)
    print("Jugador 2")
    print(B.mano)
    comprobar_pares(B)
    desplegar_mano(B)

    winner=ganador(A, B)
    print(winner)

def imagenes_cartas(jugador):
    cartas={}
    for i,carta in enumerate(jugador.mano):
        key='carta{0:d}'.format(i)
        if carta.simbolo is not "JK":
            cartas[key]="/static/images/{0}_{1}.png".format(carta.palo,carta.simbolo)
        else:
            cartas[key]="/static/images/JK.png"
    return cartas

def desplegar_mano(jugador):
    print(jugador.pares)
    print(jugador.tercias)

def comprobar_pares(jugador)->None:
    mano=jugador.mano
    diccionario=dict()
    for carta in mano:
        if carta.simbolo in diccionario:
            diccionario[carta.simbolo]+=1
        else:
            diccionario[carta.simbolo]=1
   
    color=dict()

    for carta in mano:
        if "JK" not in mano:
            if carta.palo in color:
                color[carta.palo]+=1
            else:
                color[carta.palo]=1

    mayor=-1

    for key,value in color.items():
        if color[key]>mayor:
            mayor=color[key]

    if mayor==7:
        jugador.color=mano
    
    for key,value in diccionario.items():
        if value==2:
            jugador.pares.append(key)
        if value==3:
            jugador.tercias.append(key)
        if value==4:
            jugador.poker.append(key)
    
    if "JK" in diccionario:
        comprobar_joker(jugador,1)
    #comprobar_joker(diccionario,jugador)

def comprobar_joker(jugador,a):
    joker=None
    palo=None
    mayor=-1
    llave_mayor=None
    par=None
    tercia=None
    cont=0

    for cart in jugador.mano:
        if cart.palo==None:
            cont+=1

    for carta in jugador.mano:
        if carta.palo != None:
            if carta.simbolo in jugador.pares:
                jugador.mano.remove(carta)
            if carta.simbolo in jugador.tercias:
                jugador.mano.remove(carta)
        if carta.palo==None:
            joker=carta.simbolo
            palo=carta
            if joker in jugador.pares:
                jugador.pares.remove(joker)

    for carta in jugador.mano:
        if carta.simbolo!=joker:
            for c in jugador.mano:
                if c.simbolo!=joker:
                    if tarjetas.Carta.diccionario[carta.simbolo]>=tarjetas.Carta.diccionario[c.simbolo] and tarjetas.Carta.diccionario[carta.simbolo]>=mayor:
                        llave_mayor=carta.simbolo
                        par=carta
                        mayor=tarjetas.Carta.diccionario[carta.simbolo]
    
    if palo==None:
        for jok in jugador.mano:
            if jok.palo==None:
                joker=jok.simbolo
                palo=jok

    if mayor!=-1:
        jugador.pares.append(llave_mayor+"JK")
        if palo in jugador.mano and cont==1:
            jugador.mano.remove(palo)
        if palo in jugador.mano and a==2:
            jugador.mano.remove(palo)
        if par in jugador.mano:
            jugador.mano.remove(par)

    if llave_mayor==None:
        for carta in jugador.pares:
            if mayor==-1 and carta!=None:
                for c in jugador.pares:
                    if c!=None:
                        if tarjetas.Carta.diccionario[carta]>tarjetas.Carta.diccionario[c]:
                            llave_mayor=carta.simbolo
                            par=carta

    if mayor==-1:
        jugador.pares.remove(par)
        jugador.tercias.append(llave_mayor+"JK")                    

    if cont==2 and a==1:
        print("Recursion!!!")
        comprobar_joker(jugador,2)

def jugar():
    b=tarjetas.Baraja()
    A=tarjetas.Jugador("jugador1")
    B=tarjetas.Jugador("jugador2")
    for i in range(0,7):
        A.mano.append(tarjetas.Baraja.cartas[i])
        B.mano.append(tarjetas.Baraja.cartas[i+7])

    return A,B

def jugar_web():
    A,B=jugar()
    jugador_A,jugador_B=jugar_en_web(A,B)
    comprobar_pares(A)
    comprobar_pares(B)
    winner=ganador(A, B)
    return jugador_A,jugador_B,winner

def jugar_en_web(A,B):
    jugadorA=imagenes_cartas(A)
    jugadorB=imagenes_cartas(B)
    return jugadorA,jugadorB


if __name__ == "__main__":
    main("A","B")