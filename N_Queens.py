def GerarTabuleiro(N):
    return [[0 for i in range(N)] for j in range(N)]

def PrintarTabuleiro(board):
    for row in board:
        for val in row:
            if val == 0:
                print("▢", end="  ")
            else:
                print("♕", end="  ")
        print()

def PosicaoValida(board, row, col, N):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i in range(N):
        for j in range(N):
            if (i+j == row+col) or (i-j == row-col):
                if board[i][j] == 1:
                    return False
    return True

def Solucao(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if PosicaoValida(board, i, col, N):
            board[i][col] = 1
            if Solucao(board, col+1, N):
                return True
            board[i][col] = 0
    return False

N = 8
board = GerarTabuleiro(N)
if Solucao(board, 0, N):
    PrintarTabuleiro(board)
else:
    print("Não foi possível encontrar uma solução.")