# LLvlN Interpreter

A simple interpreter for the LLvlN esoteric programming language.

## Usage

python llvln.py <filename.llvln>

## LLvlN Language Overview

LLvlN is a culinary-themed esoteric programming language with cooking-inspired commands:

- `RECIPE` - Start of program
- `DONE` - End of program
- `TASTE [ingredient]` - Input a number
- `SERVE [ingredient]` - Output a number
- `MOVE` - Move memory pointer right
- `BACK` - Move memory pointer left
- `ADD` - Increment current memory cell
- `SUB` - Decrement current memory cell
- `SPICE [ingredient] [label]` - Jump to label if current cell is non-zero
- `SALT [label]` - Unconditional jump to label
- `[label]:` - Define a label

## Example Programs

### Hello World (prints 72, 101, 108, 108, 111)
```
RECIPE
# Print "Hello, World!"
SET SOUP 72      # H
SERVE SOUP CHAR
SET SOUP 101     # e
SERVE SOUP CHAR
SET SOUP 108     # l
SERVE SOUP CHAR
SERVE SOUP CHAR  # l
SET SOUP 111     # o
SERVE SOUP CHAR
SET SOUP 44      # ,
SERVE SOUP CHAR
SET SOUP 32      # space
SERVE SOUP CHAR
SET SOUP 87      # W
SERVE SOUP CHAR
SET SOUP 111     # o
SERVE SOUP CHAR
SET SOUP 114     # r
SERVE SOUP CHAR
SET SOUP 108     # l
SERVE SOUP CHAR
SET SOUP 100     # d
SERVE SOUP CHAR
SET SOUP 33      # !
SERVE SOUP CHAR
DONE
```

### Truth Machine
```
RECIPE
# Read input and output 1 forever if 1, or output 0 once if 0
TASTE SOUP       # Read input
SERVE SOUP       # Output the number
SPICE SOUP LOOP  # If non-zero, jump to LOOP
DONE             # If zero, end

LOOP:
SERVE SOUP       # Output the number
SALT LOOP        # Infinite loop outputting 1
```

### Cat Program
```
RECIPE
# Echo input characters until EOF
LOOP:
TASTE SOUP CHAR  # Read character
CMP SOUP FISH    # Compare with FISH (0)
BLAND BEAN END   # If equal (EOF), exit
SERVE SOUP CHAR  # Output character
SALT LOOP        # Continue loop

END:
DONE
```

## Installation

1. Download or clone this repository
2. Ensure you have Python 3 installed
3. Run programs using: `python llvln.py yourprogram.llvln`

## License

This project is released into the public domain.