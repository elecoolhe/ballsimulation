# ballsimulation

A small Python Turtle animation that simulates a white ball bouncing inside a square border.

## What It Does

- Opens a 600 x 600 Turtle graphics window.
- Draws a white square border on a black background.
- Places a white circular ball at a random starting position.
- Gives the ball a random x/y velocity.
- Reverses direction when the ball reaches the border.

## Run From Source

```powershell
python ball_simulation.py
```

## Build The Executable

```powershell
python ball_simulation.py build
```

or:

```powershell
build_ball_simulation.bat
```

The built executable is expected at:

```text
dist\ball_simulation.exe
```

## Repository Contents

- `ball_simulation.py`: original source code.
- `ball_simulation.spec`: PyInstaller build specification.
- `build.bat` and `build_ball_simulation.bat`: Windows build helpers.
- `dist\ball_simulation.exe`: restored packaged executable.
- PyInstaller build artifacts are also preserved in this repository.
