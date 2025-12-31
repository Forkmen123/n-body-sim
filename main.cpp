#include <iostream>
#include <vector>
#include "Body.hpp"
#include "Vec3D.hpp"

// astronomic constants
double const G = 6.67e-11;
double const Mo = 2e30;
double const Mt = 5.972e24;
double const Rot = 150e9;
double const Vt = 30e3;
double const Ro = 700000e3;

// visual constants 
double const density = 0.001;
double const trail_length = 5000;
double const limit = 2e11;

// simulation constants
int const fps = 60;
int const dt = 3600 * 0.1;
int const play_speed = 1000;


 


