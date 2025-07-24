import math
from .tree_part import TreePart, PartType

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parts = []

        # Start with a root and a leaf
        root = TreePart(PartType.ROOT, self, x=x, y=y, angle=-90, size=10)
        leaf = TreePart(PartType.LEAF, self, x=x, y=y - 10, angle=90, size=10)

        # Add default genome
        root.code = [("GROW",)]
        leaf.code = [("GROW",)]

        root.children.append(leaf)
        leaf.parent = root

        self.parts.append(root)
        self.parts.append(leaf)

    def update(self):
        for part in self.parts:
            print("parts")
            part.execute_instruction()

    def get_part_at(self, x, y):
        for part in self.parts:
            if part.x == x and part.y == y:
                return part
        return None

    def add_part(self, parent_part, part_type, angle):
        # Calculate the position of the new part
        new_x = parent_part.x + math.cos(math.radians(parent_part.angle + angle)) * parent_part.size
        new_y = parent_part.y + math.sin(math.radians(parent_part.angle + angle)) * parent_part.size

        # Create the new part
        new_part = TreePart(part_type, self, x=new_x, y=new_y, angle=parent_part.angle + angle)
        new_part.parent = parent_part
        parent_part.children.append(new_part)
        self.parts.append(new_part)
