#include "Vec3D.hpp"
#include <cmath>
#include <iostream>
#include <string>

double x, y, z;

Vec3D::Vec3D(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {} 

Vec3D Vec3D::operator+(const Vec3D& other) const {
    return Vec3D(x + other.x, y + other.y, z + other.z);
}

Vec3D Vec3D::operator-(const Vec3D& other) const {
    return Vec3D(x - other.x, y - other.y, z - other.z);
}

Vec3D Vec3D::operator*(double scalar) const {
    return Vec3D(x * scalar, y * scalar, z * scalar);
}

Vec3D Vec3D::operator+=(const Vec3D& other) {
    x += other.x;
    y += other.y;
    z += other.z;
    return *this; // c'est comme un return self 
}

Vec3D Vec3D::operator-=(const Vec3D& other) {
    x -= other.x;
    y -= other.y;
    z -= other.z;
    return *this;
}
double& Vec3D::operator[](int index) {
    if (index == 0) return x;
    if (index == 1) return y;
    return z;
}

double Vec3D::length() const {
    return std::sqrt(x * x + y * y + z * z);
}

void Vec3D::print() const {
    std::cout << "[" << x << ", " << y << ", " << z << "]\n";
}




