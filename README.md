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

## Repository Contents

## 仓库内容

- `ball_simulation.py`: original source code.

  原始 Python 源码文件。

- `ball_simulation.spec`: PyInstaller build specification.

  PyInstaller 打包配置文件。

- `build.bat` and `build_ball_simulation.bat`: Windows build helpers.

  Windows 下使用的构建辅助脚本。

- `dist\ball_simulation.exe`: restored packaged executable.

  已复原的打包可执行程序。

- PyInstaller build artifacts are also preserved in this repository.

  仓库中也保留了 PyInstaller 生成的构建产物。
