from .view.main_window import MainWindow
from .model.simulation import Simulation

def update_simulation(app, sim):
    sim.update()
    app.draw_simulation(sim)
    app.after(100, update_simulation, app, sim)

if __name__ == "__main__":
    sim = Simulation(800, 600)
    sim.initialize()
    app = MainWindow()
    app.after(100, update_simulation, app, sim)
    app.mainloop()
