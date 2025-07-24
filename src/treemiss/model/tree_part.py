from enum import Enum

class PartType(Enum):
    ROOT = 1
    BRANCH = 2
    LEAF = 3

class TreePart:
    def __init__(self, part_type, memory_size=64):
        self.part_type = part_type
        self.memory = [0] * memory_size
        self.program_counter = 0
        self.energy = 0
        self.water = 0
        self.code = []

    def execute_instruction(self):
        if self.program_counter >= len(self.code):
            return

        instruction = self.code[self.program_counter]
        opcode = instruction[0]

        if opcode == "ADD":
            dest, src1, src2 = instruction[1:]
            self.memory[dest] = self.memory[src1] + self.memory[src2]
        elif opcode == "SUB":
            dest, src1, src2 = instruction[1:]
            self.memory[dest] = self.memory[src1] - self.memory[src2]
        elif opcode == "JMP":
            addr = instruction[1]
            self.program_counter = addr
            return
        elif opcode == "GROW":
            # Placeholder for GROW logic
            pass
        elif opcode == "SPLIT":
            # Placeholder for SPLIT logic
            pass
        elif opcode == "CHANGE":
            # Placeholder for CHANGE logic
            pass

        self.program_counter += 1
