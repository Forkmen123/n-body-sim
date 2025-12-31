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
TRAIL_LENGTH = 0 # path length
LIMIT = Rot * 2
SHOW_BODY_POSITION = False
SHOW_PARTICLES_POSITION = True

# ---------------- rendering constants ---------------------------
FPS_COUNT = 60 # fluidité / charge CPU --> n'influence pas la physique
dt = 3600 * 0.1 # équivaut à un jour complet (temps de repos de l'affichage) 
# dt determine la précision de la physique --> 'distance' parcourur par image
PLAY_SPEED = 300 # accélère la vitesse globale de l'animation

class Body:
    def __init__(self, position: tuple, mass: int, initial_speed: tuple, name: str, color=None, radius=True):
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
        if len(self.path[0]) > TRAIL_LENGTH and not isinstance(self, Particules):
            self.path[0].pop(0)
            self.path[1].pop(0)

    def reset_acceleration(self):
        self.acceleration = np.zeros(2)


class Particules(Body):
    def __init__(self, n, total_mass, color, name, radius=1000):
        self.n = n # n = nombre de particule
        self.position = np.array(np.random.uniform(-LIMIT, LIMIT, (n, 2)))
        self.vitesse = np.zeros((n, 2))
        self.acceleration = np.zeros((n, 2))
        self.color = color
        self.radius = radius
        self.total_mass = total_mass
        self.name = name

        # on doit faire poussière.particules
    def update(self, dt):
        self.vitesse += self.acceleration * dt
        self.position += self.vitesse * dt

    def reset_acceleration(self):
        self.acceleration = np.zeros((self.n, 2))

    def change_dust_position_distribution(self, distribution: str):
        pass


class Universe:
    def __init__(self):
        self.bodies = []
        self.particules = []

    def add_body(self, body: Body):
        self.bodies.append(body)

    def add_dust(self, particule: Particules):
        self.particules.append(particule) # [[(1,2), (2, 3), ...], [(1,2), (2, 3), ...]] liste de listes de tuples 

    def compute_gravity(self):
        for particule in self.particules:
            particule.reset_acceleration()

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
                        # overlap = (body1.radius + body2.radius) - dist
                        # direction = r_vec / dist

                        # body1.position += direction * (overlap / 2)
                        # body2.position -= direction * (overlap / 2)

                        # m1, m2 = body1.mass, body2.mass
                        # v1, v2 = body1.vitesse, body2.vitesse
                        # x1, x2 = body1.position, body2.position

                        # # conservation de la quantité de mouvement
                        # body1.vitesse = v1 - (2*m2 / (m1+m2)) * np.dot(v1-v2, x1-x2) / dist**2 * (x1-x2)
                        # body2.vitesse = v2 - (2*m1 / (m1+m2)) * np.dot(v2-v1, x2-x1) / dist**2 * (x2-x1)
                        pass
                    # a = -G * M / r^3 * vec(r)
                    else:
                        acc_mag = -((G * body2.mass) / (dist ** 3))
                        body1.acceleration += acc_mag * r_vec

                        acc_mag_2 = ((G * body1.mass) / (dist ** 3))
                        body2.acceleration += acc_mag_2 * r_vec
        
        for particule in self.particules:
            for body in self.bodies:
                r_vecs = body.position - particule.position
                dist = np.sqrt(np.sum(r_vecs**2, axis=1).reshape(-1, 1))
                dist = np.maximum(dist, body.radius * 5) # pour éviter d'avoir des divisions 0
        
                acc_mag = ((G * body.mass) / (dist ** 3))
                particule.acceleration += acc_mag * r_vecs

                mask = dist.flatten() < body.radius
                particule.vitesse[mask] = 0
                particule.acceleration[mask] = 0

    def step(self, dt):
        self.compute_gravity()
        for body in self.bodies:
            body.update(dt)

        for particule in self.particules:
            particule.update(dt)

def axis_in_UA(x, pos):
    return f'{x/Rot:.1f}'

def run_simulation():
    sim = Universe()

    # ---------------- init bodies  ----------------
    # (position, mass, initial_speed, name, color, radius)
    bod1 = Body([Rot, 0], Mt, [0, Vt], "terre", 'green')
    bod2 = Body([0, 0], Mo, [0, 0], "bod2", 'yellow', Ro)
    bod3 = Body([0, Rot], Mo, [0.5 * Vt, 0], "bod3", 'red', Ro)
    poussière = Particules(100, 10 * Mo, "white", "poussière", radius=Ro)

    sim.add_body(bod1)
    sim.add_body(bod2)
    sim.add_body(bod3)
    sim.add_dust(poussière)

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
    
    for particule in sim.particules:
        point, = ax.plot([], [], '.', markersize=1, label=particule.name, color=particule.color)
        points.append(point)


    ax.set_ylabel('Distance (UA)', color='white')
    ax.set_xlabel('Distance (UA)', color='white')
    ax.tick_params(colors='white')

    running = True

    while running:
        if SHOW_BODY_POSITION:
            print(f'{bod1.name}: {bod1.position[0]:.2e}, {bod1.position[1]:.2e} \
                  {bod2.name}: {bod2.position[0]:.2e}, {bod2.position[1]:.2e} \
                    {bod3.name}: {bod3.position[0]:.2e}, {bod3.position[1]:.2e}')

        # if SHOW_PARTICLES_POSITION:
            # print(poussière.position[1])     

        for i in range(PLAY_SPEED):
            sim.step(dt)
        
        for i, body in enumerate(sim.bodies):
            lines[i].set_data(body.path[0], body.path[1])
            points[i].set_data([body.position[0]], [body.position[1]])

        for i, particule in enumerate(sim.particules):
            index = i + len(sim.bodies)

            points[index].set_data(particule.position[:, 0], particule.position[:, 1])

        pause_time = FPS_COUNT ** -1
        plt.pause(pause_time)
        
        if not plt.fignum_exists(fig.number):
            running = False # validation peut-être inutile 


if __name__ == "__main__":
    run_simulation()
    # py n_body_sim.py dans le terminal fait que __name__ is set to __main__
    # sinon, si on import n_body_sim.py __name__ != "__main__"