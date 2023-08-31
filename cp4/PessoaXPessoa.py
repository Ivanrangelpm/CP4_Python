def JogoDaVelha():
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vitoria = False

    def ImprimirTabuleiro():
        print("\n")
        print('', tabuleiro[0], "!", tabuleiro[1], "!", tabuleiro[2])
        print("---!---!---")
        print('', tabuleiro[3], "!", tabuleiro[4], "!", tabuleiro[5])
        print("---!---!---")
        print('', tabuleiro[6], "!", tabuleiro[7], "!", tabuleiro[8])
        print("\n")
    def ChecaVitoria(jogador):
        for a in range(0, 7, 3):
            if tabuleiro[a] == tabuleiro[a + 1] == tabuleiro[a + 2] == jogador:
                return True
        for a in range(3):
            if tabuleiro[a] == tabuleiro[a + 3] == tabuleiro[a + 6] == jogador:
                return True
        if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador:
            return True
        if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador:
            return True
        return False

    def PegarNumero():
        while True:
            numero = input()
            try:
                numero = int(numero)
                if numero in range(1, 10):
                    return numero
                else:
                    print("\nNúmero não está no tabuleiro.")
            except ValueError:
                print("\nIsso não é um número. Tente novamente.")
                continue


    def Turno(jogador):
        espaco_colocado = PegarNumero() - 1
        if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O":
            print("\nEspaço já ocupado. Tente colocar em outro.")
            Turno(jogador)
        else:
            tabuleiro[espaco_colocado] = jogador

    jogadas = 0
    while not vitoria:
        ImprimirTabuleiro()
        vitoria = ChecaVitoria("O")
        if vitoria:
            print("Jogador O venceu!")
            break

        if jogadas == 9:
            print("O jogo acabou em empate.")
            break

        print("Jogador X, escolha um espaço.")
        Turno("X")
        jogadas += 1

        ImprimirTabuleiro()
        vitoria = ChecaVitoria("X")
        if vitoria:
            print("Jogador X venceu!")
            break

        print("Jogador O, escolha um espaço.")
        Turno("O")
        jogadas += 1

JogoDaVelha()
