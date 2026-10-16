import numpy as np
import os
import random
import chess
from PIL import Image, ImageDraw

CLASS_MAP = {
    'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
    'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12
}

DEFAULT_SPRITE_PREFIX = "Resources/processedPieceIcon/"
DEFAULT_PIECE_NAME_LIST = {
    # Lila's piece name format is "{color}{piece_name}"
    # e.g. wB = White Bishop, bN = Black Knight

    # FEN piece name format is "{piece_name}", capitalized mean white otherwise black
    # e.g. P = White pawn, p = Black pawn

    'P': "wP.png", 'N': "wN.png", 'B': "wB.png",
    'R': "wR.png", 'Q': "wQ.png", 'K': "wK.png",
    'p': "bP.png", 'n': "bN.png", 'b': "bB.png",
    'r': "bR.png", 'q': "bQ.png", 'k': "bK.png"
}

# This loads all the pieces icon into an a dictionary
# Unless the file name of icon or path prefix are different from the default ones you don't need to provide any parameter
def loadImg(spriteNameArr : dict[str, str] = DEFAULT_PIECE_NAME_LIST, spritePathPrefix : str = DEFAULT_SPRITE_PREFIX) -> dict:
    returnDict = {}

    for k, v in spriteNameArr.items():
        im = Image.open(f"{spritePathPrefix}{v}")

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

spritesList = loadImg()

generateRandomSample(spritesList)
