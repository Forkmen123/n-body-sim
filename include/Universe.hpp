#pragma once
#include <vector>
#include "Body.hpp"


class Universe {
    std::vector<Body> bodies;
    // std::vector<int> particules;
    public:
        void add_body(Body body);
        std::vector<Body>& get_bodies();
//    void add_dust(Particule particule);

    void compute_gravity();
    void step(int dt);
};