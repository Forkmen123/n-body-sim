#include "Vec3D.hpp"
#include <cmath>
#include <iostream>
#include <string>

double x, y, z;

Vec3D::Vec3D(double _x, double _y, double _z) {
    x = _x;
    y = _y;
    z = _z;
}

Vec3D Vec3D::operator+(const Vec3D& other) const {
    return Vec3D(x + other.x, y + other.y, z + other.z);
}

Vec3D Vec3D::operator-(const Vec3D& other) const {
    return Vec3D(x - other.x, y - other.y, z + other.z);
}

double Vec3D::length() const {
    return std::sqrt(x * x + y * y + z * z);
}

void Vec3D::print() const {
    std::cout << "[" << x << ", " << y << ", " << z << "]\n";
}




