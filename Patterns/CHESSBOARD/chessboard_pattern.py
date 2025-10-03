"""
Chessboard Pattern Generator

Generates an ASCII/Unicode chessboard pattern with customizable rows, columns,
cell size, and tile characters.

Defaults:
- 8x8 board
- Cell size: 2 (width and height in characters)
- Dark tile: '█'
- Light tile: ' ' (space)

Usage examples:
  python3 chessboard_pattern.py
  python3 chessboard_pattern.py --rows 10 --cols 10 --cell 3
  python3 chessboard_pattern.py --dark "#" --light "." --cell 1
  python3 chessboard_pattern.py -r 6 -c 12 -s 2 -o board.txt

Tip:
- Using the Unicode full block '█' looks great in most terminals.
- If alignment looks off in your environment, try --dark "#" or --dark "##".
"""

from __future__ import annotations
import argparse
from typing import List


def generate_chessboard(rows: int = 8,
                        cols: int = 8,
                        cell: int = 2,
                        dark: str = "█",
                        light: str = " ") -> List[str]:
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must be >= 1")
    if cell < 1:
        raise ValueError("cell size must be >= 1")

    lines: List[str] = []
    # Precompute filled tile lines for performance/readability
    dark_hline = dark * cell
    light_hline = light * cell

    for r in range(rows):
        # For each visual sub-row in the tile
        for _ in range(cell):
            row_chunks: List[str] = []
            for c in range(cols):
                # Alternate tiles: top-left is dark by convention
                is_dark = (r + c) % 2 == 0
                row_chunks.append(dark_hline if is_dark else light_hline)
            lines.append("".join(row_chunks))
    return lines


def main():
    parser = argparse.ArgumentParser(description="Generate a chessboard pattern.")
    parser.add_argument("-r", "--rows", type=int, default=8, help="Number of tile rows (default: 8)")
    parser.add_argument("-c", "--cols", type=int, default=8, help="Number of tile columns (default: 8)")
    parser.add_argument("-s", "--cell", type=int, default=2, help="Tile size in characters (width=height) (default: 2)")
    parser.add_argument("--dark", default="█", help="Character(s) for dark tiles (default: '█')")
    parser.add_argument("--light", default=" ", help="Character(s) for light tiles (default: space)")
    parser.add_argument("-o", "--output", default="", help="Optional output file to save the pattern")

    args = parser.parse_args()

    board_lines = generate_chessboard(rows=args.rows,
                                      cols=args.cols,
                                      cell=args.cell,
                                      dark=args.dark,
                                      light=args.light)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(board_lines) + "\n")
        print(f"Chessboard saved to {args.output}")
    else:
        print("\n".join(board_lines))


if __name__ == "__main__":
    main()
