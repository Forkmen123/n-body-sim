import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter

G = 6.67e-11
Mo = 2e30 # masse du soleil
Mt = 5.972e24 # masse de la terre
Rot = 150e6 # distance terre soleil
Vt = 30e3 # vitesse de révolution de la terre

class Body:
    def __init__(self, position, mass, initial_speed, name, color=None):
        self.position = np.array(position, dtype=float)
        self.vitesse = np.array(initial_speed, dtype=float)
        self.name = name
        self.mass = mass
        self.color = color
        self.acceleration = np.zeros(2)
        self.path_x = []
        self.path_y = []

    def update(self, dt):
        self.vitesse += self.acceleration * dt
        self.position += self.vitesse * dt

        self.path_x.append(self.position[0])
        self.path_y.append(self.position[1])

        MAX_LEN = 200
        if len(self.path_x) > MAX_LEN:
            self.path_x.pop(0)
            self.path_y.pop(0)

    def reset_acceleration(self):
        self.acceleration = np.zeros(2)

class Universe:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def compute_gravity(self):
        for body in self.bodies:
            body.reset_acceleration()

        # N-Body logic
        # Optimization: We could use Newton's 3rd law (F_ab = -F_ba) to halve loops,
        # but for N=3, this is readable and fast enough.
        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    r_vec = body1.position - body2.position
                    dist = np.linalg.norm(r_vec)
                    if dist == 0: continue # Avoid division by zero
                    
                    # a = -G * M / r^3 * vec(r)
                    acc_mag = -((G * body2.mass) / (dist ** 3))
                    body1.acceleration += acc_mag * r_vec

    def step(self, dt):
        self.compute_gravity()
        for body in self.bodies:
            body.update(dt)

def axis_in_UA(x, pos):
  return f'{x/Rot:.1f}'

def run_simulation():
    sim = Universe()
    # trou_noir = Body(position, mass, initial_speed, name, color)
    soleil = Body([0, 0], Mo, [0, 0], "Soleil", 'orange')
    # terre = Body([Rot, 0], Mt, [0, Vt], "Terre", 'blue')
    comete = Body([0, 1000], Mt, [0, 0], "Comète", 'red')

    # sim.add_body(trou_noir)
    sim.add_body(soleil)
    # sim.add_body(terre)
    sim.add_body(comete)

    # Setup Plot
    fig, ax = plt.subplots(figsize=(8, 8))
    # Dark background for space look
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Dynamic axis limits (start zoomed out)
    limit = 2e10
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    ax.xaxis.set_major_formatter(FuncFormatter(axis_in_UA))
    ax.yaxis.set_major_formatter(FuncFormatter(axis_in_UA))
    ax.set_ylabel('Distance (UA)', color='white')
    ax.set_xlabel('Distance (UA)', color='white')
    ax.tick_params(colors='white')


    # Store graphics objects
    lines = []
    points = []
    
    for body in sim.bodies:
        line, = ax.plot([], [], '-', lw=1, alpha=0.5, color=body.color)
        point, = ax.plot([], [], 'o', label=body.name, color=body.color)
        lines.append(line)
        points.append(point)

    dt = 3600 * 24 
    
    def update(frame):
        # Calculate physics multiple times per frame for smoothness vs speed
        # Doing 5 physics steps per animation frame speeds up the visual
        for _ in range(5):
            sim.step(dt)

        for i, body in enumerate(sim.bodies):
            # Update trails
            lines[i].set_data(body.path_x, body.path_y)
            # Update current position marker
            points[i].set_data([body.position[0]], [body.position[1]])
        
        return lines + points

    # Create animation
    ani = FuncAnimation(fig, update, frames=200, interval=20, blit=True)
    
    plt.title("N-Body Gravity Simulation", color='white')
    plt.grid(True, alpha=0.15)
    plt.show()

if __name__ == "__main__":
    run_simulation()