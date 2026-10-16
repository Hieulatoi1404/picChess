---
# PicChess

## Idea:
Input: an image of a valid 2d chess position
Processing: Using trained AI model to read the state of the board and rebuild it using FEN notation then feeding the rebuilt FEN to stockfish
Output: The best move on the board

## Progress:
### Update 1
- Implemented Synthetic data generation to train upcoming AI models
- Implemented a helper compressing module to compress chess piece icon from 250x250 -> 32x32
