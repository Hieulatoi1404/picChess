import os
import cairosvg

LICHESS_TO_FEN = {
    'wP': 'P', 'wN': 'N', 'wB': 'B', 'wR': 'R', 'wQ': 'Q', 'wK': 'K',
    'bP': 'p', 'bN': 'n', 'bB': 'b', 'bR': 'r', 'bQ': 'q', 'bK': 'k'
}

# Helper to compress 250x250 icon .png files down to 32x32 .png files
def convert_lichess_theme(svg_dir: str, out_dir: str, size=32):
    os.makedirs(out_dir, exist_ok=True)
    for lichess_name, fen_sym in LICHESS_TO_FEN.items():
        svg_path = os.path.join(svg_dir, f"{lichess_name}.svg")

        # Save as wP.png / bP.png to avoid case-insensitive filesystem collisions on macOS
        out_path = os.path.join(out_dir, f"{lichess_name}.png")
        cairosvg.svg2png(url=svg_path, write_to=out_path, output_width=size, output_height=size)

SVG_DIR = "Resources/piece/alpha"
OUT_DIR = "pieceIcon"

convert_lichess_theme(SVG_DIR, OUT_DIR)
