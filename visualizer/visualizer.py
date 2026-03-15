import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button, Slider

from utils.generator import generate_array
from algorithms.bubble_sort import bubble
from algorithms.insertion_sort import insertion
from algorithms.merge_sort import merge
from algorithms.quick_sort import quick


class Visualizer:

    def __init__(self):

        self.array_size = 40
        self.array = generate_array(self.array_size)

        self.speed = 100

        self.algorithms = {
            "Bubble": bubble,
            "Insertion": insertion,
            "Merge": merge,
            "Quick": quick
        }

        self.complexity = {
            "Bubble": "O(n²)",
            "Insertion": "O(n²)",
            "Merge": "O(n log n)",
            "Quick": "O(n log n)"
        }

        self.current_algorithm = "Bubble"

        self.generator = self.algorithms[self.current_algorithm](self.array)

        self.fig, self.ax = plt.subplots()

        plt.subplots_adjust(bottom=0.35)

        self.bars = self.ax.bar(range(len(self.array)), self.array)

        self.info_text = self.ax.text(
            0.02, 0.95, "", transform=self.ax.transAxes
        )

        self.ax.set_title("Bubble Sort")

        self.create_controls()

        self.create_animation()

    # -----------------------

    def create_animation(self):

        self.ani = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=self.generator,
            interval=self.speed,
            repeat=False
        )

    # -----------------------

    def update(self, data):

        arr, comparisons, swaps = data

        for bar, val in zip(self.bars, arr):
            bar.set_height(val)

        self.info_text.set_text(
            f"Comparisons: {comparisons}\n"
            f"Swaps: {swaps}\n"
            f"Complexity: {self.complexity[self.current_algorithm]}"
        )

        return self.bars

    # -----------------------

    def start(self, name):

        self.current_algorithm = name

        self.generator = self.algorithms[name](self.array)

        self.ax.set_title(f"{name} Sort")

        # recreate animation (THIS FIXES BUTTONS)
        self.ani.event_source.stop()

        self.create_animation()

        plt.draw()

    # -----------------------

    def pause(self, event):
        self.ani.event_source.stop()

    def resume(self, event):
        self.ani.event_source.start()

    # -----------------------

    def reset(self, event):

        self.array = generate_array(self.array_size)

        for bar, val in zip(self.bars, self.array):
            bar.set_height(val)

        self.generator = self.algorithms[self.current_algorithm](self.array)

        self.create_animation()

        plt.draw()

    # -----------------------

    def change_speed(self, val):

        self.speed = int(val)

        self.ani.event_source.interval = self.speed

    # -----------------------

    def create_controls(self):

        ax_bubble = plt.axes([0.05,0.25,0.15,0.05])
        ax_insertion = plt.axes([0.25,0.25,0.15,0.05])
        ax_merge = plt.axes([0.45,0.25,0.15,0.05])
        ax_quick = plt.axes([0.65,0.25,0.15,0.05])

        ax_pause = plt.axes([0.20,0.15,0.15,0.05])
        ax_resume = plt.axes([0.40,0.15,0.15,0.05])
        ax_reset = plt.axes([0.60,0.15,0.15,0.05])

        btn_bubble = Button(ax_bubble,"Bubble")
        btn_insertion = Button(ax_insertion,"Insertion")
        btn_merge = Button(ax_merge,"Merge")
        btn_quick = Button(ax_quick,"Quick")

        btn_pause = Button(ax_pause,"Pause")
        btn_resume = Button(ax_resume,"Resume")
        btn_reset = Button(ax_reset,"Reset")

        btn_bubble.on_clicked(lambda event: self.start("Bubble"))
        btn_insertion.on_clicked(lambda event: self.start("Insertion"))
        btn_merge.on_clicked(lambda event: self.start("Merge"))
        btn_quick.on_clicked(lambda event: self.start("Quick"))

        btn_pause.on_clicked(self.pause)
        btn_resume.on_clicked(self.resume)
        btn_reset.on_clicked(self.reset)

        ax_speed = plt.axes([0.25,0.05,0.5,0.03])

        slider = Slider(ax_speed,"Speed",10,500,valinit=self.speed)

        slider.on_changed(self.change_speed)

    # -----------------------

    def show(self):
        plt.show()