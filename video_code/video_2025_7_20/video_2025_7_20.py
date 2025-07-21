from manim import *
import random as rd
import string as str

chinese_template = TexTemplate()
chinese_template.add_to_preamble(r"\usepackage{ctex}")  # 添加中文支持
chinese_template.tex_compiler = "pdflatex"

class Chi(Tex):  # 定义了一个继承自Tex的Chi类，用于更便利地创建中文字幕
    def __init__(self, tex):
        super().__init__()
        self.tex0 = Tex(tex, tex_template = chinese_template, font_size = 40)
        self.add(self.tex0)

class MathChi(MathTex):  # 定义了一个继承自MathTex的MathChi类，用于更便利地创建中文和数学公式的混合字幕
    def __init__(self, mathtex):
        super().__init__()
        self.mathtex0 = MathTex(mathtex, tex_template = chinese_template, font_size = 40)
        self.add(self.mathtex0)

# 视频的封面
class Fengmian(Scene):
    def construct(self):
        self.camera.background_color = "#000015"
        target_tex = MathTex(
            r"\left ( \mathbb{R},+,\cdot ,\le   \right )",
            font_size = 200
        ).set_color_by_gradient(GREEN_B, BLUE_B)
        circle = Circle(
            radius = 1,
            fill_color = GREEN_B,
            fill_opacity = 0.17,
            stroke_width = 0
        ).shift(LEFT*4.5+DOWN*2)
        number_line = NumberLine(
            x_range = [0, 10, 1],
            length = 10,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [0, 2, 4, 6, 8, 10],
            font_size = 28
        ).shift(DOWN*2.2+RIGHT*2)
        dot = Dot(color = GREEN, radius = 0.08).move_to(circle.get_center())
        label = MathTex(r"x", font_size = 40, color = GREEN).next_to(dot, UP)
        xdot = Dot(number_line.n2p(3.5), color = GREEN, radius = 0.08)
        xlabel = MathTex(r"x", font_size = 44, color = GREEN).next_to(xdot, UP)
        ydot = Dot(number_line.n2p(6.4), color = GREEN, radius = 0.08)
        ylabel = MathTex(r"y", font_size = 44, color = GREEN).next_to(ydot, UP)
        tex0 = MathTex(
            r"x\cdot y=y\cdot x",
            font_size = 60
        ).shift(UP*2+RIGHT*5)
        tex1 = MathTex(
            r"O(x,\delta_{x})",
            font_size = 60
        ).shift(DOWN*1+LEFT*5.5)
        tex2 = MathTex(
            r"\text{Bolzano-Weierstrass}",
            font_size = 70
        ).shift(UP*1+RIGHT*4)
        tex3 = MathTex(
            r"\text{Heine-Borel}",
            font_size = 74
        ).shift(DOWN*1+RIGHT*4.6)
        tex4 = MathTex(
            r"|x_n-x_m|<\epsilon",
            font_size = 66
        ).shift(UP*1.5+LEFT*3.1)
        tex5 = MathTex(
            r"\forall n,m>N",
            font_size = 76
        ).shift(UP*1.9+LEFT*4.2)
        tex6 = MathTex(
            r"n\cdot x\ge y",
            font_size = 70
        ).shift(UP*1.9+RIGHT*2.3).rotate(PI/8)
        tex7 = MathTex(
            r"\text{Cauchy}",
            font_size = 60
        ).shift(LEFT*4.8).rotate(PI/12)
        tex8 = MathTex(
            r"|x_{n_k}-\mathcal{K}|<\frac{1}{2^k}",
            font_size = 65
        ).shift(UP*2.8+LEFT*1)
        combine = VGroup(
            tex0, dot, label, tex1, number_line, xdot, ydot, xlabel, ylabel, tex2, tex3, tex4, tex5, tex6, tex7, tex8
        )
        combine.set_opacity(0.3)
        self.add(circle)
        self.add(combine)
        self.add(target_tex)
        self.wait(3)

# 在视频开头展示一段名言
class First(Scene):
    def construct(self):
        tex0 = Tex(
            "Young man, in mathematics you don't understand things.",
            font_size = 48,
            color = YELLOW_A
        )
        tex1 = Tex(
            "You just get used to them.",
            font_size = 48,
            color = YELLOW_A
        )
        tex = VGroup(tex0, tex1).arrange(DOWN, aligned_edge = LEFT, buff = 0.3)
        tex2 = Tex(
            "---John von Neumann", 
            font_size = 56, 
            color = YELLOW_D
        ).next_to(tex1, DOWN).to_edge(RIGHT, buff = 1.6)
        self.wait(0.4)
        self.play(Write(tex0), run_time = 1.8)
        self.play(Write(tex1), run_time = 1)
        self.wait(2.5)
        self.play(Write(tex2), run_time = 1.8)
        self.wait(1.5)
        self.play(FadeOut(tex0), FadeOut(tex1), FadeOut(tex2), run_time = 1.8)

# 展示实数系的四个公理F, O, A, N
class Main(Scene):
    def construct(self):
        rec0 = Rectangle(height = 0.9, width = 2.7, color = YELLOW, stroke_width = 4.0)
        tex0 = MathChi(
            r"\text{设}\mathbb{R}\text{是一个集合，}x,y,z\text{都是其中的元素}"
        ).to_edge(UP, buff = 1)
        tex1 = MathChi(r"\mathbb{R}\text{上定义了两个操作：}")
        tex2 = MathChi(
            r"\text{加法}(+):\mathbb{R}\times \mathbb{R}\to \mathbb{R},\left ( x,y \right )\mapsto x+y"
        )
        tex3 = MathChi(
            r"\text{乘法}(\cdot):\mathbb{R}\times \mathbb{R}\to \mathbb{R},\left ( x,y \right )\mapsto x\cdot y"
        )
        tex4 = MathChi(r"\mathbb{R}\text{上还有一个序关系：}x\le y\text{(或者}y\le x\text{)}")
        non_target_tex = MathTex(
            r"\text{这就构成了一个四元组：}",
            tex_template = chinese_template,
            font_size = 52
        ).shift(LEFT*1.5)
        target_tex = MathTex(
            r"\left ( \mathbb{R},+,\cdot ,\le   \right )",
            font_size = 52,
            color = BLUE_C
        ).next_to(non_target_tex)
        tex5 = VGroup(non_target_tex, target_tex)
        tex = VGroup(tex0, tex1, tex2, tex3, tex4).arrange(DOWN)
        rec_tex = VGroup(rec0, target_tex)
        ani0 = tex.animate.set_opacity(0.15).set_run_time(2.5)
        self.wait(0.4)
        self.play(Write(tex0))
        self.wait(0.8)
        self.play(Write(tex1))
        self.wait(0.8)
        self.play(Write(tex2))
        self.wait(0.8)
        self.play(Write(tex3))
        self.wait(0.8)
        self.play(Write(tex4))
        self.wait(2.4)
        self.play(AnimationGroup(ani0, Write(tex5), lag_ratio = 1.3/2.5))
        self.wait(1.4)
        self.play(
            AnimationGroup(FadeOut(non_target_tex), 
            ApplyMethod(target_tex.move_to, [0, 0, 0]), 
            lag_ratio = 1.3/2.5)
        )
        self.wait()
        self.play(Create(rec0))
        self.play(rec_tex.animate.shift(UP*3.3), FadeOut(tex), run_time = 1.6)
        tex6 = MathChi(r"\text{若其满足以下公理：}").next_to(rec_tex, DOWN)
        tex7 = MathChi(
            r"\text{域公理：}\mathbb{R}\text{是一个域}"  # 域公理(F)
        ).next_to(rec_tex, DOWN)
        tex8 = MathChi(r"\text{(1)加法交换律：}x+y=y+x")
        tex9 = MathChi(r"\text{(2)加法结合律：}x+(y+z)=(x+y)+z")
        tex10 = MathChi(r"\text{(3)}\exists 0\in\mathbb{R},\forall x\in\mathbb{R},0+x=x\text{成立}")
        tex11 = MathChi(r"\text{(4)}\forall x\in\mathbb{R},\exists -x\in\mathbb{R},\text{使得}x+(-x)=0")
        tex12 = MathChi(r"\text{(5)乘法交换律：}x\cdot y=y\cdot x")
        tex13 = MathChi(r"\text{(6)乘法结合律：}x\cdot(y\cdot z)=(x\cdot y)\cdot z")
        tex14 = MathChi(
            r"\text{(7)}\exists 1 \ne 0\in\mathbb{R},\forall x\in\mathbb{R},1\cdot x=x\text{成立}"
        )
        tex15 = MathChi(
            r"\text{(8)}\forall x\in\mathbb{R}-\left\{0\right\},\exists x^{-1}\in\mathbb{R},\text{使得}x\cdot x^{-1}=1"
        )
        tex16 = MathChi(r"\text{(9)乘法分配律：}x\cdot(y+z)=x\cdot y+x\cdot z")
        math_tex = VGroup(
            tex7, tex8, tex9, tex10, tex11, tex12, tex13, tex14, tex15, tex16
        ).arrange(DOWN, aligned_edge = LEFT)
        math_tex1 = VGroup(tex8, tex9, tex10, tex11, tex12, tex13, tex14, tex15, tex15, tex16)
        self.wait(1.2)
        self.play(Write(tex6))
        rec_tex.add(tex6)
        rec_tex.remove(rec0)
        rect = VGroup(rec0)
        self.play(
            rec_tex.animate.set_opacity(0.15), 
            rect.animate.set_stroke(opacity = 0.15), 
            run_time = 1.5
        )
        self.play(FadeIn(math_tex), run_time = 2.2)
        self.wait(6.5)
        self.play(FadeOut(math_tex1), run_time = 2)
        self.play(
            tex7.animate.shift(DOWN*2+LEFT*2), 
            rect.animate.set_stroke(opacity = 1), 
            rec_tex.animate.set_opacity(1),
            run_time = 1.6
        )
        rec_tex.add(tex7)
        rec1 = Rectangle(
            height = 0.8, 
            width = 4.7, 
            color = YELLOW, 
            stroke_width = 4.0
        ).move_to(tex7.get_center())
        tex17 = MathTex(
            r"\left ( \mathbf{F} \right ) ",
            font_size = 44,
            color = YELLOW_A
        ).next_to(tex7, RIGHT, buff = 7.5)
        tex18 = MathChi(
            r"\text{序公理：}\mathbb{R}\text{是有序域}"  # 序公理(O)
        )
        tex19 = MathChi(r"\text{(1)序的传递性：}x\le y,y\le z\Rightarrow x\le z")
        tex20 = MathChi(r"\text{(2)序可以决定元素：}x\le y,y\le x\Rightarrow x=y")
        tex21 = MathChi(r"\text{(3)全序关系：}\forall x,y\in\mathbb{R},x\le y\text{或}y\le x")
        tex22 = MathChi(r"\text{(4)与加法相容：}x\le y\Rightarrow x+z\le y+z")
        tex23 = MathChi(r"\text{(5)与乘法相容：}x\ge 0,y\ge 0\Rightarrow x\cdot y\ge 0")
        math_tex2 = VGroup(tex18, tex19, tex20, tex21, tex22, tex23).arrange(DOWN, aligned_edge = LEFT)
        math_tex3 = VGroup(tex19, tex20, tex21, tex22, tex23)
        self.wait(0.8)
        self.play(Create(rec1))
        self.wait(0.6)
        self.play(Write(tex17), run_time = 1.2)
        self.wait(0.6)
        rect.add(rec1)
        rec_tex.add(tex17)
        self.play(
            rect.animate.set_stroke(opacity = 0.15),
            rec_tex.animate.set_opacity(0.15),
            run_time = 1.6
        )
        self.play(FadeIn(math_tex2), run_time = 1.6)
        self.wait(4)
        self.play(FadeOut(math_tex3), run_time = 1.3)
        self.play(
            tex18.animate.shift(DOWN*1.6+LEFT*2.05),
            rect.animate.set_stroke(opacity = 1),
            rec_tex.animate.set_opacity(1),
            run_time = 1.6
        )
        self.wait(0.8)
        rec2 = Rectangle(
            height = 0.8,
            width = 4.7,
            stroke_width = 4.0,
            color = YELLOW
        ).move_to(tex18.get_center())
        tex24 = MathTex(
            r"\left ( \mathbf{O} \right ) ",
            font_size = 44,
            color = YELLOW_A
        ).next_to(tex18, RIGHT, buff = 7.45)
        self.play(Create(rec2))
        self.wait(0.6)
        self.play(Write(tex24), run_time = 1.6)
        rect.add(rec2)
        rec_tex.add(tex18)
        rec_tex.add(tex24)
        self.wait(0.6)
        self.play(
            rect.animate.set_stroke(opacity = 0.15),
            rec_tex.animate.set_opacity(0.15),
            run_time = 1.6
        )
        tex25 = MathChi(
            r"\text{Archimedes公理：}\mathbb{R}\text{是Archimedes有序域}"  # Archimedes公理(A)
        )
        tex26 = MathChi(
            r"\forall x\in \mathbb{R}^{+},\forall y\in \mathbb{R},\exists n\in \mathbb{Z}^{+},\text{使得}n\cdot x\ge y"
        )
        math_tex4 = VGroup(tex25, tex26).arrange(DOWN, aligned_edge = LEFT)
        self.play(FadeIn(math_tex4), run_time = 1.2)
        self.wait(0.8)
        number_line = NumberLine(
            x_range = [0, 10, 1],
            length = 10,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = np.arange(0, 11, 1),
            font_size = 28
        ).shift(DOWN * 2.5)
        self.play(Create(number_line), run_time = 1.6)
        self.wait(0.8)

        # 在数轴上随机生成x和y，并找到最小的n使得nx大于等于y
        for i in range(4):
            x = rd.uniform(0, 2.5)
            y = rd.uniform(4.5, 8.5)
            n = int(np.ceil(y / x))
            x_label = MathTex(f"x = {x:.3f}", font_size = 32, color = YELLOW_A).shift(LEFT*3.5+DOWN*1)
            y_label = MathTex(f"y = {y:.3f}", font_size = 32, color = YELLOW_A).next_to(x_label, DOWN)
            n_label = MathTex(f"n = {n}", font_size = 32, color = RED).next_to(y_label, DOWN)
            d_x = Dot(number_line.n2p(x), color = YELLOW, radius = 0.06)
            l_x = MathTex(r"x", font_size = 30, color = YELLOW_A).next_to(d_x, DOWN)
            d_y = Dot(number_line.n2p(y), color = YELLOW, radius = 0.06)
            l_y = MathTex(r"y", font_size = 30, color = YELLOW_A).next_to(d_y, DOWN)
            n_d = Dot(number_line.n2p(n*x), color = RED, radius = 0.08)
            l_n_d = MathTex(
                r"n\cdot x\ge y",
                font_size = 32,
                color = RED
            ).next_to(n_d, UP)
            self.play(
                Create(d_x),
                Create(l_x),
                Create(d_y),
                Create(l_y),
                Create(x_label),
                Create(y_label),
                run_time = 0.8
            )
            self.play(Create(n_d), Create(l_n_d), Create(n_label), run_time = 0.8)
            self.wait(1.5)
            self.play(
                Uncreate(d_x),
                Uncreate(l_x),
                Uncreate(d_y),
                Uncreate(l_y),
                Uncreate(n_d),
                Uncreate(l_n_d),
                Uncreate(x_label),
                Uncreate(y_label),
                Uncreate(n_label),
                run_time = 0.8
            )

        self.play(Uncreate(number_line), FadeOut(tex26), run_time = 1.6)
        self.play(
            tex25.animate.shift(DOWN*1.2+LEFT*2.2),
            rect.animate.set_stroke(opacity = 1),
            rec_tex.animate.set_opacity(1),
            run_time = 1.6
        )
        tex27 = MathTex(
            r"\left ( \mathbf{A} \right ) ",
            font_size = 44,
            color = YELLOW_A
        ).next_to(tex25, RIGHT, buff = 3.45)
        self.wait(0.8)
        rec3 = Rectangle(
            height = 0.8,
            width = 8.7,
            stroke_width = 4.0,
            color = YELLOW
        ).move_to(tex25.get_center())
        self.play(Create(rec3))
        self.wait(0.6)
        self.play(Write(tex27))
        self.wait(0.6)
        rect.add(rec3)
        rec_tex.add(tex25)
        rec_tex.add(tex27)
        self.play(
            rect.animate.set_stroke(opacity = 0.15),
            rec_tex.animate.set_opacity(0.15),
            run_time = 1.6
        )
        tex28 = MathChi(
            r"\text{闭区间套公理：Nested Intervals Axiom}"  # 闭区间套公理(N)
        )
        tex29 = MathChi(r"\text{如果数列}\left\{a_{n}\right\},\left\{b_{n}\right\}\text{满足：}")
        tex30 = MathChi(
            r"\forall n\in\mathbb{Z}^{+},a_{n}\le a_{n+1}<b_{n+1}\le b_{n}\text{成立}\text{,且}\lim_{n \to \infty}\left ( b_{n}-a_{n} \right )=0 "
        )
        tex31 = MathChi(r"\text{那么：}")
        tex32 = MathChi(
            r"\lim_{n \to \infty}a_{n}=\lim_{n \to \infty}b_{n}=\xi\text{,且}\xi\text{是满足}\forall n\in \mathbb{Z}^{+}\left(a_{n}\le \xi\le b_{n}\right)\text{的唯一实数}"
        )
        math_tex5 = VGroup(tex28, tex29, tex30, tex31, tex32).arrange(DOWN, aligned_edge = LEFT).shift(UP*1.8)
        math_tex6 = VGroup(tex29, tex30, tex31, tex32)
        self.play(FadeIn(math_tex5), run_time = 1.8)
        self.wait(0.8)
        number_line1 = NumberLine(
            x_range = [1, 7, 1],
            length = 10,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [1, 3, 5, 7],
            font_size = 28
        ).shift(DOWN * 2.5)
        self.play(Create(number_line1), run_time = 1.6)
        self.wait(0.8)
        a = [2.4, 3.15, 3.5, 3.75, 3.875]
        b = [6.5, 5.2, 4.5, 4.25, 4.125]
        colour = [YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E]
        intervals = VGroup()
        a_labels = VGroup()
        b_labels = VGroup()
        interval = Line(number_line1.n2p(a[0]), number_line1.n2p(b[0]), color = YELLOW_A, stroke_width = 5.0)
        a_label = MathTex("a_0", color = YELLOW_A, font_size = 32).next_to(number_line1.n2p(a[0]), DOWN)
        b_label = MathTex("b_0", color = YELLOW_A, font_size = 32).next_to(number_line1.n2p(b[0]), DOWN)
        intervals.add(interval)
        a_labels.add(a_label)
        b_labels.add(b_label)
        self.play(
            Create(interval),
            Write(a_label),
            Write(b_label),
            run_time = 1.6
        )
        self.wait(0.8)

        # 生成闭区间套相应的动画，两列点越来越逼近\xi
        for i in range(1, len(a)):
            new_interval = Line(number_line1.n2p(a[i]), number_line1.n2p(b[i]), color = colour[i], stroke_width = 5.0)
            new_a_label = MathTex(
                f"a_{i}", 
                color = colour[i], 
                font_size = 32
            ).next_to(number_line1.n2p(a[i]), DOWN)
            new_b_label = MathTex(
                f"b_{i}", 
                color = colour[i], 
                font_size = 32
            ).next_to(number_line1.n2p(b[i]), DOWN)
            self.play(
                ReplacementTransform(intervals[-1].copy(), new_interval),
                ReplacementTransform(a_labels[-1].copy(), new_a_label),
                ReplacementTransform(b_labels[-1].copy(), new_b_label),
                run_time = 1.6
            )
            self.wait(0.8)
            intervals.add(new_interval)
            a_labels.add(new_a_label)
            b_labels.add(new_b_label)

        d_label = MathTex(
            r"\dots",
            font_size = 36
        ).next_to(number_line1.n2p(4), DOWN, buff = 0.7)
        convergence_point = Dot(number_line1.n2p(4), color = RED, radius = 0.08)
        c_label = MathTex(r"\xi", color = RED, font_size = 40).next_to(convergence_point, UP)
        convergence_explanation = MathTex(
            r"\lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = \xi",
            color = RED,
            font_size = 40
        ).next_to(convergence_point, UP, buff = 1.1)
        self.play(Write(d_label))
        self.wait(0.6)
        self.play(
            Create(convergence_point),
            Write(c_label),
            Write(convergence_explanation),
            run_time = 1.6
        )
        self.wait(0.8)
        self.play(
            Uncreate(intervals),
            Uncreate(a_labels),
            Uncreate(b_labels),
            Uncreate(number_line1),
            Uncreate(convergence_point),
            Uncreate(convergence_explanation),
            Uncreate(c_label),
            Uncreate(d_label),
            FadeOut(math_tex6),
            run_time = 1.6
        )
        self.play(
            tex28.animate.shift(RIGHT*0.3+DOWN*5.25),
            rect.animate.set_stroke(opacity = 1),
            rec_tex.animate.set_opacity(1),
            run_time = 1.6
        )
        self.wait(0.8)
        rec4 = Rectangle(
            height = 0.8,
            width = 8.5,
            stroke_width = 4.0,
            color = YELLOW
        ).move_to(tex28.get_center())
        tex33 = MathTex(
            r"\left ( \mathbf{N} \right ) ",
            font_size = 44,
            color = YELLOW_A
        ).next_to(tex28, RIGHT, buff = 3.7)
        self.play(Create(rec4))
        self.wait(0.6)
        self.play(Write(tex33))
        self.wait(0.6)
        rec_tex.add(tex28)
        rec_tex.add(tex33)
        r_t = VGroup(rec0, target_tex)
        rect1 = VGroup(rec1, rec2, rec3, rec4)
        rec_tex1 = VGroup(tex6, tex7, tex17, tex18, tex24, tex25, tex27, tex28, tex33)
        self.play(
            rect1.animate.set_stroke(opacity = 0.15),
            rec_tex1.animate.set_opacity(0.15),
            run_time = 1.6
        )
        tex34 = MathChi(r"\text{我们就称这样的四元组为：}").shift(UP*0.7)
        tex35 = MathTex(
            r"\text{实数}",
            tex_template = chinese_template,
            font_size = 84,
            color = BLUE_B
        ).next_to(tex34, DOWN)
        self.play(Write(tex34), run_time = 1.2)
        self.play(ReplacementTransform(r_t, tex35), run_time = 2.5)
        self.wait(1.6)
        self.play(
            FadeOut(tex35), 
            FadeOut(tex34),
            FadeOut(rect1),
            FadeOut(rec_tex1),
            run_time = 1.8
        )
        self.wait()

# A+N推导确界存在定理
class LeastBoundProperty(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\text{实际上，还有一些其他的表述也能表达实数系的性质}",
            tex_template = chinese_template,
            font_size = 44
        ).shift(UP*0.6)
        tex1 = MathTex(
            r"\text{这个视频接下来想展现这些表述}",
            tex_template = chinese_template,
            font_size = 52
        ).next_to(tex0, DOWN).set_color_by_gradient(BLUE_C, PURPLE_C)
        self.play(Write(tex0), run_time = 1.6)
        self.wait(1.4)
        self.play(Write(tex1), run_time = 1.6)
        self.play(Wiggle(tex1, scale_value = 1.1, rotation_angle = 2.5*DEGREES, run_time = 1.2))
        self.wait(1.4)
        tex2 = MathTex(
            r"\left(\mathbf{A}\right)+\left(\mathbf{N}\right)\Rightarrow\text{确界存在定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex2, DOWN).set_length(12)
        self.play(AnimationGroup(FadeOut(tex0), ReplacementTransform(tex1, tex2), lag_ratio = 0.9/2.5))
        self.wait(0.5)
        self.play(GrowFromCenter(line0), run_time = 0.8)
        self.wait(0.8)
        tex3 = MathChi(r"\underline{\text{确界存在定理}}")
        tex4 = MathChi(
            r"\text{对任意}\mathbb{R}\text{的非空子集}S,\text{若}}S\text{在}\mathbb{R}\text{内有上界},\text{则}S\text{在}\mathbb{R}\text{内有上确界}"
        )
        tex = VGroup(tex3, tex4).arrange(DOWN, aligned_edge = LEFT).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-4, 12, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-4, -2, 0, 2, 4, 6, 8, 10, 12],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line0 = Line(
            number_line0.n2p(1),
            number_line0.n2p(4.6),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label0 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line0, UP)
        self.play(Create(number_line0), Write(tex), run_time = 1.6)
        self.wait(0.8)
        self.play(Create(s_line0), Write(s_label0), run_time = 1.2)
        tex5 = MathChi(r"\text{考虑}S\text{所有上界构成的集合}").next_to(tex, DOWN)
        t_label0 = MathTex(
            r"T",
            font_size = 40,
            color = RED
        ).next_to(tex5, DOWN).shift(LEFT*2.6)
        tex6 = MathTex(
            r": = \left \{ a\in \mathbb{R}|\forall x\in S,\text{有} x\le a    \right \}",
            tex_template = chinese_template,
            font_size = 40,
            color = ORANGE
        ).next_to(t_label0, RIGHT)
        self.play(Write(tex5), run_time = 0.8)
        self.play(Write(t_label0), Write(tex6), run_time = 0.8)
        self.play(Wiggle(t_label0, scale_value = 1.3, rotation_angle = 6*DEGREES), run_time = 1.6)
        t_line0 = Line(
            number_line0.n2p(4.6),
            number_line0.n2p(12),
            stroke_width = 5.0,
            color = RED
        )
        self.play(
            ReplacementTransform(tex6, t_line0),
            FadeOut(tex5), 
            t_label0.animate.move_to(t_line0.get_center()).shift(UP*0.4),
            run_time = 2.2
        )
        tex0 = MathChi(r"\text{任取}b\in T,a\notin T,\text{则}a<b").next_to(tex, DOWN)

        # 接下来不断地取一段区间的中点，类似于二分法
        a_dot0 = Dot(number_line0.n2p(4), color = YELLOW_E, radius = 0.08)
        b_dot0 = Dot(number_line0.n2p(7), color = YELLOW_E, radius = 0.08)
        a0_label = MathTex(r"a", font_size = 30, color = YELLOW_A).next_to(a_dot0, DOWN)
        b0_label = MathTex(r"b", font_size = 30, color = YELLOW_A).next_to(b_dot0, DOWN)
        a0 = VGroup(a_dot0, a0_label)
        b0 = VGroup(b_dot0, b0_label)
        combine0 = VGroup(number_line0, s_line0, t_line0, s_label0, t_label0, a0, b0)
        number_line1 = NumberLine(
            x_range = [3.6, 5.6, 0.2],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [3.6, 4.0, 4.4, 4.8, 5.2, 5.6],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line1 = Line(
            number_line1.n2p(3.6),
            number_line1.n2p(4.6),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label1 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line1, UP)
        t_line1 = Line(
            number_line1.n2p(4.6),
            number_line1.n2p(5.6),
            stroke_width = 5.0,
            color = RED
        )
        t_label1 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line1, UP)
        a_dot1 = Dot(number_line1.n2p(4.5), color = YELLOW_E, radius = 0.08)
        b_dot1 = Dot(number_line1.n2p(4.85), color = YELLOW_E, radius = 0.08)
        a1_label = MathTex(r"a", font_size = 30, color = YELLOW_A).next_to(a_dot1, DOWN)
        b1_label = MathTex(r"b", font_size = 30, color = YELLOW_A).next_to(b_dot1, DOWN)
        a1 = VGroup(a_dot1, a1_label)
        b1 = VGroup(b_dot1, b1_label)
        combine1 = VGroup(number_line1, s_line1, t_line1, s_label1, t_label1, a1, b1)
        self.play(
            Write(tex0),
            Create(a0),
            Create(b0),
            run_time = 1.2
        )
        self.play(
            a0.animate.shift(LEFT*2),
            b0.animate.shift(LEFT*1.8),
            run_time = 0.8
        )
        self.play(
            a0.animate.shift(LEFT*3),
            b0.animate.shift(RIGHT*0.4),
            run_time = 0.8
        )
        self.play(
            a0.animate.shift(RIGHT*5.5),
            b0.animate.shift(LEFT*0.75),
            run_time = 0.8
        )
        self.play(ReplacementTransform(combine0, combine1), FadeOut(tex0), run_time = 2.2)
        mid_dot0 = Dot(number_line1.n2p(4.675), color = YELLOW_E, radius = 0.08)
        mid0_label = MathTex(r"\frac{a+b}{2}", font_size = 30, color = YELLOW_A).next_to(mid_dot0, DOWN)
        mid0 = VGroup(mid_dot0, mid0_label)
        tex0 = MathChi(
            r"\frac{a+b}{2}\in T,\text{那么令}\left [ a_{1},b_{1} \right ]=\left [ a,\frac{a+b}{2}  \right ] "
        ).next_to(tex, DOWN)
        self.play(Create(mid0), Write(tex0), run_time = 1.2)
        a_dot2 = Dot(number_line1.n2p(4.5), color = YELLOW_E, radius = 0.08)
        b_dot2 = Dot(number_line1.n2p(4.675), color = YELLOW_E, radius = 0.08)
        a2_label = MathTex(r"a_{1}", font_size = 30, color = YELLOW_A).next_to(a_dot2, DOWN)
        b2_label = MathTex(r"b_{1}", font_size = 30, color = YELLOW_A).next_to(b_dot2, DOWN)
        a2 = VGroup(a_dot2, a2_label)
        b2 = VGroup(b_dot2, b2_label)
        self.play(
            FadeOut(b1),
            ReplacementTransform(a1, a2), 
            ReplacementTransform(mid0, b2),
            run_time = 0.8
        )
        combine1.remove(a1)
        combine1.add(a2)
        combine1.remove(b1)
        combine1.add(b2)
        self.wait()
        number_line2 = NumberLine(
            x_range = [4.2, 5.0, 0.1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.2, 4.4, 4.6, 4.8, 5.0],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line2 = Line(
            number_line2.n2p(4.2),
            number_line2.n2p(4.6),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label2 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line2, UP)
        t_line2 = Line(
            number_line2.n2p(4.6),
            number_line2.n2p(5.0),
            stroke_width = 5.0,
            color = RED
        )
        t_label2 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line2, UP)
        a_dot3 = Dot(number_line2.n2p(4.5), color = YELLOW_E, radius = 0.08)
        b_dot3 = Dot(number_line2.n2p(4.675), color = YELLOW_E, radius = 0.08)
        a3_label = MathTex(r"a_{1}", font_size = 30, color = YELLOW_A).next_to(a_dot3, DOWN)
        b3_label = MathTex(r"b_{1}", font_size = 30, color = YELLOW_A).next_to(b_dot3, DOWN)
        a3 = VGroup(a_dot3, a3_label)
        b3 = VGroup(b_dot3, b3_label)
        combine2 = VGroup(number_line2, s_line2, t_line2, s_label2, t_label2, a3, b3)
        self.play(ReplacementTransform(combine1, combine2), FadeOut(tex0), run_time = 2.2)
        mid_dot1 = Dot(number_line2.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        mid1_label = MathTex(
            r"\frac{a_1+b_1}{2}", 
            font_size = 30, 
            color = YELLOW_A
        ).next_to(mid_dot1, DOWN)
        mid1 = VGroup(mid_dot1, mid1_label)
        tex0 = MathChi(
            r"\frac{a_1+b_1}{2}\notin T,\text{那么令}\left [ a_{2},b_{2} \right ]=\left [ \frac{a_1+b_1}{2},b_1  \right ] "
        ).next_to(tex, DOWN)
        self.play(Create(mid1), Write(tex0), run_time = 1.2)
        a_dot4 = Dot(number_line2.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot4 = Dot(number_line2.n2p(4.675), color = YELLOW_E, radius = 0.08)
        a4_label = MathTex(r"a_{2}", font_size = 30, color = YELLOW_A).next_to(a_dot4, DOWN)
        b4_label = MathTex(r"b_{2}", font_size = 30, color = YELLOW_A).next_to(b_dot4, DOWN)
        a4 = VGroup(a_dot4, a4_label)
        b4 = VGroup(b_dot4, b4_label)
        self.play(
            FadeOut(a3),
            ReplacementTransform(b3, b4), 
            ReplacementTransform(mid1, a4),
            run_time = 0.8
        )
        combine2.remove(a3)
        combine2.add(a4)
        combine2.remove(b3)
        combine2.add(b4)
        self.wait()
        number_line3 = NumberLine(
            x_range = [4.50, 4.80, 0.05],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.55, 4.65, 4.75],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line3 = Line(
            number_line3.n2p(4.50),
            number_line3.n2p(4.60),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label3 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line3, UP)
        t_line3 = Line(
            number_line3.n2p(4.60),
            number_line3.n2p(4.80),
            stroke_width = 5.0,
            color = RED
        )
        t_label3 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line3, UP)
        a_dot5 = Dot(number_line3.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot5 = Dot(number_line3.n2p(4.675), color = YELLOW_E, radius = 0.08)
        a5_label = MathTex(r"a_{2}", font_size = 30, color = YELLOW_A).next_to(a_dot5, DOWN)
        b5_label = MathTex(r"b_{2}", font_size = 30, color = YELLOW_A).next_to(b_dot5, DOWN)
        a5 = VGroup(a_dot5, a5_label)
        b5 = VGroup(b_dot5, b5_label)
        combine3 = VGroup(number_line3, s_line3, t_line3, s_label3, t_label3, a5, b5)
        self.play(ReplacementTransform(combine2, combine3), FadeOut(tex0), run_time = 2.2)
        mid_dot2 = Dot(number_line3.n2p(4.63125), color = YELLOW_E, radius = 0.08)
        mid2_label = MathTex(
            r"\frac{a_2+b_2}{2}", 
            font_size = 30, 
            color = YELLOW_A
        ).next_to(mid_dot2, DOWN)
        mid2 = VGroup(mid_dot2, mid2_label)
        tex0 = MathChi(r"\text{重复上述操作}\dots").next_to(tex, DOWN)
        self.play(Create(mid2), Write(tex0), run_time = 1.2)
        a_dot6 = Dot(number_line3.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot6 = Dot(number_line3.n2p(4.63125), color = YELLOW_E, radius = 0.08)
        a6_label = MathTex(r"a_{3}", font_size = 30, color = YELLOW_A).next_to(a_dot6, DOWN)
        b6_label = MathTex(r"b_{3}", font_size = 30, color = YELLOW_A).next_to(b_dot6, DOWN)
        a6 = VGroup(a_dot6, a6_label)
        b6 = VGroup(b_dot6, b6_label)
        self.play(
            FadeOut(b5),
            ReplacementTransform(a5, a6), 
            ReplacementTransform(mid2, b6),
            run_time = 0.8
        )
        combine3.remove(a5)
        combine3.add(a6)
        combine3.remove(b5)
        combine3.add(b6)
        self.wait(0.8)
        number_line4 = NumberLine(
            x_range = [4.550, 4.670, 0.025],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.550, 4.600, 4.650],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line4 = Line(
            number_line4.n2p(4.550),
            number_line4.n2p(4.600),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label4 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line4, UP)
        t_line4 = Line(
            number_line4.n2p(4.600),
            number_line4.n2p(4.670),
            stroke_width = 5.0,
            color = RED
        )
        t_label4 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line4, UP)
        a_dot7 = Dot(number_line4.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot7 = Dot(number_line4.n2p(4.63125), color = YELLOW_E, radius = 0.08)
        a7_label = MathTex(r"a_{3}", font_size = 30, color = YELLOW_A).next_to(a_dot7, DOWN)
        b7_label = MathTex(r"b_{3}", font_size = 30, color = YELLOW_A).next_to(b_dot7, DOWN)
        a7 = VGroup(a_dot7, a7_label)
        b7 = VGroup(b_dot7, b7_label)
        combine4 = VGroup(number_line4, s_line4, t_line4, s_label4, t_label4, a7, b7)
        self.play(ReplacementTransform(combine3, combine4), run_time = 0.8)
        mid_dot3 = Dot(number_line4.n2p(4.609375), color = YELLOW_E, radius = 0.08)
        mid3_label = MathTex(
            r"\frac{a_3+b_3}{2}", 
            font_size = 30, 
            color = YELLOW_A
        ).next_to(mid_dot3, DOWN)
        mid3 = VGroup(mid_dot3, mid3_label)
        self.play(Create(mid3), run_time = 0.6)
        a_dot8 = Dot(number_line4.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot8 = Dot(number_line4.n2p(4.609375), color = YELLOW_E, radius = 0.08)
        a8_label = MathTex(r"a_{4}", font_size = 30, color = YELLOW_A).next_to(a_dot8, DOWN)
        b8_label = MathTex(r"b_{4}", font_size = 30, color = YELLOW_A).next_to(b_dot8, DOWN)
        a8 = VGroup(a_dot8, a8_label)
        b8 = VGroup(b_dot8, b8_label)
        self.play(
            FadeOut(b7),
            ReplacementTransform(a7, a8), 
            ReplacementTransform(mid3, b8),
            run_time = 0.8
        )
        combine4.remove(a7)
        combine4.add(a8)
        combine4.remove(b7)
        combine4.add(b8)
        self.wait(0.8)
        number_line5 = NumberLine(
            x_range = [4.5750, 4.6500, 0.0125],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.5750, 4.6000, 4.6250, 4.6500],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line5 = Line(
            number_line5.n2p(4.5750),
            number_line5.n2p(4.6000),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label5 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line5, UP)
        t_line5 = Line(
            number_line5.n2p(4.6000),
            number_line5.n2p(4.6500),
            stroke_width = 5.0,
            color = RED
        )
        t_label5 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line5, UP)
        a_dot9 = Dot(number_line5.n2p(4.5875), color = YELLOW_E, radius = 0.08)
        b_dot9 = Dot(number_line5.n2p(4.609375), color = YELLOW_E, radius = 0.08)
        a9_label = MathTex(r"a_{4}", font_size = 30, color = YELLOW_A).next_to(a_dot9, DOWN)
        b9_label = MathTex(r"b_{4}", font_size = 30, color = YELLOW_A).next_to(b_dot9, DOWN)
        a9 = VGroup(a_dot9, a9_label)
        b9 = VGroup(b_dot9, b9_label)
        combine5 = VGroup(number_line5, s_line5, t_line5, s_label5, t_label5, a9, b9)
        self.play(ReplacementTransform(combine4, combine5), run_time = 0.8)
        mid_dot4 = Dot(number_line5.n2p(4.5984375), color = YELLOW_E, radius = 0.08)
        mid4_label = MathTex(
            r"\frac{a_4+b_4}{2}", 
            font_size = 30, 
            color = YELLOW_A
        ).next_to(mid_dot4, DOWN)
        mid4 = VGroup(mid_dot4, mid4_label)
        self.play(Create(mid4), run_time = 0.6)
        a_dot10 = Dot(number_line5.n2p(4.5984375), color = YELLOW_E, radius = 0.08)
        b_dot10 = Dot(number_line5.n2p(4.609375), color = YELLOW_E, radius = 0.08)
        a10_label = MathTex(r"a_{5}", font_size = 30, color = YELLOW_A).next_to(a_dot10, DOWN)
        b10_label = MathTex(r"b_{5}", font_size = 30, color = YELLOW_A).next_to(b_dot10, DOWN)
        a10 = VGroup(a_dot10, a10_label)
        b10 = VGroup(b_dot10, b10_label)
        self.play(
            FadeOut(a9),
            ReplacementTransform(mid4, a10), 
            ReplacementTransform(b9, b10),
            run_time = 0.8
        )
        combine5.remove(a9)
        combine5.add(a10)
        combine5.remove(b9)
        combine5.add(b10)
        self.wait(0.8)
        mid_dot5 = Dot(number_line5.n2p(4.60390625), color = YELLOW_E, radius = 0.08)
        mid5_label = MathTex(
            r"\frac{a_5+b_5}{2}", 
            font_size = 30, 
            color = YELLOW_A
        ).next_to(mid_dot5, DOWN)
        mid5 = VGroup(mid_dot5, mid5_label)
        self.play(Create(mid5), run_time = 0.6)
        a_dot11 = Dot(number_line5.n2p(4.5984375), color = YELLOW_E, radius = 0.08)
        b_dot11 = Dot(number_line5.n2p(4.60390625), color = YELLOW_E, radius = 0.08)
        a11_label = MathTex(r"a_{6}", font_size = 30, color = YELLOW_A).next_to(a_dot11, DOWN)
        b11_label = MathTex(r"b_{6}", font_size = 30, color = YELLOW_A).next_to(b_dot11, DOWN)
        a11 = VGroup(a_dot11, a11_label)
        b11 = VGroup(b_dot11, b11_label)
        self.play(
            FadeOut(b10),
            FadeOut(tex0),
            ReplacementTransform(a10, a11), 
            ReplacementTransform(mid5, b11),
            run_time = 0.8
        )
        combine5.remove(a10)
        combine5.add(a11)
        combine5.remove(b10)
        combine5.add(b11)
        self.wait(0.8)

        tex0 = MathChi(r"\text{于是，得到了一个闭区间列，使得：}")
        tex5 = MathChi(
            r"\forall n\in \mathbb{Z}^{+},a_{n}\notin T,b_{n}\in T,\text{且}b_n-a_n=\frac{b-a}{2^n}"
        )
        text = VGroup(tex0, tex5).arrange(DOWN, aligned_edge = LEFT).next_to(tex, DOWN).shift(RIGHT*1)
        interval0 = MathTex(r"[a,b]", font_size = 36, color = YELLOW_A)
        interval1 = MathTex(r"[a_1,b_1]", font_size = 36, color = YELLOW_B)
        interval2 = MathTex(r"[a_2,b_2]", font_size = 36, color = YELLOW_C)
        interval3 = MathTex(r"[a_3,b_3]", font_size = 36, color = YELLOW_D)
        interval4 = MathTex(r"\dots", font_size = 36, color = YELLOW_E)
        interval = VGroup(
            interval0, 
            interval1, 
            interval2, 
            interval3, 
            interval4
        ).arrange(DOWN).shift(LEFT*4.5+DOWN*0.6)
        self.play(ReplacementTransform(combine5, interval), Write(text), run_time = 1.6)
        self.wait(1.6)
        tex7 = MathTex(
            r"\text{由}\left( \mathbf{A}\right)\text{得：}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left( \mathbf{A}\right)": YELLOW_A}
        )
        tex8 = MathTex(
            r"\forall \epsilon >0,\exists N\in\mathbb{Z}^{+},\forall n>N:",
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"N": RED_B}
        )
        tex9 = MathTex(
            r"\left|b-a\right|<\epsilon\cdot 2^n",
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B}
        )
        text1 = VGroup(tex7, tex8, tex9).arrange(DOWN).next_to(tex, DOWN).shift(RIGHT*1)
        self.play(ReplacementTransform(text, text1), run_time = 1.6)
        self.wait(1.4)
        tex10 = MathTex(
            r"\frac{\left|b-a\right|}{2^n}<\epsilon",
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B}
        ).next_to(tex8, DOWN)
        self.play(ReplacementTransform(tex9, tex10), run_time = 1.2)
        self.play(Wiggle(tex10, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.2)
        self.wait(0.4)
        self.play(FadeOut(tex7), FadeOut(tex8), run_time = 0.7)
        tex7 = MathTex(
            r"\lim_{n \to \infty}\frac{b-a}{2^n} =0",
            font_size = 40,
            color = BLUE_B
        ).move_to(tex8.get_center())
        self.play(ReplacementTransform(tex10, tex7), run_time = 0.7)
        tex11 = MathTex(
            r"\lim_{n \to \infty}\left(b_n-a_n\right)=",
            font_size = 40,
            color = BLUE_B
        ).move_to(tex8.get_center()).shift(LEFT*1.2+DOWN*0.1)
        self.play(Write(tex11), tex7.animate.shift(RIGHT*1.6), run_time = 1.2)
        text2 = VGroup(tex7, tex11)
        rect0 = Rectangle(
            height = 1.1,
            width = 5.9,
            stroke_width = 4.0,
            color = YELLOW
        ).move_to(text2.get_center())
        self.wait(0.4)
        self.play(Create(rect0), run_time = 0.6)
        self.play(Uncreate(rect0), run_time = 0.6)
        self.wait(0.6)
        tex8 = MathChi(r"\text{这就满足了闭区间套的要求}").shift(RIGHT*1+DOWN*1)
        tex12 = MathTex(
            r"\text{于是存在唯一的实数}\xi\text{满足}\forall n\in \mathbb{Z}^{+}\left(a_{n}\le \xi\le b_{n}\right)",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\xi": PURPLE_B}
        ).next_to(tex, DOWN)
        self.play(Write(tex8), run_time = 0.8)
        self.wait()
        number_line5 = NumberLine(
            x_range = [4.5750, 4.6500, 0.0125],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.5750, 4.6000, 4.6250, 4.6500],
            font_size = 28
        ).shift(DOWN * 1.5)
        s_line5 = Line(
            number_line5.n2p(4.5750),
            number_line5.n2p(4.6000),
            stroke_width = 5.0,
            color = YELLOW_C
        )
        s_label5 = MathTex(r"S", font_size = 40, color = YELLOW_C).next_to(s_line5, UP)
        t_line5 = Line(
            number_line5.n2p(4.6000),
            number_line5.n2p(4.6500),
            stroke_width = 5.0,
            color = RED
        )
        t_label5 = MathTex(r"T", font_size = 40, color = RED).next_to(t_line5, UP)
        combine5 = VGroup(number_line5, s_line5, t_line5, s_label5, t_label5)
        self.play(
            ReplacementTransform(interval, combine5), 
            ReplacementTransform(tex8, tex12),
            FadeOut(text2), 
            run_time = 1.6
        )
        dot_xi = Dot(number_line5.n2p(4.6), color = PURPLE_B, radius = 0.08)
        xi_label = MathTex(r"\xi", font_size = 40, color = PURPLE_B).next_to(dot_xi, UP)
        xi_tex = MathTex(
            r"\lim_{n \to \infty}a_n=\lim_{n \to \infty}b_n=\xi", 
            font_size = 40,
            color = PURPLE_B
        ).next_to(dot_xi, UP).shift(UP*0.7)
        xi = VGroup(dot_xi, xi_label)
        self.play(Create(xi), Write(xi_tex), run_time = 1.2)
        self.wait(1.6)
        self.play(FadeOut(tex12), FadeOut(xi_tex), run_time = 0.8)
        tex7 = MathTex(
            r"\text{若}\xi\notin T,\text{那么}\exists x\in S,\text{使得} x>\xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\xi": PURPLE_B}
        ).next_to(tex, DOWN)
        x_dot = Dot(number_line5.n2p(4.596), color = BLUE_B, radius = 0.08)
        x_label = MathTex(r"x", font_size = 30).next_to(x_dot, UP)
        x = VGroup(x_dot, x_label)
        self.play(Write(tex7), xi.animate.shift(LEFT*2), Create(x), run_time = 1.2)
        delta_brace = BraceBetweenPoints(
            number_line5.n2p(4.590625), 
            number_line5.n2p(4.596), 
            DOWN, 
            buff = 0.2
        )
        delta_label = MathTex(r"\epsilon", color = GREEN_B, font_size = 32).next_to(delta_brace, DOWN)
        delta = VGroup(delta_brace, delta_label)
        tex8 = MathTex(
            r"\text{令}\epsilon= x - \xi >0",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\xi": PURPLE_B}
        ).next_to(tex7, DOWN)
        self.play(Write(tex8), Create(delta_label), GrowFromCenter(delta_brace), run_time = 0.8)
        self.wait(0.9)
        self.play(Uncreate(delta), run_time = 0.8)
        tex11 = MathTex(
            r"\exists N\in \mathbb{Z}^{+},\forall n>N:b_n- \xi < \epsilon =x- \xi",
            font_size = 40,
            tex_to_color_map = {r"\xi": PURPLE_B, r"\epsilon": GREEN_B}
        ).next_to(tex8, DOWN)
        bn_dot = Dot(number_line5.n2p(4.605), color = YELLOW_A, radius = 0.08)
        bn_label = MathTex(r"b_n", font_size = 30).next_to(bn_dot, UP)
        bn = VGroup(bn_dot, bn_label)
        self.play(Create(bn), run_time = 0.6)
        self.play(AnimationGroup(Write(tex11), bn.animate.shift(LEFT*2.7), lag_ratio = 1.0/2.0))
        text2 = VGroup(tex7, tex8, tex11)
        tex12 = MathChi(r"\text{这就推出了}b_n<x,\text{即}b_n\notin T").move_to(tex8.get_center())
        self.wait(0.9)
        self.play(AnimationGroup(FadeOut(text2), Write(tex12), lag_ratio = 1.0/2.0))
        tex7 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex12)
        self.play(Write(tex7), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex7, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        self.play(
            FadeOut(tex12), 
            FadeOut(tex7),
            Uncreate(x), 
            Uncreate(bn), 
            xi.animate.shift(RIGHT*2),
            run_time = 1.6
        )
        tex7 = MathTex(
            r"\text{若}\exists \eta \in T,\text{使得}\eta <\xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\eta": BLUE_B, r"\xi": PURPLE_B} 
        ).next_to(tex, DOWN)
        eta_dot = Dot(number_line5.n2p(4.604), color = BLUE_B, radius = 0.08)
        eta_label = MathTex(r"\eta", font_size = 30, color = BLUE_B).next_to(eta_dot, UP)
        eta = VGroup(eta_dot, eta_label)
        self.wait(0.6)
        self.play(xi.animate.shift(RIGHT*2), Write(tex7), Create(eta), run_time = 1.2)
        delta_brace = BraceBetweenPoints(
            number_line5.n2p(4.604), 
            number_line5.n2p(4.609375), 
            DOWN, 
            buff = 0.2
        )
        delta_label = MathTex(r"\epsilon", color = GREEN_B, font_size = 32).next_to(delta_brace, DOWN)
        delta = VGroup(delta_brace, delta_label)
        tex8 = MathTex(
            r"\text{令}\epsilon= \xi - \eta >0",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\xi": PURPLE_B, r"\eta": BLUE_B}
        ).next_to(tex7, DOWN)
        self.play(Write(tex8), Create(delta_label), GrowFromCenter(delta_brace), run_time = 0.8)
        self.wait(0.9)
        self.play(Uncreate(delta), run_time = 0.8)
        tex11 = MathTex(
            r"\exists N\in \mathbb{Z}^{+},\forall n>N:\xi - a_n < \epsilon = \xi - \eta",
            font_size = 40,
            tex_to_color_map = {r"\xi": PURPLE_B, r"\epsilon": GREEN_B, r"\eta": BLUE_B}
        ).next_to(tex8, DOWN)
        an_dot = Dot(number_line5.n2p(4.595), color = YELLOW_A, radius = 0.08)
        an_label = MathTex(r"a_n", font_size = 30).next_to(an_dot, UP)
        an = VGroup(an_dot, an_label)
        self.play(Create(an), run_time = 0.6)
        self.play(AnimationGroup(Write(tex11), an.animate.shift(RIGHT*2.7), lag_ratio = 1.0/2.0))
        text2 = VGroup(tex7, tex8, tex11)
        tex12 = MathTex(
            r"\text{这就推出了}a_n> \eta,\text{即}a_n\in T",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\eta": BLUE_B}
        ).move_to(tex8.get_center())
        self.wait(0.9)
        self.play(AnimationGroup(FadeOut(text2), Write(tex12), lag_ratio = 1.0/2.0))
        tex7 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex12)
        self.play(Write(tex7), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex7, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        self.play(
            FadeOut(tex12), 
            FadeOut(tex7),
            Uncreate(eta), 
            Uncreate(an), 
            xi.animate.shift(LEFT*2),
            run_time = 1.6
        )
        tex7 = MathTex(
            r"\text{所以}\xi = \min T = \sup S ",
            tex_template = chinese_template, 
            font_size = 40, 
            tex_to_color_map = {r"\xi": PURPLE_B, r"T": RED, r"S": YELLOW_C}
        ).next_to(tex, DOWN)
        self.play(Write(tex7), run_time = 1.2)
        combine5.add(xi)
        combine5.add(tex4)
        combine5.add(line0)
        combine5.add(tex2)
        self.play(
            AnimationGroup(
                combine5.animate.set_opacity(0.15), 
                tex3.animate.shift(DOWN*2.4+RIGHT*0.5).scale(1.2), 
                lag_ratio = 1.0/2.0
            )
        )
        tex11 = MathTex(
            r"\left(\mathbf{L}\right)",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex3, RIGHT, buff = 5.5)
        tex12 = MathTex(
            r"\left(\mathbf{L}\right)\Rightarrow\text{单调有界定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        self.play(Write(tex11), run_time = 1.2)
        text2 = VGroup(tex3, tex11)
        combine6 = VGroup(number_line5, s_line5, t_line5, s_label5, t_label5, xi, tex4, tex2, tex7)
        self.wait(0.8)
        self.play(
            AnimationGroup(
                FadeOut(combine6), 
                ReplacementTransform(text2, tex12), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# 确界存在定理推导单调有界定理
class MonotoneConvergenceTheorem(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{L}\right)\Rightarrow\text{单调有界定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathChi(r"\underline{\text{单调有界定理}}")
        tex2 = MathChi(
            r"\text{若一个数列单调递增且有上界，那么该数列收敛}"
        )
        tex = VGroup(tex1, tex2).arrange(DOWN, aligned_edge = LEFT).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-2, 10, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-2, 0, 2, 4, 6, 8, 10],
            font_size = 28
        ).shift(DOWN * 1.5)
        self.play(Write(tex), Create(number_line0), run_time = 1.6)
        tex3 = MathTex(
            r"\text{设}\left\{x_n\right\}\text{有上界，由}\left(\mathbf{L}\right)\text{得：}\left\{x_n\right\}\text{有上确界}\beta",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{L}\right)": YELLOW_A, r"\beta": ORANGE}
        ).next_to(tex, DOWN)
        numbers = [1.3, 2.1, 2.9, 3.5, 3.75]
        colors = [YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E]
        ds = list(str.ascii_uppercase)
        lbs = list(str.ascii_uppercase)
        dots = VGroup()
        labels = VGroup()
        for i in range(5):
            ds[i] = Dot(number_line0.n2p(numbers[i]), color = colors[i], radius = 0.08)
            lbs[i]= MathTex(f"x_{i}", color = colors[i], font_size = 30).next_to(ds[i], DOWN)
            self.play(Create(ds[i]), Create(lbs[i]), run_time = 0.8)
            self.wait(0.3)
            dots.add(ds[i])
            labels.add(lbs[i])
        b_dot = Dot(number_line0.n2p(5.8), color = YELLOW_A, radius = 0.08)
        b_label = MathTex(r"b", font_size = 30, color = YELLOW_A).next_to(b_dot, UP)
        b = VGroup(b_dot, b_label)
        tex4 = MathTex(r"\dots", font_size = 36).next_to(number_line0.n2p(3.8), DOWN, buff = 0.7)
        self.play(Create(tex4), run_time = 0.9)
        beta_dot = Dot(number_line0.n2p(4), color = ORANGE, radius = 0.08)
        beta_label = MathTex(
            r"\beta = \sup\left\{x_n\right\}",
            font_size = 30,
            color = ORANGE
        ).next_to(beta_dot, UP)
        beta1_label = MathTex(
            r"\beta",
            font_size = 30,
            color = ORANGE
        ).next_to(beta_dot, UP)
        beta = VGroup(beta_dot, beta_label)
        beta1 = VGroup(beta_dot, beta1_label)
        self.play(AnimationGroup(Write(tex3), Create(b), lag_ratio = 1.6/2.4))
        self.play(ReplacementTransform(b, beta), run_time = 1.2)
        self.wait(0.4)
        self.play(FadeOut(tex4), ReplacementTransform(beta, beta1), run_time = 0.6)
        tex4 = MathTex(
            r"\forall \epsilon >0,\exists N\in\mathbb{Z}^{+}:\beta-\epsilon<x_N\le \beta\text{(上确界定义)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\beta": ORANGE, r"x_N": YELLOW_E}
        ).next_to(tex3, DOWN)
        combine0 = VGroup(number_line0, dots, labels, beta1)
        number_line1 = NumberLine(
            x_range = [3.5, 4.4, 0.1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [3.6, 3.8, 4.0, 4.2, 4.4],
            font_size = 28
        ).shift(DOWN * 1.5)
        beta2_dot = Dot(number_line1.n2p(4), color = ORANGE, radius = 0.08)
        beta2_label = MathTex(
            r"\beta",
            font_size = 30,
            color = ORANGE
        ).next_to(beta2_dot, UP)
        beta2 = VGroup(beta2_dot, beta2_label)
        ds1 = list(str.ascii_uppercase)
        lbs1 = list(str.ascii_uppercase)
        dots1 = VGroup()
        labels1 = VGroup()
        for i in range(5):
            ds1[i] = Dot(number_line1.n2p(numbers[i]), color = colors[i], radius = 0.08)
            lbs1[i]= MathTex(f"x_{i}", color = colors[i], font_size = 30).next_to(ds1[i], DOWN)
            dots1.add(ds1[i])
            labels1.add(lbs1[i])
        combine1 = VGroup(number_line1, dots1, labels1, beta2)
        self.play(ReplacementTransform(combine0, combine1), run_time = 2.2)
        be_dot = Dot(number_line1.n2p(3.85), color = YELLOW_A, radius = 0.08)
        be_label = MathTex(
            r"\beta - \epsilon",
            font_size = 30,
            tex_to_color_map = {r"\beta": ORANGE, r"\epsilon": GREEN_B}
        ).next_to(be_dot, UP)
        be = VGroup(be_dot, be_label)
        xn_dot = Dot(number_line1.n2p(3.88), color = YELLOW_E, radius = 0.08)
        xn_label = MathTex(
            r"x_N",
            font_size = 30,
            color = YELLOW_E
        ).next_to(xn_dot, DOWN)
        xn = VGroup(xn_dot, xn_label)
        delta_brace = BraceBetweenPoints(
            number_line1.n2p(3.85), 
            number_line1.n2p(4), 
            DOWN, 
            buff = 0.2
        )
        delta_label = MathTex(r"\epsilon", color = GREEN_B, font_size = 32).next_to(delta_brace, DOWN)
        delta = VGroup(delta_brace, delta_label)
        self.play(Create(be), Create(xn), Write(tex4), run_time = 1.2)
        self.play(GrowFromCenter(delta), run_time = 0.8)
        self.wait(0.9)
        self.play(Uncreate(delta), run_time = 0.8)
        tex5 = MathTex(
            r"\forall \epsilon >0,\exists N\in\mathbb{Z}^{+},\forall n>N:\beta-\epsilon<x_N\le x_n \le \beta\text{(单调递增)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"x_N\le x_n": YELLOW_E, r"\beta": ORANGE}
        ).next_to(tex3, DOWN)
        self.play(FadeOut(tex3), ReplacementTransform(tex4, tex5), run_time = 1.6)
        xn1_dot = Dot(number_line1.n2p(3.92), color = YELLOW_E, radius = 0.08)
        xn1_label = MathTex(
            r"x_{N+1}",
            font_size = 30,
            color = YELLOW_E
        ).next_to(xn1_dot, DOWN)
        xn1 = VGroup(xn1_dot, xn1_label)
        xn2_dot = Dot(number_line1.n2p(3.95), color = YELLOW_E, radius = 0.08)
        xn2_label = MathTex(
            r"x_{N+2}",
            font_size = 30,
            color = YELLOW_E
        ).next_to(xn2_dot, UP)
        xn2 = VGroup(xn2_dot, xn2_label)
        xn3_dot = Dot(number_line1.n2p(3.98), color = YELLOW_E, radius = 0.08)
        xn3_label = MathTex(
            r"x_{N+3}",
            font_size = 30,
            color = YELLOW_E
        ).next_to(xn3_dot, DOWN)
        xn3 = VGroup(xn3_dot, xn3_label)
        self.play(Create(xn1), run_time = 0.8)
        self.wait(0.2)
        self.play(Create(xn2), run_time = 0.8)
        self.wait(0.2)
        self.play(Create(xn3), run_time = 0.8)
        self.wait(0.2)
        tex3 = MathTex(r"\dots", font_size = 36).next_to(number_line1.n2p(3.99), DOWN, buff = 0.7)
        self.play(Create(tex3), run_time = 0.9)
        tex4 = MathTex(
            r"\text{于是得到}\lim_{n \to \infty}x_n=\beta=\sup\left\{x_n\right\}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {
                r"\lim_{n \to \infty}x_n=": YELLOW_E, 
                r"\beta=\sup\left\{x_n\right\}": ORANGE
            }
        ).next_to(tex, DOWN)
        self.play(Write(tex4), FadeOut(tex5), run_time = 1.6)
        combine0 = VGroup(number_line1, beta2, tex3, be, xn, xn1, xn2, xn3, line0, tex0, tex2, dots1, labels1)
        self.play(
            AnimationGroup(
                combine0.animate.set_opacity(0.15),
                tex1.animate.shift(DOWN*2.4).scale(1.2),
                lag_ratio = 1.0/2.0
            )
        )
        tex5 = MathTex(
            r"\left(\mathbf{M}\right)",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 5.5)
        text = VGroup(tex1, tex5)
        tex6 = MathTex(
            r"\left(\mathbf{M}\right)\Rightarrow\left(\mathbf{A}\right)+\left(\mathbf{N}\right)",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        self.play(Write(tex5), run_time = 1.2)
        self.wait(0.8)
        combine1 = VGroup(number_line1, beta2, tex3, be, xn, xn1, xn2, xn3, tex0, tex2, tex4, dots1, labels1)
        self.play(
            AnimationGroup(
                FadeOut(combine1), 
                ReplacementTransform(text, tex6), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# 单调有界定理推导A+N
class AAplusNIA(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{M}\right)\Rightarrow\left(\mathbf{A}\right)+\left(\mathbf{N}\right)",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathTex(
            r"\underline{\text{闭区间套公理}\left(\mathbf{N}\right)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{N}\right)": YELLOW_A}
        ).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-2, 10, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-2, 0, 2, 4, 6, 8, 10],
            font_size = 28
        ).shift(DOWN * 1.5)
        self.play(Write(tex1), Create(number_line0), run_time = 1.6)
        tex2 = MathTex(
            r"\forall n\in\mathbb{Z}^{+},a_{n}\le a_{n+1}<b_{n+1}\le b_{n}\text{成立}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"a_{n}\le a_{n+1}": BLUE, r"b_{n+1}\le b_{n}": RED}
        ).next_to(tex1, DOWN)
        self.play(Write(tex2), run_time = 1.2)
        numbers1 = [1.7, 2.8, 3.4, 3.8, 4.25]
        numbers2 = [7.2, 6.2, 5.4, 5.0, 4.75]
        colors1 = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        colors2 = [RED_A, RED_B, RED_C, RED_D, RED_E]
        ds = list(str.ascii_uppercase)
        lbs = list(str.ascii_uppercase)
        dots = VGroup()
        labels = VGroup()
        tex3 = MathTex(r"\dots", font_size = 36).next_to(number_line0.n2p(4.5), DOWN, buff = 0.7)
        for i in range(5):
            ds[i] = Dot(number_line0.n2p(numbers1[i]), color = colors1[i], radius = 0.08)
            lbs[i] = MathTex(f"a_{i}", color = colors1[i], font_size = 30).next_to(ds[i], DOWN)
            ds[i+6] = Dot(number_line0.n2p(numbers2[i]), color = colors2[i], radius = 0.08)
            lbs[i+6] = MathTex(f"b_{i}", color = colors2[i], font_size = 30).next_to(ds[i+6], DOWN)
            self.play(Create(ds[i]), Create(lbs[i]), Create(ds[i+6]), Create(lbs[i+6]), run_time = 0.8)
            self.wait(0.3)
            dots.add(ds[i])
            labels.add(lbs[i])
            dots.add(ds[i+6])
            labels.add(lbs[i+6])
        combine0 = VGroup(number_line0, dots, labels)
        self.play(Create(tex3), run_time = 0.9)
        self.wait(0.6)
        self.play(FadeOut(tex3), run_time = 0.7)
        number_line1 = NumberLine(
            x_range = [3.5, 5.1, 0.2],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [3.5, 3.9, 4.3, 4.7, 5.1],
            font_size = 28
        ).shift(DOWN * 1.5)
        ds1 = list(str.ascii_uppercase)
        lbs1 = list(str.ascii_uppercase)
        dots1 = VGroup()
        labels1 = VGroup()
        for i in range(5):
            ds1[i] = Dot(number_line1.n2p(numbers1[i]), color = colors1[i], radius = 0.08)
            lbs1[i]= MathTex(f"a_{i}", color = colors1[i], font_size = 30).next_to(ds1[i], DOWN)
            ds1[i+6] = Dot(number_line1.n2p(numbers2[i]), color = colors2[i], radius = 0.08)
            lbs1[i+6]= MathTex(f"b_{i}", color = colors2[i], font_size = 30).next_to(ds1[i+6], DOWN)
            dots1.add(ds1[i])
            labels1.add(lbs1[i])
            dots1.add(ds1[i+6])
            labels1.add(lbs1[i+6])
        combine1 = VGroup(number_line1, dots1, labels1)
        self.play(ReplacementTransform(combine0, combine1), run_time = 2.2)
        tex3 = MathTex(
            r"\dots", 
            font_size = 36, 
            color = BLUE
        ).next_to(number_line1.n2p(4.35), DOWN, buff = 0.7)
        tex4 = MathTex(
            r"\dots", 
            font_size = 36,
            color = RED
        ).next_to(number_line1.n2p(4.70), DOWN, buff = 0.7)
        self.play(Create(tex3), Create(tex4), run_time = 0.9)
        self.wait(0.4)
        tex5 = MathTex(
            r"\text{由}\left(\mathbf{M}\right)\text{得}\lim_{n \to \infty}a_{n}=\alpha=\sup\left\{a_n\right\},\lim_{n \to \infty}b_{n}=\beta=\inf\left\{b_n\right\}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {
                r"\left(\mathbf{M}\right)": YELLOW_A,
                r"\lim_{n \to \infty}a_{n}=\alpha=\sup\left\{a_n\right\}": BLUE,
                r"\lim_{n \to \infty}b_{n}=\beta=\inf\left\{b_n\right\}": RED
            }
        ).next_to(tex2, DOWN)
        alpha_dot = Dot(number_line1.n2p(4.40), color = BLUE, radius = 0.08)
        alpha_label = MathTex(
            r"\alpha = \sup\left\{a_n\right\}",
            font_size = 30,
            color = BLUE
        ).next_to(alpha_dot, UP)
        beta_dot = Dot(number_line1.n2p(4.65), color = RED, radius = 0.08)
        beta_label = MathTex(
            r"\beta = \inf\left\{b_n\right\}",
            font_size = 30,
            color = RED
        ).next_to(beta_dot, UP)
        alpha = VGroup(alpha_dot, alpha_label)
        beta = VGroup(beta_dot, beta_label)
        self.play(Write(tex5), Create(alpha), Create(beta), run_time = 1.6)
        self.wait(1.6)
        tex6 = MathTex(
            r"\text{而同时}\lim_{n \to \infty}(b_n-a_n) = \beta-\alpha = 0",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"b_n": RED, r"a_n": BLUE, r"\beta": RED, r"\alpha": BLUE}
        ).next_to(tex2, DOWN)
        albe = VGroup(alpha, beta)
        xi_dot = Dot(number_line1.n2p(4.5), color = PURPLE_B, radius = 0.08)
        xi_label = MathTex(r"\xi", font_size = 40, color = PURPLE_B).next_to(xi_dot, UP)
        xi = VGroup(xi_dot, xi_label)
        self.play(ReplacementTransform(tex5, tex6), run_time = 1.2)
        tex5 = MathTex(
            r"\text{这就得到了}\beta = \alpha = \xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\beta": RED, r"\alpha": BLUE, r"\xi": PURPLE_B}
        ).next_to(tex6, DOWN)
        self.play(
            AnimationGroup(Write(tex5), ReplacementTransform(albe, xi), lag_ratio = 1.2/2.5)
        )
        self.play(Wiggle(xi_label, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.2)
        self.play(FadeOut(tex5), FadeOut(tex6), run_time = 0.8)
        tex5 = MathTex(
            r"\text{显然}\forall n\in\mathbb{Z}^{+}:a_n\le\xi\le b_n",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"a_n": BLUE, r"\xi": PURPLE_B, r"b_n": RED}
        ).next_to(tex2, DOWN)
        self.play(Write(tex5), run_time = 1.2)
        tex6 = MathTex(
            r"\text{若}\exists \zeta\ne\xi(\text{不妨设}\zeta>\xi),\text{满足}\forall n\in\mathbb{Z}^{+}:a_n\le\zeta\le b_n",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\zeta": PURPLE_A, r"\xi": PURPLE_B, r"a_n": BLUE, r"b_n": RED}
        ).next_to(tex5, DOWN)
        zeta_dot = Dot(number_line1.n2p(4.64), color = PURPLE_A, radius = 0.08)
        zeta_label = MathTex(r"\zeta", font_size = 40, color = PURPLE_A).next_to(zeta_dot, UP)
        zeta = VGroup(zeta_dot, zeta_label)
        self.play(AnimationGroup(Write(tex6), Create(zeta), lag_ratio = 1.2/2.4))
        self.wait(0.4)
        self.play(
            AnimationGroup(FadeOut(tex5), tex6.animate.move_to(tex5.get_center()), lag_ratio = 1.0/2.0)
        )
        tex5 = MathTex(
            r"\text{令}\epsilon = \zeta - \xi >0",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\zeta": PURPLE_A, r"\xi": PURPLE_B}
        ).next_to(tex6, DOWN)
        delta_brace = BraceBetweenPoints(
            number_line1.n2p(4.5), 
            number_line1.n2p(4.64), 
            DOWN, 
            buff = 0.2
        )
        delta_label = MathTex(r"\epsilon", color = GREEN_B, font_size = 32).next_to(delta_brace, DOWN)
        delta = VGroup(delta_brace, delta_label)
        self.play(Write(tex5), Create(delta_label), GrowFromCenter(delta_brace), run_time = 0.8)
        self.wait(0.9)
        self.play(Uncreate(delta), run_time = 0.8)
        tex7 = MathTex(
            r"\text{则}\exists N\in\mathbb{Z}^{+},\forall n>N:b_n-\xi<\epsilon=\zeta-\xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"b_n": RED, r"\zeta": PURPLE_A, r"\xi": PURPLE_B}
        ).next_to(tex5, DOWN)
        text0 = VGroup(tex5, tex6)
        bn_dot = Dot(number_line1.n2p(4.6), color = RED, radius = 0.08)
        bn_label = MathTex(r"b_n", font_size = 30, color = RED).next_to(bn_dot, UP)
        bn = VGroup(bn_dot, bn_label)
        self.play(Write(tex7), Create(bn), run_time = 1.2)
        self.wait(0.9)
        self.play(
            AnimationGroup(FadeOut(text0), tex7.animate.move_to(tex6.get_center()), lag_ratio = 1.0/2.0)
        )
        tex5 = MathTex(
            r"\text{这就推出了}b_n<\zeta",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"b_n": RED, r"\zeta": PURPLE_A}
        ).next_to(tex7, DOWN)
        tex6 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex5, RIGHT)
        self.play(Write(tex5), run_time = 0.9)
        self.play(Write(tex6), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex6, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        text0 =VGroup(tex6, tex7)
        tex8 = MathTex(
            r"\text{于是}\zeta=\xi,\text{即}\xi\text{有唯一性}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\zeta": PURPLE_A, r"\xi": PURPLE_B}
        ).next_to(tex2, DOWN)
        self.play(AnimationGroup(FadeOut(text0), ReplacementTransform(tex5, tex8), lag_ratio = 1.0/2.0))
        self.play(zeta.animate.shift(LEFT*1.4), run_time = 0.6)
        self.wait(0.4)
        combine2 = VGroup(number_line1, zeta, xi, bn, dots1, labels1, tex2, tex3, tex4)
        self.play(
            AnimationGroup(
                combine2.animate.set_opacity(0.15), 
                tex1.animate.shift(DOWN*2.4+LEFT*3).scale(1.2),
                lag_ratio = 1.0/2.0
            )
        )
        tex5 = MathTex(
            r"\text{得证!}",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 4.5)
        self.play(Write(tex5), run_time = 1.2)
        combine2.add(tex5)
        combine2.add(tex1)
        combine2.add(tex8)
        self.wait(0.8)
        self.play(FadeOut(combine2), run_time = 1.2)
        self.remove(tex1)
        self.remove(tex5)
        self.remove(tex8)
        tex9 = MathTex(
            r"\underline{\text{Archimedes公理}\left(\mathbf{A}\right)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{A}\right)": YELLOW_A}
        ).next_to(line0, DOWN)
        self.play(Write(tex9), run_time = 1.3)
        tex10 = MathTex(
            r"\text{只需用}\left(\mathbf{M}\right)\text{证明}\lim_{n \to \infty}\frac{1}{n}\text{存在即可(证明和思考留给观众)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{M}\right)": YELLOW_A}
        )
        self.wait(0.4)
        self.play(Write(tex10), run_time = 1.6)
        self.wait(3.5)
        self.play(FadeOut(tex9), FadeOut(tex10), run_time = 1.6)
        tex9 = MathTex(
            r"\left(\mathbf{A}\right)+\left(\mathbf{N}\right)\Rightarrow\text{Heine-Borel定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        self.play(ReplacementTransform(tex0, tex9), run_time = 1.3)
        self.wait(0.4)

# A+N推导Heine-Borel定理
class HeineBorelTheorem(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{A}\right)+\left(\mathbf{N}\right)\Rightarrow\text{Heine-Borel定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathChi(r"\underline{\text{Heine-Borel定理}}")
        tex2 = MathChi(
            r"\text{一个闭区间}[a,b]\text{的任意开覆盖}\mathcal{F}\text{都有有限的子覆盖}"
        )
        tex = VGroup(tex1, tex2).arrange(DOWN, aligned_edge = LEFT).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-2, 10, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-2, 0, 2, 4, 6, 8, 10],
            font_size = 28
        ).shift(DOWN * 1.5)
        line1 = Line(number_line0.n2p(1.5), number_line0.n2p(5.5), stroke_width = 5.0, color = YELLOW_A)
        a_dot = Dot(number_line0.n2p(1.5), color = YELLOW_E, radius = 0.08)
        a_label = MathTex(r"a", color = YELLOW_A, font_size = 30).next_to(a_dot, DOWN)
        a = VGroup(a_dot, a_label)
        b_dot = Dot(number_line0.n2p(5.5), color = YELLOW_E, radius = 0.08)
        b_label = MathTex(r"b", color = YELLOW_A, font_size = 30).next_to(b_dot, DOWN)
        b = VGroup(b_dot, b_label)
        self.play(
            Write(tex), Create(number_line0), GrowFromCenter(line1), Create(a), Create(b), run_time = 1.6
        )
        radiuses = [0.67, 0.8, 0.3, 0.5, 0.72, 0.38, 0.25, 0.5, 0.6, 0.45]
        positions = [1.9, 2.3, 2.5, 2.8, 3.5, 3.7, 4.05, 4.35, 4.8, 5.2]
        yuans = list(str.ascii_uppercase)
        circles = VGroup()
        unit_length = number_line0.unit_size
        for i in range(10):
            yuans[i] = Circle(
                radius = radiuses[i]*unit_length, 
                fill_color = BLUE_B, 
                fill_opacity = 0.25, 
                stroke_width = 0
            ).move_to(number_line0.n2p(positions[i]))
            circles.add(yuans[i])
        self.play(Create(circles), run_time = 3.2)
        f_label = MathTex(r"\mathcal{F}", font_size = 48).next_to(number_line0.n2p(3.5), UP).shift(UP*1.1)
        self.play(Write(f_label), run_time = 0.8)
        self.play(Wiggle(f_label, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.2)
        self.wait(0.4)
        self.play(Uncreate(f_label), run_time = 0.8)
        tex3 = MathChi(
            r"\text{若}[a,b]\text{不能被}\mathcal{F}\text{中有限个开区间覆盖}"
        ).next_to(tex, DOWN)
        mid_dot = Dot(number_line0.n2p(3.5), color = YELLOW_E, radius = 0.08)
        mid_label = MathTex(r"\frac{a+b}{2}", color = YELLOW_A, font_size = 30).next_to(mid_dot, DOWN)
        mid = VGroup(mid_dot, mid_label)
        self.play(Write(tex3), run_time = 1.2)
        tex4 = MathChi(
            r"\text{那么}[a,\frac{a+b}{2}],[\frac{a+b}{2},b]\text{中至少有一个不能被}\mathcal{F}\text{中有限个开区间覆盖}"
        ).next_to(tex3, DOWN)
        tex5 = MathChi(r"\text{将其设为}[a_1,b_1]").next_to(tex3, DOWN)
        self.play(Write(tex4), Create(mid), run_time = 1.2)
        self.wait(2.5)
        a1_dot = Dot(number_line0.n2p(3.5), color = YELLOW_E, radius = 0.08)
        a1_label = MathTex(r"a_1", color = YELLOW_A, font_size = 30).next_to(a1_dot, DOWN)
        a1 = VGroup(a1_dot, a1_label)
        b1_dot = Dot(number_line0.n2p(5.5), color = YELLOW_E, radius = 0.08)
        b1_label = MathTex(r"b_1", color = YELLOW_A, font_size = 30).next_to(b1_dot, DOWN)
        b1 = VGroup(b1_dot, b1_label)
        self.play(
            ReplacementTransform(tex4, tex5), 
            FadeOut(a),
            ReplacementTransform(mid, a1),
            ReplacementTransform(b, b1),
            run_time = 1.4
        )
        self.wait(0.8)
        tex4 = MathChi(
            r"\text{那么}[a_1,\frac{a_1+b_1}{2}],[\frac{a_1+b_1}{2},b_1]\text{中也至少有一个不能被}\mathcal{F}\text{中有限个开区间覆盖}"
        ).next_to(tex3, DOWN)
        mid1_dot = Dot(number_line0.n2p(4.5), color = YELLOW_E, radius = 0.08)
        mid1_label = MathTex(
            r"\frac{a_1+b_1}{2}", color = YELLOW_A, font_size = 30
        ).next_to(mid1_dot, DOWN)
        mid1 = VGroup(mid1_dot, mid1_label)
        self.play(ReplacementTransform(tex5, tex4), Create(mid1), run_time = 1.2)
        self.wait(2.5)
        a2_dot = Dot(number_line0.n2p(3.5), color = YELLOW_E, radius = 0.08)
        a2_label = MathTex(r"a_2", color = YELLOW_A, font_size = 30).next_to(a2_dot, DOWN)
        a2 = VGroup(a2_dot, a2_label)
        b2_dot = Dot(number_line0.n2p(4.5), color = YELLOW_E, radius = 0.08)
        b2_label = MathTex(r"b_2", color = YELLOW_A, font_size = 30).next_to(b2_dot, DOWN)
        b2 = VGroup(b2_dot, b2_label)
        tex5 = MathChi(r"\text{将其设为}[a_2,b_2]").next_to(tex3, DOWN)
        self.play(
            ReplacementTransform(tex4, tex5), 
            FadeOut(b1),
            ReplacementTransform(a1, a2),
            ReplacementTransform(mid1, b2),
            run_time = 1.4
        )
        self.wait(0.8)
        tex4 = MathChi(r"\text{重复上述操作}\dots").next_to(tex3, DOWN)
        self.play(ReplacementTransform(tex5, tex4), run_time = 0.8)
        combine0 = VGroup(number_line0, circles, line1, a2, b2)
        number_line1 = NumberLine(
            x_range = [3.15, 5.10, 0.15],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [3.15, 3.45, 3.75, 4.05, 4.35, 4.65, 4.95],
            font_size = 28
        ).shift(DOWN * 1.5)
        line2 = Line(number_line1.n2p(1.50), number_line1.n2p(5.50), stroke_width = 5.0, color = YELLOW_A)
        a3_dot = Dot(number_line1.n2p(3.50), color = YELLOW_E, radius = 0.08)
        a3_label = MathTex(r"a_2", color = YELLOW_A, font_size = 30).next_to(a3_dot, DOWN)
        a3 = VGroup(a3_dot, a3_label)
        b3_dot = Dot(number_line1.n2p(4.50), color = YELLOW_E, radius = 0.08)
        b3_label = MathTex(r"b_2", color = YELLOW_A, font_size = 30).next_to(b3_dot, DOWN)
        b3 = VGroup(b3_dot, b3_label)
        circles1 = VGroup()
        unit_length1 = number_line1.unit_size
        for i in range(10):
            yuans[i+11] = Circle(
                radius = radiuses[i]*unit_length1, 
                fill_color = BLUE_B, 
                fill_opacity = 0.25, 
                stroke_width = 0
            ).move_to(number_line1.n2p(positions[i]))
            circles1.add(yuans[i+11])
        combine1 = VGroup(number_line1, circles1, line2, a3, b3)
        self.play(ReplacementTransform(combine0, combine1), run_time = 2.2)
        mid2_dot = Dot(number_line1.n2p(4.00), color = YELLOW_E, radius = 0.08)
        mid2_label = MathTex(
            r"\frac{a_2+b_2}{2}", color = YELLOW_A, font_size = 30
        ).next_to(mid2_dot, DOWN)
        mid2 = VGroup(mid2_dot, mid2_label)
        self.play(Create(mid2), run_time = 0.9)
        a4_dot = Dot(number_line1.n2p(4.00), color = YELLOW_E, radius = 0.08)
        a4_label = MathTex(r"a_3", color = YELLOW_A, font_size = 30).next_to(a4_dot, DOWN)
        a4 = VGroup(a4_dot, a4_label)
        b4_dot = Dot(number_line1.n2p(4.50), color = YELLOW_E, radius = 0.08)
        b4_label = MathTex(r"b_3", color = YELLOW_A, font_size = 30).next_to(b4_dot, DOWN)
        b4 = VGroup(b4_dot, b4_label)
        self.play(
            FadeOut(a3), ReplacementTransform(mid2, a4), ReplacementTransform(b3, b4), run_time = 0.8
        )
        self.wait(0.4)
        mid3_dot = Dot(number_line1.n2p(4.25), color = YELLOW_E, radius = 0.08)
        mid3_label = MathTex(
            r"\frac{a_3+b_3}{2}", color = YELLOW_A, font_size = 30
        ).next_to(mid3_dot, DOWN)
        mid3 = VGroup(mid3_dot, mid3_label)
        self.play(Create(mid3), run_time = 0.9)
        a5_dot = Dot(number_line1.n2p(4.00), color = YELLOW_E, radius = 0.08)
        a5_label = MathTex(r"a_4", color = YELLOW_A, font_size = 30).next_to(a5_dot, DOWN)
        a5 = VGroup(a5_dot, a5_label)
        b5_dot = Dot(number_line1.n2p(4.25), color = YELLOW_E, radius = 0.08)
        b5_label = MathTex(r"b_4", color = YELLOW_A, font_size = 30).next_to(b5_dot, DOWN)
        b5 = VGroup(b5_dot, b5_label)
        self.play(
            FadeOut(b4), ReplacementTransform(mid3, b5), ReplacementTransform(a4, a5), run_time = 0.8
        )
        self.wait(0.4)
        tex6 = MathTex(
            r"\dots", 
            font_size = 36
        ).next_to(number_line1.n2p(4.04), DOWN, buff = 0.7)
        tex7 = MathTex(
            r"\dots", 
            font_size = 36
        ).next_to(number_line1.n2p(4.21), DOWN, buff = 0.7)
        self.play(Create(tex6), Create(tex7), run_time = 0.9)
        self.wait(0.4)
        an_dot = Dot(number_line1.n2p(4.09), color = YELLOW_E, radius = 0.08)
        an_label = MathTex(r"a_n", color = YELLOW_A, font_size = 30).next_to(an_dot, DOWN)
        an = VGroup(an_dot, an_label)
        bn_dot = Dot(number_line1.n2p(4.17), color = YELLOW_E, radius = 0.08)
        bn_label = MathTex(r"b_n", color = YELLOW_A, font_size = 30).next_to(bn_dot, DOWN)
        bn = VGroup(bn_dot, bn_label)
        self.play(Create(an), Create(bn), run_time = 0.8)
        self.play(FadeOut(tex3), FadeOut(tex4), run_time = 0.8)
        tex3 = MathChi(r"\text{这就构成了一个下降的闭区间列}\left\{[a_n,b_n]\right\}").next_to(tex, DOWN)
        tex4 = MathTex(
            r"\text{并且由}\left(\mathbf{A}\right)\text{得}\lim_{n \to \infty}(b_n-a_n)=\lim_{n \to \infty}\frac{b-a}{2^n}=0",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{A}\right)": YELLOW_A}
        ).next_to(tex3, DOWN) 
        tex5 = MathTex(
            r"\text{这就得到了}\lim_{n \to \infty}a_n=\lim_{n \to \infty}b_n=\xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\lim_{n \to \infty}a_n=\lim_{n \to \infty}b_n=\xi": PURPLE_A}
        ).move_to(tex4.get_center())
        dot_xi = Dot(number_line1.n2p(4.125), color = PURPLE_A, radius = 0.08)
        xi_label = MathTex(r"\xi", font_size = 40, color = PURPLE_A).next_to(dot_xi, UP)
        xi = VGroup(dot_xi, xi_label)
        self.play(AnimationGroup(Write(tex3), Write(tex4), lag_ratio = 1.2/2.4))
        self.wait(1.2)
        self.play(
            AnimationGroup(FadeOut(tex3), ReplacementTransform(tex4, tex5), Create(xi), lag_ratio = 0.5)
        )
        self.wait(0.8)
        tex3 = MathTex(
            r"\mathcal{F}\text{中必存在}(\alpha,\beta),\text{使得}\xi\in(\alpha,\beta)\text{(覆盖的定义)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"(\alpha,\beta)": ORANGE, r"\xi": PURPLE_A}
        ).next_to(tex, DOWN)
        self.play(AnimationGroup(FadeOut(tex5), Write(tex3), lag_ratio = 0.5))
        alpha_dot = Dot(number_line1.n2p(3.80), color = ORANGE, radius = 0.08)
        alpha_label = MathTex(r"\alpha", color = ORANGE, font_size = 40).next_to(alpha_dot, UP)
        alpha = VGroup(alpha_dot, alpha_label)
        beta_dot = Dot(number_line1.n2p(4.30), color = ORANGE, radius = 0.08)
        beta_label = MathTex(r"\beta", color = ORANGE, font_size = 40).next_to(beta_dot, UP)
        beta = VGroup(beta_dot, beta_label)
        self.wait(0.8)
        self.play(Create(alpha), Create(beta), run_time = 0.8)
        self.wait(0.4)
        tex4 = MathTex(
            r"\text{而}\lim_{n \to \infty}a_n=\lim_{n \to \infty}b_n=\xi",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\lim_{n \to \infty}a_n=\lim_{n \to \infty}b_n=\xi": PURPLE_A}
        ).next_to(tex, DOWN)
        tex5 = MathTex(
            r"\text{说明}\exists N\in\mathbb{Z}^{+},\forall n>N:\alpha<a_n<b_n<\beta",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\alpha": ORANGE, r"\beta": ORANGE}
        ).next_to(tex4, DOWN)
        self.play(AnimationGroup(ReplacementTransform(tex3, tex4), Write(tex5), lag_ratio = 1.2/2.4))
        self.wait(0.8)
        tex3 = MathTex(
            r"\text{我们得到}\exists N\in\mathbb{Z}^{+},\forall n>N:[a_n,b_n]\text{被}(\alpha,\beta)\text{覆盖}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"(\alpha,\beta)": ORANGE}
        ).next_to(tex, DOWN)
        redcircle = Circle(
            radius = 0.25*unit_length1, 
            fill_color = RED_B, 
            fill_opacity = 0.25, 
            stroke_width = 0
        ).move_to(number_line1.n2p(4.05))
        self.play(FadeOut(tex4), run_time = 0.8)
        self.play(
            AnimationGroup(
                ReplacementTransform(tex5, tex3), 
                ReplacementTransform(circles1[6], redcircle), 
                lag_ratio = 1.2/2.4
            )
        )
        tex4 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex3, RIGHT)
        self.play(Write(tex4), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex4, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        text0 = VGroup(tex3, tex4)
        circles1.add(redcircle)
        combine1.add(line0)
        combine1.add(tex0)
        combine1.add(tex6)
        combine1.add(tex7)
        combine1.add(an)
        combine1.add(bn)
        combine1.add(a5)
        combine1.add(b5)
        combine1.add(xi)
        combine1.add(alpha)
        combine1.add(beta)
        combine1.add(text0)
        combine1.add(line2)
        self.play(
            AnimationGroup(
                combine1.animate.set_opacity(0.15), 
                tex1.animate.shift(DOWN*2.4+LEFT*0.5).scale(1.2), 
                lag_ratio = 1.0/2.0
            )
        )
        tex8 = MathTex(
            r"\left(\mathbf{H}\right)",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 6.5)
        tex9 = MathTex(
            r"\left(\mathbf{H}\right)\Rightarrow\text{Bolzano-Weierstrass聚点定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        text = VGroup(tex1, tex8)
        self.play(Write(tex8), run_time = 1.2)
        self.wait(0.8)
        combine1 = VGroup(
            number_line1, line2, beta, alpha, an, bn, a5, b5, circles1, tex2, xi, tex6, tex7, text0, tex0
        )
        self.play(
            AnimationGroup(
                FadeOut(combine1), 
                ReplacementTransform(text, tex9), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# Heine-Borel定理推导Bolzano-Weierstrass聚点定理
class WeierstrassTheorem(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{H}\right)\Rightarrow\text{Bolzano-Weierstrass聚点定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathChi(r"\underline{\text{Bolzano-Weierstrass聚点定理}}")
        tex2 = MathChi(r"\text{每个}\mathbb{R}\text{上无穷、有界的子集}S\text{都有至少一个聚点}")
        tex = VGroup(tex1, tex2).arrange(DOWN, aligned_edge = LEFT).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-4, 12, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-4, -2, 0, 2, 4, 6, 8, 10, 12],
            font_size = 28
        ).shift(DOWN * 1.5)
        self.play(Write(tex), Create(number_line0), run_time = 1.6)
        zeros = [0] * 114
        ones = [1] * 114
        rd.seed(42)
        dots = VGroup()
        for i in range(45):
            ones[i] = rd.uniform(1.6, 6.4)
            zeros[i] = Dot(number_line0.n2p(ones[i]), color = YELLOW, radius = 0.05)
            dots.add(zeros[i])
        self.play(Create(dots), run_time = 3.5)
        s_label = MathTex(r"S", font_size = 48).next_to(number_line0.n2p(4.0), UP).shift(UP*0.3)
        a_dot = Dot(number_line0.n2p(0.8), color = ORANGE, radius = 0.08)
        a_label = MathTex(r"a", color = ORANGE, font_size = 40).next_to(a_dot, UP)
        a = VGroup(a_dot, a_label)
        b_dot = Dot(number_line0.n2p(6.8), color = ORANGE, radius = 0.08)
        b_label = MathTex(r"b", color = ORANGE, font_size = 40).next_to(b_dot, UP)
        b = VGroup(b_dot, b_label)
        tex3 = MathTex(
            r"\text{由于}S\text{有界，所以存在闭区间}][a,b],\text{使得}S\subseteq[a,b]",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"[a,b]": ORANGE}
        ).next_to(tex, DOWN)
        self.play(AnimationGroup(Write(s_label), Write(tex3), lag_ratio = 0.6))
        self.play(Create(a), Create(b), run_time = 1.2)
        self.wait(2)
        self.play(FadeOut(s_label), run_time = 0.8)
        circle_tracker = ValueTracker(1.4)
        radius_tracker = ValueTracker(0.45)
        circle = always_redraw(lambda: Circle(
            radius = radius_tracker.get_value(),
            color = BLUE_B,
            fill_opacity = 0.25,
            stroke_width = 0
        ).move_to(number_line0.n2p(circle_tracker.get_value())))

        def count_points_in_circle(points):
            # 计算给定点组中有多少点在圆内
            in_circle = []
            circle_center = circle.get_center()
            radius = circle.radius
        
            for point in points:
            # 计算点到圆心的距离
                distance = np.linalg.norm(point.get_center() - circle_center)
                if distance < radius:
                    in_circle.append(point)
                
            return in_circle
        
        count_tex = always_redraw(lambda: MathTex(
            r"n =", f"{len(count_points_in_circle(dots))}",
            tex_template = chinese_template,
            font_size = 40,
            color = YELLOW_A
        ).to_edge(UL).shift(DOWN*3))
        tex4 = MathTex(
            r"\text{若}S\text{无聚点},\text{那么每个}x\in[a,b]\text{的邻域}O(x,\delta _{x})\text{至多含}S\text{中有限个数}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"[a,b]": ORANGE, r"O(x,\delta _{x})": BLUE_B}
        ).next_to(tex, DOWN)
        self.play(ReplacementTransform(tex3, tex4), run_time = 1.2)
        tex5 = MathTex(
            r"(n\text{为邻域内包含的}S\text{的元素数})",
            tex_template = chinese_template,
            font_size = 40,
            color = YELLOW_A
        ).next_to(count_tex, RIGHT)
        text0 = VGroup(count_tex, tex5)
        x_dot = always_redraw(lambda: Dot(
            number_line0.n2p(circle_tracker.get_value()),
            color = BLUE_E,
            radius = 0.06
        ))
        x_label = always_redraw(lambda: MathTex(
            r"x",
            color = BLUE_B,
            font_size = 30
        ).next_to(number_line0.n2p(circle_tracker.get_value()), UP))
        x = VGroup(x_dot, x_label)
        self.play(AnimationGroup(Create(x), Create(circle), Write(text0), lag_ratio = 0.6))
        self.wait(0.6)
        animations = [
            {"center": 3.0, "radius": 0.6, "time": 0.9},
            {"center": 4.7, "radius": 0.3, "time": 0.9},
            {"center": 3.5, "radius": 0.25, "time": 0.9},
            {"center": 5.8, "radius": 0.8, "time": 0.9},
            {"center": 4.9, "radius": 0.4, "time": 0.9},
        ]
        for anim in animations:
            self.play(
                circle_tracker.animate.set_value(anim["center"]),
                radius_tracker.animate.set_value(anim["radius"]),
                run_time = anim["time"]
            )
            self.wait(0.8)
        self.play(FadeOut(x), FadeOut(circle), FadeOut(text0), FadeOut(tex4), run_time = 0.9)
        tex4 = MathTex(
            r"\text{令}E=\bigcup_{x\in[a,b]}^{} O(x,\delta _{x})\supseteq [a,b]\supseteq S",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"[a,b]": ORANGE, r"O(x,\delta _{x})": BLUE_B}
        ).next_to(tex, DOWN)
        self.play(Write(tex4), run_time = 1.2)
        tex3 = MathTex(
            r"\text{由}\left(\mathbf{H}\right)\text{得}\exists N\in\mathbb{Z}^{+},\text{使得}\mathfrak{E}=\bigcup_{k=1}^{N} O(x_k,\delta _{x_k})\supseteq [a,b]\supseteq S",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {
                r"\left(\mathbf{H}\right)": YELLOW_A, 
                r"[a,b]": ORANGE, 
                r"O(x_k,\delta _{x_k})": BLUE_B
            }
        ).next_to(tex4, DOWN).shift(UP*0.3)
        self.wait(0.8)
        self.play(Write(tex3), run_time = 1.2)
        self.wait(1.2)
        self.play(AnimationGroup(FadeOut(tex4), tex3.animate.move_to(tex4.get_center()), lag_ratio = 0.5))
        radiuses = [0.67, 0.8, 0.3, 0.5, 0.72, 0.38, 0.25, 0.5, 0.6, 0.45]
        positions = [1.35, 2.1, 2.8, 3.1, 3.6, 3.8, 4.35, 4.95, 5.8, 6.6]
        yuans = [0] * 114
        circles = VGroup()
        for i in range(10):
            yuans[i] = Circle(
                radius = radiuses[i], 
                fill_color = BLUE_B, 
                fill_opacity = 0.25, 
                stroke_width = 0
            ).move_to(number_line0.n2p(positions[i]))
            circles.add(yuans[i])
        self.play(Create(circles), run_time = 2.8)
        tex4 = MathTex(
            r"\text{每个}O(x_k,\delta _{x_k})\text{至多含}S\text{中有限个数},\text{故}\mathfrak{E}\text{也至多含}S\text{中有限个数}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"O(x_k,\delta _{x_k})": BLUE_B}
        ).next_to(tex, DOWN)
        self.play(ReplacementTransform(tex3, tex4), run_time = 1.2)
        self.wait(2.3)
        tex3 = MathChi(
            r"\text{又因为}\mathfrak{E}\supseteq S,\text{故}S\text{至多含有限个数}"
        ).next_to(tex, DOWN)
        self.play(ReplacementTransform(tex4, tex3), run_time = 1.2)
        tex5 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex3, RIGHT)
        text1 = VGroup(tex5, tex3)
        self.play(Write(tex5), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex5, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        combine0 = VGroup(number_line0, a, b, dots, circles, text1, line0, tex0)
        self.play(
            AnimationGroup(
                combine0.animate.set_opacity(0.15), 
                tex1.animate.shift(DOWN*2.4+LEFT*0.5).scale(1.2), 
                lag_ratio = 1.0/2.0
            )
        )
        tex6 = MathTex(
            r"\left(\mathbf{W}\right)",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 3)
        tex7 = MathTex(
            r"\left(\mathbf{W}\right)\Rightarrow\text{Bolzano-Weierstrass致密性定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        text = VGroup(tex1, tex6)
        self.play(Write(tex6), run_time = 1.2)
        self.wait(0.8)
        combine1 = VGroup(number_line0, circles, dots, a, b, tex0, tex2, text1)
        self.play(
            AnimationGroup(
                FadeOut(combine1), 
                ReplacementTransform(text, tex7), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# Bolzano-Weierstrass聚点定理推导Bolzano-Weierstrass致密性定理
class BolzanoTheorem(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{W}\right)\Rightarrow\text{Bolzano-Weierstrass致密性定理}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathChi(r"\underline{\text{Bolzano-Weierstrass致密性定理}}")
        tex2 = MathChi(r"\text{每个}\mathbb{R}\text{上的有界数列都有至少一个收敛的子数列}")
        tex = VGroup(tex1, tex2).arrange(DOWN, aligned_edge = LEFT).next_to(line0, DOWN)
        number_line0 = NumberLine(
            x_range = [-4, 12, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-4, -2, 0, 2, 4, 6, 8, 10, 12],
            font_size = 28
        ).shift(DOWN * 1.5)
        self.play(Write(tex), run_time = 1.6)
        tex3 = MathChi(r"\text{设数列}\left\{x_n\right\}\text{有界},\text{值域是}E").next_to(tex, DOWN)
        tex4 = MathChi(
            r"E\text{是有限集时},\exists e\in E,\text{使得}x_{n_1}=x_{n_2}=\dots=e(n_1<n_2<\dots)"
        ).next_to(tex3, DOWN)
        tex5 = MathChi(r"\text{这样就得到了收敛子列}\lim_{k \to \infty}x_{n_k}=e").next_to(tex4, DOWN)
        self.play(Write(tex3), run_time = 1.2)
        self.play(Write(tex4), run_time = 1.2)
        self.play(Write(tex5), run_time = 1.2)
        self.wait(2.3)
        text0 = VGroup(tex4, tex5)
        self.play(Create(number_line0), FadeOut(text0), run_time = 1.6)
        tex4 = MathTex(
            r"E\text{是无限集时},\text{由}\left(\mathbf{W}\right)\text{得}E\text{上有聚点}b,\text{其任意邻域}O(b,\epsilon)\text{都含}E\text{中无限个数}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{W}\right)": YELLOW_A, r"O(b,\epsilon)": GREEN_B}
        ).next_to(tex3, DOWN)
        self.play(Write(tex4), run_time = 1.2)
        b_dot = Dot(number_line0.n2p(5.7), color = GREEN_E, radius = 0.08)
        b_label = MathTex(r"b", color = GREEN_A, font_size = 40).next_to(b_dot, UP)
        b = VGroup(b_dot, b_label)
        circle0 = Circle(
            radius = 1,
            fill_color = GREEN_B,
            fill_opacity = 0.25,
            stroke_width = 0
        ).move_to(b_dot.get_center())
        self.play(Create(b), GrowFromCenter(circle0), run_time = 1.2)
        self.wait(0.5)
        tex5 = MathTex(
            r"\text{于是}\exists n_1\in\mathbb{Z}^{+}:x_{n_1}\in O(b,1)",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"O(b,1)": GREEN_B}
        ).next_to(tex3, DOWN)
        x1_dot = Dot(number_line0.n2p(6.4), color = YELLOW, radius = 0.08)
        x1_label = MathTex(r"x_{n_1}", font_size = 30).next_to(x1_dot, UP)
        x1 = VGroup(x1_dot, x1_label)
        self.play(AnimationGroup(ReplacementTransform(tex4, tex5), Create(x1), lag_ratio = 0.6))
        self.wait(0.8)
        combine0 = VGroup(number_line0, b, circle0, x1)
        number_line1 = NumberLine(
            x_range = [3, 9, 0.5],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [3, 4, 5, 6, 7, 8, 9],
            font_size = 28
        ).shift(DOWN * 1.5)
        b1_dot = Dot(number_line1.n2p(5.7), color = GREEN_E, radius = 0.08)
        b1_label = MathTex(r"b", color = GREEN_A, font_size = 40).next_to(b1_dot, UP)
        b1 = VGroup(b1_dot, b1_label)
        circle1 = Circle(
            radius = 1.333333,
            fill_color = GREEN_B,
            fill_opacity = 0.25,
            stroke_width = 0
        ).move_to(b1_dot.get_center())
        x_dot1 = Dot(number_line1.n2p(6.4), color = YELLOW, radius = 0.08)
        x_label1 = MathTex(r"x_{n_1}", font_size = 30).next_to(x_dot1, UP)
        x_1 = VGroup(x_dot1, x_label1)
        combine1 = VGroup(number_line1, b1, circle1, x_1)
        self.play(ReplacementTransform(combine0, combine1), FadeOut(tex5), run_time = 1.6)
        tex5 = MathTex(
            r"\exists n_2>n_1:x_{n_2}\in O(b,\frac{1}{2})",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"O(b,\frac{1}{2})": GREEN_B}
        ).next_to(tex3, DOWN)
        x2_dot = Dot(number_line1.n2p(5.3), color = YELLOW, radius = 0.08)
        x2_label = MathTex(r"x_{n_2}", font_size = 30).next_to(x2_dot, UP)
        x2 = VGroup(x2_dot, x2_label)
        self.play(AnimationGroup(Write(tex5), Create(x2), lag_ratio = 0.6))
        number_line2 = NumberLine(
            x_range = [4.5, 7.5, 0.2],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.5, 4.9, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3],
            font_size = 28
        ).shift(DOWN * 1.5)
        b2_dot = Dot(number_line2.n2p(5.7), color = GREEN_E, radius = 0.08)
        b2_label = MathTex(r"b", color = GREEN_A, font_size = 40).next_to(b2_dot, UP)
        b2 = VGroup(b2_dot, b2_label)
        circle2 = Circle(
            radius = 1.333333,
            fill_color = GREEN_B,
            fill_opacity = 0.25,
            stroke_width = 0
        ).move_to(b2_dot.get_center())
        x_dot2 = Dot(number_line2.n2p(6.4), color = YELLOW, radius = 0.08)
        x_label2 = MathTex(r"x_{n_1}", font_size = 30).next_to(x_dot2, UP)
        x_2 = VGroup(x_dot2, x_label2)
        x_dot3 = Dot(number_line2.n2p(5.3), color = YELLOW, radius = 0.08)
        x_label3 = MathTex(r"x_{n_2}", font_size = 30).next_to(x_dot3, UP)
        x_3 = VGroup(x_dot3, x_label3)
        combine1.add(x2)
        combine2 = VGroup(number_line2, b2, circle2, x_2, x_3)
        self.play(ReplacementTransform(combine1, combine2), FadeOut(tex5), run_time = 1.6)
        tex5 = MathTex(
            r"\text{同理}\exists n_3>n_2:x_{n_3}\in O(b,\frac{1}{4})\dots",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"O(b,\frac{1}{4})": GREEN_B}
        ).next_to(tex3, DOWN)
        x3_dot = Dot(number_line2.n2p(5.88), color = YELLOW, radius = 0.08)
        x3_label = MathTex(r"x_{n_3}", font_size = 30).next_to(x3_dot, UP)
        x3 = VGroup(x3_dot, x3_label)
        self.play(AnimationGroup(Write(tex5), Create(x3), lag_ratio = 0.6))
        self.wait(0.4)
        circle3 = Circle(
            radius = 0.666667,
            fill_color = GREEN_B,
            fill_opacity = 0.25,
            stroke_width = 0
        ).move_to(b2_dot.get_center())
        self.play(ReplacementTransform(circle2, circle3), run_time = 0.9)
        x4_dot = Dot(number_line2.n2p(5.60), color = YELLOW, radius = 0.08)
        x4_label = MathTex(r"x_{n_4}", font_size = 30).next_to(x4_dot, UP)
        x4 = VGroup(x4_dot, x4_label)
        self.wait(0.4)
        self.play(Create(x4), run_time = 0.9)
        tex4 = MathTex(r"\dots", font_size = 34).next_to(number_line2.n2p(5.62), DOWN, buff = 0.3)
        self.play(Create(tex4), run_time = 0.9)
        self.play(FadeOut(tex3), FadeOut(tex5), run_time = 1.2)
        tex3 = MathChi(
            r"\text{这就得到了一个子列}\left\{x_{n_k}\right\}\text{满足}\left|x_{n_k}-b\right|<\frac{1}{2^{k-1}}"
        ).next_to(tex, DOWN)
        self.play(Write(tex3), run_time = 1.2)
        tex5 = MathChi(r"\text{进而推出}\lim_{k \to \infty}x_{n_k}=b").next_to(tex3, DOWN)
        self.play(Write(tex5), run_time = 1.2)
        self.wait(1.6)
        self.play(AnimationGroup(FadeOut(tex3), tex5.animate.move_to(tex3.get_center()), lag_ratio = 0.6))
        self.wait(0.4)
        rec = Rectangle(
            height = 0.9,
            width = 4.6,
            stroke_width = 4.0,
            color = YELLOW
        ).move_to(tex5.get_center())
        self.play(Create(rec), run_time = 0.6)
        self.play(Uncreate(rec), run_time = 0.6)
        combine0 = VGroup(number_line2, b2, circle3, x_2, x_3, line0, tex0, tex2, x2, x3, x4, tex4)
        self.play(
            AnimationGroup(
                combine0.animate.set_opacity(0.15), 
                tex1.animate.shift(DOWN*2.4+LEFT*0.5).scale(1.2), 
                lag_ratio = 1.0/2.0
            )
        )
        tex6 = MathTex(
            r"\left(\mathbf{B}\right)",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 3)
        tex7 = MathTex(
            r"\left(\mathbf{B}\right)\Rightarrow\left(\mathbf{M}\right)",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        text = VGroup(tex1, tex6)
        self.play(Write(tex6), run_time = 1.2)
        self.wait(0.8)
        combine1 = VGroup(number_line2, b2, circle3, x_2, x_3, tex0, tex2, x2, x3, x4, tex4, tex5)
        self.play(
            AnimationGroup(
                FadeOut(combine1), 
                ReplacementTransform(text, tex7), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# Bolzano-Weierstrass致密性定理推导单调有界定理
class MCT(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\left(\mathbf{B}\right)\Rightarrow\left(\mathbf{M}\right)",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathTex(
            r"\underline{\text{单调有界定理}\left(\mathbf{M}\right)}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{M}\right)": YELLOW_A}
        ).next_to(line0, DOWN)
        tex2 = MathChi(r"\text{设}\left\{x_n\right\}\text{单调递增有上界}").next_to(tex1, DOWN)
        number_line0 = NumberLine(
            x_range = [-2, 12, 1],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [-2, 0, 2, 4, 6, 8, 10, 12],
            font_size = 28
        ).shift(DOWN * 1.5)
        self.play(Write(tex1), Create(number_line0), run_time = 1.6)
        self.play(Write(tex2), run_time = 1.2)
        positions = [2.8, 3.6, 4.3, 4.7, 4.9]
        zeros = [0] * 114
        ones = [0] * 114
        colors = [YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D, YELLOW_E]
        xs = VGroup()
        x_labels = VGroup()
        for i in range(5):
            zeros[i] = Dot(number_line0.n2p(positions[i]), color = colors[i], radius = 0.08)
            ones[i] = MathTex(f"x_{i}", color = colors[i], font_size = 30).next_to(zeros[i], DOWN)
            xs.add(zeros[i])
            x_labels.add(ones[i])
            self.play(Create(xs[i]), Create(x_labels[i]), run_time = 0.8)
            self.wait(0.3)
        tex3 = MathTex(
            r"\dots", color = YELLOW_E, font_size = 36
        ).next_to(number_line0.n2p(5.3), DOWN, buff = 0.7)
        self.play(Create(tex3), run_time = 0.9)
        self.wait(0.4)
        tex4 = MathTex(
            r"\text{由}\left(\mathbf{B}\right)\text{得},\text{存在收敛的}\left\{x_{n_k}\right\},\text{设其收敛于}\mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\left(\mathbf{B}\right)": YELLOW_A, r"\mathcal{A}": ORANGE}
        ).next_to(tex2, DOWN)
        self.play(Write(tex4), run_time = 1.2)
        combine0 = VGroup(number_line0, xs, x_labels)
        positions1 = [5.21, 5.5, 5.66, 5.73, 5.86]
        number_line1 = NumberLine(
            x_range = [4.6, 7, 0.2],
            length = 16,
            color = BLUE_B,
            include_numbers = True,
            numbers_to_include = [4.6, 5.0, 5.4, 5.8, 6.4, 7.0],
            font_size = 28
        ).shift(DOWN * 1.5)
        xns = VGroup()
        xn_labels = VGroup()
        xs1 = VGroup()
        x_labels1 = VGroup()
        for i in range(5):
            zeros[i+6] = Dot(number_line1.n2p(positions[i]), color = colors[i], radius = 0.08)
            ones[i+6] = MathTex(f"x_{i}", color = colors[i], font_size = 30).next_to(zeros[i+6], DOWN)
            xs1.add(zeros[i+6])
            x_labels1.add(ones[i+6])
        combine1 = VGroup(number_line1, xs1, x_labels1)
        for i in range(5):
            zeros[i+11] = Dot(number_line1.n2p(positions1[i]), color = colors[i], radius = 0.08)
            xns.add(zeros[i+11])
        ones[11] = MathTex(r"x_{n_1}", color = YELLOW_A, font_size = 30).next_to(xns[0], DOWN)
        ones[12] = MathTex(r"x_{n_2}", color = YELLOW_B, font_size = 30).next_to(xns[1], DOWN)
        ones[13] = MathTex(r"x_{n_3}", color = YELLOW_C, font_size = 30).next_to(xns[2], DOWN)
        ones[14] = MathTex(r"x_{n_4}", color = YELLOW_D, font_size = 30).next_to(xns[3], DOWN)
        ones[15] = MathTex(r"x_{n_5}", color = YELLOW_E, font_size = 30).next_to(xns[4], DOWN)
        self.play(
            AnimationGroup(FadeOut(tex3), ReplacementTransform(combine0, combine1), lag_ratio = 0.6)
        )
        self.wait(0.6)
        for i in range(5):
            xn_labels.add(ones[i+11])
            self.play(Create(xns[i]), Create(xn_labels[i]), run_time = 0.8)
            self.wait(0.3)
        tex3 = MathTex(
            r"\dots", color = YELLOW_E, font_size = 36
        ).next_to(number_line1.n2p(6.1), DOWN, buff = 0.7)
        a_dot = Dot(number_line1.n2p(6.3), color = ORANGE, radius = 0.08)
        a_label = MathTex(r"\mathcal{A}", color = ORANGE, font_size = 40).next_to(a_dot, UP)
        a = VGroup(a_dot, a_label)
        self.play(Create(tex3), run_time = 0.9)
        self.wait(0.4)
        self.play(Write(a), run_time = 0.8)
        self.wait(0.3)
        tex5 = MathTex(
            r"\text{若}\exists N\in\mathbb{Z}^{+},\text{使得}x_N>\mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE}
        ).next_to(tex4, DOWN)
        self.play(Write(tex5), run_time = 1.2)
        xn_dot = Dot(number_line1.n2p(6.45), color = YELLOW_A, radius = 0.08)
        xn_label = MathTex(r"x_N", font_size = 30).next_to(xn_dot, UP)
        xn = VGroup(xn_dot, xn_label)
        self.play(Create(xn), run_time = 0.8)
        tex6 = MathTex(
            r"\text{显然}k\text{充分大时}:n_k>N,\text{那么}x_{n_k}\ge x_N>\mathcal{A}(\text{单调递增})",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE}
        ).next_to(tex5, DOWN)
        self.play(Write(tex6), run_time = 1.2)
        xn1_dot = Dot(number_line1.n2p(6.52), color = YELLOW_A, radius = 0.08)
        xn1_label = MathTex(r"x_{n_k}", font_size = 30).next_to(xn1_dot, UP)
        xn1 = VGroup(xn1_dot, xn1_label)
        self.play(Create(xn1), run_time = 0.8)
        tex7 = MathTex(
            r"\text{显然}\lim_{k \to \infty}x_{n_k}\ge x_N>\mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE}
        ).next_to(tex4, DOWN)
        text = VGroup(tex5, tex6)
        self.wait(2.2)
        self.play(AnimationGroup(FadeOut(text), Write(tex7), lag_ratio = 0.6))
        tex5 = MathTex(
            r"\text{矛盾！}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW
        ).next_to(tex7, RIGHT).shift(UP*0.1)
        self.play(Write(tex5), run_time = 0.7)
        self.wait(0.4)
        self.play(Wiggle(tex5, scale_value = 1.2, rotation_angle = 5*DEGREES), run_time = 1.3)
        self.wait(0.4)
        self.play(FadeOut(tex5), run_time = 0.8)
        tex5 = MathTex(
            r"\text{故}\forall n \in\mathbb{Z}^{+},x_n\le \mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE}
        ).next_to(tex4, DOWN)
        self.play(ReplacementTransform(tex7, tex5), FadeOut(xn), FadeOut(xn1), run_time = 1.2)
        self.wait(1.3)
        self.play(FadeOut(tex5), run_time = 0.9)
        tex5 = MathTex(
            r"\forall \epsilon >0,\exists K\in\mathbb{Z}^{+},\forall k>K:\mathcal{A}-\epsilon<x_{n_k}\le\mathcal{A}",
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\mathcal{A}": ORANGE}
        ).next_to(tex4, DOWN)
        xn_dot = Dot(number_line1.n2p(5.98), color = YELLOW_A, radius = 0.08)
        xn_label = MathTex(r"x_{n_k}", font_size = 30).next_to(xn_dot, DOWN)
        xn = VGroup(xn_dot, xn_label)
        ae_dot = Dot(number_line1.n2p(5.91), color = ORANGE, radius = 0.08)
        ae_label = MathTex(
            r"\mathcal{A}-\epsilon", 
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE, r"\epsilon": GREEN_B}
        ).next_to(ae_dot, UP)
        ae = VGroup(ae_dot, ae_label)
        self.play(Write(tex5), Create(ae), Create(xn), run_time = 1.2)
        self.wait(0.6)
        self.play(FadeOut(xn), run_time = 0.9)
        tex6 = MathTex(
            r"\text{令}N=n_{K+1},\forall n>N:\mathcal{A}-\epsilon<x_{n_{K+1}}=x_{N}\le x_{n}\le\mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\epsilon": GREEN_B, r"\mathcal{A}": ORANGE}
        ).next_to(tex5, DOWN)
        xn_dot = Dot(number_line1.n2p(6.15), color = YELLOW_A, radius = 0.08)
        xn_label = MathTex(r"x_{n}", font_size = 30).next_to(xn_dot, DOWN)
        xn = VGroup(xn_dot, xn_label)
        xnk_dot = Dot(number_line1.n2p(6.05), color = YELLOW_A, radius = 0.08)
        xnk_label = MathTex(r"x_{n_{K+1}}", font_size = 30).next_to(xnk_dot, DOWN)
        xnk = VGroup(xnk_dot, xnk_label)
        self.play(Write(tex6), Create(xnk), Create(xn), run_time = 1.2)
        self.wait(2.3)
        self.play(FadeOut(tex4), FadeOut(tex5), FadeOut(tex6), run_time = 0.9)
        tex4 = MathTex(
            r"\text{于是得出}\lim_{n \to \infty}x_n=\mathcal{A}",
            tex_template = chinese_template,
            font_size = 40,
            tex_to_color_map = {r"\mathcal{A}": ORANGE}
        ).next_to(tex2, DOWN)
        self.play(Write(tex4), run_time = 1.2)
        self.wait(0.8)
        combine2 = VGroup(
            number_line1, xns, xs1, xn_labels, x_labels1, tex3, tex0, line0, a, ae, xn, xnk, tex2
        )
        self.play(
            AnimationGroup(
                combine2.animate.set_opacity(0.15), 
                tex1.animate.shift(DOWN*2.4+LEFT*3).scale(1.2),
                lag_ratio = 1.0/2.0
            )
        )
        tex5 = MathTex(
            r"\text{得证!}",
            tex_template = chinese_template,
            font_size = 48,
            color = YELLOW_A
        ).next_to(tex1, RIGHT, buff = 4.5)
        self.play(Write(tex5), run_time = 1.2)
        text0 = VGroup(tex1, tex5)
        combine3 = VGroup(
            number_line1, xns, xs1, xn_labels, x_labels1, tex3, tex0, tex4, a, ae, xn, xnk, tex2
        )
        self.wait(0.8)
        tex7 = MathTex(
            r"\text{总结}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        self.play(
            AnimationGroup(
                FadeOut(combine3), 
                ReplacementTransform(text0, tex7), 
                lag_ratio = 1.2/2.5
            )
        )
        self.play(line0.animate.set_opacity(1), run_time = 0.8)
        self.wait(0.4)

# 总结
class Conclusion(Scene):
    def construct(self):
        tex0 = MathTex(
            r"\text{总结}",
            tex_template = chinese_template,
            font_size = 44,
            color = YELLOW_A
        ).to_edge(UP, buff = 0.3)
        line0 = Line(stroke_width = 5.0, color = BLUE_B).next_to(tex0, DOWN).set_length(12)
        self.add(tex0)
        self.add(line0)
        self.wait(0.4)
        tex1 = MathTex(
            r"\text{我们刚刚推导出了下图所示的逻辑链：}",
            tex_template = chinese_template,
            font_size = 40
        ).next_to(line0, DOWN)
        self.play(Write(tex1), run_time = 1.6)
        tex2 = MathTex(
            r"\left(\mathbf{H}\right)",
            font_size = 44,
            color = YELLOW_A
        ).shift(RIGHT*1.8)
        tex3 = MathTex(
            r"\left(\mathbf{A}\right)+\left(\mathbf{N}\right)",
            font_size = 44,
            color = YELLOW_A
        ).shift(UP*1.8)
        tex4 = MathTex(
            r"\left(\mathbf{B}\right)",
            font_size = 44,
            color = YELLOW_A
        ).shift(DOWN*1.8)
        tex5 = MathTex(
            r"\left(\mathbf{M}\right)",
            font_size = 44,
            color = YELLOW_A
        )
        tex6 = MathTex(
            r"\left(\mathbf{L}\right)",
            font_size = 44,
            color = YELLOW_A
        ).shift(LEFT*1.8)
        tex7 = MathTex(
            r"\left(\mathbf{W}\right)",
            font_size = 44,
            color = YELLOW_A
        ).shift(RIGHT*1.8+DOWN*1.8)
        arrow0 = MathTex(r"\Longrightarrow", font_size = 44, color = YELLOW_A).shift(LEFT*0.9)
        arrow1 = MathTex(r"\Longleftarrow", font_size = 44, color = YELLOW_A).shift(RIGHT*0.9+DOWN*1.8)
        arrow2 = MathTex(r"\Longrightarrow", font_size = 44, color = YELLOW_A).shift(DOWN*0.9).rotate(PI/2)
        arrow3 = MathTex(
            r"\Longrightarrow", font_size = 44, color = YELLOW_A
        ).shift(RIGHT*1.8+DOWN*0.9).rotate(3*PI/2)
        arrow4 = MathTex(r"\Longrightarrow", font_size = 44, color = YELLOW_A).shift(UP*0.9).rotate(PI/2)
        arrow5 = MathTex(
            r"\Longrightarrow", font_size = 44, color = YELLOW_A
        ).shift(LEFT*1.1+UP*0.9).rotate(5*PI/4).scale(1.4)
        arrow6 = MathTex(
            r"\Longrightarrow", font_size = 44, color = YELLOW_A
        ).shift(RIGHT*1.1+UP*0.9).rotate(7*PI/4).scale(1.4)
        combine0 = VGroup(
            tex3, arrow5, tex6, arrow0, tex5, arrow4, arrow6, tex2, arrow3, tex7, arrow1, tex4, arrow2
        )
        self.play(Create(combine0), run_time = 2.5)
        self.wait(3.3)
        tex8 = MathTex(
            r"\text{你还记得这些字母所代表的是哪个定理吗？}",
            tex_template = chinese_template,
            font_size = 40
        ).next_to(combine0, DOWN)
        self.play(Write(tex8), run_time = 1.6)
        self.wait(3.3)
        combine1 = VGroup(combine0, tex8, tex1)
        tex9 = MathTex(
            r"\text{这些表述在说明实数系的完备性上是}\text{等价}\text{的}",
            tex_template = chinese_template,
            font_size = 44,
            tex_to_color_map = {r"\text{等价}": YELLOW}
        ).shift(UP*0.5)
        tex10 = MathTex(
            r"\text{每个都可以作为}\text{公理}\text{去推出其他命题}",
            tex_template = chinese_template,
            font_size = 44,
            tex_to_color_map = {r"\text{公理}": RED}
        ).next_to(tex9, DOWN)
        self.play(
            AnimationGroup(
                combine1.animate.set_opacity(0.15), 
                Write(tex9),
                Write(tex10),
                lag_ratio = 0.6
            )
        )
        self.wait(2)
        combine2 = VGroup(combine1, tex9, tex10)
        self.play(FadeOut(combine2), run_time = 0.9)
        tex1 = MathTex(
            r"\text{你或许还听说过Cauchy收敛原理：}",
            tex_template = chinese_template,
            font_size = 40
        ).next_to(line0, DOWN)
        self.play(Write(tex1), run_time = 1.2)
        self.wait(0.6)
        tex2 = MathTex(
            r"\text{数列}\left\{x_n\right\}\text{收敛}\Leftrightarrow \forall \epsilon>0,\exists N\in\mathbb{Z}^{+},\forall n,m>N:\left|x_n-x_m\right|<\epsilon",
            tex_template = chinese_template,
            font_size = 40
        ).next_to(tex1, DOWN)
        self.play(Write(tex2), run_time = 1.2)
        self.wait(0.9)
        tex3 = MathTex(
            r"\text{这是否和我们刚刚提及的那些表述等价呢？}",
            tex_template = chinese_template,
            font_size = 40
        )
        tex4 = MathTex(
            r"\text{这就留给观众作思考了}\dots",
            tex_template = chinese_template,
            font_size = 40
        )
        text = VGroup(tex3, tex4).arrange(DOWN)
        self.play(Write(tex3), run_time = 1.2)
        self.wait(0.9)
        self.play(Write(tex4), run_time = 1.2)
        self.wait(3.3)
        combine3 = VGroup(text, line0, tex0, tex1, tex2)
        self.play(FadeOut(combine3), run_time = 2.2)

# 在视频结尾显示作者的名字        
class Final(Scene):
    def construct(self):
        tex0 = Tex(
            "By Trance\_Kernel",
            font_size = 100,
            color = YELLOW_A
        )
        self.wait(0.4)
        self.play(Write(tex0), run_time = 1.8)
        self.wait(3)
        self.play(FadeOut(tex0))
