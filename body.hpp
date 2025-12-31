#include <string>
#include <vector>

struct Body {
    std::vector<double> position{3};
    std::vector<double> vitesse{3};
    std::vector<double> acceleration{3};
    std::vector<double> path{trail_length};

    private:
        std::string _name;
        std::string _color;

    Body(std::vector<double> position, double mass, \
    std::vector<double> initial_speed, std::string name, \
    std::string color, double radius);

    void update(double dt);

    void reset_acceleration();
};


