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

# 第二部分：从epsilon-N到epsilon-delta
class ChapterTwo(Scene):
    def construct(self):
        title = MathTex(
            r"\text{二、从}\epsilon-N\text{到}\epsilon-\delta", tex_template = chinese_template, font_size = 40,
            tex_to_color_map = {r"\epsilon-N": YELLOW_D, r"\epsilon-\delta": TEAL}
        ).scale(1.8)
        self.wait(0.4)
        self.play(Write(title), run_time = 1.6)
        self.wait(2)
        self.play(FadeOut(title), run_time = 0.9)
        limit0 = MathTex(r"\forall\epsilon>0,", font_size = 64.8, color = GREEN_B)
        limit1 = MathTex(r"\exists N,", font_size = 64.8, color = YELLOW)
        limit2 = MathTex(r"\forall n>N:\left | a_n-c\right |<", font_size = 64.8, color = ORANGE)
        limit3 = MathTex(r"\epsilon", font_size = 64.8, color = GREEN_B)
        limit = VGroup(limit0, limit1, limit2, limit3).arrange(RIGHT, buff = 0.3)
        self.play(Write(limit), run_time = 1.6)
        self.wait(2)
        self.play(limit.animate.shift(2 * UP), run_time = 1.6)
        self.wait(0.3)
        series = MathTex(r"a_n=\frac{1}{n}", font_size = 64).shift(0.5 * DOWN + 4 * LEFT)
        self.play(Write(series))
        fracs = VGroup()
        arrows = VGroup()
        numbers = VGroup()
        for i in range(1, 10):
            frac = MathTex(f"\\frac{1}{i}", font_size = 64, color = YELLOW_E).shift(0.5 * UP + 1.9 * LEFT + i * RIGHT)
            arrow = MathTex(r"\uparrow", font_size = 64).shift(0.7 * DOWN + 1.9 * LEFT +  i * RIGHT)
            number = MathTex(f"{i}", font_size = 64, color = YELLOW_B).shift(1.5 * DOWN + 1.9 * LEFT + i * RIGHT)
            fracs.add(frac)
            arrows.add(arrow)
            numbers.add(number)
        self.wait(1.6)
        for i in range(9):
            self.play(LaggedStart(Write(numbers[i]), Write(arrows[i]), Write(fracs[i]), lag_ratio = 0.6), run_time = 0.3)
        self.wait(2)
        integrity = VGroup(series, fracs, arrows, numbers)
        function_limit0 = MathTex(r"\lim_{x \to x_0}f(x) = ", font_size = 72, color = YELLOW_A).shift(0.5 * DOWN + 0.6 * LEFT)
        function_limit1 = Tex("?", font_size = 80, color = RED_C).shift(0.3 * DOWN + 1.7 * RIGHT)
        function_limit = VGroup(function_limit0, function_limit1)
        self.play(ReplacementTransform(integrity, function_limit), run_time = 1.9)
        self.wait(2)
        axes = Axes(
            x_range = [-1, 10.25, 1], y_range = [-2.5, 5, 1], x_length = 15, y_length = 10, axis_config = {"include_ticks": True}
        ).set_stroke(background = True)
        dots = VGroup()
        for i in range(1, 10):
            dot = Dot(axes.coords_to_point(i, 1/i), color = YELLOW_E).set_z_index(1)
            dots.add(dot)
        grid = NumberPlane(
            x_range = [-1, 10.25, 1], y_range = [-2.5, 5, 1], 
            x_length = 15, y_length = 10, 
            background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)
        graph = axes.plot(lambda x: 1/x, x_range = [0.1, 12], color = YELLOW, stroke_width = 4)
        self.play(Create(axes), Create(grid), Create(dots), FadeOut(function_limit), run_time = 2.4)
        self.wait(0.5)
        self.play(Create(graph))
        self.wait(2)
        dotx_tracker = ValueTracker(1)
        dot_x = Dot(color = GREEN_A).move_to(axes.coords_to_point(1, 1)).set_z_index(2)
        dot_0 = Dot(color = GREEN_A).move_to(axes.coords_to_point(1, 0)).set_z_index(2)
        line = Line(axes.coords_to_point(1, 1), axes.coords_to_point(1, 0), color = GREEN_E, stroke_width = 4)
        dot_x.add_updater(lambda d: d.move_to(axes.coords_to_point(dotx_tracker.get_value(), 1/dotx_tracker.get_value())))
        dot_0.add_updater(lambda d: d.move_to(axes.coords_to_point(dotx_tracker.get_value(), 0)))
        line.add_updater(lambda l: l.put_start_and_end_on(dot_x.get_center(), dot_0.get_center()))
        x_label0 = always_redraw(
            lambda: MathTex(
                r"X=" + f"{dotx_tracker.get_value():.2f}", font_size = 54, color = YELLOW
            ).shift(0.8 * UP + 3 * LEFT)
        )
        x_label1 = always_redraw(
            lambda: MathTex(
                r"\forall x>X:\left | \frac{1}{x}-0 \right |<\frac{1}{X}=" + f"{1/dotx_tracker.get_value():.2f}", 
                font_size = 54, color = ORANGE
            ).shift(0.8 * UP + 2.5 * RIGHT)
        )
        area = always_redraw(lambda: axes.get_area(graph, x_range = [dotx_tracker.get_value(), 10.25], color = GREEN_B, opacity = 0.3))
        self.play(Create(dot_x), Create(dot_0), Create(line), Create(area), run_time = 1.6)
        self.play(Flash(dot_x, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.play(Write(x_label0), Write(x_label1), run_time = 1.2)
        self.wait(0.8)
        self.play(dotx_tracker.animate.set_value(2.5), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(5.14), run_time = 2)
        self.wait(1.4)
        self.play(dotx_tracker.animate.set_value(9.191), run_time = 2)
        self.wait(2.4)
        a = VGroup(limit1, x_label0)
        b = VGroup(limit2, x_label1)
        neolimit0 = MathTex(r"\exists X>0,", font_size = 64.8, color = YELLOW).shift(2 * UP + 2.5 * LEFT)
        neolimit1 = MathTex(r"\forall x>X:\left | f(x)-c\right |<", font_size = 64.8, color = ORANGE).shift(2 * UP + 2.1 * RIGHT)
        self.play(
            ReplacementTransform(a, neolimit0), ReplacementTransform(b, neolimit1), 
            limit3.animate.shift(0.8 * RIGHT), limit0.animate.shift(1 * LEFT), run_time = 2.2
        )
        self.wait(1.6)
        neolimit = VGroup(limit3, neolimit0, neolimit1, limit0)
        neointegrity = VGroup(axes, grid, graph, dots, dot_x, dot_0, line, area)
        self.play(FadeOut(neointegrity), neolimit.animate.shift(2 * DOWN), run_time = 1.8)
        self.wait(0.4)
        rect = SurroundingRectangle(neolimit, color = TEAL_A, buff = 0.4, stroke_width = 4)
        self.play(ShowPassingFlash(rect), time_width = 0.7, run_time = 1.6)
        self.wait(2)
        lrarrow = MathTex(r"\Leftrightarrow ", font_size = 64.8, color = YELLOW_A).rotate(PI/2)
        limit_fx = MathTex(r"\lim_{x \to +\infty}f(x)=c", font_size = 64.8, color = YELLOW_A).shift(1 * DOWN)
        self.play(neolimit.animate.shift(0.8 * UP), Create(lrarrow), DrawBorderThenFill(limit_fx), run_time = 1.6)
        self.wait(1.7)
        self.play(FadeOut(neolimit), FadeOut(lrarrow), FadeOut(limit_fx), FadeIn(axes), FadeIn(grid), FadeIn(graph), run_time = 1.8)
        dotx_tracker = ValueTracker(9)
        neodot = Dot(color = GREEN_A).move_to(axes.coords_to_point(9, 1/9)).set_z_index(2)
        neodot.add_updater(lambda d: d.move_to(axes.coords_to_point(dotx_tracker.get_value(), 1/dotx_tracker.get_value())))
        self.wait(0.3)
        self.play(Create(neodot), run_time = 1.2)
        self.wait(0.4)
        self.play(dotx_tracker.animate.set_value(2), run_time = 2)
        self.wait(0.3)
        self.play(Flash(neodot, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.wait(2.5)
        unit_size = axes.get_x_unit_size()
        width_tracker = ValueTracker(1)
        neighborhood = always_redraw(
            lambda: Rectangle(
                width = 2 * width_tracker.get_value() * unit_size, height = 10 * unit_size, color = GREEN_B, stroke_width = 0, 
                fill_opacity = 0.4
            ).move_to(neodot.get_center())
        )
        y_rect = always_redraw(
            lambda: Rectangle(
                width = 16 * unit_size, height = 2 * width_tracker.get_value() * unit_size, color = BLUE_B, stroke_width = 0, 
                fill_opacity = 0.4
            ).move_to(neodot.get_center())
        )
        neighborhood = always_redraw(
            lambda: Rectangle(
                width = 2 * width_tracker.get_value() * unit_size, height = 10 * unit_size, color = GREEN_B, stroke_width = 0, 
                fill_opacity = 0.3
            ).move_to(neodot.get_center())
        )
        y_rect = always_redraw(
            lambda: Rectangle(
                width = 16 * unit_size, height = width_tracker.get_value() * unit_size, color = BLUE_B, stroke_width = 0, 
                fill_opacity = 0.3
            ).move_to(neodot.get_center())
        )
        self.play(GrowFromCenter(neighborhood), run_time = 1.3)
        self.wait(0.5)
        neighbor0 = always_redraw(
            lambda: MathTex(
                r"\delta=" + f"{width_tracker.get_value():.2f}", font_size = 54, color = YELLOW
            ).shift(2 * UP + 3.5 * LEFT)
        )
        neighbor1 = always_redraw(
            lambda: MathTex(
                r"\forall x:0<\left| x-2\right |<\delta=" + f"{width_tracker.get_value():.2f}" + r",", font_size = 54, color = ORANGE
            ).shift(3.3 * UP + 3 * RIGHT)
        )
        neighbor2 = always_redraw(
            lambda: MathTex(
                r"\left |\frac{1}{x}-\frac{1}{2}\right |=\left |\frac{x-2}{2x}\right |<\frac{\delta}{2}=" + 
                f"{width_tracker.get_value()/2:.2f}", font_size = 54, color = GREEN_B
            ).shift(1.7 * UP + 2.7 * RIGHT)
        )
        self.play(Write(neighbor0), Write(neighbor1), Write(neighbor2), run_time = 2)
        self.wait(0.4)
        n_rect = SurroundingRectangle(neighbor2, color = TEAL_A, buff = 0.3, stroke_width = 4)
        self.play(ShowPassingFlash(n_rect), time_width = 0.7, run_time = 1.6)
        self.wait(0.6)
        self.play(GrowFromCenter(y_rect), run_time = 1.1)
        self.wait(0.5)
        self.play(width_tracker.animate.set_value(0.514), run_time = 1.8)
        self.wait(1.4)
        self.play(width_tracker.animate.set_value(0.251), run_time = 1.8)
        self.wait(1.4)
        self.play(width_tracker.animate.set_value(0.114), run_time = 1.8)
        self.wait(1.4)
        self.play(width_tracker.animate.set_value(0.056), run_time = 1.8)
        self.wait(2.4)
        dot_limit0 = MathTex(r"\forall\epsilon>0,", font_size = 54, color = GREEN_B).shift(2 * UP + 5.5 * LEFT)
        dot_limit1 = MathTex(r"\exists\delta=2\epsilon>0,", font_size = 54, color = YELLOW).shift(2 * UP + 3 * LEFT)
        dot_limit2 = MathTex(r"\forall x:0<\left |x-2\right |<\delta,", font_size = 54, color = ORANGE).shift(2 * UP + 1 * RIGHT)
        dot_limit3 = MathTex(
            r"\left |\frac{1}{x}-\frac{1}{2}\right |<\epsilon", font_size = 54, color = GREEN_B
        ).shift(2 * UP + 5 * RIGHT)
        dot_limit = VGroup(dot_limit0, dot_limit1, dot_limit2, dot_limit3)
        self.play(
            ReplacementTransform(neighbor0, dot_limit0), Write(dot_limit1), 
            ReplacementTransform(neighbor1, dot_limit2), ReplacementTransform(neighbor2, dot_limit3), run_time = 2
        )
        self.wait(1.6)
        self.play(FadeOut(axes), FadeOut(grid), FadeOut(graph), FadeOut(neodot), FadeOut(y_rect), FadeOut(neighborhood), run_time = 1.7)
        ed_limit0 = MathTex(r"\forall\epsilon>0,", font_size = 54, color = GREEN_B)
        ed_limit1 = MathTex(r"\exists\delta>0,", font_size = 54, color = YELLOW)
        ed_limit2 = MathTex(r"\forall x:0<\left |x-x_0\right |<\delta,", font_size = 54, color = ORANGE)
        ed_limit3 = MathTex(r"\left |f(x)-c\right |<\epsilon", font_size = 54, color = GREEN_B)
        ed_limit = VGroup(ed_limit0, ed_limit1, ed_limit2, ed_limit3).arrange(RIGHT, buff = 0.3)
        self.play(
            ReplacementTransform(dot_limit0, ed_limit0), ReplacementTransform(dot_limit1, ed_limit1), 
            ReplacementTransform(dot_limit2, ed_limit2), ReplacementTransform(dot_limit3, ed_limit3), run_time = 1.8
        )
        self.wait()
        ed_rect = SurroundingRectangle(ed_limit, color = TEAL_A, buff = 0.3, stroke_width = 4)
        self.play(ShowPassingFlash(ed_rect), time_width = 0.7, run_time = 1.6)
        self.wait(2.2)
        ed_arrow = MathTex(r"\Leftrightarrow", font_size = 64.8, color = YELLOW_A).rotate(PI/2)
        ed_def = MathTex(r"\lim_{x \to x_0}f(x)=c", font_size = 64.8, color = YELLOW_A).shift(1 * DOWN)
        self.play(Create(ed_arrow), DrawBorderThenFill(ed_def), ed_limit.animate.shift(0.8 * UP), run_time = 2.1)
        self.wait(2)
        ed = MathTex(r"\epsilon-\delta", font_size = 180, color = TEAL)
        ied = VGroup(ed_limit, ed_arrow, ed_def)
        self.play(AnimationGroup(ied.animate.set_opacity(0.2), DrawBorderThenFill(ed), lag_ratio = 0.6), run_time = 2.4)
        self.wait(2.5)
        self.play(FadeOut(ed))
        self.play(ied.animate.set_opacity(1), run_time = 1.8)
        ed_rect2 = SurroundingRectangle(ed_limit2, color = TEAL_A, buff = 0.1, stroke_width = 4)
        self.wait(2)
        self.play(ShowPassingFlash(ed_rect2), time_width = 0.7, run_time = 1.6)
        self.wait(2.4)
        self.play(FadeOut(ied), run_time = 1.6)
        self.wait(0.5)
