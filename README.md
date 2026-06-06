# ballsimulation

A small Python Turtle animation that simulates a white ball bouncing inside a square border.

一个使用 Python Turtle 编写的小型动画程序，用来模拟白色小球在方形边框内反弹运动。

## What It Does

## 功能说明

- Opens a 600 x 600 Turtle graphics window.

  打开一个 600 x 600 的 Turtle 图形窗口。

- Draws a white square border on a black background.

  在黑色背景上绘制一个白色方形边框。

- Places a white circular ball at a random starting position.

  在随机初始位置放置一个白色圆形小球。

- Gives the ball a random x/y velocity.

  为小球设置随机的 x/y 方向速度。

- Reverses direction when the ball reaches the border.

  当小球碰到边框时，自动反转运动方向。

## Run From Source

## 从源码运行

```powershell
python ball_simulation.py
```

## Build The Executable

## 构建可执行文件

```powershell
python ball_simulation.py build
```

or:

或者：

```powershell
build_ball_simulation.bat
```

The built executable is expected at:

构建完成后的可执行文件预计位于：

```text
dist\ball_simulation.exe
```

A preserved PyInstaller build snapshot is available at:

已保留的一次 PyInstaller 打包现场备份位于：

```text
pyinstaller_build_backup\
```

## Multi-ball Chaos Version

## 多小球混乱度版本

The new version is available in:

新版程序位于：

```text
multi_ball_chaos_simulation.py
```

It simulates 30 balls with random initial positions and velocities, displays the current system chaos value in real time, and draws a live chaos curve in the Turtle window.

它会模拟 30 个小球的随机初始位置和随机速度，在 Turtle 窗口中实时显示当前系统混乱度，并绘制实时混乱度曲线。

Run it with:

运行方式：

```powershell
python multi_ball_chaos_simulation.py
```

When the window is closed, the program saves:

关闭窗口后，程序会保存：

```text
chaos_history.csv
chaos_over_time.png
```

The chaos value combines position dispersion and velocity dispersion. A higher value means the balls are more spatially spread out and their velocity vectors are more varied.

混乱度由位置分散度和速度分散度共同计算得到。数值越高，表示小球在空间上越分散，速度方向和大小也越不一致。

## Repository Contents

## 仓库内容

- `ball_simulation.py`: original source code.

  原始 Python 源码文件。

- `ball_simulation.spec`: PyInstaller build specification.

  PyInstaller 打包配置文件。

- `multi_ball_chaos_simulation.py`: 30-ball chaos simulation source code.

  30 个小球混乱度模拟的新版本源码。

- `build.bat` and `build_ball_simulation.bat`: Windows build helpers.

  Windows 下使用的构建辅助脚本。

- `pyinstaller_build_backup\dist\ball_simulation.exe`: restored packaged executable.

  已复原的打包可执行程序。

- `pyinstaller_build_backup\build\ball_simulation\`: preserved PyInstaller build artifacts.

  已保留的 PyInstaller 构建中间产物，可用于查询打包现场和排查依赖问题。
