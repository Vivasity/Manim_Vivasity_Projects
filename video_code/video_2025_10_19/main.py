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

# 视频的前言
class Main(Scene):
    def construct(self):
        series = []
        for i in range(1, 9):
            frac = MathTex(f"\\frac{1}{i},", font_size = 90)
            series.append(frac)
        group = VGroup(*series).arrange(RIGHT, buff = 0.8)
        group.move_to(RIGHT * 5)
        self.wait(1.6)
        self.play(LaggedStart(*[Write(frac) for frac in series], lag_ratio = 0.5, run_time = 6))
        n_item = MathTex(r"\cdots,\frac{1}{n},\cdots\cdots", font_size = 90).next_to(series[-1], RIGHT, buff = 0.6)
        integrity = VGroup(group, n_item)
        self.play(integrity.animate.shift(LEFT * 12), run_time = 3.5)
        self.wait(1.5)
        limit = MathTex(r"\lim_{n \to \infty}\frac{1}{n}", font_size = 90, color = YELLOW_A)
        question0 = MathTex(r"=", font_size = 90, color = YELLOW_A)
        question1 = Tex("?", font_size = 150, color = RED_C)
        question = VGroup(question0, question1).arrange(RIGHT, buff = 0.5).shift(RIGHT * 1.2)
        self.play(ReplacementTransform(integrity, limit), run_time = 1.5)
        self.wait(2.5)
        self.play(AnimationGroup(limit.animate.shift(LEFT * 1.5), Create(question), lag_ratio = 0.6), run_time = 1.5)
        self.wait(2.4)
        zero = Tex("0", font_size = 90, color = ORANGE).move_to(question1.get_center())
        rect = SurroundingRectangle(zero, color = YELLOW, buff = 0.2, stroke_width = 4)
        self.play(ReplacementTransform(question1, zero), run_time = 1.3)
        self.wait(0.5)
        self.play(ShowPassingFlash(rect, time_width = 0.8))
        self.wait(0.5)
        self.play(FadeOut(question0), FadeOut(zero), FadeOut(limit), run_time = 1.6)
        self.wait(0.4)

class SubMain(Scene):
    def construct(self):
        a = MathTex(r"a=", font_size = 60, color = YELLOW_A).shift(2.2 * UP + 6 * LEFT)
        vect = 2.4 * DOWN + 6 * LEFT
        axis_x = Arrow(0.5 * LEFT, 12.5 * RIGHT, max_tip_length_to_length_ratio = 0.0177, stroke_width = 3.3).shift(vect)
        axis_y = Arrow(0.5 * DOWN, 3.7 * UP, max_tip_length_to_length_ratio = 0.06, stroke_width = 3.3).shift(vect)
        self.play(Write(a), Create(axis_x), Create(axis_y), run_time = 1.3)
        self.wait(0.5)
        t = 0.5

        def tex_updater(mob: VMobject, dt):
            x = mob.get_x()
            v = max(x + 4.8, 1.8)
            mob.shift(v * dt * RIGHT).set_opacity(clip(inverse_interpolate(8, 0, x), 0, 1))
            return x > 8
        
        def texs_updater(mob: VGroup, dt):
            mob.time += dt
            while(mob.time >= t):
                mob.add(MathTex(r"\frac{1}{" + str(mob.counter + 1) + r"}", font_size = 60, color = GREEN_B).shift(2.2 * UP + 5 * LEFT))
                mob.time -= t
                mob.counter += 1
            to_remove = []
            for submob in mob.submobjects:
                if_remove = tex_updater(submob, dt)
                if if_remove:
                    to_remove.append(submob)
            mob.remove(*to_remove)
        
        texs = VGroup()
        texs.counter, texs.time = 0, 0
        texs.add_updater(texs_updater)
        
        def point_updater(mob: VMobject, dt):
            x = mob.get_x()
            v = (6 + x) * max(1/(0.1 + 0.6 * (3 - x)), 0.05)
            mob.shift(v * dt * LEFT).set_opacity(clip(inverse_interpolate(-6, -1.5, x), 0.25, 1))
            return x > 8
        
        def points_updater(mob: VGroup, dt):
            mob.time += dt
            while(mob.time >= t):
                new_point = Dot(np.array([3, 2.9 * 1/(mob.counter + 2) - 2.4, 0]), color = BLUE_B)
                mob.add(new_point)
                mob.time -= t
                mob.counter += 1
            for submob in mob.submobjects:
                point_updater(submob, dt)
        
        point_0 = Dot(0.5 * UP + 3 * RIGHT, color = BLUE_B)
        points = VGroup(point_0)
        points.counter, points.time = 0, 0
        points.add_updater(points_updater)
        self.add(texs, points).wait(20)
        self.remove(texs).remove(points)
        self.play(FadeOut(a), Uncreate(axis_x), Uncreate(axis_y), run_time = 1.4)
        self.wait(0.6)
