# 1. Variables
CXX      := g++
CXXFLAGS := -std=c++17 -Iinclude -O3
LDFLAGS  := -lsfml-graphics -lsfml-window -lsfml-system
SOURCES  := main.cpp $(wildcard src/*.cpp)
TARGET   := n-body-sim

# 2. The default rule (what happens when you just type 'make')
all:
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(TARGET) $(LDFLAGS)

# 3. Cleanup rule
clean:
	rm -f $(TARGET)
