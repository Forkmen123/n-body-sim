# --- CONFIGURATION ---
CXX = g++
CXXFLAGS = -I include -Wall -std=c++17
OBJDIR = obj
TARGET = sim

# Liste des fichiers sources (avec leurs chemins)
SRCS = main.cpp src/Vec3D.cpp src/Body.cpp src/Particules.cpp src/Universe.cpp

# Transformation magique : 
# On transforme "src/Body.cpp" en "obj/Body.o"
OBJS = $(addprefix $(OBJDIR)/, $(notdir $(SRCS:.cpp=.o)))

# --- RÈGLES ---

# Règle finale : lie les objets présents dans obj/
$(TARGET): $(OBJDIR) $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET)

# Règle pour compiler main.cpp vers obj/main.o
$(OBJDIR)/main.o: main.cpp | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Règle générique pour tous les fichiers dans src/ vers obj/
$(OBJDIR)/%.o: src/%.cpp | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Crée le dossier obj/ s'il n'existe pas
$(OBJDIR):
	mkdir -p $(OBJDIR)

clean:
	rm -rf $(OBJDIR) $(TARGET)# ==========================================
# VARIABLES : Configuration du projet
# ==========================================

# Le compilateur à utiliser
CXX = g++

# Options de compilation
# -I include : dit au compilateur de chercher les .hpp dans le dossier include
# -Wall : affiche tous les avertissements (warnings) pour coder proprement
# -std=c++17 : utilise la version moderne du C++
CXXFLAGS = -I include -Wall -std=c++17

# Liste de tous les fichiers objets (.o) à créer
# On liste les fichiers du dossier src et le main à la racine
OBJ = main.o src/Vec3D.o src/Body.o src/Particules.o src/Universe.o

# Nom de l'exécutable final
TARGET = sim

# ==========================================
# RÈGLES DE COMPILATION
# ==========================================

# Règle principale : crée l'exécutable final en liant tous les .o
$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $(TARGET)

# --- Compilation des fichiers dans le dossier src/ ---

src/Vec3D.o: src/Vec3D.cpp include/Vec3D.hpp
	$(CXX) $(CXXFLAGS) -c src/Vec3D.cpp -o src/Vec3D.o

src/Body.o: src/Body.cpp include/Body.hpp include/Vec3D.hpp
	$(CXX) $(CXXFLAGS) -c src/Body.cpp -o src/Body.o

src/Particules.o: src/Particules.cpp include/Particules.hpp include/Vec3D.hpp
	$(CXX) $(CXXFLAGS) -c src/Particules.cpp -o src/Particules.o

src/Universe.o: src/Universe.cpp include/Universe.hpp include/Body.hpp
	$(CXX) $(CXXFLAGS) -c src/Universe.cpp -o src/Universe.o

# --- Compilation du fichier main à la racine ---

main.o: main.cpp include/Vec3D.hpp include/Body.hpp include/Particules.hpp include/Universe.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o

# --- Nettoyage des fichiers temporaires ---

clean:
	rm -f $(OBJ) $(TARGET)
