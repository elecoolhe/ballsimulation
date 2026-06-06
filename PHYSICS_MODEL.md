# Physics Model And Calculation Notes

# 物理建模与计算说明

This document describes the physical assumptions, parameter settings, equations, and calculation steps used by `multi_ball_chaos_simulation.py`.

本文档说明 `multi_ball_chaos_simulation.py` 使用的物理假设、参数设定、计算方程和逐帧计算步骤。

## 1. Modeling Goal

## 1. 建模目标

The program simulates 30 equal-mass balls moving inside a two-dimensional square box. Each ball has a random initial position and velocity. The balls elastically reflect from the box boundary and collide elastically with each other. The program also computes a simple system chaos index over time.

程序模拟 30 个等质量小球在二维方形边界内运动。每个小球具有随机初始位置和随机速度。小球碰到边界后发生理想反射，小球之间也发生理想弹性碰撞。程序同时计算一个简化的系统混乱度指标，并记录其随时间的变化。

## 2. Physical Assumptions

## 2. 物理假设

- The simulation is two-dimensional.

  系统是二维平面运动。

- Each ball is treated as a moving particle with a visible radius.

  每个小球被视为具有可见半径的运动粒子。

- Balls collide with the square boundary and with each other.

  小球与方形边界以及其他小球发生碰撞。

- Ball-ball collisions assume equal mass and ideal elasticity.

  小球之间的碰撞假设为等质量理想弹性碰撞。

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

## 7. Ball-Ball Elastic Collision Equations

## 7. 小球-小球弹性碰撞方程

For balls `i` and `j`, define the center-to-center vector:

对于小球 `i` 和 `j`，定义两球中心连线向量：

```text
r = (x_j - x_i, y_j - y_i)
d = sqrt((x_j - x_i)^2 + (y_j - y_i)^2)
```

A collision is detected when:

当满足以下条件时认为发生碰撞：

```text
d < 2 * BALL_RADIUS
```

The collision normal is:

碰撞法线方向为：

```text
n = r / d = (n_x, n_y)
```

The program first corrects overlap to prevent balls from sticking together:

程序首先修正重叠距离，避免小球黏连：

```text
overlap = 2 * BALL_RADIUS - d
x_i = x_i - n_x * overlap / 2
y_i = y_i - n_y * overlap / 2
x_j = x_j + n_x * overlap / 2
y_j = y_j + n_y * overlap / 2
```

The relative normal velocity is:

相对法向速度为：

```text
p = dot(v_i - v_j, n)
```

Only approaching balls are resolved. If `p <= 0`, the balls are already moving apart along the normal direction and only the overlap correction is kept.

程序只处理正在相互靠近的小球。如果 `p <= 0`，说明两球已经沿法线方向远离，此时只保留重叠修正。

For equal-mass ideal elastic collision, the normal velocity components are exchanged:

对于等质量理想弹性碰撞，沿法线方向的速度分量发生交换：

```text
v_i' = v_i - p * n
v_j' = v_j + p * n
```

The tangential velocity components remain unchanged. In the ideal model, total kinetic energy is approximately conserved except for numerical and discrete-time errors.

切向速度分量保持不变。在理想模型中，除数值误差和离散时间步误差外，总动能近似守恒。

## 8. Chaos Index Definition

## 8. 混乱度指标定义

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

## 9. Calculation Steps

## 9. 计算步骤

Each frame follows these steps:

每一帧的计算流程如下：

1. Move each ball according to its current velocity.

   按照当前速度更新每个小球的位置。

2. Check whether the next position crosses a boundary.

   检查下一帧位置是否越过边界。

3. Reverse the corresponding velocity component when a boundary collision occurs.

   如果发生边界碰撞，则反转对应方向的速度分量。

4. Detect and resolve ball-ball elastic collisions.

   检测并处理小球之间的理想弹性碰撞。

5. Correct overlap between colliding balls.

   修正发生碰撞的小球之间的重叠。

6. Draw each ball at its updated position.

   将每个小球绘制到更新后的位置。

7. Compute the system chaos index, total collision count, and total kinetic energy.

   计算系统混乱度、累计碰撞次数和系统总动能。

8. Append the current time and chaos value to the history arrays.

   将当前时间和混乱度追加到历史数据中。

9. Update the on-screen chaos value, collision count, energy value, and live curve.

   更新窗口中的混乱度数值、碰撞次数、能量数值和实时曲线。

10. When the window closes, save `chaos_history.csv` and `chaos_over_time.png`.

   关闭窗口后，保存 `chaos_history.csv` 和 `chaos_over_time.png`。

## 10. Model Limitations

## 10. 模型局限

- Ball-ball collisions assume equal mass and equal radius.

  小球之间的碰撞假设所有小球具有相同质量和相同半径。

- No gravity, friction, rotational motion, or acceleration is used.

  没有引入重力、摩擦、旋转运动或加速度。

- The chaos index is a descriptive engineering metric, not a rigorous entropy measurement.

  混乱度是一个描述性的工程指标，不是严格的熵度量。

- The time unit is frame-based rather than a calibrated physical second.

  时间单位以程序帧更新为基础，并不是经过物理标定的真实秒级动力学模型。

## 11. Possible Future Improvements

## 11. 后续可改进方向

- Add different masses and radii for different balls.

  为不同小球增加不同质量和半径。

- Add explicit momentum and energy conservation diagnostics.

  增加更明确的动量和能量守恒诊断。

- Add gravity or external force fields.

  增加重力或外部力场。

- Replace the descriptive chaos index with entropy, phase-space dispersion, or a Lyapunov-style divergence metric.

  将描述性混乱度替换或扩展为熵、相空间分散度或类似李雅普诺夫指数的发散指标。
