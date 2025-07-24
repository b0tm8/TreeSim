from .tree import Tree
from .tree_part import PartType
import math

class Simulation:
    def __init__(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height
        self.trees = []
        self.sunlight = []
        self.water = []

    def initialize(self):
        # Initialize the world with sunlight and water
        self.sunlight = [100] * self.world_width  # Example initial sunlight
        self.water = [100] * self.world_width     # Example initial water

        # Create some initial trees
        self.trees.append(Tree(self.world_width / 2, self.world_height / 2))

    def update(self):
        # Update sunlight and water distribution
        for x in range(self.world_width):
            sunlight = 100
            for y in range(self.world_height):
                part = self.get_part_at(x, y)
                if part and part.part_type == PartType.LEAF:
                    part.energy += sunlight * part.size * abs(math.sin(math.radians(part.angle)))
                    sunlight *= 0.5  # Dim the sunlight for parts below

        for tree in self.trees:
            for part in tree.parts:
                if part.part_type == PartType.ROOT:
                    part.water += part.size * (part.y / self.world_height)

        # Update all trees
        for tree in self.trees:
            tree.update()

    def get_part_at(self, x, y):
        for tree in self.trees:
            part = tree.get_part_at(x, y)
            if part:
                return part
        return None
