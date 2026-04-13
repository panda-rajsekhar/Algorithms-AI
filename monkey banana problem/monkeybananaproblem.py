import matplotlib.pyplot as plt
import numpy as np
import time

class MonkeyBananaProblem3D:
    def __init__(self):
        self.positions = {"door": 0.0, "window": 4.0, "middle": 2.0}
        
        # Configurable constants
        self.box_height = 1.5
        self.banana_height = 3.5
        self.tolerance = 0.3
        
        # State variables
        self.monkey_x = self.positions["door"]
        self.box_x = self.positions["window"]
        self.monkey_height = 0.0
        self.has_banana = False
        
        self.fig = None
        self.ax = None

    # ✅ SAFE location detection
    def get_location_name(self, x):
        for k, v in self.positions.items():
            if abs(v - x) < self.tolerance:
                return k
        return "unknown"

    def get_current_state(self):
        monkey_pos = self.get_location_name(self.monkey_x)
        box_pos = self.get_location_name(self.box_x)
        
        state = f"Monkey at {monkey_pos} | "
        state += f"Box at {box_pos} | "
        state += f"Height: {'On Box' if self.monkey_height > 1 else 'On Floor'} | "
        state += f"Banana: {'Yes 🍌' if self.has_banana else 'No'}"
        return state

    def print_state(self, title="CURRENT STATE"):
        print(f"\n🔹 {title}")
        print("-" * 70)
        print(self.get_current_state())
        print("-" * 70)

    def setup_3d_plot(self):
        self.fig = plt.figure(figsize=(13, 9))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel("Room X")
        self.ax.set_ylabel("Room Y")
        self.ax.set_zlabel("Height")

    def update_3d_plot(self, step_name=""):
        if self.fig is None:
            self.setup_3d_plot()
        
        self.ax.cla()
        self.ax.set_xlim(0, 5)
        self.ax.set_ylim(0, 3)
        self.ax.set_zlim(0, 4)

        # Floor
        self.ax.plot([0, 5], [1.5, 1.5], [0, 0])

        # Banana
        self.ax.scatter([2.0], [1.5], [self.banana_height], s=400, marker='o')

        # Box
        self.ax.bar3d(self.box_x - 0.35, 1.15, 0, 0.7, 0.7, self.box_height, alpha=0.8)

        # Monkey
        color = 'green' if self.has_banana else 'red'
        self.ax.scatter(self.monkey_x, 1.5, self.monkey_height + 0.3, 
                        c=color, s=350)

        # Banana in hand
        if self.has_banana:
            self.ax.scatter(self.monkey_x, 1.5, self.monkey_height + 0.8, 
                            s=150, marker='*')

        self.ax.set_title(f"{step_name}\n{self.get_current_state()}")
        plt.pause(1.5)

    def move_monkey(self, location):
        print(f"\n🚶 Move monkey to {location}")
        self.monkey_x = self.positions[location]
        self.update_3d_plot(f"Move → {location}")

    def push_box(self, location):
        if abs(self.monkey_x - self.box_x) < self.tolerance:
            print(f"🛠️ Push box to {location}")
            self.box_x = self.positions[location]
            self.monkey_x = self.box_x
            self.update_3d_plot(f"Push Box → {location}")
        else:
            print("❌ Monkey must be at the box!")

    def climb_box(self):
        if abs(self.monkey_x - self.box_x) < self.tolerance:
            print("🧗 Climb box")
            self.monkey_height = self.box_height
            self.update_3d_plot("Climb Box")
        else:
            print("❌ Monkey not at box!")

    def grasp_banana(self):
        if (abs(self.monkey_x - 2.0) < self.tolerance and 
            abs(self.box_x - 2.0) < self.tolerance and 
            self.monkey_height >= self.box_height):
            
            print("🍌 Grasp banana!")
            self.has_banana = True
            self.update_3d_plot("Grasp Banana")
        else:
            print("❌ Conditions not satisfied!")

    def solve(self):
        print("🐵🍌 MONKEY BANANA 3D SIMULATION 🍌🐵")

        self.print_state("INITIAL STATE")
        self.update_3d_plot("Initial")

        self.move_monkey("window")
        self.print_state("Step 1")

        self.push_box("middle")
        self.print_state("Step 2")

        self.climb_box()
        self.print_state("Step 3")

        self.grasp_banana()
        self.print_state("FINAL STATE")

        if self.has_banana:
            print("\n🎉 GOAL ACHIEVED 🎉")
        else:
            print("\n❌ Goal Failed")

        plt.show()


if __name__ == "__main__":
    problem = MonkeyBananaProblem3D()
    problem.solve()     
