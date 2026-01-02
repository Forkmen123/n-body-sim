#include "Vec3D.hpp"
#include "Body.hpp"
#include <cmath>
#include <iostream>
#include <string>


Body::Body(std::string name, double mass, Vec3D position, Vec3D velocity, std::string color, double radius, Vec3D acceleration) : 
    _name(name), 
    _mass(mass), 
    _pos(position), 
    _vel(velocity), 
    _color(color), 
    _radius(radius), 
    _acc(acceleration)
{



}





