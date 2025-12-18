import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter


# astrophysical constants
G = 6.67e-11
Mo = 2e30 # masse du soleil
Mt = 5.972e24 # masse de la terre
Rot = 150e9 # distance terre soleil
Vt = 30e3 # vitesse de révolution de la terre
Ro = 700000e3 # rayon du soleil


class Body:
    def __init__(self, position, mass, initial_speed, name, color=None, radius=True):
        self.position = np.array(position, dtype=float)
        self.vitesse = np.array(initial_speed, dtype=float)
        self.name = name
        self.mass = mass
        self.color = color
        self.acceleration = np.zeros(2)
        self.path = [[], []] # [[historique path x], [historique path x]]

        # calculs pour le rayon
        if radius is True:
            # density = 1410 # densité du soleil en kg/m^3
            density = 0.001 
            vol = self.mass / density
            self.radius = (3 * vol / (4 * np.pi)) ** (1/3)
        else:
            self.radius = radius
            
    def update(self, dt):
        # euler integration --> peut être plus précis
        self.vitesse += self.acceleration * dt
        self.position += self.vitesse * dt
        
        TRAIL_LENGTH = 2000 # path length
        self.path[0].append(self.position[0])
        self.path[1].append(self.position[1])
        if len(self.path[0]) > TRAIL_LENGTH:
            self.path[0].pop(0)
            self.path[1].pop(0)

    def reset_acceleration(self):
        self.acceleration = np.zeros(2)


class Particules(Body):
    def __init__(self, n, color='gray'):
        self.n = n # n = nombre de particulesi

    def random_speed(self, chaos: float): # 0 = peu chaos... 1 = très cahotique  
        pass 


class Universe:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def add_particules(self, particules):
        pass

    def compute_gravity(self):
        for body in self.bodies:
            body.reset_acceleration() # on reset l'accélération après chaque dt...
        
    # N-Body logic
    # Optimization: We could use Newton's 3rd law (F_ab = -F_ba) to halve loops,
    # but for N=3, this is readable and fast enough.

        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):
                if i > j:
                    r_vec = body1.position - body2.position
                    dist = np.linalg.norm(r_vec)

                    if dist < body1.radius + body2.radius: 
                        m1, m2 = body1.mass, body2.mass
                        v1, v2 = body1.vitesse, body2.vitesse
                        x1, x2 = body1.position, body2.position

                        # conservation de la quantité de mouvement
                        body1.vitesse = v1 - (2*m2 / (m1+m2)) * np.dot(v1-v2, x1-x2) / dist**2 * (x1-x2)
                        body2.vitesse = v1 - (2*m1 / (m1+m2)) * np.dot(v2-v1, x2-x1) / dist**2 * (x2-x1)
                    
                    # a = -G * M / r^3 * vec(r)
                    else:
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
    # (position, mass, initial_speed, name, color, radius)
    soleil = Body([0, 0], 0.2*Mo, [0, 0], "Soleil", 'orange', Ro)
    terre = Body([Rot, 0], Mt, [0, Vt], "Terre", 'blue')
    bod1 = Body([0,  Rot], 40*Mt, [0, -0.1*Vt], "Comète", 'red')
    bod2 = Body([0, -Rot], Mt, [0, 0.1*Vt], "Comète", 'red')

    # sim.add_body(trou_noir)
    # sim.add_body(soleil)
    sim.add_body(terre)
    sim.add_body(bod1)
    sim.add_body(bod2)

    # Setup Plot
    fig, ax = plt.subplots(figsize=(8, 8))
    # Dark background for space look
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Dynamic axis limits (start zoomed out)
    limit = 2e11
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
        point, = ax.plot([], [], 'o', markersize=body.radius/10e7, label=body.name, color=body.color)
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
            lines[i].set_data(body.path[0], body.path[1])
            # Update current position marker
            points[i].set_data([body.position[0]], [body.position[1]])
        
        return lines + points

    # Create animation
    ani = FuncAnimation(fig, update, frames=200, interval=20, blit=True)
    
    plt.title("N-Body Gravity Simulation", color='white')
    # plt.grid(True, alpha=0.15)
    plt.show()



running = True
while running:
    for i in range(10):
        

if __name__ == "__main__":
    run_simulation()
    # py n_body_sim.py dans le terminal fait que __name__ is set to __main__
    # sinon, si on import n_body_sim.py __name__ != "__main__"