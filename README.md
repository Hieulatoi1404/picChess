
<h1 align=center> 
PicChess 
</h1>

<br>
<h2 align=center>
Idea
</h2>

- **Input**: an image of a valid 2d chess position <br>
- **Processing**: Using trained AI model to read the state of the board and rebuild it using FEN notation then feeding the rebuilt FEN to stockfish <br>
- **Output**: The best move on the board

<br>
<h2 align=center>
Progress
</h2>

### Update 1
- Implemented Synthetic data generation to train upcoming AI models
- Implemented a helper compressing module to compress chess piece icon from 250x250 -> 32x32
### Update 2
- Implemented Synthetic Dataset with Image Processing (Torch + Albumentations) to provide synthetic dataset pipeline for training AI.
- Refactor helperModule.py to use OOP for modularity and usage between files.
- Restructure Folders/Files.
