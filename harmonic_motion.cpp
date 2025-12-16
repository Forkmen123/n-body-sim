#include <iostream> // This is like "import" for printing text
#include <string>
#include <vector>
#include <fstream> // file stream


class Spring {
    public: // public, private, protected
        double k; // int, bool, char, std::string
        double mass;
        double position;
        double c;
        double velocity;
        double acceleration;
        double F;
    
        Spring(double k_val, double mass_val, double position_val, double c_val) {
        // ici c'est le __init__
            k = k_val;
            mass = mass_val;
            position = position_val;
            c = c_val;
            velocity = 0.0;
            acceleration = 0.0;
        }

        void update(double dt) {
            double F = - k * position - c * velocity;
            acceleration = F / mass;
            velocity = velocity + dt * acceleration;
            position = position + dt * velocity;
        }
    }; 


int main() { // << are insertion operators
    std::string bienvenue = "The simulation is starting...";
    std::cout << bienvenue << std::endl; // standard character output
    
    Spring a(10.0, 0.1, 10.0, 0.2);
    std::cout << a.mass << std::endl;

    int step = 2000;
    double total_time = 5.0;
    double dt = total_time / step;

    std::vector<double> position_history(step); // this is an empty list
    // (step) is for the size of the list
    std::ofstream file("results.csv"); // output file stream
    
    //  for (start; stop; increment) i++ veut dire i += 1
    for (int i = 0; i < step; i++) {
        a.update(dt);
        position_history[i] = a.position;
    }

    for (int i = 0; i < step; i++) {
        file << position_history[i] << std::endl;
    }

    return 0; // pour la bonne gestion d'erreurs
}

