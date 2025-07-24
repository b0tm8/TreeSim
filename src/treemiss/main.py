from .view.main_window import MainWindow
from .model.simulation import Simulation

def update_simulation(app):
    if app.simulation_running:
        app.simulation.update()
        app.draw_simulation(app.simulation)
    app.after(100, update_simulation, app)

if __name__ == "__main__":
    sim = Simulation(800, 600)
    sim.initialize()
    app = MainWindow(sim)
    app.after(100, update_simulation, app)
    app.mainloop()
