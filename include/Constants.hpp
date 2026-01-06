#pragma once

namespace Const {
// on ajoute constexpr pour que le calcul de la 
// valeur de la constante soit calculé pendant 
// la compilation et non pendant que le programme roule 

    // astronomic constants
    inline constexpr double G = 6.67e-11; 
    inline constexpr double PI = 3.14159265358979323846;
    inline constexpr double Mo = 2e30;
    inline constexpr double Mt = 5.972e24;
    inline constexpr double Rot = 150e9;
    inline constexpr double Vt = 30e3;
    inline constexpr double Ro = 700000e3;

    // // visual constants 
    inline constexpr double DENSITY = 0.001;
    inline constexpr double TRAIL_LENGTH = 5000;
    inline constexpr double SCALE = 100.0 / Rot; // in meters

    // // simulation constants
    inline constexpr int fps = 60;
    inline constexpr int play_speed = 5;
    inline constexpr int dt = 3600 * 0.1 * play_speed;
    
    // screen constants 
    inline constexpr int screenWidth = 800;
    inline constexpr int screenHeight = 600;
};