from manim import *

chinese_template = TexTemplate()
chinese_template.add_to_preamble(r"\usepackage{ctex}")  # 添加中文支持
chinese_template.tex_compiler = "pdflatex"

config.background_color = "#000012"  # 设置Scene背景颜色

class Chi(Tex):  # 定义了一个继承自Tex的Chi类，用于更便利地创建中文字幕
    def __init__(self, tex):
        super().__init__()
        self.text = Tex(tex, tex_template = chinese_template, font_size = 40)
        self.add(self.text)

class MathChi(MathTex):  # 定义了一个继承自MathTex的MathChi类，用于更便利地创建中文和数学公式的混合字幕
    def __init__(self, mathtex):
        super().__init__()
        self.mathtext = MathTex(mathtex, tex_template = chinese_template, font_size = 40)
        self.add(self.mathtext)

# 第一部分：要有多近，就有多近
class ChapterOne(Scene):
    def construct(self):
        title = Chi("一、要有多近，就有多近").scale(1.8)
        self.wait(0.4)
        self.play(Write(title), run_time = 1.6)
        self.wait(2)
        self.play(FadeOut(title), run_time = 0.9)
        series = MathTex(r"a_n=\frac{1}{n}", font_size = 90, color = YELLOW_A)
        self.wait(1.6)
        self.play(DrawBorderThenFill(series), run_time = 1.2)
        self.wait(0.5)
        rect = SurroundingRectangle(series, color = TEAL_A, buff = 0.4, stroke_width = 5)
        self.play(ShowPassingFlash(rect), time_width = 0.7)
        self.wait(7.5)
        self.play(series.animate.shift(2.6 * UP), run_time = 1.7)
        self.wait(0.4)
        line = NumberLine(x_range = [-8, 8, 2], length = 16, include_numbers = True).shift(1.8 * DOWN).set_stroke(background = True)
        dota_tracker, dotb_tracker = ValueTracker(-2.712), ValueTracker(3.005)
        dot_a = Dot(color = ORANGE).add_updater(lambda m: m.move_to(line.n2p(dota_tracker.get_value())))
        dot_b = Dot(color = ORANGE).add_updater(lambda m: m.move_to(line.n2p(dotb_tracker.get_value())))
        distance_label = always_redraw(
            lambda: MathTex(
                r"\left | AB \right |=\left |" + f"{dota_tracker.get_value():.3f}" + r"-" +
                f"{dotb_tracker.get_value():.3f}" + r"\right |=" + f"{abs(dotb_tracker.get_value() - dota_tracker.get_value()):.3f}", 
                font_size = 48, color = RED
            ).shift(0.8 * UP + 3.3 * LEFT)
        )
        dota_label = always_redraw(lambda: MathTex(r"A", font_size = 44, color = ORANGE).next_to(dot_a, UP, buff = 0.2))
        dotb_label = always_redraw(lambda: MathTex(r"B", font_size = 44, color = ORANGE).next_to(dot_b, UP, buff = 0.2))
        self.play(Create(line))
        self.wait(0.4)
        self.add(dot_a, dot_b, dota_label, dotb_label)
        self.play(Write(distance_label), run_time = 1.5)
        self.wait(0.5)
        self.play(dota_tracker.animate.set_value(-1.417), dotb_tracker.animate.set_value(2.183), run_time = 1.8)
        self.wait(0.8)
        self.play(dota_tracker.animate.set_value(2.457), dotb_tracker.animate.set_value(-1.718), run_time = 1.8)
        self.wait(0.8)
        self.play(dota_tracker.animate.set_value(-4.677), dotb_tracker.animate.set_value(5.182), run_time = 1.8)
        self.wait(0.8)
        self.play(FadeOut(distance_label), Uncreate(dot_a), Uncreate(dot_b), Uncreate(dota_label), Uncreate(dotb_label), run_time = 1.4)
        neoline = NumberLine(x_range = [-6, 6, 2], length = 16, include_numbers = True).shift(1 * DOWN)
        dot_o = Dot(color = BLUE_D).move_to(neoline.n2p(0))
        doto_label = MathTex(r"O", font_size = 44, color = BLUE_D).next_to(dot_o, UP, buff = 0.2)
        dots = VGroup()
        n = 1
        for i in range(1, 30):
            dot = Dot(color = BLUE_D).move_to(neoline.n2p(1/n)).set_z_index(1)
            dots.add(dot)
            n += 1
        self.wait(0.8)
        self.play(ReplacementTransform(line, neoline), run_time = 1.2)
        self.play(Create(dot_o), Create(doto_label))
        self.play(ReplacementTransform(series, dots), run_time = 1.7)
        self.wait(0.4)
        equal = MathTex(r"\left | \frac{1}{n}-0\right |=\frac{1}{n}", font_size = 64, color = GOLD_A).shift(1 * UP)
        self.play(DrawBorderThenFill(equal), run_time = 1.6)
        self.wait(2.5)
        dot_c = Dot(color = GOLD_A).move_to(line.n2p(-1))
        dotc_label = MathTex(r"c", font_size = 44, color = GOLD_A).next_to(dot_c, UP, buff = 0.2)
        dotc = VGroup(dot_c, dotc_label)
        neoequal = MathTex(r"\left | \frac{1}{n}- c \right |=\frac{1}{n}- c", font_size = 64, color = GOLD_A).shift(1 * UP)
        self.play(Create(dotc), run_time = 1.2)
        self.wait(0.3)
        self.play(Flash(dot_c, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.play(ReplacementTransform(equal, neoequal), run_time = 1.6)
        self.wait(0.6)
        self.play(dotc.animate.shift(3.52 * LEFT), run_time = 1.3)
        self.wait(0.9)
        self.play(dotc.animate.shift(1.12 * RIGHT), run_time = 1.3)
        self.wait(0.9)
        self.play(dotc.animate.shift(3.36 * LEFT), run_time = 1.3)
        self.wait(0.9)
        self.play(dotc.animate.shift(5.92 * RIGHT), run_time = 1.3)
        self.wait(0.9)
        self.play(FadeOut(neoequal), Uncreate(dotc), run_time = 1.6)
        self.wait(3)
        neoneoline = NumberLine(x_range = [-6, 6, 2], length = 96, include_numbers = True).shift(1 * DOWN)
        unit_size = neoneoline.get_unit_size()
        neodots = VGroup()
        n = 1
        for i in range(1, 30):
            dot = Dot(color = BLUE_D).move_to(neoneoline.n2p(1/n)).set_z_index(1)
            neodots.add(dot)
            n += 1
        self.play(ReplacementTransform(neoline, neoneoline), ReplacementTransform(dots, neodots), run_time = 2)
        self.wait(1.3)
        dotx_tracker, r_tracker = ValueTracker(2), ValueTracker(2)
        dot_x = Dot(color = GREEN_A, radius = 0.1).move_to(neoneoline.n2p(0.5)).set_z_index(2)
        circle = always_redraw(
            lambda: Circle(
                radius = 1/(r_tracker.get_value()) * unit_size, color = GREEN_B, fill_opacity = 0.3, stroke_width = 0
            ).move_to(neoneoline.n2p(0))
        )
        dot_x.add_updater(lambda m: m.move_to(neoneoline.n2p(1/(dotx_tracker.get_value()))))
        n_label0 = always_redraw(
            lambda: MathTex(
                r"N=" + f"{dotx_tracker.get_value():.0f}", font_size = 54, color = YELLOW
            ).shift(1.9 * UP + 3.3 * LEFT)
        )
        n_label1 = always_redraw(
            lambda: MathTex(
                r"\frac{1}{N}=" + r"\frac{1}{" + f"{dotx_tracker.get_value():.0f}" + r"}", 
                font_size = 54, color = ORANGE
            ).shift(1.9 * UP + 4 * RIGHT)
        )
        n_label2 = MathTex(r"\forall n>N:\frac{1}{n}<", font_size = 54, color = ORANGE).shift(1.9 * UP + 1 * RIGHT)
        self.add(dot_x).wait(0.6)
        self.play(Flash(dot_x, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.wait(1.3)
        self.play(Write(n_label0), Write(n_label1), Write(n_label2), run_time = 1.9)
        self.wait(0.4)
        self.play(GrowFromCenter(circle), run_time = 1.3)
        self.wait(0.4)
        self.play(dotx_tracker.animate.set_value(4), r_tracker.animate.set_value(4), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(8), r_tracker.animate.set_value(8), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(15), r_tracker.animate.set_value(15), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(25), r_tracker.animate.set_value(25), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(114), r_tracker.animate.set_value(114), run_time = 3.5)
        self.wait(2.4)
        rect_n = SurroundingRectangle(n_label0, color = TEAL_A, buff = 0.1, stroke_width = 3)
        rect_epsilon = SurroundingRectangle(n_label1, color = TEAL_A, buff = 0.1, stroke_width = 3)
        self.play(ShowPassingFlash(rect_n), ShowPassingFlash(rect_epsilon), time_width = 0.7, run_time = 1.8)
        self.wait(1.5)
        e_label0 = MathTex(
            r"N= \frac{1}{\epsilon}", font_size = 54, tex_to_color_map = {r"N=": YELLOW, r"\frac{1}{\epsilon}": GREEN_B}
        ).shift(1.9 * UP + 3.3 * LEFT)
        e_label1 = MathTex(
            r"\frac{1}{N}= \epsilon", font_size = 54, tex_to_color_map = {r"\frac{1}{N}=": ORANGE, r"\epsilon": GREEN_B}
        ).shift(1.9 * UP + 4 * RIGHT)
        self.play(ReplacementTransform(n_label0, e_label0), ReplacementTransform(n_label1, e_label1), run_time = 1.3)
        self.wait(2)
        self.play(dotx_tracker.animate.set_value(3), r_tracker.animate.set_value(3), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(6), r_tracker.animate.set_value(6), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(21), r_tracker.animate.set_value(21), run_time = 2)
        self.wait(2.4)
        e_label2 = MathTex(
            r"\exists N= \frac{1}{\epsilon},", font_size = 54, 
            tex_to_color_map = {r"\exists N=": YELLOW, r"\frac{1}{\epsilon},": GREEN_B}
        ).shift(1.9 * UP + 2 * LEFT)
        e_label3 = MathTex(r"\epsilon", font_size = 54, color = GREEN_B).shift(1.9 * UP + 3 * RIGHT)
        e_label4 = MathTex(r"\forall \epsilon>0,", font_size = 54, color =GREEN_B).shift(1.9 * UP + 4.2 * LEFT)
        self.play(ReplacementTransform(e_label0, e_label2), ReplacementTransform(e_label1, e_label3), run_time = 1.4)
        self.play(Write(e_label4), run_time = 1.3)
        self.wait(1.8)
        e_label5 = MathTex(
            r"\exists N= \left \lfloor \frac{1}{\epsilon }  \right \rfloor +1,", font_size = 54, 
            tex_to_color_map = {r"\exists N=": YELLOW, r"\left \lfloor \frac{1}{\epsilon }  \right \rfloor +1,": GREEN_B}
        ).shift(1.9 * UP + 1.2 * LEFT)
        limit_part = VGroup(n_label2, e_label3)
        self.play(ReplacementTransform(e_label2, e_label5), limit_part.animate.shift(1.6 * RIGHT), run_time = 1.4)
        self.wait(1.7)
        limit = VGroup(e_label4, e_label5, limit_part)
        num_line = VGroup(neoneoline, dot_o, doto_label, dot_x, circle, neodots)
        self.play(limit.animate.shift(1.9 * DOWN), FadeOut(num_line), run_time = 1.8)
        self.wait(1.9)
        neolimit = MathTex(
            r"\forall\epsilon>0, \exists N, \forall n>N:\left | a_n-c\right |< \epsilon", 
            font_size = 54, tex_to_color_map = {
                r"\forall\epsilon>0,": GREEN_B, r"\exists N,": YELLOW, 
                r"\forall n>N:\left | a_n-c\right |<": ORANGE, r"\epsilon": GREEN_B
            }
        )
        self.play(ReplacementTransform(limit, neolimit), run_time = 1.6)
        self.play(neolimit.animate.scale(1.2), run_time = 0.8)
        self.wait(0.6)
        rect_l = SurroundingRectangle(neolimit, color = TEAL_A, buff = 0.4, stroke_width = 5)
        self.play(ShowPassingFlash(rect_l), time_width = 0.7, run_time = 1.6)
        self.wait(2.2)
        arrow = MathTex(r"\Leftrightarrow ", font_size = 64.8, color = YELLOW_A).rotate(PI/2)
        limit_an = MathTex(r"\lim_{n \to \infty}a_n=c ", font_size = 72, color = YELLOW_A).shift(1 * DOWN)
        self.play(Create(arrow), DrawBorderThenFill(limit_an), neolimit.animate.shift(0.9 * UP), run_time = 2.1)
        self.wait(2.5)
        epsilon_n = MathTex(r"\epsilon-N", font_size = 180, color = YELLOW_D)
        integrity = VGroup(neolimit, arrow, limit_an)
        self.play(AnimationGroup(integrity.animate.set_opacity(0.2), DrawBorderThenFill(epsilon_n), lag_ratio = 0.6), run_time = 2.4)
        self.wait(2.5)
        self.play(FadeOut(integrity), FadeOut(epsilon_n), run_time = 1.6)
        self.wait(0.4)

# 演示一个数列的例子
class ExampleAnimation(Scene):
    def construct(self):
        line = NumberLine(x_range = [-6, 6, 2], length = 96, include_numbers = True).shift(1 * DOWN)
        an = MathTex(
            r"a_n=\begin{cases}\frac{1}{n},n=2k-1(k\ge 1) \\ \frac{1}{2},n=2k+2(k\ge 0) \end{cases}",
            font_size = 54, color = YELLOW_A
        )
        dot_o = Dot(color = BLUE_D).move_to(line.n2p(0))
        doto_label = MathTex(r"O", font_size = 44, color = BLUE_D).next_to(dot_o, UP, buff = 0.2)
        unit_size = line.get_unit_size()
        dots = VGroup()
        n = 1
        for i in range(1, 30):
            dot = Dot(color = BLUE_D).move_to(line.n2p(1/n)).set_z_index(1)
            dots.add(dot)
            n += 1
        an_label0 = MathTex(r"a_{4}=\frac{1}{2}>\frac{1}{3}", font_size = 40, color = YELLOW_A).next_to(dots[1], UP, buff = 0.3)
        an_label1 = MathTex(r"a_{16}=\frac{1}{2}>\frac{1}{15}", font_size = 40, color = YELLOW_A).next_to(dots[1], UP, buff = 0.3)
        an_label2 = MathTex(r"a_{26}=\frac{1}{2}>\frac{1}{25}", font_size = 40, color = YELLOW_A).next_to(dots[1], UP, buff = 0.3)
        an_label3 = MathTex(r"a_{92}=\frac{1}{2}>\frac{1}{91}", font_size = 40, color = YELLOW_A).next_to(dots[1], UP, buff = 0.3)
        self.wait(1.3)
        dotx_tracker, r_tracker = ValueTracker(2), ValueTracker(2)
        dot_x = Dot(color = GREEN_A, radius = 0.1).move_to(line.n2p(0.5)).set_z_index(2)
        circle = always_redraw(
            lambda: Circle(
                radius = 1/(r_tracker.get_value()) * unit_size, color = GREEN_B, fill_opacity = 0.3, stroke_width = 0
            ).move_to(line.n2p(0))
        )
        dot_x.add_updater(lambda m: m.move_to(line.n2p(1/(dotx_tracker.get_value()))))
        n_label0 = always_redraw(
            lambda: MathTex(
                r"N=" + f"{dotx_tracker.get_value():.0f}", font_size = 54, color = YELLOW
            ).shift(1.5 * UP + 4.3 * LEFT)
        )
        self.play(Write(an), run_time = 1.7)
        self.wait(2)
        self.play(an.animate.shift(2.7 * UP), Create(line), Create(dot_o), Create(doto_label), Create(dots), run_time = 2)
        self.wait(0.4)
        self.add(dot_x).wait(0.6)
        self.play(Flash(dot_x, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.wait(1.3)
        self.play(Write(n_label0), run_time = 1.3)
        self.wait(0.4)
        self.play(GrowFromCenter(circle), run_time = 1.3)
        self.wait(0.4)
        self.play(dotx_tracker.animate.set_value(3), r_tracker.animate.set_value(3), run_time = 1.6)
        self.play(Flash(dots[1], color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10))
        self.add(an_label0).wait(2)
        self.remove(an_label0).wait(0.3)
        self.play(dotx_tracker.animate.set_value(15), r_tracker.animate.set_value(15), run_time = 1.6)
        self.play(Flash(dots[1], color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10))
        self.add(an_label1).wait(2)
        self.remove(an_label1).wait(0.3)
        self.play(dotx_tracker.animate.set_value(25), r_tracker.animate.set_value(25), run_time = 1.6)
        self.play(Flash(dots[1], color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10))
        self.add(an_label2).wait(2)
        self.remove(an_label2).wait(0.3)
        self.play(dotx_tracker.animate.set_value(91), r_tracker.animate.set_value(91), run_time = 3.2)
        self.play(Flash(dots[1], color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10))
        self.add(an_label3).wait(2)
        self.remove(an_label3).wait(0.3)
        self.wait(2.4)
