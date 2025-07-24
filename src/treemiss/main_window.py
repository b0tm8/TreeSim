import tkinter as tk
from tkinter import ttk

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
        center_panel = ttk.Frame(main_frame)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ttk.Label(center_panel, text="Simulation Display").pack(pady=10)

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

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
