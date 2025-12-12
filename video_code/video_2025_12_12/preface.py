from manim import *

config.background_color = "#000012"  # 设置Scene背景颜色

# 视频开头的引入部分
class Preface(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 0 * DEGREES, theta = -90 * DEGREES)
        axes = ThreeDAxes(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], z_range = [-2, 6, 1], 
            x_length = 8, y_length = 8, z_length = 8, axis_config = {"tip_width": 0.12, "tip_height": 0.15}
        )
        grid = NumberPlane(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], x_length = 8, y_length = 8, 
            background_line_style = {"stroke_opacity": 0.4}
        )
        focus0 = Dot(axes.coords_to_point(-np.sqrt(5), 0, 0), color = YELLOW).set_z_index(1)
        focus1 = Dot(axes.coords_to_point(np.sqrt(5), 0, 0), color = YELLOW).set_z_index(1)
        label0 = MathTex(r"F_1", color = YELLOW, font_size = 44).next_to(focus0, DOWN, buff = 0.2)
        label1 = MathTex(r"F_2", color = YELLOW, font_size = 44).next_to(focus1, DOWN, buff = 0.2)
        distance_label = MathTex(
            r"\left| F_{1}A \right|+\left| F_{2}A \right|=6", font_size = 44, color = YELLOW_A
        ).shift(3.2 * UP).set_z_index(2)
        rect = SurroundingRectangle(distance_label, color = YELLOW, buff = 0.2, stroke_width = 4, fill_color = "#000012")
        neorect = SurroundingRectangle(
            distance_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vdis = VGroup(distance_label, neorect)
        moving_dot = Dot(color = YELLOW).shift(2 * UP).set_z_index(1)
        moving_label = MathTex(r"A", font_size = 44, color = YELLOW).next_to(moving_dot, UP, buff = 0.2)
        line0 = Line(focus0.get_center(), moving_dot.get_center(), color = YELLOW_E)
        line1 = Line(focus1.get_center(), moving_dot.get_center(), color = YELLOW_E)
        self.play(Create(focus0), Create(focus1), Write(label0), Write(label1), run_time = 1.4)
        self.wait()
        
        # 更新点到焦点的连接线函数
        def update_lines(mob):
            line0.put_start_and_end_on(focus0.get_center(), moving_dot.get_center())
            line1.put_start_and_end_on(focus1.get_center(), moving_dot.get_center())
        
        # 创建轨迹
        trajectory = VMobject(color = TEAL_A)
        trajectory.set_points_as_corners([moving_dot.get_center(), moving_dot.get_center()])
        
        # 更新轨迹函数
        def update_trajectory(mob):
            previous_path = mob.copy()
            previous_path.add_points_as_corners([moving_dot.get_center()])
            mob.become(previous_path)
        
        trajectory.add_updater(update_trajectory)
        self.add(moving_dot, trajectory)
        self.play(Create(line0), Create(line1), Create(moving_label), run_time = 1.2)
        line0.add_updater(update_lines)
        line1.add_updater(update_lines)
        self.wait()
        self.play(Write(distance_label), run_time = 1.3)
        self.wait()
        self.play(ShowPassingFlash(rect), time_width = 0.6, run_time = 1.5)
        self.wait()
        
        # 动画：让点沿椭圆轨迹移动
        for t in np.linspace(PI / 2, 2.5 * PI, 60):
            x = 3 * np.cos(t)
            y = 2 * np.sin(t)
            x_ = 3.4 * np.cos(t)
            y_ = 2.4 * np.sin(t)
            self.play(
                moving_dot.animate.move_to([x, y, 0]), moving_label.animate.move_to([x_, y_, 0]), run_time = 0.033, rate_func = smooth
            )
        
        self.wait(3)
        line0.remove_updater(update_lines)
        line1.remove_updater(update_lines)
        trajectory.remove_updater(update_trajectory)
        self.play(Uncreate(line0), Uncreate(line1), FadeOut(moving_label), FadeOut(moving_dot), run_time = 1.2)
        self.wait()
        origin = Dot()
        origin_label = MathTex(r"O", font_size = 48).next_to(origin, DL, buff = 0.16)
        self.play(Create(origin), Write(origin_label), run_time = 1.3)
        self.add(neorect).wait(0.6)
        self.play(Create(axes), Create(grid), run_time = 1.6)
        self.wait()
        neolabel0 = MathTex(r"F_1(-\sqrt{5},0)", color = YELLOW, font_size = 44).next_to(focus0, DOWN, buff = 0.2).set_z_index(1)
        neolabel1 = MathTex(r"F_2(\sqrt{5},0)", color = YELLOW, font_size = 44).next_to(focus1, DOWN, buff = 0.2).set_z_index(1)
        vf1 = VGroup(focus0, neolabel0)
        vf2 = VGroup(focus1, neolabel1)
        dot = Dot(axes.c2p(1.2, 2 * np.sqrt(21) / 5, 0), color = YELLOW)
        dot_label = MathTex(r"A(x,y)", font_size = 44, color = YELLOW).next_to(dot, UR, buff = 0.14)
        vdot = VGroup(dot, dot_label)
        self.play(ReplacementTransform(label0, neolabel0), ReplacementTransform(label1, neolabel1), Create(vdot), run_time = 1.2)
        equation = MathTex(
            r"\sqrt{(x+\sqrt{5})^2+y^2}+\sqrt{(x-\sqrt{5})^2+y^2}=6", font_size = 44, color = YELLOW_A
        ).shift(3.2 * UP).set_z_index(2)
        self.wait(0.8)
        equa_rect = SurroundingRectangle(
            equation, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vequa = VGroup(equation, equa_rect)
        self.play(ReplacementTransform(vdis, vequa), run_time = 1.2)
        self.wait(0.7)
        ellipse = MathTex(r"\frac{x^2}{9}+\frac{y^2}{4}=1", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        self.wait(0.8)
        elli_rect = SurroundingRectangle(
            ellipse, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        velli = VGroup(ellipse, elli_rect)
        self.play(ReplacementTransform(vequa, velli), run_time = 1.2)
        self.wait()
        self.play(FadeOut(vdot), run_time = 0.8)
        self.wait(0.8)

        def hyperbola_right(t):
            a, b = 2, 1  
            return axes.coords_to_point(a * np.cosh(t), b * np.sinh(t), 0)
        
        def hyperbola_left(t):
            a, b = 2, 1
            return axes.coords_to_point(-a * np.cosh(t), b * np.sinh(t), 0)
        
        # 创建双曲线
        hyperbola_r = ParametricFunction(hyperbola_right, t_range = [-1.4, 1.4], color = TEAL_A)
        hyperbola_l = ParametricFunction(hyperbola_left, t_range = [-1.4, 1.4], color = TEAL_A)
        hyperbola = VGroup(hyperbola_l, hyperbola_r)
        hyper_label = MathTex(r"\frac{x^2}{4}-y^2=1", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        hyper_rect = SurroundingRectangle(
            hyper_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vhyper = VGroup(hyper_label, hyper_rect)
        self.play(ReplacementTransform(trajectory, hyperbola), ReplacementTransform(velli, vhyper), run_time = 1.6)
        self.wait(0.8)

        def parabola_func(x):
            return axes.coords_to_point(x, x**2 / 2, 0)
        
        parabola = ParametricFunction(parabola_func, t_range = [-3, 3], color = TEAL_A)
        para_label = MathTex(r"y=\frac{x^2}{2}", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        para_rect = SurroundingRectangle(
            para_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vpara = VGroup(para_label, para_rect)
        self.play(
            ReplacementTransform(hyperbola, parabola), ReplacementTransform(vhyper, vpara), FadeOut(vf1), FadeOut(vf2), run_time = 1.6
        )
        self.wait(0.8)
        circle = Circle(radius = 2, color = TEAL_A)
        cir_label = MathTex(r"x^2+y^2=4", font_size = 44, color = YELLOW_A).shift(3.2 * UP).set_z_index(2)
        cir_rect = SurroundingRectangle(
            cir_label, buff = 0.2, stroke_width = 0, fill_color = "#000012", fill_opacity = 0.8
        ).set_z_index(1)
        vcir = VGroup(cir_label, cir_rect)
        self.play(ReplacementTransform(parabola, circle), ReplacementTransform(vpara, vcir), run_time = 1.6)
        self.wait(0.8)

        def helix_func(t):
            return axes.coords_to_point(2 * np.cos(t), 2 * np.sin(t), t / 2)
        
        helix = ParametricFunction(helix_func, t_range = [0, 2 * PI], color = TEAL_A)

        def circle_func(t):
            return np.array([2 * np.cos(t), 2 * np.sin(t), 0])
                
        # 获取曲线上一点处的单位切向量
        def get_tangent_vector(func, t, delta = 0.01):
            r_t = func(t)
            r_t_plus = func(t + delta)
            return (r_t_plus - r_t) / np.linalg.norm(r_t_plus - r_t)
        
        # 获取曲线上一点处的单位法向量
        def get_normal_vector(func, t, delta = 0.01):
            T_t = get_tangent_vector(func, t)
            T_t_plus = get_tangent_vector(func, t + delta)
            return (T_t_plus - T_t) / np.linalg.norm(T_t_plus - T_t)
        
        # 计算曲线上一点处的单位副法向量
        def get_binormal_vector(func, t):
            T = get_tangent_vector(func, t)
            N = get_normal_vector(func, t)
            return np.cross(T, N)
    
        t_tracker = ValueTracker(0)
        moving_dot = always_redraw(
            lambda: Dot(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), color = YELLOW
            ).set_z_index(1)
        )
        moving_vector = always_redraw(
            lambda: Arrow(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0) + get_tangent_vector(circle_func, t_tracker.get_value()), 
                buff = 0, color = RED
            )
        )
        self.play(Create(moving_dot), Create(moving_vector), run_time = 1.3)
        self.play(t_tracker.animate.set_value(PI), run_time = 2.2)
        self.wait()
        self.play(FadeOut(moving_dot), FadeOut(moving_vector), FadeOut(vcir), run_time = 0.8)
        self.wait(0.6)
        self.move_camera(phi = 60 * DEGREES, theta = 30 * DEGREES, distance = 0, run_time = 2.5)
        self.play(ReplacementTransform(circle, helix), run_time = 1.6)
        t_tracker = ValueTracker(0)
        frenet_l = MathTex(r"\{", font_size = 48)
        dot = MathTex(r"\vec{r};", font_size = 48, color = YELLOW_B)
        alpha = MathTex(r"\vec{\alpha},", font_size = 48, color = RED)
        beta = MathTex(r"\vec{\beta},", font_size = 48, color = GREEN)
        gamma = MathTex(r"\vec{\gamma}", font_size = 48, color = BLUE)
        frenet_r = MathTex(r"\}", font_size = 48)
        frenet = VGroup(frenet_l, dot, alpha, beta, gamma, frenet_r).arrange(RIGHT, buff = 0.1).shift(3.8 * LEFT + 2.8 * UP)
        moving_dot = always_redraw(
            lambda: Dot3D(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), color = YELLOW
            )
        )
        moving_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(0, 0, 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                color = YELLOW_B
            )
        )
        moving_a_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_tangent_vector(helix_func, t_tracker.get_value()), 
                color = RED
            )
        )
        moving_b_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_normal_vector(helix_func, t_tracker.get_value()), 
                color = GREEN
            )
        )
        moving_y_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_binormal_vector(helix_func, t_tracker.get_value()), 
                color = BLUE
            )
        )
        moving_frame = VGroup(moving_dot, moving_vector, moving_a_vector, moving_b_vector, moving_y_vector)
        frenet.set_opacity(0)
        self.play(Create(moving_frame), run_time = 1.2)
        self.play(t_tracker.animate.set_value(3 * PI / 2), run_time = 3.3)
        self.add_fixed_in_frame_mobjects(frenet)
        self.play(frenet.animate.set_opacity(1), run_time = 0.8)
        self.wait()
        kappa = MathTex(r"\kappa", color = ORANGE, font_size = 168).shift(2.6 * RIGHT + 2.4 * UP).set_opacity(0)
        tau = MathTex(r"\tau", color = YELLOW_A, font_size = 168).shift(5 * RIGHT + 2.4 * UP).set_opacity(0)
        krect = SurroundingRectangle(kappa, color = YELLOW, buff = 0.2, stroke_width = 4).set_stroke(opacity = 0)
        trect = SurroundingRectangle(tau, color = YELLOW, buff = 0.2, stroke_width = 4).set_stroke(opacity = 0)
        self.add_fixed_in_frame_mobjects(kappa, tau, krect, trect)
        self.play(kappa.animate.set_opacity(1), tau.animate.set_opacity(1), run_time = 0.8)
        self.wait()
        self.play(krect.animate.set_stroke(opacity = 1), trect.animate.set_stroke(opacity = 1), run_time = 0.25)
        self.wait(0.1)
        self.play(krect.animate.set_stroke(opacity = 0), trect.animate.set_stroke(opacity = 0), run_time = 0.25)
        self.play(krect.animate.set_stroke(opacity = 1), trect.animate.set_stroke(opacity = 1), run_time = 0.25)
        self.wait(0.1)
        self.play(krect.animate.set_stroke(opacity = 0), trect.animate.set_stroke(opacity = 0), run_time = 0.25)
        self.wait()
