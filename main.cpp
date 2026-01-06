#include <iostream>
#include <string>
#include <vector>
#include "include/Vec3D.hpp"
#include "include/Body.hpp"
// #include "include/Particules.hpp"
#include "include/Universe.hpp"
#include "include/Constants.hpp"
#include <SFML/Graphics.hpp>

using namespace Const;


sf::Vector2f meters_to_pixels(Vec3D position) {
    float x = static_cast<float>(position.x * SCALE) + (screenWidth / 2.0f);
    float y = static_cast<float>(-position.y * SCALE) + (screenHeight / 2.0f);
    return {x, y};
}

int main() {
    std::cout << "\033[2J\033[H" << std::flush;

    Universe sim;
    Body bod1("terre", Mt, Vec3D(0, Rot, 0), Vec3D(Vt, 0, 0), "Green");
    Body bod2("autre", Mt, Vec3D(0, 0.5*Rot, 0), Vec3D(-Vt, 0, 0), "Orange");
    Body bod3("soleil", 8 * Mo, Vec3D(0, 0, 0), Vec3D(0, 0.2* Vt, 0), "Orange");
    Body bod4("soleil2", Mt, Vec3D(Rot, 0, 0), Vec3D(-Vt, Vt, 0), "Orange");

    sim.add_body(bod1);
    sim.add_body(bod2);
    sim.add_body(bod3);
    sim.add_body(bod4);

    sf::RenderWindow window(
        sf::VideoMode({screenWidth, screenHeight}), 
        "N-body simulation", 
        sf::Style::Default, 
        sf::State::Windowed
    );
    // création des planètes

    sf::CircleShape shape(5.f);
    shape.setOrigin({5.f, 5.f});

    while (window.isOpen()) { // std::optional est une liste vide
        while (const std::optional event = window.pollEvent()) {
            if (event->is<sf::Event::Closed>()) { // comme un isinstance(event, Event)
                window.close();
            }
        }

        sim.compute_gravity();
        sim.step(dt);
        window.clear(sf::Color::Black);

        int totalFrames;
        totalFrames++;
        std::cout << "\033[H" << std::flush;
        // on rajoute & pour dire qu'on ne fait pas de copie
        for (Body& body : sim.get_bodies()) {
            if (totalFrames % 50 == 0) {
                std::cout << "frame: " << totalFrames << " " 
                << body._name
                << " - pos: ";
                body._pos.display();
                std::cout << std::endl;
            }
            
            shape.setPosition(meters_to_pixels(body._pos));
            window.draw(shape);
        }
        
        window.display();
    }
    return 0;
}