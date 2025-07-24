import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from treemiss.model.tree_part import TreePart, PartType

class TestTreePart(unittest.TestCase):
    def test_initialization(self):
        part = TreePart(PartType.ROOT, None)
        self.assertEqual(part.part_type, PartType.ROOT)
        self.assertEqual(len(part.memory), 64)
        self.assertEqual(part.program_counter, 0)
        self.assertEqual(part.energy, 0)
        self.assertEqual(part.water, 0)
        self.assertEqual(part.code, [])

    def test_add_instruction(self):
        part = TreePart(PartType.LEAF, None)
        part.memory[1] = 10
        part.memory[2] = 20
        part.code = [("ADD", 0, 1, 2)]
        part.execute_instruction()
        self.assertEqual(part.memory[0], 30)
        self.assertEqual(part.program_counter, 1)

    def test_sub_instruction(self):
        part = TreePart(PartType.BRANCH, None)
        part.memory[1] = 30
        part.memory[2] = 10
        part.code = [("SUB", 0, 1, 2)]
        part.execute_instruction()
        self.assertEqual(part.memory[0], 20)
        self.assertEqual(part.program_counter, 1)

    def test_jmp_instruction(self):
        part = TreePart(PartType.ROOT, None)
        part.code = [("JMP", 5)]
        part.execute_instruction()
        self.assertEqual(part.program_counter, 5)

    def test_mul_instruction(self):
        part = TreePart(PartType.LEAF, None)
        part.memory[1] = 10
        part.memory[2] = 20
        part.code = [("MUL", 0, 1, 2)]
        part.execute_instruction()
        self.assertEqual(part.memory[0], 200)

    def test_div_instruction(self):
        part = TreePart(PartType.BRANCH, None)
        part.memory[1] = 20
        part.memory[2] = 10
        part.code = [("DIV", 0, 1, 2)]
        part.execute_instruction()
        self.assertEqual(part.memory[0], 2)

    def test_mod_instruction(self):
        part = TreePart(PartType.ROOT, None)
        part.memory[1] = 20
        part.memory[2] = 10
        part.code = [("MOD", 0, 1, 2)]
        part.execute_instruction()
        self.assertEqual(part.memory[0], 0)

    def test_jmpz_instruction(self):
        part = TreePart(PartType.ROOT, None)
        part.memory[1] = 0
        part.code = [("JMPZ", 5, 1)]
        part.execute_instruction()
        self.assertEqual(part.program_counter, 5)

    def test_jmpnz_instruction(self):
        part = TreePart(PartType.ROOT, None)
        part.memory[1] = 1
        part.code = [("JMPNZ", 5, 1)]
        part.execute_instruction()
        self.assertEqual(part.program_counter, 5)

if __name__ == '__main__':
    unittest.main()
