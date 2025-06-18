from manim import *
class Try(Scene):
    def construct(self):
        label0 = Text("Hello Manim!", font_size = 60, color = WHITE)
        s = Square(side_length = 2.5, color = BLUE, fill_opacity = 0.5)
        c = Circle(radius = 2.5, color = RED, fill_opacity = 0.7)
        label1 = Text("This is a square.", font_size = 36, color = WHITE).next_to(s, DOWN)
        label2 = Text("This is a circle.", font_size = 36, color = WHITE).next_to(c, DOWN)
        self.play(Write(label0))
        self.wait(0.5)
        self.play(FadeOut(label0))
        self.wait(0.5)
        self.play(FadeIn(s), Write(label1))
        self.wait()
        self.play(ReplacementTransform(s, c), ReplacementTransform(label1, label2))
        self.wait(1.5)
        self.play(FadeOut(c), FadeOut(label2))
        self.wait()