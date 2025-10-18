from manim import *

config.background_color = "#000012"  # 设置Scene背景颜色

class First(Scene):
    def construct(self):
        tex = Tex("What we know is not much. What we do not know is immense.", font_size = 48, color = YELLOW_A)
        name = Tex("---Pierre Simon Laplace", font_size = 56, color = YELLOW_D).next_to(tex, DOWN, buff = 0.7).to_edge(RIGHT, buff = 1.6)
        self.wait(0.4)
        self.play(Write(tex), run_time = 2.2)
        self.wait(2.8)
        self.play(Write(name), run_time = 1.8)
        self.wait(2.2)
        self.play(FadeOut(tex), FadeOut(name), run_time = 1.8)
