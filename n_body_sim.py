import numpy as np
import matplotlib.pyplot as plt


# astrophysical constants
G = 6.67e-11
Mo = 2e30 # masse du soleil
Mt = 5.972e24 # masse de la terre
Rot = 150e9 # distance terre soleil
Vt = 30e3 # vitesse de révolution de la terre
Ro = 700000e3 # rayon du soleil

# other constants
# ---------------- visual constants ---------------------------
DENSITY = 0.001 # density = 1410 # densité du soleil en kg/m^3
TRAIL_LENGTH = 50000 # path length
LIMIT = 2e11

# ---------------- rendering constants ---------------------------
FPS_COUNT = 60 # fluidité / charge CPU --> n'influence pas la physique
dt = 3600 * 0.1 # équivaut à un jour complet (temps de repos de l'affichage) 
# dt determine la précision de la physique --> 'distance' parcourur par image
PLAY_SPEED = 1000 # accélère la vitesse globale de l'animation

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
            vol = self.mass / DENSITY
            self.radius = (3 * vol / (4 * np.pi)) ** (1/3)
        else:
            self.radius = radius
            
    def update(self, dt):
        # euler integration --> peut être plus précis
        self.vitesse += self.acceleration * dt
        self.position += self.vitesse * dt
        
        self.path[0].append(self.position[0])
        self.path[1].append(self.position[1])
        if len(self.path[0]) > TRAIL_LENGTH and isinstance(self, Body):
            self.path[0].pop(0)
            self.path[1].pop(0)

    def reset_acceleration(self):
        self.acceleration = np.zeros(2)


class Particules(Body):
    def __init__(self, n, color='red'):
        self.n = n # n = nombre de particules
        self.position = np.array(np.random.uniform(-LIMIT, LIMIT, (n, 2)))
        self.vitesse = np.zeros((n, 2))
        self.acceleration = np.zeros((n, 2))
        self.color = color
        self.radius = 10000

    def update(self, dt):
        self.vitesse += self.acceleration * dt
        self.position += self.vitesse * dt

    def reset_acceleration(self):
        self.acceleration = np.zeros((self.n, 2))

    def change_dust_position_distribution(self, type_de_distribution: str):
        pass

class Universe:
    def __init__(self):
        self.bodies = []
        self.dust = []

    def add_body(self, body):
        self.bodies.append(body)

    def add_dust(self, particles):
        self.dust.append(particles)

    def compute_gravity(self):
        for particules in self.dust:
            particules.reset_acceleration()

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
                        overlap = (body1.radius + body2.radius) - dist
                        direction = r_vec / dist

                        body1.position += direction * (overlap / 2)
                        body2.position -= direction * (overlap / 2)

                        m1, m2 = body1.mass, body2.mass
                        v1, v2 = body1.vitesse, body2.vitesse
                        x1, x2 = body1.position, body2.position

                        # conservation de la quantité de mouvement
                        body1.vitesse = v1 - (2*m2 / (m1+m2)) * np.dot(v1-v2, x1-x2) / dist**2 * (x1-x2)
                        body2.vitesse = v2 - (2*m1 / (m1+m2)) * np.dot(v2-v1, x2-x1) / dist**2 * (x2-x1)
                    
                    # a = -G * M / r^3 * vec(r)
                    else:
                        acc_mag = -((G * body2.mass) / (dist ** 3))
                        body1.acceleration += acc_mag * r_vec
        
        for particules in self.dust:
            for body in self.bodies:
                r_vecs = body.position - particules.position
                dist = np.sqrt(np.sum(r_vecs**2, axis=1).reshape(-1, 1))
                dist = np.maximum(dist, 1) # pour éviter d'avoir des divisions 0
        
                acc_mag = ((G * body2.mass) / (dist ** 3))
                particules.acceleration += acc_mag * r_vecs

                mask = dist.flatten() < body.radius
                particules.vitesse[mask] = 0
                particules.acceleration[mask] = 0

    def step(self, dt):
        self.compute_gravity()
        for body in self.bodies:
            body.update(dt)

def axis_in_UA(x, pos):
    return f'{x/Rot:.1f}'

def run_simulation():
    sim = Universe()

    # ---------------- init bodies  ----------------
    # (position, mass, initial_speed, name, color, radius)
    trou_noir = Body([Ro, Ro], 1*Mo, [0, 0], "Trou Noir", 'white', Ro)
    soleil = Body([0, 0], Mo, [0, 0], "Soleil", 'orange', Ro)
    terre = Body([Rot, 0], Mt, [0, Vt], "Terre", 'blue')
    bod1 = Body([0,  Rot], Mo, [0, -0.1*Vt], "Comète", 'red', Ro)
    bod2 = Body([0, -Rot], Mt, [-0.5*Vt, 0.1*Vt], "Comète", 'red')
    dust = Particules(100)

    # sim.add_body(trou_noir)
    sim.add_body(soleil)
    sim.add_body(terre)
    sim.add_body(dust)
    # sim.add_body(bod2)

    fig, ax = plt.subplots(figsize=(8, 8))
    plt.ion() # interactive mode 
    
    # -------------------------------------------- styling/animation ------
    plt.title("N-Body Gravity Simulation", color='white')
    plt.grid(True, alpha=0.15)
    plt.show()

    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    ax.set_xlim(-LIMIT, LIMIT)
    ax.set_ylim(-LIMIT, LIMIT)

    lines = []
    points = []
    for body in sim.bodies:
        line, = ax.plot([], [], '-', lw=1, alpha=0.5, color=body.color)
        point, = ax.plot([], [], 'o', markersize=body.radius/10e7, label=body.name, color=body.color)
        lines.append(line)
        points.append(point)

    ax.set_ylabel('Distance (UA)', color='white')
    ax.set_xlabel('Distance (UA)', color='white')
    ax.tick_params(colors='white')

    running = True

    while running:
        for i in range(PLAY_SPEED):
            sim.step(dt)
        
        for i, body in enumerate(sim.bodies):
            if isinstance(body, Body):
                lines[i].set_data(body.path[0], body.path[1])
                points[i].set_data([body.position[0]], [body.position[1]])
            else:
                points[i].set_data([body.position[0]], [body.position[1]])

        pause_time = FPS_COUNT ** -1
        plt.pause(pause_time)
        
        if not plt.fignum_exists(fig.number):
            running = False # validation peut-être inutile 


if __name__ == "__main__":
    run_simulation()
    # py n_body_sim.py dans le terminal fait que __name__ is set to __main__
    # sinon, si on import n_body_sim.py __name__ != "__main__"