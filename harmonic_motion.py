import numpy as np
import matplotlib.pyplot as plt

g = 9.81

class Spring:
    def __init__(self, k: float, mass: float, position: float, c: float=0):
        self.k = k
        self.mass = mass
        self.position = np.array([position])
        self.c = c # damping coefficient
        self.velocity = np.array([0.])
        self.acceleration = np.array([0.])

    def update(self, dt):
        F = - self.k * self.position - self.c * self.velocity
        self.acceleration = F / self.mass 
        # ici je ne veux pas additionner l'accélération de différents
        # objets, parce que sinon l'accélération --> oo

        self.velocity = self.velocity + dt * self.acceleration 
        self.position = self.position + dt * self.velocity

a = Spring(10, 0.1, 10, 0.2)

step = 2000
total_time = 5
dt = total_time / step

position = np.zeros(step)

for i in range(step):
    a.update(dt)
    position[i] = a.position[0]


time = np.linspace(0, total_time, step)

time_elapsed = 0

plt.xlim(0, total_time)
plt.ylim(-position[0], position[0])
vertical_line = plt.axvline(0, color="red")
plt.plot(time, position)

for i in range(step):
    if i % 25 == 0:
        vertical_line.set_xdata([time[i], time[i]])
        plt.pause(dt)

plt.show()
