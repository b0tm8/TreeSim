import tkinter as tk
from tkinter import ttk
from ..model.tree_part import PartType

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TreeSim")
        self.geometry("1200x800")

        # Main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left panel for statistics
        left_panel = ttk.Frame(main_frame, width=200)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Label(left_panel, text="Statistics").pack(pady=10)

        # Center panel for simulation display
        self.center_panel = ttk.Frame(main_frame)
        self.center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.center_panel, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Right panel for statistics
        right_panel = ttk.Frame(main_frame, width=200)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y)
        ttk.Label(right_panel, text="Statistics").pack(pady=10)

        # Control panel at the bottom
        control_panel = ttk.Frame(self, height=100)
        control_panel.pack(side=tk.BOTTOM, fill=tk.X)

        # Control buttons
        ttk.Button(control_panel, text="Start").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_panel, text="Stop").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_panel, text="Reset").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_panel, text="Save").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_panel, text="Load").pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(control_panel, text="Menu").pack(side=tk.RIGHT, padx=5, pady=5)

    def draw_simulation(self, simulation):
        self.canvas.delete("all")
        for tree in simulation.trees:
            for part in tree.parts:
                x1 = part.x - part.size / 2
                y1 = part.y - part.size / 2
                x2 = part.x + part.size / 2
                y2 = part.y + part.size / 2
                if part.part_type == PartType.ROOT:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="brown")
                elif part.part_type == PartType.BRANCH:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="saddlebrown")
                elif part.part_type == PartType.LEAF:
                    self.canvas.create_oval(x1, y1, x2, y2, fill="green")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
