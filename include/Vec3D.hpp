#pragma once
#include <cmath>
#include <string>


struct Vec3D {
    double x, y, z;

    Vec3D(double _x = 0, double _y = 0, double _z = 0);

    Vec3D operator+(const Vec3D& other) const;

    Vec3D operator-(const Vec3D& other) const;

    double length() const;

    void print() const;
};




