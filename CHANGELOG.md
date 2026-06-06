# Changelog

All notable changes to this project are recorded here.

本文件用于记录项目的重要版本变化。

## v1.3.0

Ball-ball elastic collision version.

小球-小球弹性碰撞版本。

- Added ideal elastic collisions between balls in `multi_ball_chaos_simulation.py`.
- Added overlap correction to reduce sticking after collisions.
- Added real-time total collision count display.
- Added real-time total kinetic energy display.
- Updated `PHYSICS_MODEL.md` with ball-ball collision equations and revised calculation steps.
- Updated README to describe the collision-enabled version.

中文：

- 在 `multi_ball_chaos_simulation.py` 中新增小球之间的理想弹性碰撞。
- 增加重叠修正，减少碰撞后小球黏连。
- 增加实时累计碰撞次数显示。
- 增加实时系统总动能显示。
- 更新 `PHYSICS_MODEL.md`，加入小球-小球碰撞方程和新版计算步骤。
- 更新 README，说明支持弹性碰撞的新版本。

## v1.2.0

Current stable version.

当前稳定版本。

- Added `PHYSICS_MODEL.md` with physical assumptions, parameter settings, equations, calculation steps, limitations, and future improvement notes.
- Added README links for the physical model documentation.
- Confirmed the multi-ball chaos simulation source and project documentation are synchronized to GitHub.

中文：

- 新增 `PHYSICS_MODEL.md`，说明物理假设、参数设定、计算方程、计算步骤、模型局限和后续改进方向。
- 在 README 中增加物理建模说明文档入口。
- 确认多小球混乱度模拟源码和项目文档已同步到 GitHub。

## v1.1.0

Multi-ball chaos simulation version.

多小球混乱度模拟版本。

- Added `multi_ball_chaos_simulation.py`.
- Added 30 balls with random initial positions and random velocities.
- Added real-time chaos calculation.
- Added a live chaos-over-time curve in the Turtle window.
- Added output files generated on window close: `chaos_history.csv` and `chaos_over_time.png`.
- Updated `.gitignore` to ignore generated chaos output files.

中文：

- 新增 `multi_ball_chaos_simulation.py`。
- 增加 30 个小球，并支持随机初始位置和随机速度。
- 增加实时混乱度计算。
- 在 Turtle 窗口中增加实时混乱度变化曲线。
- 关闭窗口后生成 `chaos_history.csv` 和 `chaos_over_time.png`。
- 更新 `.gitignore`，避免误提交运行生成的数据和图片。

## v1.0.0

Restored original project version.

原始项目复原版本。

- Restored `ball_simulation.py`, the original single-ball Turtle simulation.
- Restored `ball_simulation.spec` and Windows build scripts.
- Preserved the original PyInstaller build snapshot under `pyinstaller_build_backup`.
- Added bilingual README documentation.
- Added Git LFS handling for large binary packaging artifacts.

中文：

- 复原 `ball_simulation.py` 原始单小球 Turtle 模拟程序。
- 复原 `ball_simulation.spec` 和 Windows 构建脚本。
- 将原始 PyInstaller 打包现场保留到 `pyinstaller_build_backup`。
- 增加中英文 README 文档。
- 为较大的二进制打包产物配置 Git LFS。
