from .tree_part import TreePart, PartType

class Tree:
    def __init__(self):
        self.parts = []
        # Start with a single root part
        self.parts.append(TreePart(PartType.ROOT))

    def update(self):
        for part in self.parts:
            part.execute_instruction()
