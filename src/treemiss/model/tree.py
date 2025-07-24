import math
from .tree_part import TreePart, PartType

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parts = []

        # Start with a root and a leaf
        root = TreePart(PartType.ROOT, self, x=x, y=y, angle=-90, length=10)
        leaf = TreePart(PartType.LEAF, self, x=x, y=y - 10, angle=90, length=10)

        # Add default genome
        root.code = [("GROW",)] * 10 + [("SPLIT", 0)]
        leaf.code = [("GROW",)] * 10 + [("SPLIT", 0)]
        root.memory[0] = 0
        leaf.memory[0] = 0

        root.children.append(leaf)
        leaf.parent = root

        self.parts.append(root)
        self.parts.append(leaf)

    def update(self):
        self.update_positions()
        for part in self.parts:
            part.execute_instruction()

    def update_positions(self):
        for part in self.parts:
            if part.parent:
                part.x = part.parent.x + math.cos(math.radians(part.parent.angle)) * part.parent.length
                part.y = part.parent.y + math.sin(math.radians(part.parent.angle)) * part.parent.length

    def get_part_at(self, x, y):
        for part in self.parts:
            if part.x == x and part.y == y:
                return part
        return None

    def add_part(self, parent_part, part_type, angle):
        # Calculate the position of the new part
        new_x = parent_part.x + math.cos(math.radians(parent_part.angle + angle)) * parent_part.length
        new_y = parent_part.y + math.sin(math.radians(parent_part.angle + angle)) * parent_part.length

        # Create the new part
        new_part = TreePart(part_type, self, x=new_x, y=new_y, angle=parent_part.angle + angle)
        new_part.parent = parent_part
        parent_part.children.append(new_part)
        self.parts.append(new_part)
