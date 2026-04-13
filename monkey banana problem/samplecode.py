class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_location = "door"
        self.box_location = "window"
        self.monkey_on_box = False
        self.has_banana = False

    def display_state(self):
        print(f"\nMonkey is at: {self.monkey_location}")
        print(f"Box is at: {self.box_location}")
        print(f"Monkey on box: {self.monkey_on_box}")
        print(f"Monkey has banana: {self.has_banana}")

    def move_monkey(self, location):
        print(f"\nAction: Move monkey to {location}")
        self.monkey_location = location

    def push_box(self, location):
        if self.monkey_location == self.box_location:
            print(f"\nAction: Push box to {location}")
            self.box_location = location
            self.monkey_location = location
        else:
            print("\nMonkey must be at the box to push it!")

    def climb_box(self):
        if self.monkey_location == self.box_location:
            print("\nAction: Climb on box")
            self.monkey_on_box = True
        else:
            print("\nMonkey must be at the box to climb on it!")

    def grasp_banana(self):
        if self.monkey_location == "middle" and self.box_location == "middle" and self.monkey_on_box:
            print("\nAction: Grasp banana ")
            self.has_banana = True
        else:
            print("\nCannot grasp banana yet — preconditions not met.")

    def solve(self):
        self.display_state()

        # Step 1: Move to window (where the box is)
        self.move_monkey("window")

        # Step 2: Push box to the middle (under bananas)
        self.push_box("middle")

        # Step 3: Climb on the box
        self.climb_box()

        # Step 4: Try to grasp banana
        self.grasp_banana()

        self.display_state()

        if self.has_banana:
            print("\n Goal Achieved: Monkey has the banana!")
        else:
            print("\n Goal NOT Achieved.")

# Main Execution
if __name__ == "__main__":
    print(" Monkey and Banana Problem Simulation ")
    problem = MonkeyBananaProblem()
    problem.solve()
