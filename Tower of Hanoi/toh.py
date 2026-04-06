import sys
import copy
import matplotlib
matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import FancyBboxPatch


class HanoiApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tower of Hanoi")
        self.setGeometry(100, 100, 1100, 650)

        self.num_disks = 3
        self.frame_index = 0
        self.manual_mode = False
        self.selected_peg = None

        # Live graph data
        self.graph_x = []
        self.graph_y = []

        self.init_ui()
        self.apply_dark_mode()
        self.generate()

    # ---------------- UI ----------------

    def init_ui(self):

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        top_layout = QHBoxLayout()

        self.spinbox = QSpinBox()
        self.spinbox.setRange(1, 10)
        self.spinbox.setValue(3)

        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate)

        self.mode_btn = QPushButton("Manual Mode")
        self.mode_btn.clicked.connect(self.toggle_mode)

        top_layout.addWidget(QLabel("Disks:"))
        top_layout.addWidget(self.spinbox)
        top_layout.addWidget(self.generate_btn)
        top_layout.addWidget(self.mode_btn)

        left_layout.addLayout(top_layout)

        # Canvas
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvas(self.fig)
        left_layout.addWidget(self.canvas)

        self.canvas.mpl_connect('button_press_event', self.on_click)

        # Buttons
        btn_layout = QHBoxLayout()

        self.run_btn = QPushButton("Run")
        self.stop_btn = QPushButton("Stop")

        self.run_btn.clicked.connect(self.run)
        self.stop_btn.clicked.connect(self.stop)

        btn_layout.addWidget(self.run_btn)
        btn_layout.addWidget(self.stop_btn)

        left_layout.addLayout(btn_layout)

        # Info Panel
        self.step_label = QLabel("Step: 0")
        self.desc_label = QLabel("Description: Ready")
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("color: #00FFFF;")

        self.total_moves_label = QLabel("Total Moves: 0")
        self.complexity_label = QLabel("Time: O(2^n)")

        left_layout.addWidget(self.step_label)
        left_layout.addWidget(self.desc_label)
        left_layout.addWidget(self.total_moves_label)
        left_layout.addWidget(self.complexity_label)

        # Graph
        right_layout = QVBoxLayout()

        self.graph_fig, self.graph_ax = plt.subplots(figsize=(4, 4))
        self.graph_canvas = FigureCanvas(self.graph_fig)

        right_layout.addWidget(QLabel("Live Moves Progress"))
        right_layout.addWidget(self.graph_canvas)

        main_layout.addLayout(left_layout, 3)
        main_layout.addLayout(right_layout, 1)

        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_run)

    # ---------------- DARK MODE ----------------

    def apply_dark_mode(self):
        self.setStyleSheet("""
            QWidget { background-color: #121212; color: #E0E0E0; }
            QPushButton { background-color: #1f1f1f; padding: 6px; }
            QPushButton:hover { background-color: #333; }
        """)

    # ---------------- HANOI ----------------

    def hanoi(self, n, s, d, a):
        if n == 1:
            self.moves.append((s, d))
            return
        self.hanoi(n-1, s, a, d)
        self.moves.append((s, d))
        self.hanoi(n-1, a, d, s)

    # ---------------- GENERATE ----------------

    def generate(self):

        self.num_disks = self.spinbox.value()

        self.initial_pegs = [list(range(self.num_disks, 0, -1)), [], []]

        self.moves = []
        self.hanoi(self.num_disks, 0, 2, 1)

        pegs = copy.deepcopy(self.initial_pegs)

        self.states = [copy.deepcopy(pegs)]
        self.move_descriptions = ["Initial State"]

        names = ['A', 'B', 'C']

        for s, d in self.moves:
            disk = pegs[s].pop()
            pegs[d].append(disk)

            self.states.append(copy.deepcopy(pegs))
            self.move_descriptions.append(f"Move disk {disk} from {names[s]} → {names[d]}")

        self.frame_index = 0

        total_moves = (2**self.num_disks) - 1
        self.total_moves_label.setText(f"Total Moves: {total_moves}")

        # Reset graph
        self.graph_x = [0]
        self.graph_y = [0]

        self.plot_graph()
        self.draw_state()

    # ---------------- GRAPH ----------------

    def plot_graph(self):

        self.graph_ax.clear()

        self.graph_fig.patch.set_facecolor('#121212')
        self.graph_ax.set_facecolor('#1e1e1e')

        self.graph_ax.grid(True, linestyle='--', alpha=0.3)

        for spine in self.graph_ax.spines.values():
            spine.set_visible(False)

        self.graph_ax.plot(self.graph_x, self.graph_y,
                           marker='o', color='#4DABF7')

        # Highlight current point
        self.graph_ax.scatter(self.graph_x[-1], self.graph_y[-1],
                              color='#00FFFF', s=80, zorder=5)

        self.graph_ax.set_xlim(0, len(self.states))
        self.graph_ax.set_ylim(0, len(self.states))

        color = '#00FFFF'

        self.graph_ax.set_title("Live Moves Progress", color=color)
        self.graph_ax.set_xlabel("Steps", color=color)
        self.graph_ax.set_ylabel("Moves", color=color)

        self.graph_ax.tick_params(colors=color)

        self.graph_canvas.draw()

    # ---------------- DRAW ----------------

    def draw_state(self):

        state = self.states[self.frame_index]
        n = self.num_disks

        self.ax.clear()

        self.fig.patch.set_facecolor('#121212')
        self.ax.set_facecolor('#1e1e1e')

        self.ax.set_title("Tower of Hanoi", color='cyan', fontsize=14)

        self.ax.set_xlim(-1, 3)
        self.ax.set_ylim(0, n + 3)

        self.ax.grid(True, linestyle='--', alpha=0.3)

        self.ax.set_xticks([0,1,2])
        self.ax.set_xticklabels(['A','B','C'])
        self.ax.tick_params(colors='cyan')

        for spine in self.ax.spines.values():
            spine.set_visible(False)

        peg_colors = ['#FF8787', '#74C0FC', '#8CE99A']

        for i in range(3):
            self.ax.plot([i,i],[0,n+1],linewidth=6,
                         color=peg_colors[i],
                         solid_capstyle='round')

        colors = ['#FF6B6B','#FFA94D','#FFD43B',
                  '#69DB7C','#4DABF7','#B197FC']

        for i in range(3):
            for j, disk in enumerate(state[i]):

                max_width = 0.8
                min_width = 0.2
                width = min_width + (disk / self.num_disks) * (max_width - min_width)

                shadow = FancyBboxPatch(
                    (i - width/2 + 0.04, j - 0.04),
                    width, 0.6,
                    boxstyle="round,pad=0.02,rounding_size=0.15",
                    linewidth=0, facecolor='black', alpha=0.25
                )

                disk_patch = FancyBboxPatch(
                    (i - width/2, j),
                    width, 0.6,
                    boxstyle="round,pad=0.02,rounding_size=0.15",
                    linewidth=1, edgecolor='#222',
                    facecolor=colors[disk % len(colors)]
                )

                self.ax.add_patch(shadow)
                self.ax.add_patch(disk_patch)

        self.step_label.setText(f"Step: {self.frame_index}")
        self.desc_label.setText(self.move_descriptions[self.frame_index])

        self.canvas.draw()

    # ---------------- CONTROLS ----------------

    def run(self):
        self.timer.start(250)

    def stop(self):
        self.timer.stop()

    def auto_run(self):
        if self.frame_index < len(self.states)-1:
            self.frame_index += 1

            self.graph_x.append(self.frame_index)
            self.graph_y.append(self.frame_index)

            self.draw_state()
            self.plot_graph()
        else:
            self.timer.stop()

    # ---------------- MANUAL ----------------

    def toggle_mode(self):
        self.manual_mode = not self.manual_mode
        self.mode_btn.setText("Auto Mode" if self.manual_mode else "Manual Mode")

    def on_click(self, event):
        if not self.manual_mode or event.xdata is None:
            return

        peg = round(event.xdata)
        if peg not in [0,1,2]:
            return

        state = self.states[self.frame_index]

        if self.selected_peg is None:
            if state[peg]:
                self.selected_peg = peg
            return

        src = self.selected_peg
        dest = peg

        if state[dest] and state[dest][-1] < state[src][-1]:
            self.selected_peg = None
            return

        new_state = copy.deepcopy(state)
        disk = new_state[src].pop()
        new_state[dest].append(disk)

        self.states.append(new_state)
        self.move_descriptions.append(f"(Manual) Move disk {disk}")

        self.frame_index += 1

        self.graph_x.append(self.frame_index)
        self.graph_y.append(self.frame_index)

        self.draw_state()
        self.plot_graph()

        self.selected_peg = None


# ---------------- MAIN ----------------

app = QApplication(sys.argv)
window = HanoiApp()
window.show()
sys.exit(app.exec())
