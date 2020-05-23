import pprint
# Declare Chessbord
chessBoard = {'1a': 'wrook', '2a': 'wpawn', '3a': '', '4a': '', '5a': '', '6a': '', '7a': 'bpawn', '8a': 'brook',
              '1b': 'bknight', '2b': 'bpawn', '3b': '', '4b': '', '5b': '', '6b': '', '7b': 'bpawn', '8b': 'bknight',
              '1c': 'wbishop', '2c': 'wpawn', '3c': '', '4c': '', '5c': '', '6c': '', '7c': 'wpawn', '8c': 'wbishop',
              '1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '', '5d': '', '6d': '', '7d': 'bpawn', '8d': 'bking',
              '1e': 'wking', '2e': 'wpawn', '3e': '', '4e': '', '5e': '', '6e': '', '7e': 'bpawn', '8e': 'bqueen',
              '1f': 'wbishop', '2f': 'wpawn', '3f': '', '4f': '', '5f': '', '6f': '', '7f': 'bpawn', '8f': 'bbishop',
              '1g': 'wknight', '2g': 'wpawn', '3g': '', '4g': '', '5g': '', '6g': '', '7g': 'bpawn', '8g': 'bknight',
              '1h': 'wrook', '2h': 'wpawn', '3h': '', '4h': '', '5h': '', '6h': '', '7h': 'bpawn', '8h': 'brook',
              }

whitePieces = {}
blackPieces = {}


def findWhitePieces(piece):
    if piece[1:] == 'rook':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1
    elif piece[1:] == 'pawn':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1
    elif piece[1:] == 'knight':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1
    elif piece[1:] == 'bishop':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1
    elif piece[1:] == 'queen':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1
    elif piece[1:] == 'king':
        whitePieces.setdefault(piece, 0)
        whitePieces[piece] = whitePieces[piece] + 1


def findBlackPieces(piece):
    if piece[1:] == 'rook':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1
    elif piece[1:] == 'pawn':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1
    elif piece[1:] == 'knight':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1
    elif piece[1:] == 'bishop':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1
    elif piece[1:] == 'queen':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1
    elif piece[1:] == 'king':
        blackPieces.setdefault(piece, 0)
        blackPieces[piece] = blackPieces[piece] + 1


colorChecker = {
    'w': findWhitePieces,
    'b': findBlackPieces,
}


def countPieces(piecesDict):
    count = 0
    for v in piecesDict.values():
        count += v
    return count


def printItems():
    print('valid WHITE pieces found:')
    for k, v in whitePieces.items():
        print(str(v) + ' ' + k + 's')
    print('valid BLACK pieces found: ')
    for k, v in whitePieces.items():
        print(str(v) + ' ' + k + 's')


def isValidChessBoard(chessBoard):

    for k in chessBoard.items():
        # check validity board size is 8 x 8 and their lables
        count = 0
        for k in chessBoard:
            # first char of the chessboard key
            rangeValue = k[0]
            alphaValue = k[1]
            if int(rangeValue) >= 1 or int(rangeValue) <= 8:
                # pprint.pprint('k[0]: ' + k[0])
                if alphaValue >= 'a' or alphaValue <= 'h':
                    # pprint.pprint('k[1]: ' + k[1])
                    count += 1
            else:
                print('invalid space found')
    if count == 64:
        print('Board has valid number of spaces \n')
    print('Checking Contents of Board (Pieces)')
    for k, v in chessBoard.items():
            # Check piece namea and quantity
        # pprint.pprint('Piece Found:' + v)
        if v != '':
            colorPiece = v[0]
            # print(colorPiece)
            func = colorChecker.get(
                colorPiece, lambda key: print("Invalid Piece Found at " + str(k)))
            func(v)

        elif v == '':
            print('Empty Space Found at ' + str(k))
    if countPieces(whitePieces) == 16 and countPieces(blackPieces) == 16:
        printItems()


isValidChessBoard(chessBoard)
