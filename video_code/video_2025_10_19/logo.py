from manim import *

config.background_color = "#000012"  # 设置Scene背景颜色

class Logo(Scene):
    def construct(self):
        author = MathTex("\mathbf{Trance\_Kernel}", color = YELLOW_A, font_size = 81).shift(DOWN * 0.6)
        underline = Line(color = YELLOW_A, stroke_width = 2.5).set_length(6.1).next_to(author, DOWN)
        matrix = Matrix([[r"\mathbf{T}_r", ""], ["", r"\mathbf{K}_e"]])
        matrix.set_color_by_gradient(GREEN_B, BLUE_E)
        self.play(DrawBorderThenFill(matrix), run_time = 2.5)
        self.play(matrix.animate.shift(UP * 1).scale(1.2), run_time = 0.8)
        self.play(AnimationGroup(DrawBorderThenFill(author), GrowFromCenter(underline), lag_ratio = 0.8))
        self.wait(3.5)
