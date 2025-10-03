# Chessboard Pattern (Python)

A tiny, fun script that prints a configurable chessboard pattern to your terminal. No dependencies, just Python.

## Why?
- Quick pattern practice
- Easy to tweak
- Looks cool in the terminal (especially with Unicode blocks)

## Features
- Set board size (rows/cols)
- Set cell size (how big each square is)
- Choose characters for dark/light tiles
- Print to screen or save to a file

## Requirements
- Python 3.x
- Works on Windows, macOS, Linux

## Usage

```bash
# Default: 8x8 board, cell size 2, dark="█", light=" "
python3 chessboard_pattern.py

# Custom size
python3 chessboard_pattern.py --rows 10 --cols 10 --cell 3

# Custom characters
python3 chessboard_pattern.py --dark "#" --light "."

# Save to a file
python3 chessboard_pattern.py -o board.txt
```

## Example Output (8x8, cell=2, dark="█")
```
████    ████    ████    ████
████    ████    ████    ████
    ████    ████    ████    
    ████    ████    ████    
████    ████    ████    ████
████    ████    ████    ████
    ████    ████    ████    
    ████    ████    ████    
████    ████    ████    ████
████    ████    ████    ████
    ████    ████    ████    
    ████    ████    ████    
████    ████    ████    ████
████    ████    ████    ████
    ████    ████    ████    
    ████    ████    ████    
```

## Notes
- If alignment looks off in your terminal, try `--dark "#" --light " "` or smaller `--cell`.
- Unicode block `█` looks great in most terminals, but you can use whatever you like.
