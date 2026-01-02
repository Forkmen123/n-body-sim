#pragma once 
#include "Vec3D.hpp"
#include <string>
#include <vector>


struct Body {
    std::string _name;
    double _mass;
    Vec3D _pos;
    Vec3D _vel;
    std::string _color;
    double _radius;
    Vec3D _acc;
    std::vector<Vec3D> path;

    Body(std::string name, double mass, Vec3D position, Vec3D velocity, std::string color, double radius = 0, Vec3D acceleration = Vec3D(0, 0, 0));

    void update(double dt) {

    }
       
    void reset_acceleration() {

    }
};


