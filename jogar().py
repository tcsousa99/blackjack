def valor(mao):
    valor = 0
    contador_As = 0
    nobreza = ['J','Q','K']
    for carta in mao:
        if carta[0] in nobreza:
            valor += 10
        elif carta[0] == 'A':
            valor += 11
            contador_As += 1
        else:
            valor += int(carta[0])
    while contador_As != 0 and valor > 21:
        valor -= 10
        contador_As -= 1

    return valor

def ler_baralho(n):
    abrir_fich = open("baralhos/baralho_{}.txt".format(n),'r')
    lista = abrir_fich.readlines()
    baralho = []
    new_baralho = []
    for i in range(len(lista)):
        baralho.append(lista[i].split())
    for j in range(len(baralho)):
        par = ()
        for g in range(2):
            par +=(baralho[j][g],)
        new_baralho.append(par)
    return new_baralho

def bust(mao):
    rebentou = False
    if valor(mao)>21:
        rebentou = True
    return rebentou

def decisao_dealer(mao):
    decisao = "STAND"

    if valor(mao) < 17:
        decisao = "HIT"

    return decisao

def add_card(mao,contador,i):
    baralho = ler_baralho(i)
    mao.append(baralho[contador])
    return mao

def printer(mao):
    bonito = ""
    for i in range(len(mao)):
        s = "({},{})".format(mao[i][0],mao[i][1])
        bonito += s
    bonito += " - {} -".format(valor(mao))
    return bonito

def calcula_hint(mao_jogador, mao_dealer):
    baralho = ler_baralho(1)                    
    numero_busts = 0                            
    

    for i in mao_jogador:               
        baralho.remove(i)

    for j in mao_dealer:                
        baralho.remove(j)

    for i in baralho:                            
        mao_jogador.append(i)
        if bust(mao_jogador):
            numero_busts += 1
        mao_jogador.remove(i)


    probabilidade = round((numero_busts / len(baralho))*100, 3)       
    return probabilidade

def decisions(jogador,decisao,mao_jogador,mao_dealer,contador, i):
    resultado = ""
    while ((decisao.upper() == "HIT" or decisao.upper() == "HINT") and not bust(mao_jogador)):
        print("{} decidiu {}".format(jogador,decisao.upper()))
        if decisao.upper() == "HIT":
            contador += 1
            Nova_maoj = add_card(mao_jogador,contador,i)
            print(printer(Nova_maoj))
            if not bust(Nova_maoj):
                decisao = input("HIT, STAND ou HINT ? ")

            else:
                print("BUST com {} pontos".format(valor(Nova_maoj)))
                resultado = "derrota"
        else:
            probabilidade = calcula_hint(mao_jogador,mao_dealer)
            print("A probabilidade de rebentar com a proxima carta é: {}".format(probabilidade))
            decisao = input("HIT, STAND ou HINT ? ")

    if (decisao.upper() != "HIT" or decisao.upper()!= "HINT") and resultado != "derrota":
        print("{} decidiu STAND".format(jogador))
        print("\n* Joga o dealer *")
        print("Mão dealer:\n" + printer(mao_dealer))  
        dealer = decisao_dealer(mao_dealer)
        Nova_maod = mao_dealer
        if blackjack(Nova_maod):
            print("Dealer fez BLACKJACK!\n")
            resultado = "derrota"
        elif dealer == "STAND":
            print("Dealer decidiu STAND\n")

        while dealer == "HIT" and not bust(Nova_maod):
            print("Dealer decidiu HIT")
            contador += 1
            Nova_maod = add_card(mao_dealer,contador,i)
            print("Mão dealer:\n" + printer(Nova_maod))
            dealer = decisao_dealer(Nova_maod)
            if bust(Nova_maod):
                print("BUST com {} pontos".format(valor(Nova_maod)))
                resultado = "vitória"
            else:
                print("Dealer decidiu STAND")
    if resultado == "":
        Nova_maoj = mao_jogador
        Nova_maod = mao_dealer
        if valor(Nova_maoj) < valor(Nova_maod):
            resultado = "derrota"
        elif valor(Nova_maoj) > valor(Nova_maod):
            resultado = "vitória"
        else:
            resultado = "empate"

    return resultado

def blackjack(mao):
    blackjack = False
    if len(mao) == 2 and valor(mao)== 21:
        blackjack = True
    return blackjack




def ronda(i,jogador,aposta):
    a = ""
    contador = 3
    ganho = 0
    print("\n*** Ronda {} ***".format(i))
    baralho = ler_baralho(i)
    mao_jogador = [baralho[0],baralho[2]]
    mao_dealer = [baralho[1],baralho[3]]
    print("Dealer: ({},{})(?,?)".format(baralho[1][0],baralho[1][1]))
    print("Jogador: " + printer(mao_jogador))
    print("* Joga {} *".format(jogador))

    if (blackjack(mao_jogador) and not blackjack(mao_dealer)):
        resultado = "vitória Blackjack"
        ganho = aposta * 3/2
        print("{} fez BLACKJACK!\n".format(jogador))
              
    elif (blackjack(mao_jogador) and blackjack(mao_dealer)):
        resultado = "empate"
        ganho = 0
        print("{} fez BLACKJACK!".format(jogador))
        print("Mão Dealer: " + printer(mao_dealer))
        print("{} fez BLACKJACK!".format(jogador))
    else:
        decisao = input("HIT, STAND ou HINT ? ")


        resultado = decisions(jogador,decisao,mao_jogador,mao_dealer,contador,i)
        if resultado == "vitória":
            ganho = aposta
        elif resultado == "derrota":
            ganho = -aposta
        else:

            ganho = 0

    return resultado, ganho


def jogar():
    jogador = input("Digite o seu nome: ")
    try:
        montante = int(input("Montante inicial (100)?  "))
    except:
        montante = 100
    try:
        aposta = int(input("Valor da aposta (10)?  "))
    except:
        aposta = 10
    if aposta > montante:
        aposta = 10

    print("=== Vamos começar ===\nJogador: {}\nSaldo inicial: {}\nValor da aposta: {}\n".format(jogador,montante,aposta))
    QUIT = ""
    i = 1
    while QUIT.upper() != "QUIT" and montante > aposta:
        RONDA = ronda(i, jogador, aposta)
        i += 1
        montante = montante + RONDA[1]
        print("Resultado da ronda: {} com ganho {}".format(RONDA[0],RONDA[1]))
        print("O seu saldo actual é: {}".format(montante))
        QUIT = input("Mais uma ronda (QUIT para terminar)? ")



        
            

            
    
    
    

jogar()
    
    
        

