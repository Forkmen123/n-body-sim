using namespace std;
#include <cmath>


struct Vec3D {
    double x, y, z;

    Vec3D(double _x = 0, double _y = 0, double _z = 0) {
        x = _x;
        y = _y;
        z = _z;
    }

    Vec3D operator+(const Vec3D& other) const {
        return Vec3D(x + other.x, y + other.y, z + other.z);
    }

    Vec3D operator-(const Vec3D& other) const {
        return Vec3D(x - other.x, y - other.y, z + other.z);
    }

    double length(const Vec3D& other) const {
        return x * other.x + y * other.y + z * other.z;
    }
};

