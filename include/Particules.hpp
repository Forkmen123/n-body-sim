#pragma once 
#include "Vec3D.hpp"
#include <string>
#include <vector>


struct Particules : public Body {
    std::string _name;
    int _total_mass;
    int _n;
    Vec3D _pos;
    std::string _color;

    Particules(
        std::string name, 
        int mass,
        int total_mass,
    );
};

// class Particules(Body):
//     def __init__(self, n, total_mass, color, name, radius=1000):
//         self.n = n # n = nombre de particule
//         self.position = np.array(np.random.uniform(-LIMIT, LIMIT, (n, 2)))
//         self.vitesse = np.zeros((n, 2))
//         self.acceleration = np.zeros((n, 2))
//         self.color = color
//         self.radius = radius
//         self.total_mass = total_mass
//         self.name = name

//         # on doit faire poussière.particules
//     def update(self, dt):
//         self.vitesse += self.acceleration * dt
//         self.position += self.vitesse * dt

//     def reset_acceleration(self):
//         self.acceleration = np.zeros((self.n, 2))

//     def change_dust_position_distribution(self, distribution: str):
//         pass
