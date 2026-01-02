#pragma once 
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

    Body(std::string name, double mass, Vec3D position, Vec3D velocity, std::string color, double radius = 0, Vec3D acceleration = Vec3D(0, 0, 0));

    void update(double dt);
       
    void reset_acceleration();
};


