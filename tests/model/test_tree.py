import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from treemiss.model.tree import Tree
from treemiss.model.tree_part import PartType

class TestTree(unittest.TestCase):
    def test_initialization(self):
        tree = Tree()
        self.assertEqual(len(tree.parts), 1)
        self.assertEqual(tree.parts[0].part_type, PartType.ROOT)

    def test_update(self):
        tree = Tree()
        tree.parts[0].code = [("ADD", 0, 1, 2)]
        tree.parts[0].memory[1] = 5
        tree.parts[0].memory[2] = 10
        tree.update()
        self.assertEqual(tree.parts[0].memory[0], 15)

if __name__ == '__main__':
    unittest.main()
