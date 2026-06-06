import turtle
import random
import sys  # 添加导入sys模块

# 设置窗口和边界
WIDTH, HEIGHT = 600, 600
BORDER = 250

# 初始化turtle
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.bgcolor("black")
window.tracer(0)

# 创建小球
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)

# 设置初始速度和位置
ball.dx = random.uniform(2, 5) * random.choice([-1, 1])
ball.dy = random.uniform(2, 5) * random.choice([-1, 1])
ball.goto(random.randint(-BORDER, BORDER), random.randint(-BORDER, BORDER))

# 绘制边界
border = turtle.Turtle()
border.color("white")
border.penup()
border.goto(-BORDER, -BORDER)
border.pendown()
for _ in range(4):
    border.forward(BORDER * 2)
    border.left(90)
border.hideturtle()

# 运动函数
def move_ball():
    x, y = ball.position()
    
    # 检查边界碰撞
    if x > BORDER or x < -BORDER:
        ball.dx *= -1
    if y > BORDER or y < -BORDER:
        ball.dy *= -1
    
    # 更新位置
    ball.setx(x + ball.dx)
    ball.sety(y + ball.dy)
    
    # 继续运动
    window.update()
    window.ontimer(move_ball, 10)

# 开始模拟
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        import PyInstaller.__main__
        PyInstaller.__main__.run([
            '--onefile',
            'ball_simulation.py'
        ])
    else:
        move_ball()
        turtle.done()