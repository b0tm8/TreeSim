from enum import Enum

class PartType(Enum):
    ROOT = 1
    BRANCH = 2
    LEAF = 3

class TreePart:
    def __init__(self, part_type, tree, memory_size=64, x=0, y=0, angle=0, length=1):
        self.part_type = part_type
        self.tree = tree
        self.memory = [0] * memory_size
        self.program_counter = 0
        self.energy = 0
        self.water = 0
        self.code = []
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.parent = None
        self.children = []

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
        elif opcode == "MUL":
            dest, src1, src2 = instruction[1:]
            self.memory[dest] = self.memory[src1] * self.memory[src2]
        elif opcode == "DIV":
            dest, src1, src2 = instruction[1:]
            self.memory[dest] = self.memory[src1] // self.memory[src2]
        elif opcode == "MOD":
            dest, src1, src2 = instruction[1:]
            self.memory[dest] = self.memory[src1] % self.memory[src2]
        elif opcode == "JMP":
            addr = instruction[1]
            self.program_counter = addr
            return
        elif opcode == "JMPZ":
            addr, val = instruction[1:]
            if self.memory[val] == 0:
                self.program_counter = addr
                return
        elif opcode == "JMPNZ":
            addr, val = instruction[1:]
            if self.memory[val] != 0:
                self.program_counter = addr
                return
        elif opcode == "GROW":
            self.length += 1
        elif opcode == "SPLIT":
            angle = self.memory[instruction[1]]
            self.tree.add_part(self, self.part_type, angle)
            self.memory[instruction[1]] += 10
        elif opcode == "CHANGE":
            new_type_val = self.memory[instruction[1]]
            new_type = PartType(new_type_val)
            self.part_type = new_type

        self.program_counter += 1