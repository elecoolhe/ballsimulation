import csv
import math
import random
import time
import turtle


BALL_COUNT = 30
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
SIM_CENTER_X = -220
SIM_CENTER_Y = 0
BORDER = 250
BALL_RADIUS = 8
MIN_INITIAL_DISTANCE = 22
MIN_SPEED = 1.5
MAX_SPEED = 4.5
FRAME_MS = 16
HISTORY_LIMIT = 220

GRAPH_LEFT = 120
GRAPH_RIGHT = 470
GRAPH_BOTTOM = -250
GRAPH_TOP = 250


class Ball:
    def __init__(self, turtle_obj, x, y, dx, dy):
        self.turtle = turtle_obj
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        next_x = self.x + self.dx
        next_y = self.y + self.dy

        if next_x > BORDER - BALL_RADIUS or next_x < -BORDER + BALL_RADIUS:
            self.dx *= -1
            next_x = self.x + self.dx

        if next_y > BORDER - BALL_RADIUS or next_y < -BORDER + BALL_RADIUS:
            self.dy *= -1
            next_y = self.y + self.dy

        self.x = next_x
        self.y = next_y
        self.turtle.goto(SIM_CENTER_X + self.x, SIM_CENTER_Y + self.y)


def create_writer(color="white"):
    writer = turtle.Turtle(visible=False)
    writer.speed(0)
    writer.penup()
    writer.color(color)
    return writer


def draw_rectangle(drawer, left, bottom, right, top):
    drawer.penup()
    drawer.goto(left, bottom)
    drawer.pendown()
    drawer.goto(right, bottom)
    drawer.goto(right, top)
    drawer.goto(left, top)
    drawer.goto(left, bottom)
    drawer.penup()


def choose_initial_position(existing_positions):
    for _ in range(1000):
        x = random.randint(-BORDER + BALL_RADIUS, BORDER - BALL_RADIUS)
        y = random.randint(-BORDER + BALL_RADIUS, BORDER - BALL_RADIUS)
        if all(math.hypot(x - ox, y - oy) >= MIN_INITIAL_DISTANCE for ox, oy in existing_positions):
            return x, y
    return random.randint(-BORDER, BORDER), random.randint(-BORDER, BORDER)


def create_balls():
    colors = [
        "white",
        "cyan",
        "yellow",
        "orange",
        "lime",
        "magenta",
        "deepskyblue",
        "tomato",
        "gold",
        "violet",
    ]
    balls = []
    positions = []

    for index in range(BALL_COUNT):
        x, y = choose_initial_position(positions)
        positions.append((x, y))

        speed = random.uniform(MIN_SPEED, MAX_SPEED)
        angle = random.uniform(0, math.tau)
        dx = math.cos(angle) * speed
        dy = math.sin(angle) * speed

        ball_turtle = turtle.Turtle()
        ball_turtle.shape("circle")
        ball_turtle.color(colors[index % len(colors)])
        ball_turtle.penup()
        ball_turtle.speed(0)
        ball_turtle.shapesize(BALL_RADIUS / 10)
        ball_turtle.goto(SIM_CENTER_X + x, SIM_CENTER_Y + y)

        balls.append(Ball(ball_turtle, x, y, dx, dy))

    return balls


def calculate_chaos(balls):
    mean_x = sum(ball.x for ball in balls) / len(balls)
    mean_y = sum(ball.y for ball in balls) / len(balls)
    mean_dx = sum(ball.dx for ball in balls) / len(balls)
    mean_dy = sum(ball.dy for ball in balls) / len(balls)

    position_spread = sum(math.hypot(ball.x - mean_x, ball.y - mean_y) for ball in balls) / len(balls)
    velocity_spread = sum(math.hypot(ball.dx - mean_dx, ball.dy - mean_dy) for ball in balls) / len(balls)

    max_position_spread = math.sqrt(2) * BORDER
    max_velocity_spread = MAX_SPEED * 2

    position_score = min(position_spread / max_position_spread, 1.0)
    velocity_score = min(velocity_spread / max_velocity_spread, 1.0)

    return (0.65 * position_score + 0.35 * velocity_score) * 100


def draw_live_graph(graph_pen, chaos_history):
    graph_pen.clear()
    graph_pen.color("gray70")
    draw_rectangle(graph_pen, GRAPH_LEFT, GRAPH_BOTTOM, GRAPH_RIGHT, GRAPH_TOP)

    graph_pen.goto(GRAPH_LEFT, GRAPH_TOP + 18)
    graph_pen.color("white")
    graph_pen.write("Chaos over time", align="left", font=("Arial", 12, "normal"))

    graph_pen.goto(GRAPH_LEFT - 38, GRAPH_TOP - 6)
    graph_pen.write("100", align="left", font=("Arial", 8, "normal"))
    graph_pen.goto(GRAPH_LEFT - 24, GRAPH_BOTTOM - 4)
    graph_pen.write("0", align="left", font=("Arial", 8, "normal"))

    visible = chaos_history[-HISTORY_LIMIT:]
    if len(visible) < 2:
        return

    graph_width = GRAPH_RIGHT - GRAPH_LEFT
    graph_height = GRAPH_TOP - GRAPH_BOTTOM
    step = graph_width / (len(visible) - 1)

    graph_pen.color("cyan")
    graph_pen.penup()
    for index, value in enumerate(visible):
        x = GRAPH_LEFT + index * step
        y = GRAPH_BOTTOM + (max(0, min(value, 100)) / 100) * graph_height
        if index == 0:
            graph_pen.goto(x, y)
            graph_pen.pendown()
        else:
            graph_pen.goto(x, y)
    graph_pen.penup()


def save_chaos_history(time_history, chaos_history):
    with open("chaos_history.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["time_seconds", "chaos"])
        writer.writerows(zip(time_history, chaos_history))

    if not chaos_history:
        return

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        plt.figure(figsize=(8, 4.5))
        plt.plot(time_history, chaos_history, color="#0077cc", linewidth=1.6)
        plt.title("System Chaos Over Time")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Chaos (0-100)")
        plt.ylim(0, 100)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("chaos_over_time.png", dpi=150)
        plt.close()
    except Exception as exc:
        print(f"Could not save chaos plot: {exc}")


def main():
    window = turtle.Screen()
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.title("Multi-ball Chaos Simulation")
    window.bgcolor("black")
    window.tracer(0)

    border_pen = create_writer()
    draw_rectangle(
        border_pen,
        SIM_CENTER_X - BORDER,
        SIM_CENTER_Y - BORDER,
        SIM_CENTER_X + BORDER,
        SIM_CENTER_Y + BORDER,
    )

    info_writer = create_writer()
    info_writer.goto(SIM_CENTER_X - BORDER, SIM_CENTER_Y + BORDER + 28)

    graph_pen = create_writer()
    balls = create_balls()
    start_time = time.perf_counter()
    time_history = []
    chaos_history = []
    frame_counter = 0

    def update():
        nonlocal frame_counter

        for ball in balls:
            ball.move()

        elapsed = time.perf_counter() - start_time
        chaos = calculate_chaos(balls)
        time_history.append(round(elapsed, 3))
        chaos_history.append(round(chaos, 4))

        info_writer.clear()
        info_writer.write(
            f"Balls: {BALL_COUNT}   Time: {elapsed:6.2f}s   Chaos: {chaos:6.2f}",
            align="left",
            font=("Arial", 12, "normal"),
        )

        if frame_counter % 5 == 0:
            draw_live_graph(graph_pen, chaos_history)

        frame_counter += 1
        window.update()
        window.ontimer(update, FRAME_MS)

    update()

    try:
        turtle.done()
    finally:
        save_chaos_history(time_history, chaos_history)


if __name__ == "__main__":
    main()
