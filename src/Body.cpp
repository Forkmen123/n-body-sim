#include "Vec3D.hpp"
#include "Body.hpp"
#include <cmath>
#include <iostream>
#include <string>
#include "Constants.hpp"
#include <numbers>


Body::Body(
    std::string name, 
    double mass, 
    Vec3D position, 
    Vec3D velocity, 
    std::string color, 
    double radius, 
    Vec3D acceleration) : 
    _name(name), 
    _mass(mass), 
    _pos(position), 
    _vel(velocity), 
    _color(color), 
    _radius(radius), 
    _acc(acceleration)
    
{
    if (radius == 0) {
        double vol = mass / Const::DENSITY;
        radius = (3 * vol / pow((4 * Const::PI), 1.0/3.0));
    } 
}

void Body::update(double dt) {
    _vel += _acc * dt;
    _pos += _vel * dt;

    // seulement pour les bodies
    path[0].push_back(_pos[0]);
    path[1].push_back(_pos[1]);
    if (path[0].size() > Const::TRAIL_LENGTH) {
        path[0].pop_back();
        path[1].pop_back();
    }
}

void Body::reset_acceleration() {
    _acc = Vec3D(0, 0, 0);
}



