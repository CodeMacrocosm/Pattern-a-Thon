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


# Example:

          T
      A       T
   G             C
  C               G
   T             A
      A       T
          G
      G       C
   A             T
  T               A
   C             G
      G       C
          T
      A       T
   G             C
  C               G
   T             A
      A       T
          G
      G       C
   A             T
  T               A
   C             G
      G       C