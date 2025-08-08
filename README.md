# 🎮 PyGame Project Template

**✨ Quick start for PyGame development with a clean modular structure**

---

## 📂 Project Structure

```
game_template/  
│  
├── 🚀 main.py                # Main executable file  
├── 📁 src/                   # Source code  
│   ├── 📂 modules/          # Utility modules (helpers, tools)  
│   ├── 🎭 scenes/           # Game scenes/screens (menus, levels)  
│   ├── 👾 sprites/          # Custom sprites and game objects  
│   ├── ⚙️ app.py            # Application core (settings, main loop)  
│   ├── 🔊 audio.py          # Sound and music manager  
│   ├── 🖼️ scene.py          # Base Scene class  
│   ├── � sprite.py         # Base Sprite class  
├── 📝 logs/                 # Game logs (if enabled)  
├── 🗃️ assets/               # Resources  
│   ├── 🖼️ images/           # Textures, sprites, backgrounds  
│   ├── 🎵 sounds/           # SFX and music  
│   └── 🔠 fonts/            # Fonts  
└── 📜 README.md             # Documentation  
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash  
   git clone <your-repo>  
   cd game_template  
   ```  

2. **Install dependencies** (PyGame + ColorLog):
   ```bash  
   pip install pygame colorlog  
   ```  

3. **Run the game**:
   ```bash  
   python main.py  
   ```  

---

## 🎯 Example Projects

🔗 *[Fate Bound](https://github.com/TheSpace-hub/FateBound)* - Soul Knight-style roguelike game.  
🔗 *[Traffic Lights City](https://github.com/TheSpace-hub/TrafficLightsCity)* - Traffic light simulation service tester.

## 🧩 How to Extend

1. **Add a new scene**:
    - Create a file in `src/scenes/` (e.g., `level1.py`).
    - Inherit from the `Scene` base class.

2. **Create a sprite**:
    - Add a class in `src/sprites/` (e.g., `enemy.py`).
    - Use the base `Sprite` class for automatic image handling.

3. **Manage assets**:
    - Place images in `assets/images/`, sounds in `assets/sounds/`.  
