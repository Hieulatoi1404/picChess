import numpy as np
import os
import random
import chess
from PIL import Image, ImageDraw

CLASS_MAP = {
    'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
    'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12
}

spritesPathList = {
    'P': "pieceIcon/wP.png", 'N': "pieceIcon/wN.png", 'B': "pieceIcon/wB.png",
    'R': "pieceIcon/wR.png", 'Q': "pieceIcon/wQ.png", 'K': "pieceIcon/wK.png",
    'p': "pieceIcon/bP.png", 'n': "pieceIcon/bN.png", 'b': "pieceIcon/bB.png",
    'r': "pieceIcon/bR.png", 'q': "pieceIcon/bQ.png", 'k': "pieceIcon/bK.png"
}


def loadImg(spritesPathArr : dict[str, str]):
    returnDict = {}

    for k, v in spritesPathArr.items():
        im = Image.open(v)

        returnDict[k] = im
    
    return returnDict

def generateBoardPos(depth = 15) -> chess.Board:
    board = chess.Board()

    for i in range(depth):
        if (board.is_game_over()):
            break
        
        move = random.choice(list(board.legal_moves))
        board.push(move)
    
    return board

def generateRandomSample(sprites = None, lightSqCol = (240,217,181), darkSqCol = (181, 136, 99)):
    board = generateBoardPos(30)

    canvas = Image.new("RGBA", (256, 256))
    draw = ImageDraw.Draw(canvas)

    isLight = True

    for i in range(8):
        for j in range(8):
            color = lightSqCol
            if ((i + j) % 2 != 0):
                color = darkSqCol

            draw.rectangle([(j * 32, i * 32), (32 + j * 32, 32 + i * 32)], fill=color, width=32)

    arr = np.zeros((8, 8), dtype=np.int64)
    for sq, piece in board.piece_map().items():
        r = 7 - chess.square_rank(sq)
        c = chess.square_file(sq)
        symbol = piece.symbol()

        arr[r, c] = CLASS_MAP[symbol]
        canvas.alpha_composite(sprites[symbol], dest=(c * 32, r * 32))

    canvas.show()
    return np.array(canvas.convert('RGB')), arr

spritesList = loadImg(spritesPathList)

generateRandomSample(spritesList)
