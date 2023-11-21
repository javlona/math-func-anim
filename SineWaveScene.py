from manim import *
import numpy as np

class SineWaveScene(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": BLUE},
        )

        # Create a Sine wave function
        sine_wave = axes.plot(lambda x: np.sin(x), color=RED)

        # Create labels for the axes
        labels = axes.get_axis_labels()

        # Animate the creation of the axes and the sine wave
        self.play(Create(axes), Write(labels))
        self.play(Create(sine_wave))
        self.wait(2)

        # Animate the wave changing with a different frequency
        new_wave = axes.plot(lambda x: np.sin(2*x), color=GREEN)
        self.play(Transform(sine_wave, new_wave))
        self.wait(2)

SineWaveScene().render()
