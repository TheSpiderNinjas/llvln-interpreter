#!/usr/bin/env python3
"""
LLvlN Interpreter
A simple interpreter for the LLvlN esoteric programming language.
"""

import sys

class LLvlNInterpreter:
    def __init__(self):
        self.memory = [0] * 30000  # Memory cells
        self.pointer = 0           # Memory pointer
        self.input_buffer = []     # Input buffer
        self.program = []          # Program instructions
        self.pc = 0               # Program counter
        self.labels = {}          # Label positions
        
    def load_program(self, filename):
        """Load and parse a LLvlN program from file."""
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        in_recipe = False
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if line == "RECIPE":
                in_recipe = True
                continue
            elif line == "DONE":
                break
                
            if in_recipe:
                # Check for labels
                if line.endswith(':'):
                    label = line[:-1]
                    self.labels[label] = len(self.program)
                else:
                    self.program.append(line)
    
    def execute(self):
        """Execute the loaded program."""
        while self.pc < len(self.program):
            instruction = self.program[self.pc].strip()
            
            if instruction.startswith("TASTE"):
                # Input
                if not self.input_buffer:
                    try:
                        inp = input()
                        self.input_buffer = [int(x) for x in inp.split()]
                    except (ValueError, EOFError):
                        self.input_buffer = [0]
                
                if self.input_buffer:
                    self.memory[self.pointer] = self.input_buffer.pop(0)
                    
            elif instruction.startswith("SERVE"):
                # Output
                print(self.memory[self.pointer], end='')
                
            elif instruction.startswith("MOVE"):
                # Move pointer right
                self.pointer = (self.pointer + 1) % len(self.memory)
                
            elif instruction.startswith("BACK"):
                # Move pointer left
                self.pointer = (self.pointer - 1) % len(self.memory)
                
            elif instruction.startswith("ADD"):
                # Increment current cell
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
                
            elif instruction.startswith("SUB"):
                # Decrement current cell
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
                
            elif instruction.startswith("SPICE"):
                # Conditional jump (if current cell != 0)
                parts = instruction.split()
                if len(parts) >= 3 and self.memory[self.pointer] != 0:
                    label = parts[2]
                    if label in self.labels:
                        self.pc = self.labels[label]
                        continue
                        
            elif instruction.startswith("SALT"):
                # Unconditional jump
                parts = instruction.split()
                if len(parts) >= 2:
                    label = parts[1]
                    if label in self.labels:
                        self.pc = self.labels[label]
                        continue
            
            self.pc += 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python llvln.py <filename.llvln>")
        sys.exit(1)
    
    interpreter = LLvlNInterpreter()
    try:
        interpreter.load_program(sys.argv[1])
        interpreter.execute()
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
