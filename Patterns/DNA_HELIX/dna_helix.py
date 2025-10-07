"""
DNA Double Helix ASCII Pattern

Concept:
- Two sinusoidal strands 180 degrees out of phase (π shift) create the helix.
- Optional "bonds" connect the two strands periodically to enhance the look.

Parameters:
- height (H): number of rows to print
- amplitude (A): horizontal spread of each strand
- wavelength (L): rows per full sinusoidal cycle
- bond_period (K): every K-th row will draw horizontal bonds between strands (0 to disable)
- padding (P): spaces on both sides for margin

Usage:
  python3 dna_helix.py
  python3 dna_helix.py 24 8 12 3
  python3 dna_helix.py --height 32 --amplitude 10 --wavelength 16 --bond-period 4 --padding 2

Notes:
- Keep wavelength >= 2 for a sensible wave.
- amplitude >= 1 is recommended.
"""

import argparse
import math
import sys
from typing import List, Tuple


def generate_dna_helix(
    height: int = 24,
    amplitude: int = 8,
    wavelength: int = 12,
    bond_period: int = 3,
    padding: int = 2,
    strand_pairs: List[Tuple[str, str]] = None,
    bond_char: str = "-",
) -> List[str]:
    """
    Return a list of strings representing the DNA double helix.

    strand_pairs: optional sequence of (left_char, right_char) to cycle through rows.
                  If None, defaults to common base pairs.
    """
    if strand_pairs is None:
        strand_pairs = [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]

    if height <= 0:
        raise ValueError("height must be > 0")
    if amplitude < 1:
        raise ValueError("amplitude must be >= 1")
    if wavelength < 2:
        raise ValueError("wavelength must be >= 2")
    if padding < 0:
        raise ValueError("padding must be >= 0")
    if bond_period < 0:
        raise ValueError("bond_period must be >= 0")

    # Grid width to accommodate sinusoidal range + margins
    width = 2 * amplitude + 2 * padding + 1
    mid = padding + amplitude  # center column around which strands oscillate

    lines: List[str] = []
    for r in range(height):
        phase = (2.0 * math.pi * r) / float(wavelength)

        # Two strands π out of phase
        x1 = int(round(mid + amplitude * math.sin(phase)))
        x2 = int(round(mid + amplitude * math.sin(phase + math.pi)))

        # Clip to bounds defensively (should already be within [0, width-1])
        x1 = max(0, min(width - 1, x1))
        x2 = max(0, min(width - 1, x2))

        left = min(x1, x2)
        right = max(x1, x2)

        row = [" "] * width

        # Choose strand characters for this row
        c1, c2 = strand_pairs[r % len(strand_pairs)]

        # Place the two strand characters
        row[x1] = c1
        row[x2] = c2

        # Optionally draw bonds between strands every K-th row
        if bond_period > 0 and r % bond_period == 0 and right - left > 1:
            for c in range(left + 1, right):
                row[c] = bond_char

        # Right-strip to keep the output tight while preserving left spacing
        lines.append("".join(row).rstrip())

    return lines


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Print a DNA double helix ASCII pattern.")
    parser.add_argument("height", nargs="?", type=int, default=24, help="number of rows (default: 24)")
    parser.add_argument("amplitude", nargs="?", type=int, default=8, help="horizontal spread (default: 8)")
    parser.add_argument("wavelength", nargs="?", type=int, default=12, help="rows per wave cycle (default: 12)")
    parser.add_argument("bond_period", nargs="?", type=int, default=3, help="bond row period, 0 disables (default: 3)")
    parser.add_argument("--padding", "-p", type=int, default=2, help="left/right margin spaces (default: 2)")
    parser.add_argument("--bond-char", "-b", type=str, default="-", help="character for bonds (default: '-')")

    args = parser.parse_args(argv)

    try:
        lines = generate_dna_helix(
            height=args.height,
            amplitude=args.amplitude,
            wavelength=args.wavelength,
            bond_period=args.bond_period,
            padding=args.padding,
            bond_char=args.bond_char[:1] if args.bond_char else "-",
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    for line in lines:
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))