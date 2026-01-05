#include "Vec3D.hpp"
#include "Body.hpp"
#include "Universe.hpp"
#include "Constants.hpp"
#include <vector>


void Universe::add_body(Body body) {
    bodies.push_back(body);
}

std::vector<Body>& Universe::get_bodies() {
    return bodies;
}


// void Universe::add_dust(Particules particules) {
//     particules.push_back(particules);
// }

void Universe::compute_gravity() {
    for (Body body : bodies) {
       body.reset_acceleration();
    }

    // for (Particule particule : particules) {
    //     particule.reset_acceleration();
    // }
    size_t n = bodies.size();
    
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = i + 1; j < n; ++j) {
            Body& b1 = bodies[i];
            Body& b2 = bodies[j];
            Vec3D r_vec = b1._pos - b2._pos;

            double dist = r_vec.length();
            // if (dist < b1._radius + b2._radius) {
                // conditions à ajouter
            // }
            // else {
            double pow_dist = pow(dist, 3);

            Vec3D acc_mag = -((Const::G * b2._mass) / pow_dist);
            for (int i = 0; i < 3; i++) {
                b1._acc[i] += acc_mag[i] * r_vec[i];
            }

            Vec3D acc_mag_2 = ((Const::G * b1._mass) / pow_dist);
            for (int i = 0; i < 3; i++) {
                b2._acc[i] += acc_mag_2[i] * r_vec[i];
            }

            // }

            // for particule in particules

        }
    }

}

void Universe::step(int dt) {
    this->compute_gravity();

    for (Body& body : bodies) {
        body.update(dt);
    }
    // for particule in particules 
}
