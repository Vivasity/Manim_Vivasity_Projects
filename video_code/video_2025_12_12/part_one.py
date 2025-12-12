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

# 以圆为例引入参数方程
class CirclePara(Scene):
    def construct(self):
        axes = Axes(x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9)
        grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9, background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)
        
        def circle(t):
            return axes.c2p(2 * np.cos(t), 2 * np.sin(t))
        
        circ = ParametricFunction(circle, t_range = [0, 2 * PI], color = TEAL_A)
        self.play(GrowFromCenter(grid), run_time = 0.7)
        self.play(Create(circ), run_time = 1.3)
        self.wait()
        t_tracker = ValueTracker(0)
        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value())), color = YELLOW)
        )
        moving_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(0, 0), end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value())), 
                color = YELLOW_B, buff = 0
            )
        )
        cir_label = MathTex(r"x^2+y^2=4", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        cir_rect = SurroundingRectangle(
            cir_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vcir = VGroup(cir_rect, cir_label)
        self.play(Create(vcir), run_time = 1.5)
        self.wait()
        self.play(Create(moving_dot))
        self.play(Flash(moving_dot, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.wait()
        self.play(t_tracker.animate.set_value(2 * PI), run_time = 3.5)
        self.wait()
        dashed_line = DashedLine(start = axes.c2p(1, -np.sqrt(3)), end = axes.c2p(1, np.sqrt(3)), dash_length = 0.2, stroke_width = 4)
        xdot = Dot(axes.c2p(1, 0), color = YELLOW).set_z_index(1)
        xlabel = MathTex(r"x", font_size = 44, color = YELLOW).next_to(xdot, DR, buff = 0.14)
        x = VGroup(xdot, xlabel)
        y1dot = Dot(axes.c2p(1, np.sqrt(3)), color = YELLOW).set_z_index(1)
        y1label = MathTex(r"y_1", font_size = 44, color = YELLOW).next_to(y1dot, RIGHT, buff = 0.14)
        y1 = VGroup(y1dot, y1label)
        y2dot = Dot(axes.c2p(1, -np.sqrt(3)), color = YELLOW).set_z_index(1)
        y2label = MathTex(r"y_2", font_size = 44, color = YELLOW).next_to(y2dot, RIGHT, buff = 0.14)
        y2 = VGroup(y2dot, y2label)
        self.play(Create(x), GrowFromCenter(dashed_line), run_time = 1.6)
        self.play(Create(y1), Create(y2))
        self.wait()
        self.play(FadeOut(x), FadeOut(dashed_line), FadeOut(y1), FadeOut(y2), run_time = 1.6)
        self.remove(vcir)
        self.add(moving_vector).wait()
        self.play(t_tracker.animate.set_value(9 * PI / 4), run_time = 1.8)
        sec = always_redraw(
            lambda: Sector(
                outer_radius = 0.5, start_angle = 0, angle = t_tracker.get_value() - 2 * PI, stroke_color = YELLOW_D, 
                fill_color = YELLOW_D, stroke_width = 3, fill_opacity = 0.5
            ).shift(0.5 * DOWN)
        )
        t = MathTex(r"t", font_size = 44, color = YELLOW).move_to(axes.c2p(0.7, 0.3))
        self.play(Create(sec), Create(t), run_time = 1.3)
        self.wait()
        xdashed_line = DashedLine(
            start = axes.c2p(np.sqrt(2), np.sqrt(2)), end = axes.c2p(np.sqrt(2), 0), dash_length = 0.2, stroke_width = 4
        )
        ydashed_line = DashedLine(
            start = axes.c2p(np.sqrt(2), np.sqrt(2)), end = axes.c2p(0, np.sqrt(2)), dash_length = 0.2, stroke_width = 4
        )
        red_line = Line(axes.c2p(0, 0), axes.c2p(np.sqrt(2), 0), color = RED, stroke_width = 6)
        green_line = Line(axes.c2p(0, 0), axes.c2p(0, np.sqrt(2)), color = GREEN, stroke_width = 6)
        red_label = MathTex(r"2\cos t", font_size = 44, color = RED).move_to(axes.c2p(0.7, -0.4))
        x_equa = MathTex(r"x=", font_size = 44, color = YELLOW_A).move_to(axes.c2p(3.5, 3.8))
        green_label = MathTex(r"2\sin t", font_size = 44, color = GREEN).move_to(axes.c2p(-0.65, 0.7))
        y_equa = MathTex(r"y=", font_size = 44, color = YELLOW_A).move_to(axes.c2p(3.5, 3.2))
        bracket = MathTex(r"\left\{\begin{matrix} \\  \end{matrix}\right.", font_size = 64, color = YELLOW_A).move_to(axes.c2p(2.9, 3.5))
        self.play(ReplacementTransform(moving_vector.copy(), red_line), Create(xdashed_line), run_time = 1.4)
        self.play(Write(red_label))
        self.wait()
        self.play(Create(x_equa), red_label.animate.shift(4.25 * UP + 3.9 * RIGHT), run_time = 1.4)
        self.play(ReplacementTransform(moving_vector.copy(), green_line), Create(ydashed_line), run_time = 1.4)
        self.play(Write(green_label))
        self.wait()
        self.play(Create(y_equa), green_label.animate.shift(2.6 * UP + 5.23 * RIGHT), run_time = 1.4)
        self.play(GrowFromCenter(bracket), run_time = 0.8)
        self.wait()
        vpara = VGroup(bracket, x_equa, y_equa)
        mapping0 = MathTex(r"t \longmapsto ", font_size = 44, color = YELLOW_A).move_to(axes.c2p(1.3, 2.8))
        mapping1 = MathTex(r"(", font_size = 44, color = YELLOW_A).move_to(axes.c2p(2, 2.8))
        mapping2 = MathTex(r",", font_size = 44, color = YELLOW_A).move_to(axes.c2p(3.4, 2.63))
        mapping3 = MathTex(r")", font_size = 44, color = YELLOW_A).move_to(axes.c2p(4.8, 2.8))
        self.play(
            ReplacementTransform(vpara, mapping0), Create(mapping1), Create(mapping2), Create(mapping3),
            red_label.animate.move_to(axes.c2p(2.7, 2.8)), green_label.animate.move_to(axes.c2p(4.1, 2.8)), run_time = 2
        )
        vmapping = VGroup(mapping0, mapping1, red_label, mapping2, green_label, mapping3).set_z_index(2)
        mapping_rect = SurroundingRectangle(vmapping, color = YELLOW, buff = 0.2, stroke_width = 4)
        self.play(ShowPassingFlash(mapping_rect), time_width = 0.6, run_time = 1.5)
        self.wait()
        new_equa = MathTex(r"\vec{r}(t)=(2\cos t, 2\sin t)", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        new_rect = SurroundingRectangle(
            new_equa, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vnew = VGroup(new_rect, new_equa)
        v_dash_line = VGroup(xdashed_line, ydashed_line, red_line, green_line)
        self.play(FadeIn(new_rect), FadeOut(v_dash_line), ReplacementTransform(vmapping, new_equa), run_time = 1.6)
        t_value = always_redraw(
            lambda: MathTex(r"=" + f"{t_tracker.get_value() - 2 * PI:.3f}", font_size = 44, color = YELLOW).move_to(axes.c2p(3.3, 0.3))
        )
        self.wait()
        self.play(t.animate.move_to(axes.c2p(2.3, 0.3)), Write(t_value), run_time = 1.2)
        self.wait()
        self.play(t_tracker.animate.set_value(2.47 * PI), run_time = 1.6)
        self.wait()
        self.play(t_tracker.animate.set_value(17 * PI / 6), run_time = 1.6)
        self.wait()
        self.play(t_tracker.animate.set_value(3.64 * PI), run_time = 1.6)
        self.wait()
        self.play(t_tracker.animate.set_value(9 * PI / 4), run_time = 1.6)
        self.wait()
        fderivative = MathTex(
            r"{f}'(x)=\lim_{\Delta x \to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x} ", font_size = 44, color = GREEN_B
        ).move_to(axes.c2p(-3.6, 2.5))
        rderivative = MathTex(
            r"{\vec{r}}'(t)=\lim_{\Delta t \to 0}\frac{\vec{r}(t+\Delta t)-\vec{r}(t)}{\Delta t} ", font_size = 44, color = GREEN_B
        ).move_to(fderivative.get_center())
        frect = SurroundingRectangle(fderivative, color = YELLOW, buff = 0.1, stroke_width = 4)
        self.play(DrawBorderThenFill(fderivative), run_time = 1.4)
        self.play(ShowPassingFlash(frect), time_width = 0.6, run_time = 1.5)
        self.wait()
        self.play(ReplacementTransform(fderivative, rderivative), run_time = 1.4)
        self.wait()
        tp_tracker = ValueTracker(2.5 * PI)
        rp_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(0, 0), end = axes.c2p(2 * np.cos(tp_tracker.get_value()), 2 * np.sin(tp_tracker.get_value())), 
                color = GREEN_B, buff = 0
            )
        )
        p_sec = always_redraw(
            lambda: Sector(
                outer_radius = 0.5, start_angle = PI / 4, angle = tp_tracker.get_value() - t_tracker.get_value(), 
                stroke_color = GREEN_D, fill_color = GREEN_D, stroke_width = 3, fill_opacity = 0.5
            ).shift(0.5 * DOWN)
        )
        dt_value = always_redraw(
            lambda: MathTex(
                r"\Delta t=" + f"{tp_tracker.get_value() - t_tracker.get_value():.3f}", font_size = 44, color = GREEN_B
            ).move_to(axes.c2p(3, 1.2))
        )
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value())), 
                end = axes.c2p(2 * np.cos(tp_tracker.get_value()), 2 * np.sin(tp_tracker.get_value())), color = RED, buff = 0
            )
        )
        rd_label = MathTex(
            r"(2\cos (t+\Delta t)-2\cos t, 2\sin (t+\Delta t)-2\sin t)", font_size = 33, color = RED
        ).move_to(axes.c2p(3.6, 2.7))
        self.play(
            AnimationGroup(ReplacementTransform(rderivative, rp_vector), Create(p_sec), Create(d_vector), lag_ratio = 0.6), 
            run_time = 1.8
        )
        self.play(ReplacementTransform(p_sec.copy(), dt_value), run_time = 1.4)
        self.play(ReplacementTransform(d_vector.copy(), rd_label), run_time = 1.4)
        self.wait()
        rd_label_dt = MathTex(
            r"\left (\frac{2\cos (t+\Delta t)-2\cos t}{\Delta t}, \frac{2\sin (t+\Delta t)-2\sin t}{\Delta t}\right )", font_size = 33,
            color = RED
        ).move_to(axes.c2p(3.6, 2.7))
        new_d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(np.sqrt(2), np.sqrt(2)), 
                end = axes.c2p(1.414 + (2 * np.cos(tp_tracker.get_value()) - 1.414) / (tp_tracker.get_value() - 9 * PI / 4), 1.414 + 2 * (np.sin(tp_tracker.get_value()) - 0.707) / (tp_tracker.get_value() - 9 * PI / 4)), 
                color = RED, buff = 0
            )
        )
        self.play(ReplacementTransform(rd_label, rd_label_dt), ReplacementTransform(d_vector, new_d_vector), run_time = 1.4)
        self.wait()
        lm_rd_label_dt = MathTex(
            r"\lim_{\Delta t \to 0}\left (\frac{2\cos (t+\Delta t)-2\cos t}{\Delta t}, \frac{2\sin (t+\Delta t)-2\sin t}{\Delta t}\right )", 
            font_size = 28, color = RED
        ).move_to(axes.c2p(3.6, 2.7))
        self.play(ReplacementTransform(rd_label_dt, lm_rd_label_dt), run_time = 1.4)
        self.wait()
        lm_rd_label = MathTex(r"\left ({(2\cos t)}', {(2\sin t)}'\right )", font_size = 44, color = RED).move_to(axes.c2p(3.6, 2.7))
        self.play(tp_tracker.animate.set_value(9 * PI / 4 + 0.01), ReplacementTransform(lm_rd_label_dt, lm_rd_label), run_time = 2)
        self.wait()
        rd_label = MathTex(r"\left (-2\sin t, 2\cos t\right )", font_size = 44, color = RED).move_to(axes.c2p(3.6, 2.7))
        self.play(ReplacementTransform(lm_rd_label, rd_label), run_time = 1.4)
        self.wait()
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value())), 
                end = axes.c2p(2 * (np.cos(t_tracker.get_value()) - np.sin(t_tracker.get_value())), 2 * (np.sin(t_tracker.get_value()) + np.cos(t_tracker.get_value()))), 
                color = RED, buff = 0
            )
        )
        self.play(ReplacementTransform(new_d_vector, d_vector), FadeOut(p_sec), FadeOut(dt_value), FadeOut(rp_vector))
        self.play(t_tracker.animate.set_value(4 * PI), run_time = 4)
        self.wait()
        self.play(FadeOut(sec), FadeOut(d_vector), FadeOut(rd_label), FadeOut(t_value), FadeOut(vnew), FadeOut(t))
        self.wait()
        t_tracker = ValueTracker(0)

        def neocircle(t):
            return axes.c2p(2 * np.cos(t / 2), 2 * np.sin(t / 2))
        
        moving_arc = always_redraw(lambda: ParametricFunction(neocircle, t_range = [0, t_tracker.get_value()], color = YELLOW))
        nmoving_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(0, 0), end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                color = YELLOW_B, buff = 0
            )
        )
        nmoving_dot = always_redraw(
            lambda: Dot(axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), color = YELLOW)
        )
        self.remove(moving_dot, moving_vector).add(moving_arc, nmoving_vector, nmoving_dot)
        rs_label = MathTex(r"\vec{r}(s)", font_size = 44, color = YELLOW_A).move_to(axes.c2p(3.5, 3.5))
        self.play(Flash(nmoving_dot, color = YELLOW, flash_radius = 0.3, line_length = 0.2, num_lines = 10, run_time = 1.5))
        self.play(t_tracker.animate.set_value(1), run_time = 1.6)
        s_label = always_redraw(
            lambda: MathTex(r"s=" + f"{t_tracker.get_value():.3f}", font_size = 44, color = YELLOW).move_to(axes.c2p(3.5, 1.5))
        )
        self.play(ReplacementTransform(moving_arc.copy(), s_label))
        self.wait(0.7)
        self.play(Wiggle(nmoving_vector))
        self.play(ReplacementTransform(nmoving_vector.copy(), rs_label))
        self.wait()
        sec = Sector(
            outer_radius = 0.5, start_angle = 0, angle = 1 / 2, stroke_color = YELLOW_D, fill_color = YELLOW_D, stroke_width = 3,
            fill_opacity = 0.5
        ).shift(0.5 * DOWN)
        self.add(sec).wait()
        group = VGroup(rs_label, sec)
        new_rs_label = MathTex(
            r"\vec{r}(s)= \left (2\cos \frac{s}{2}, 2\sin \frac{s}{2} \right )", font_size = 44, color = YELLOW_A
        ).move_to(axes.c2p(3.5, 3.5))
        d_label = MathTex(
            r"\frac{\mathrm{d} \vec{r}}{\mathrm{d} s} = \left (-\sin \frac{s}{2}, \cos \frac{s}{2} \right )", font_size = 44, color = RED
        ).move_to(axes.c2p(3.5, 2.5))
        dist_label = MathTex(
            r"\left \| \frac{\mathrm{d} \vec{r}}{\mathrm{d} s} \right \| \equiv 1", font_size = 44, color = RED
        ).move_to(axes.c2p(3.5, 2.5))
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2) - np.sin(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2) + np.cos(t_tracker.get_value() / 2)), 
                color = RED, buff = 0
            )
        )
        self.play(ReplacementTransform(group, new_rs_label), run_time = 1.4)
        self.wait()
        self.play(ReplacementTransform(new_rs_label.copy(), d_label), Create(d_vector), run_time = 1.4)
        self.wait()
        self.play(ReplacementTransform(d_label, dist_label), run_time = 1.4)
        self.play(Wiggle(d_vector))
        self.wait()
        self.play(t_tracker.animate.set_value(4 * PI), run_time = 4)
        self.wait()
        self.remove(moving_arc, s_label, nmoving_dot, nmoving_vector).wait()
        vector = [0] * 114
        vvector = VGroup()

        for i in range(10):
            m = PI * (i + 1) / 5
            vector[i] = Arrow(
                start = axes.c2p(2 * np.cos(m), 2 * np.sin(m)), 
                end = axes.c2p(2 * np.cos(m) - np.sin(m), 2 * np.sin(m) + np.cos(m)), color = RED, buff = 0
            )
            self.play(Create(vector[i]), run_time = 0.25)
            vvector.add(vector[i])

        self.remove(d_vector).wait()

        for i in range(10):
            m = PI * (i + 1) / 5
            self.play(vvector[i].animate.shift(-2 * np.cos(m) * RIGHT - 2 * np.sin(m) * UP), run_time = 0.2)

        def yellow_circle(t):
            return axes.c2p(np.cos(t), np.sin(t))
        
        ycirc = ParametricFunction(yellow_circle, t_range = [0, 2 * PI], color = YELLOW)
        vvector.remove(vector[7])
        self.wait()
        self.play(Create(ycirc), run_time = 1.3)
        self.play(
            FadeOut(vvector), circ.animate.set_stroke(opacity = 0.3), new_rs_label.animate.set_opacity(0.3), run_time = 1.4
        )
        self.wait()
        green_vector = Arrow(
            start = axes.c2p(-np.sin(8 * PI / 5), np.cos(8 * PI / 5)), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(8 * PI / 5), np.cos(8 * PI / 5) - np.sin(8 * PI / 5)), 
            color = GREEN, buff = 0
        )
        green_vector_1 = Arrow(
            start = axes.c2p(-np.sin(8 * PI / 5), np.cos(8 * PI / 5)), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(43 * PI / 30), np.cos(8 * PI / 5) - np.sin(43 * PI / 30)), 
            color = GREEN, buff = 0
        )
        green_vector_2 = Arrow(
            start = axes.c2p(-np.sin(8 * PI / 5), np.cos(8 * PI / 5)), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(9 * PI / 5), np.cos(8 * PI / 5) - np.sin(9 * PI / 5)), 
            color = GREEN, buff = 0
        )
        redp_vector = Arrow(
            start = axes.c2p(0, 0), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(43 * PI / 30), np.cos(8 * PI / 5) - np.sin(43 * PI / 30)), 
            color = RED_A, buff = 0
        )
        redm_vector = Arrow(
            start = axes.c2p(0, 0), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(9 * PI / 5), np.cos(8 * PI / 5) - np.sin(9 * PI / 5)), 
            color = RED_A, buff = 0
        )
        self.play(Create(green_vector))
        self.play(ReplacementTransform(green_vector, green_vector_1), run_time= 1.2)
        self.play(Create(redp_vector))
        self.wait()
        self.play(Uncreate(redp_vector), run_time = 0.5)
        self.play(ReplacementTransform(green_vector_1, green_vector_2), run_time= 1.2)
        self.play(Create(redm_vector))
        self.wait()
        self.play(Uncreate(redm_vector), run_time = 0.5)
        self.wait()
        green_vector = Arrow(
            start = axes.c2p(-np.sin(8 * PI / 5), np.cos(8 * PI / 5)), 
            end = axes.c2p(-np.sin(8 * PI / 5) - np.cos(8 * PI / 5), np.cos(8 * PI / 5) - np.sin(8 * PI / 5)), 
            color = GREEN, buff = 0
        )
        self.play(ReplacementTransform(green_vector_2, green_vector), run_time= 1.2)
        self.wait()
        proof0 = MathTex(r"\left \| \vec{r}(t) \right \| \equiv 1", font_size = 44, color = GREEN)
        proof1 = MathTex(r"\Rightarrow \left \| \vec{r}(t) \right \|^2=1\Rightarrow \vec{r}^2(t) =1", font_size = 44, color = GREEN)
        proof2 = MathTex(
            r"\Rightarrow {\left (\vec{r}^2(t)\right )}'= 2\vec{r}(t)\cdot {\left (\vec{r}(t) \right )}'=0", 
            font_size = 44, color = GREEN
        )
        proof3 = MathTex(r"\Rightarrow \vec{r}(t)\perp {(\vec{r}(t))}'", font_size = 44, color = GREEN)
        proof = VGroup(proof0, proof1, proof2, proof3).arrange(DOWN, buff = 0.3).move_to(axes.c2p(-3.6, 2.5)).set_z_index(2)
        prect = SurroundingRectangle(
            proof, color = YELLOW_A, buff = 0.1, stroke_width = 4, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        self.add(proof, prect).wait()
        self.remove(proof, prect).wait()

# 展示选取不同参数的两个圆的参数方程的例子
class TwoExamples(Scene):
    def construct(self):
        small_tip_config = {
            "tip_length": 0.08,
            "tip_width": 0.14
        }
        left_screen = Rectangle(height = 6.5, width = 6.5, color = YELLOW, stroke_width = 4)
        right_screen = Rectangle(height = 6.5, width = 6.5, color = YELLOW, stroke_width = 4)
        left_screen.to_edge(LEFT, buff = 0.25)
        right_screen.to_edge(RIGHT, buff = 0.25)
        left_axes = Axes(
            x_range = [-3, 3, 1], y_range = [-3, 3, 1], x_length = 6, y_length = 6, axis_config = {**small_tip_config}
        ).move_to(left_screen.get_center())
        right_axes = Axes(
            x_range = [-3, 3, 1], y_range = [-3, 3, 1], x_length = 6, y_length = 6, axis_config = {**small_tip_config}
        ).move_to(right_screen.get_center())

        def l_circle(t):
            return left_axes.c2p(np.cos(t), np.sin(t))
        
        def r_circle(t):
            return right_axes.c2p(np.cos(t), np.sin(t))
        
        lcirc = ParametricFunction(l_circle, t_range = [0, 2 * PI], color = TEAL_A)
        rcirc = ParametricFunction(r_circle, t_range = [0, 2 * PI], color = TEAL_A)
        t_tracker = ValueTracker(0)
        l_equa = MathTex(r"(\cos t, \sin t)", font_size = 36, color = YELLOW_A).move_to(left_axes.c2p(-1.9, 2.5))
        l_deri = MathTex(r"(-\sin t, \cos t)", font_size = 36, color = RED).move_to(left_axes.c2p(-1.7, 1.9))
        lmoving_dot = always_redraw(
            lambda: Dot(left_axes.c2p(np.cos(t_tracker.get_value()), np.sin(t_tracker.get_value())), color = YELLOW)
        )
        lmoving_vector = always_redraw(
            lambda: Arrow(
                start = left_axes.c2p(0, 0), end = left_axes.c2p(np.cos(t_tracker.get_value()), np.sin(t_tracker.get_value())), 
                color = YELLOW_B, buff = 0
            )
        )
        ld_vector = always_redraw(
            lambda: Arrow(
                start = left_axes.c2p(np.cos(t_tracker.get_value()), np.sin(t_tracker.get_value())), 
                end = left_axes.c2p(np.cos(t_tracker.get_value()) - np.sin(t_tracker.get_value()), np.sin(t_tracker.get_value()) + np.cos(t_tracker.get_value())), 
                color = RED, buff = 0
            )
        )
        t_value = always_redraw(
            lambda: MathTex(r"t=" + f"{t_tracker.get_value():.3f}", font_size = 36, color = YELLOW).move_to(left_axes.c2p(2, 0.3))
        )
        s_tracker = ValueTracker(0)
        r_equa = MathTex(r"(\cos (t^2), \sin (t^2))", font_size = 36, color = YELLOW_A).move_to(right_axes.c2p(-1.9, 2.5))
        r_deri = MathTex(r"(-2t\sin (t^2), 2t\cos (t^2))", font_size = 30, color = RED).move_to(right_axes.c2p(-1.7, 1.9))
        rmoving_dot = always_redraw(
            lambda: Dot(right_axes.c2p(np.cos(s_tracker.get_value() ** 2), np.sin(s_tracker.get_value() ** 2)), color = YELLOW)
        )
        rmoving_vector = always_redraw(
            lambda: Arrow(
                start = right_axes.c2p(0, 0), 
                end = right_axes.c2p(np.cos(s_tracker.get_value() ** 2), np.sin(s_tracker.get_value() ** 2)), color = YELLOW_B, buff = 0
            )
        )
        rd_vector = always_redraw(
            lambda: Arrow(
                start = right_axes.c2p(np.cos(s_tracker.get_value() ** 2), np.sin(s_tracker.get_value() ** 2)), 
                end = right_axes.c2p(np.cos(s_tracker.get_value() ** 2) - 2 * s_tracker.get_value() * np.sin(s_tracker.get_value() ** 2), np.sin(s_tracker.get_value() ** 2) + 2 * s_tracker.get_value() * np.cos(s_tracker.get_value() ** 2)), 
                color = RED, buff = 0
            )
        )
        s_value = always_redraw(
            lambda: MathTex(r"t=" + f"{s_tracker.get_value():.3f}", font_size = 36, color = YELLOW).move_to(right_axes.c2p(2, 0.3))
        )
        self.add(
            left_screen, right_screen, left_axes, right_axes, lcirc, rcirc, lmoving_dot, lmoving_vector, rmoving_dot, rmoving_vector,
            ld_vector, rd_vector, l_equa, l_deri, r_equa, r_deri, t_value, s_value
        )
        self.wait()
        self.play(t_tracker.animate.set_value(2 * PI), s_tracker.animate.set_value(np.sqrt(2 * PI)), run_time = 4)
        self.wait()

# 一个|dr / ds|不恒为1的例子
class StrangeCurve(Scene):
    def construct(self):
        axes = Axes(x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9)
        grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9, background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)

        def curve(t):
            return axes.c2p(t ** 2 / 2, t ** 3 / 3)
        
        the_curve = ParametricFunction(curve, t_range = [-3, 3], color = TEAL_A)
        self.add(grid)
        curve_label = MathTex(
            r"\vec{r}(t)= \left (\frac{t^2}{2}, \frac{t^3}{3} \right )", font_size = 44, color = YELLOW_A
        ).shift(3.2 * UP).set_z_index(2)
        curve_rect = SurroundingRectangle(
            curve_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vcurve = VGroup(curve_rect, curve_label)
        t_tracker = ValueTracker(-2)
        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(t_tracker.get_value() ** 2 / 2, t_tracker.get_value() ** 3 / 3), color = YELLOW)
        )
        moving_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(0, 0), end = axes.c2p(t_tracker.get_value() ** 2 / 2, t_tracker.get_value() ** 3 / 3), 
                color = YELLOW_B, buff = 0
            )
        )
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(t_tracker.get_value() ** 2 / 2, t_tracker.get_value() ** 3 / 3), 
                end = axes.c2p(t_tracker.get_value() ** 2 / 2 + t_tracker.get_value(), t_tracker.get_value() ** 3 / 3 + t_tracker.get_value() ** 2), 
                color = RED, buff = 0
            )
        )
        d_label = MathTex(
            r"\frac{\mathrm{d} \vec{r}}{\mathrm{d} t} = (t, t^2)", font_size = 44, color = RED
        ).move_to(axes.c2p(4.5, 2.5))
        t_value = always_redraw(
            lambda: MathTex(r"t=" + f"{t_tracker.get_value():.3f}", font_size = 44, color = YELLOW).move_to(axes.c2p(4.5, 0.5))
        )
        d_value = always_redraw(
            lambda: MathTex(
                r"\frac{\mathrm{d} \vec{r}}{\mathrm{d} t} = (" + f"{t_tracker.get_value():.3f}" + r"," + f"{t_tracker.get_value() ** 2:.3f}" + r")", 
                font_size = 44, color = RED
            ).move_to(axes.c2p(4.5, 2.5))
        )
        self.play(Create(the_curve), Create(vcurve), run_time = 0.8)
        self.play(Create(moving_dot), Create(moving_vector), run_time = 1.2)
        self.play(
            Create(d_vector), ReplacementTransform(curve_label.copy(), d_label), ReplacementTransform(moving_dot.copy(), t_value), 
            run_time = 1.6
        )
        self.wait()
        self.play(ReplacementTransform(d_label, d_value))
        self.wait()
        self.play(t_tracker.animate.set_value(0), run_time = 2.5)
        self.wait()
        self.play(t_tracker.animate.set_value(2), run_time = 2.5)
        self.wait()

# 一个曲线曲率不断变化的例子
class SineCurve(Scene):
    def construct(self):
        axes = Axes(x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9)
        grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9, background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)

        def sinefunc(t):
            return axes.c2p(t, 3 * np.sin(t))
        
        sine = ParametricFunction(sinefunc, t_range = [-8, 8], color = TEAL_A)
        t_tracker = ValueTracker(- 1.64 * PI)
        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(t_tracker.get_value(), 3 * np.sin(t_tracker.get_value())), color = YELLOW).set_z_index(2)
        )
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(t_tracker.get_value(), 3 * np.sin(t_tracker.get_value())), 
                end = axes.c2p(t_tracker.get_value() + 1 / np.sqrt(1 + 9 * np.cos(t_tracker.get_value()) ** 2), 3 * np.sin(t_tracker.get_value()) + 3 * np.cos(t_tracker.get_value()) / np.sqrt(1 + 9 * np.cos(t_tracker.get_value()) ** 2)), 
                color = RED, buff = 0
            )
        )
        dd_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(t_tracker.get_value(), 3 * np.sin(t_tracker.get_value())), 
                end = axes.c2p(t_tracker.get_value() + 9 * np.sin(t_tracker.get_value()) * np.cos(t_tracker.get_value()) / (1 + 9 * np.cos(t_tracker.get_value()) ** 2) ** 1.5, 3 * np.sin(t_tracker.get_value()) - 3 * np.sin(t_tracker.get_value()) / (1 + 9 * np.cos(t_tracker.get_value()) ** 2) ** 1.5), 
                color = GREEN, buff = 0
            )
        )
        d_label = MathTex(r"\left \| \dot{r} \right \| \equiv 1", font_size = 44, color = RED).move_to(axes.c2p(4.7, 3.5))
        dd_label = always_redraw(
            lambda: MathTex(
                r"\left \| \ddot{r} \right \|=" + f"{np.sqrt((9 * np.sin(t_tracker.get_value()) * np.cos(t_tracker.get_value()) / (1 + 9 * np.cos(t_tracker.get_value()) ** 2) ** 1.5) ** 2 + (3 * np.sin(t_tracker.get_value()) / (1 + 9 * np.cos(t_tracker.get_value()) ** 2) ** 1.5) ** 2):.3f}",
                font_size = 44, color = GREEN
            ).move_to(axes.c2p(4.7, 2.5))
        )
        self.add(grid, sine, moving_dot, d_vector, dd_vector, d_label, dd_label).wait()
        self.play(t_tracker.animate.set_value(-0.62 * PI), run_time = 3)
        self.wait()
        self.play(t_tracker.animate.set_value(PI / 4), run_time = 3)
        self.wait()
        self.play(t_tracker.animate.set_value(PI / 2), run_time = 3)
        self.wait()
        self.play(t_tracker.animate.set_value(1.33 * PI), run_time = 3)
        self.wait()
        dd_label.clear_updaters()
        moving_dot.clear_updaters()
        d_vector.clear_updaters()
        dd_vector.clear_updaters()
        integrity = VGroup(grid, moving_dot, d_vector, dd_vector, d_label, dd_label)
        kappa = MathTex(r"\kappa", font_size = 340, color = ORANGE).set_z_index(1)
        rkappa = SurroundingRectangle(kappa, color = YELLOW, buff = 0.2, stroke_width = 6).set_z_index(1)
        self.play(integrity.animate.set_opacity(0.3), sine.animate.set_stroke(opacity = 0.3), Create(kappa))
        self.wait(0.8)
        self.play(ShowPassingFlash(rkappa), time_width = 0.6, run_time = 1.5)
        self.wait()

# 得到二维Frenet标架
class TwoDimFrame(Scene):
    def construct(self):
        axes = Axes(x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9)
        grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-4, 5, 1], x_length = 16, y_length = 9, background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)
        
        def circle(t):
            return axes.c2p(2 * np.cos(t), 2 * np.sin(t))
        
        circ = ParametricFunction(circle, t_range = [0, 2 * PI], color = TEAL_A)
        rs_label = MathTex(
            r"\vec{r}(s)= \left (2\cos \frac{s}{2}, 2\sin \frac{s}{2} \right )", font_size = 44, color = YELLOW_A
        ).move_to(axes.c2p(3.5, 3.5))
        d_label = MathTex(
            r"\left \| \dot{r} \right \| \equiv 1", font_size = 44, color = RED
        ).move_to(axes.c2p(3.5, 2.5))
        dd_label = MathTex(
            r"\kappa = \left \| \ddot{r} \right \| \equiv \frac{1}{2}", font_size = 44, color = GREEN
        ).move_to(axes.c2p(3.5, 1.5))
        ndd_label = MathTex(
            r"\left \| \frac{\ddot{r}}{\kappa} \right \| \equiv 1", font_size = 44, color = GREEN
        ).move_to(axes.c2p(3.5, 1.5))
        t_tracker = ValueTracker(0)
        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), color = YELLOW)
        )
        moving_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(0, 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                color = YELLOW_A, buff = 0, max_tip_length_to_length_ratio = 0.08
            )
        )
        d_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2) - np.sin(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2) + np.cos(t_tracker.get_value() / 2)), 
                color = RED, buff = 0
            )
        )
        dd_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2) - 0.5 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2) - 0.5 * np.sin(t_tracker.get_value() / 2)), 
                color = GREEN, buff = 0, max_tip_length_to_length_ratio = 0.4
            ).set_stroke(width = 4)
        )
        self.add(grid, circ, rs_label, moving_vector, d_label, dd_label, moving_dot, d_vector, dd_vector).wait()
        self.play(t_tracker.animate.set_value(4 * PI), run_time = 4)
        self.wait()
        self.play(
            Wiggle(d_vector, scale_value = 1.3, rotation_angle = 15 * DEGREES), 
            Wiggle(dd_vector, scale_value = 1.3, rotation_angle = 15 * DEGREES)
        )
        self.wait()
        ndd_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2) - np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2) - np.sin(t_tracker.get_value() / 2)), 
                color = GREEN, buff = 0
            ).set_stroke(width = 4)
        )
        self.play(ReplacementTransform(dd_vector, ndd_vector), ReplacementTransform(dd_label, ndd_label), run_time = 1.4)
        self.wait()
        self.play(t_tracker.animate.set_value(4.25 * PI))
        self.wait(0.5)
        inclined_grid = NumberPlane(
            x_range = [-12, 12, 1], y_range = [-8, 8, 1], x_length = 24, y_length = 16, 
            background_line_style = {"stroke_color": GREEN_A, "stroke_opacity": 0.4}, axis_config = {"stroke_opacity": 0},
            faded_line_style = {"stroke_color": GREEN, "stroke_opacity": 0.4}
        ).move_to(axes.c2p(2 * np.cos(0.125 * PI), 2 * np.sin(0.125 * PI))).set_stroke(background = True)
        inclined_grid.rotate(0.125 * PI)
        self.play(GrowFromCenter(inclined_grid), run_time = 1.6)
        self.wait()
        nd_label = MathTex(r"\vec{\alpha} : = \dot{r}", font_size = 44, color = RED).move_to(axes.c2p(3.5, 2.5))
        nndd_label = MathTex(r"\vec{\beta} : = \frac{\ddot{r}}{\kappa}", font_size = 44, color = GREEN).move_to(axes.c2p(3.5, 1.5))
        self.play(FadeOut(inclined_grid), run_time = 0.8)
        self.play(ReplacementTransform(d_label, nd_label), ReplacementTransform(ndd_label, nndd_label), run_time = 1.2)
        self.wait()
        dd_label2 = MathTex(r"\kappa \vec{\beta} = \ddot{r}", font_size = 44, color = GREEN).move_to(axes.c2p(3.5, 1.5))
        self.play(ReplacementTransform(nndd_label, dd_label2), run_time = 1.2)
        self.wait()
        dd_label3 = MathTex(r"\dot{\vec{\alpha}} = \kappa \vec{\beta}", font_size = 44, color = GREEN).move_to(axes.c2p(3.5, 1.5))
        self.play(ReplacementTransform(dd_label2, dd_label3), run_time = 1.2)
        self.wait()
        ddd_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2)), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value() / 2) + 0.5 * np.sin(t_tracker.get_value() / 2), 2 * np.sin(t_tracker.get_value() / 2) - 0.5 * np.cos(t_tracker.get_value() / 2)), 
                color = RED_A, buff = 0, max_tip_length_to_length_ratio = 0.4
            ).set_stroke(width = 4)
        )
        ddd_label = MathTex(r"\dot{\vec{\beta}} = -\kappa \vec{\alpha}", font_size = 44, color = RED_A).move_to(axes.c2p(3.65, 2.5))
        self.play(Create(ddd_vector), ReplacementTransform(nd_label, ddd_label), run_time = 1.2)
        self.wait()
        self.play(ddd_label.animate.shift(DOWN), dd_label3.animate.shift(UP), run_time = 1.2)
        self.wait()
        self.play(FadeOut(ddd_vector), ddd_label.animate.set_color(RED), dd_label3.animate.set_color(GREEN), run_time = 1.2)
        self.wait()
        label = VGroup(ddd_label, dd_label3)
        matrix0 = MathTex(r"\begin{pmatrix} \dot{\vec{\alpha }} \\ \dot{\vec{\beta}} \end{pmatrix}", font_size = 44, color = GREEN)
        matrix1 = MathTex(r"=", font_size = 44, color = YELLOW_A)
        matrix2 = MathTex(r"\begin{pmatrix} 0 & \kappa \\ -\kappa & 0 \end{pmatrix}", font_size = 44, color = ORANGE)
        matrix3 = MathTex(r"\begin{pmatrix} \vec{\alpha } \\ \vec{\beta} \end{pmatrix}", font_size = 44, color = RED)
        matrix = VGroup(matrix0, matrix1, matrix2, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(4, 2))
        self.play(ReplacementTransform(label, matrix), run_time = 1.6)
        self.wait()
        matrix4 = MathTex(r"\kappa", font_size = 44, color = ORANGE)
        matrix5 = MathTex(r"\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}", font_size = 44, color = YELLOW_A)
        small_matrix = VGroup(matrix4, matrix5).arrange(RIGHT, buff = 0.1)
        new_matrix = VGroup(matrix0, matrix1, small_matrix, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(4, 2))
        self.play(ReplacementTransform(matrix, new_matrix), run_time = 1.6)
        self.wait()
        mrect = SurroundingRectangle(matrix5, color = YELLOW, buff = 0.05, stroke_width = 4)
        self.play(ShowPassingFlash(mrect), time_width = 0.6, run_time = 1.5)
        self.wait(0.5)
        krect = SurroundingRectangle(matrix4, color = YELLOW, buff = 0.05, stroke_width = 4)
        self.play(ShowPassingFlash(krect), time_width = 0.6, run_time = 1.5)
        self.wait()
        frect = SurroundingRectangle(matrix, color = YELLOW, buff = 0.1, stroke_width = 4)
        self.play(Create(frect), run_time = 1.5)
        self.wait()

# 旋转变换与缩放变换
class RotateAndTract(Scene):
    def construct(self):
        small_tip_config = {
            "tip_length": 0.08,
            "tip_width": 0.14
        }
        left_screen = Rectangle(height = 6.5, width = 6.5, color = YELLOW, stroke_width = 4)
        right_screen = Rectangle(height = 6.5, width = 6.5, color = YELLOW, stroke_width = 4)
        left_screen.to_edge(LEFT, buff = 0.25)
        right_screen.to_edge(RIGHT, buff = 0.25)
        left_axes = Axes(
            x_range = [-1.5, 1.5, 1], y_range = [-1.5, 1.5, 1], x_length = 6, y_length = 6, axis_config = {**small_tip_config}
        ).move_to(left_screen.get_center())
        right_axes = Axes(
            x_range = [-1.5, 1.5, 1], y_range = [-1.5, 1.5, 1], x_length = 6, y_length = 6, axis_config = {**small_tip_config}
        ).move_to(right_screen.get_center())
        t_tracker = ValueTracker(0)
        lmoving_vector = always_redraw(
            lambda: Arrow(
                start = left_axes.c2p(0, 0), end = left_axes.c2p(np.cos(t_tracker.get_value()), np.sin(t_tracker.get_value())), 
                color = RED, buff = 0
            )
        )
        r_vector = Arrow(start = right_axes.c2p(0, 0), end = right_axes.c2p(1, 0), color = GREEN, buff = 0)
        s_tracker = ValueTracker(0)
        rmoving_vector = always_redraw(
            lambda: Arrow(
                start = right_axes.c2p(0, 0), 
                end = right_axes.c2p(0.5 * np.cos(s_tracker.get_value()), 0.5 * np.sin(s_tracker.get_value())), color = GREEN, buff = 0
            )
        )
        self.add(left_screen, right_screen, left_axes, right_axes, lmoving_vector, r_vector).wait()
        self.play(t_tracker.animate.set_value(PI / 2), ReplacementTransform(r_vector, rmoving_vector), run_time = 1.4)
        self.wait()
        lmoving_vector.clear_updaters()
        l_vector = Arrow(start = left_axes.c2p(0, 0), end = left_axes.c2p(0, 0.5), color = RED, buff = 0)
        self.play(s_tracker.animate.set_value(PI / 2), ReplacementTransform(lmoving_vector, l_vector), run_time = 1.4)
        self.wait()

# 二维到三维的过渡
class TwoDtoThreeD(Scene):
    def construct(self):
        twod = MathChi(r"\text{二维}").scale(2.4)
        arrow = MathTex(r"\Longrightarrow", font_size = 130, color = YELLOW_A)
        threed = MathChi(r"\text{三维}").scale(2.4)
        quest = MathTex(r"?", font_size = 180, color = RED)
        integrity = VGroup(twod, arrow, threed).arrange(RIGHT, buff = 0.3)
        self.add(twod)
        self.play(AnimationGroup(Create(arrow), Write(threed), lag_ratio = 0.6), run_time = 1.8)
        self.wait(0.8)
        self.play(DrawBorderThenFill(quest), run_time = 1.4)
        self.wait()
