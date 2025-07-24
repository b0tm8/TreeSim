import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from treemiss.model.simulation import Simulation

class TestSimulation(unittest.TestCase):
    def test_initialization(self):
        sim = Simulation(10, 20)
        self.assertEqual(sim.world_width, 10)
        self.assertEqual(sim.world_height, 20)
        self.assertEqual(sim.trees, [])
        self.assertEqual(sim.sunlight, [])
        self.assertEqual(sim.water, [])

    def test_initialize(self):
        sim = Simulation(10, 20)
        sim.initialize()
        self.assertEqual(len(sim.trees), 1)
        self.assertEqual(len(sim.sunlight), 10)
        self.assertEqual(len(sim.water), 10)

    def test_update(self):
        sim = Simulation(10, 20)
        sim.initialize()
        sim.trees[0].parts[0].code = [("ADD", 0, 1, 2)]
        sim.trees[0].parts[0].memory[1] = 5
        sim.trees[0].parts[0].memory[2] = 10
        sim.update()
        self.assertEqual(sim.trees[0].parts[0].memory[0], 15)

    def test_sunlight_and_water(self):
        sim = Simulation(100, 100)
        sim.initialize()
        tree = sim.trees[0]
        root = tree.parts[0]
        leaf = tree.parts[1]

        # Set leaf to be perpendicular to sunlight
        leaf.angle = 90

        sim.update()

        self.assertGreater(leaf.energy, 0)
        self.assertGreater(root.water, 0)

if __name__ == '__main__':
    unittest.main()
