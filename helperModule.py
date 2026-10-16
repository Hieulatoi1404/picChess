from numpy import void
import os

try:
    import cairosvg
except ImportError:
    raise Exception("Missing module: Install cairosvg before proceeding")


class compressIconSVG:
    def __init__(self, svgDir : str = None, outDir : str = None, size : int = 32) -> void:
        if svgDir is None or outDir is None:
            raise Exception("svgDir and outDir can't be empty!")
        if size < 0:
            raise Exception("size can't be negative!")
        
        self.__svgDir = svgDir
        self.__outDir = outDir
        self.__size = size

        self.__LICHESS_TO_FEN = {
            # For piece naming format, take a look in main.py

            'wP': 'P', 'wN': 'N', 'wB': 'B', 'wR': 'R', 'wQ': 'Q', 'wK': 'K',
            'bP': 'p', 'bN': 'n', 'bB': 'b', 'bR': 'r', 'bQ': 'q', 'bK': 'k'
        }
    
    @property
    def svgDir(self):
        return self.__svgDir
    
    @property
    def outDir(self):
        return self.__outDir
    
    @property
    def size(self):
        return self.__size

    @outDir.setter
    def outDir(self, newOutDir : str = None):
        if (newOutDir is None):
            raise Exception("out_dir can't be empty!")
        
        self.__outDir = newOutDir
    
    @svgDir.setter
    def svgDir(self, newSVGDir : str = None):
        if (newSVGDir is None):
            raise Exception("svg_dir can't be empty!")
        
        self.__svgDir = newSVGDir
    
    @size.setter
    def size(self, newSize : int = 32):
        if (newSize < 0):
            raise Exception("size can't be negative!")
        
        self.__size = newSize

    # Helper to compress 250x250 icon .png files down to 32x32 .png files
    def compress(self):
        os.makedirs(self.__outDir, exist_ok=True)
        for lichess_name, fen_sym in self.__LICHESS_TO_FEN.items():

            # Save as wP.png / bP.png to avoid case-insensitive filesystem collisions on macOS
            svg_path = os.path.join(self.__svgDir, f"{lichess_name}.svg")
            out_path = os.path.join(self.__outDir, f"{lichess_name}.png")

            cairosvg.svg2png(url=svg_path, write_to=out_path, output_width=self.__size, output_height=self.__size)
