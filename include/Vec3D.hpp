#pragma once
#include <cmath>
#include <string>
#include <iostream>


struct Vec3D {
    double x, y, z;

    Vec3D(double _x = 0, double _y = 0, double _z = 0);

    Vec3D operator+(const Vec3D& other) const;
    Vec3D operator-(const Vec3D& other) const;
    Vec3D operator*(double scalar) const;
    Vec3D operator+=(const Vec3D& other);
    Vec3D operator-=(const Vec3D& other);
    double& operator[](int index);

    double length() const;
    void print() const;
};




