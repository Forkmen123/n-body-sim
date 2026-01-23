#include "Vec3D.hpp"
#include "Particules.hpp"
#include <cmath>
#include <iostream>
#include <string>
#include "Constants.hpp"
#include <numbers>


Body::Particules(
    std::string _name, 
    double _total_mass, 
    Vec3D _pos, 
    Vec3D vel, 
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

