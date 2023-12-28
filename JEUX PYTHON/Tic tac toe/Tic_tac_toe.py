import random

def drawBoard(board):
    # Cette fonction affiche le tableau que l'on n'a passé.
    # "board" est une liste de 10 chaines représentant le tableau (ignore l'index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Laisse le joueur choisir sa lettre
    # Retourne  une liste avec la lettre du joueur comme premier élement et la lettre de l'ordinateur comme deuxiéme.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Tu veux être X ou O?')
        letter = input().upper()

    # la premier élement de la liste est la lettre du joueur, et la second lettre a l'ordinateur.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # choix aléatoire du joueur qui commence.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
     # Cette fonction retourne 'True' si le joueur veut rejouer à nouveau, sinon retourne 'False'
    print('Voulez-vous jouer de nouveau? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # D'après un tableau et une lettre d'un joueur, la fonction retourne Vrai si le joueur à gagné.
    # Utilisation de 'bo' au lieu de 'board' et au lieu de la lettre .
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # en haut
            (bo[4] == le and bo[5] == le and bo[6] == le) or # au milieu
            (bo[1] == le and bo[2] == le and bo[3] == le) or # en bas
            (bo[7] == le and bo[4] == le and bo[1] == le) or # sur le côté gauche
            (bo[8] == le and bo[5] == le and bo[2] == le) or # au milieu
            (bo[9] == le and bo[6] == le and bo[3] == le) or # sur le côté droit
            (bo[7] == le and bo[5] == le and bo[3] == le) or # en diagonale
            (bo[9] == le and bo[5] == le and bo[1] == le))   # en diagonale

def getBoardCopy(board):
    # Faites un duplicata du tableau et retourne le duplicata.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Retourne 'True' si le mouvement passé est libre sur le tableau.
    return board[move] == ' '

def getPlayerMove(board):
    # Laisse le joueur taper son mouvement
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Quel est ton coup suivant? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Bienvenue dans Tic Tac Toe!')

while True:
    # restaure le tableau
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('Le ' + turn + ' joue en premier.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! vous êtes le vainqueur!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Egalité!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("L'ordinateur vous a battus!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Egalité')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
