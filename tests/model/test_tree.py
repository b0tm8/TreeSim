import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from treemiss.model.tree import Tree
from treemiss.model.tree_part import PartType, TreePart

class TestTree(unittest.TestCase):
    def test_initialization(self):
        tree = Tree(0, 0)
        self.assertEqual(len(tree.parts), 2)
        self.assertEqual(tree.parts[0].part_type, PartType.ROOT)
        self.assertEqual(tree.parts[1].part_type, PartType.LEAF)

    def test_update(self):
        tree = Tree(0, 0)
        tree.parts[0].code = [("ADD", 0, 1, 2)]
        tree.parts[0].memory[1] = 5
        tree.parts[0].memory[2] = 10
        tree.update()
        self.assertEqual(tree.parts[0].memory[0], 15)

    def test_add_part(self):
        tree = Tree(0, 0)
        parent_part = tree.parts[0]
        tree.add_part(parent_part, PartType.BRANCH, 45)
        self.assertEqual(len(tree.parts), 3)
        self.assertEqual(tree.parts[2].part_type, PartType.BRANCH)
        self.assertEqual(tree.parts[2].parent, parent_part)
        self.assertIn(tree.parts[2], parent_part.children)

if __name__ == '__main__':
    unittest.main()
