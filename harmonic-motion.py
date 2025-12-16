import numpy as np
import matplotlib.pyplot as plt

g = 9.81

class Spring:
    def __init__(self, k: float, mass: float, position: float):
        self.k = k
        self.mass = mass
        self.position = np.array([position])
        self.velocity = np.array([0.])
        self.acceleration = np.array([0.])

    def update(self, dt):
        F = -self.k * self.position
        self.acceleration = F / self.mass 
        # ici je ne veux pas additionner l'accélération de différents
        # objets, parce que sinon l'accélération --> oo

        self.velocity = self.velocity + dt * self.acceleration 
        self.position = self.position + dt * self.velocity


a = Spring(1, 1, 1)

step = 2000
total_time = 20
dt = total_time / step

position = np.zeros(step)

for i in range(step):
    a.update(dt)
    position[i] = a.position[0]


time = np.linspace(0, total_time, step)
plt.plot(time, position)
plt.show()