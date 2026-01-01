#pragma once 
using namespace std;
#include "Vec3D.hpp"
#include <string>
#include <vector>


struct Body {
    Vec3D position;
    Vec3D vitesse;
    Vec3D acceleration;

    std::vector<Vec3D> path;

    private:
        std::string _name;
        std::string _color;

    Body(std::vector<double> position, double mass, \
    std::vector<double> initial_speed, std::string name, \
    std::string color, double radius);

    // void update(double dt);
       

    // void reset_acceleration();
};


