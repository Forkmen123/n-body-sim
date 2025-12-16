#include <iostream> // This is like "import" for printing text
#include <string>


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


int main() {
    std::string bienvenue = "The simulation is starting...";
    std::cout << bienvenue << std::endl;
    
    Spring a(10.0, 0.1, 10.0, 0.2);
    std::cout << a.mass << std::endl;

    int step = 2000;
    int total_time = 5;
    double dt = total_time / step;

//  for (start; stop; increment) i++ veut dire i += 1
    for (int i = 0; i < step; i++) {
        a.update(dt);
        double position = a.position;
    }

    return 0; // pour la bonne gestion d'erreurs
}

// step = 2000
// total_time = 5
// dt = total_time / step

// position = np.zeros(step)

// for i in range(step):
//     a.update(dt)
//     position[i] = a.position[0]


// time = np.linspace(0, total_time, step)

// time_elapsed = 0

// plt.xlim(0, total_time)
// plt.ylim(-position[0], position[0])
// vertical_line = plt.axvline(0, color="red")
// plt.plot(time, position)

// for i in range(step):
//     if i % 25 == 0:
//         vertical_line.set_xdata([time[i], time[i]])
//         plt.pause(dt)
    

// plt.show()