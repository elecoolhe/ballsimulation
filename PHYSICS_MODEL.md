# Physics Model And Calculation Notes

# 物理建模与计算说明

This document describes the physical assumptions, parameter settings, equations, and calculation steps used by `multi_ball_chaos_simulation.py`.

本文档说明 `multi_ball_chaos_simulation.py` 使用的物理假设、参数设定、计算方程和逐帧计算步骤。

## 1. Modeling Goal

## 1. 建模目标

The program simulates 30 point-like balls moving inside a two-dimensional square box. Each ball has a random initial position and velocity. The balls elastically reflect from the box boundary. The program also computes a simple system chaos index over time.

程序模拟 30 个近似质点小球在二维方形边界内运动。每个小球具有随机初始位置和随机速度。小球碰到边界后发生理想反射。程序同时计算一个简化的系统混乱度指标，并记录其随时间的变化。

## 2. Physical Assumptions

## 2. 物理假设

- The simulation is two-dimensional.

  系统是二维平面运动。

- Each ball is treated as a moving particle with a visible radius.

  每个小球被视为具有可见半径的运动粒子。

- Balls collide only with the square boundary.

  小球只与方形边界发生碰撞。

- Ball-ball collisions are not included in this version.

  当前版本不计算小球之间的相互碰撞。

- Boundary collisions are ideal elastic reflections.

  小球与边界碰撞被处理为理想弹性反射。

- There is no gravity, friction, air resistance, or energy loss.

  系统中不考虑重力、摩擦、空气阻力或能量损失。

- The simulation uses discrete time steps.

  程序使用离散时间步进行更新。

## 3. Parameter Settings

## 3. 参数设定

| Parameter | Value | Meaning |
| --- | ---: | --- |
| `BALL_COUNT` | `30` | Number of balls in the system / 系统中的小球数量 |
| `WINDOW_WIDTH` | `1000` | Turtle window width in pixels / Turtle 窗口宽度 |
| `WINDOW_HEIGHT` | `700` | Turtle window height in pixels / Turtle 窗口高度 |
| `BORDER` | `250` | Half side length of the square simulation area / 方形模拟区域半边长 |
| `BALL_RADIUS` | `8` | Visible ball radius used for boundary checks / 用于边界判断的小球可见半径 |
| `MIN_INITIAL_DISTANCE` | `22` | Minimum preferred distance between initial ball centers / 初始小球中心之间的推荐最小距离 |
| `MIN_SPEED` | `1.5` | Minimum initial speed / 初始速度最小值 |
| `MAX_SPEED` | `4.5` | Maximum initial speed / 初始速度最大值 |
| `FRAME_MS` | `16` | Timer interval between frames, approximately 60 FPS / 每帧计时器间隔，约每秒 60 帧 |
| `HISTORY_LIMIT` | `220` | Recent chaos values displayed in the live graph / 实时曲线显示的最近混乱度数据点数量 |

## 4. State Variables

## 4. 状态变量

For ball `i`, the simulation stores:

对于第 `i` 个小球，程序保存以下状态变量：

```text
x_i, y_i      position components / 小球位置分量
dx_i, dy_i    velocity components per frame / 每帧移动的速度分量
```

The velocity is generated from a random speed and random direction:

速度由随机速度大小和随机方向生成：

```text
speed_i ~ Uniform(MIN_SPEED, MAX_SPEED)
theta_i ~ Uniform(0, 2π)
dx_i = cos(theta_i) * speed_i
dy_i = sin(theta_i) * speed_i
```

## 5. Motion Equations

## 5. 运动方程

Without collision, each frame uses:

如果没有碰撞，每一帧的位置更新为：

```text
x_i(t + 1) = x_i(t) + dx_i(t)
y_i(t + 1) = y_i(t) + dy_i(t)
```

There is no acceleration in this version:

当前版本不考虑加速度：

```text
dx_i(t + 1) = dx_i(t)
dy_i(t + 1) = dy_i(t)
```

## 6. Boundary Reflection Equations

## 6. 边界反射方程

The valid region for a ball center is:

小球中心允许运动的区域为：

```text
-(BORDER - BALL_RADIUS) <= x_i <= BORDER - BALL_RADIUS
-(BORDER - BALL_RADIUS) <= y_i <= BORDER - BALL_RADIUS
```

If the next x-position crosses the left or right boundary:

如果下一帧 x 方向位置越过左右边界：

```text
if next_x > BORDER - BALL_RADIUS or next_x < -BORDER + BALL_RADIUS:
    dx_i = -dx_i
```

If the next y-position crosses the upper or lower boundary:

如果下一帧 y 方向位置越过上下边界：

```text
if next_y > BORDER - BALL_RADIUS or next_y < -BORDER + BALL_RADIUS:
    dy_i = -dy_i
```

This is equivalent to an ideal elastic reflection from a fixed wall. The speed magnitude remains unchanged.

这等价于小球与固定墙面发生理想弹性反射。碰撞后速度大小不变，仅对应方向分量变号。

## 7. Chaos Index Definition

## 7. 混乱度指标定义

This project uses a simplified, observable chaos index rather than a strict thermodynamic entropy or Lyapunov exponent. It combines position dispersion and velocity dispersion.

本项目使用一个简化、可观测的混乱度指标，不是严格的热力学熵或李雅普诺夫指数。它由位置分散度和速度分散度共同构成。

For `N` balls, the mean position is:

对于 `N` 个小球，平均位置为：

```text
x_mean = (1 / N) * sum(x_i)
y_mean = (1 / N) * sum(y_i)
```

The mean velocity is:

平均速度为：

```text
dx_mean = (1 / N) * sum(dx_i)
dy_mean = (1 / N) * sum(dy_i)
```

Position dispersion:

位置分散度：

```text
position_spread = (1 / N) * sum(sqrt((x_i - x_mean)^2 + (y_i - y_mean)^2))
```

Velocity dispersion:

速度分散度：

```text
velocity_spread = (1 / N) * sum(sqrt((dx_i - dx_mean)^2 + (dy_i - dy_mean)^2))
```

Normalized scores:

归一化分量：

```text
position_score = min(position_spread / (sqrt(2) * BORDER), 1)
velocity_score = min(velocity_spread / (2 * MAX_SPEED), 1)
```

Final chaos value:

最终混乱度：

```text
chaos = (0.65 * position_score + 0.35 * velocity_score) * 100
```

The result is approximately in the range `0` to `100`.

计算结果大致落在 `0` 到 `100` 的范围内。

## 8. Calculation Steps

## 8. 计算步骤

Each frame follows these steps:

每一帧的计算流程如下：

1. Move each ball according to its current velocity.

   按照当前速度更新每个小球的位置。

2. Check whether the next position crosses a boundary.

   检查下一帧位置是否越过边界。

3. Reverse the corresponding velocity component when a boundary collision occurs.

   如果发生边界碰撞，则反转对应方向的速度分量。

4. Draw each ball at its updated position.

   将每个小球绘制到更新后的位置。

5. Compute the system chaos index.

   计算系统混乱度。

6. Append the current time and chaos value to the history arrays.

   将当前时间和混乱度追加到历史数据中。

7. Update the on-screen chaos value and live curve.

   更新窗口中的混乱度数值和实时曲线。

8. When the window closes, save `chaos_history.csv` and `chaos_over_time.png`.

   关闭窗口后，保存 `chaos_history.csv` 和 `chaos_over_time.png`。

## 9. Model Limitations

## 9. 模型局限

- No ball-ball collision is modeled.

  没有模拟小球之间的碰撞。

- No mass, force, or acceleration is used.

  没有引入质量、力或加速度。

- The chaos index is a descriptive engineering metric, not a rigorous entropy measurement.

  混乱度是一个描述性的工程指标，不是严格的熵度量。

- The time unit is frame-based rather than a calibrated physical second.

  时间单位以程序帧更新为基础，并不是经过物理标定的真实秒级动力学模型。

## 10. Possible Future Improvements

## 10. 后续可改进方向

- Add elastic collisions between balls.

  增加小球之间的弹性碰撞。

- Add mass and momentum conservation.

  引入质量和动量守恒。

- Add gravity or external force fields.

  增加重力或外部力场。

- Replace the descriptive chaos index with entropy, phase-space dispersion, or a Lyapunov-style divergence metric.

  将描述性混乱度替换或扩展为熵、相空间分散度或类似李雅普诺夫指数的发散指标。
