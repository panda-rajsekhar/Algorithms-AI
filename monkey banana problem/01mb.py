import matplotlib.pyplot as plt

class MonkeyBananaProblemEmoji:
    def __init__(self):
        # Positions
        self.positions = {"door": 0.0, "window": 4.0, "middle": 2.0}

        # State
        self.monkey_x = self.positions["door"]
        self.box_x = self.positions["window"]
        self.monkey_height = 0.0
        self.has_banana = False

        # Config
        self.box_height = 1.5
        self.tolerance = 0.3

        self.fig = None
        self.ax = None

    def get_location_name(self, x):
        for k, v in self.positions.items():
            if abs(v - x) < self.tolerance:
                return k
        return "unknown"

    def get_current_state(self):
        return f"Monkey: {self.get_location_name(self.monkey_x)} | Box: {self.get_location_name(self.box_x)} | Banana: {'Yes 🍌' if self.has_banana else 'No'}"

    def draw_emoji(self, emoji, x, y, size=25):
        self.ax.text(x, y, emoji, fontsize=size, ha='center', va='center')

    def update_plot(self, step_name=""):
        if self.fig is None:
            self.fig, self.ax = plt.subplots(figsize=(10, 6))

        self.ax.clear()

        self.ax.set_xlim(0, 5)
        self.ax.set_ylim(0, 3)
        self.ax.set_aspect('equal')

        self.ax.set_title(f"{step_name}\n{self.get_current_state()}")

        # Clean UI
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_facecolor("#e6f2ff")

        # Floor
        self.ax.plot([0, 5], [1.2, 1.2], linewidth=3)

        # 🍌 Banana (top)
        self.draw_emoji("🍌", 2.0, 2.4, size=30)

        # 📦 Box
        self.draw_emoji("📦", self.box_x, 1.25, size=28)

        # 🐵 Monkey
        y_offset = 1.2 + self.monkey_height
        self.draw_emoji("🐵", self.monkey_x, y_offset, size=30)

        # 🍌 Banana in hand
        if self.has_banana:
            self.draw_emoji("🍌", self.monkey_x + 0.3, y_offset + 0.3, size=20)

        plt.pause(1.2)
        plt.draw()

    # Actions
    def move_monkey(self, location):
        self.monkey_x = self.positions[location]
        self.update_plot(f"Move → {location}")

    def push_box(self, location):
        if abs(self.monkey_x - self.box_x) < self.tolerance:
            self.box_x = self.positions[location]
            self.monkey_x = self.box_x
            self.update_plot(f"Push → {location}")

    def climb_box(self):
        if abs(self.monkey_x - self.box_x) < self.tolerance:
            self.monkey_height = self.box_height
            self.update_plot("Climb Box")

    def grasp_banana(self):
        if (abs(self.monkey_x - 2.0) < self.tolerance and 
            abs(self.box_x - 2.0) < self.tolerance and 
            self.monkey_height >= self.box_height):
            self.has_banana = True
            self.update_plot("Grasp Banana")

    def solve(self):
        self.update_plot("Initial")
        self.move_monkey("window")
        self.push_box("middle")
        self.climb_box()
        self.grasp_banana()
        plt.show()


if __name__ == "__main__":
    problem = MonkeyBananaProblemEmoji()
    problem.solve()
