from manim import *

chinese_template = TexTemplate()
chinese_template.add_to_preamble(r"\usepackage{ctex}")  # 添加中文支持
chinese_template.tex_compiler = "pdflatex"

config.background_color = "#000012"  # 设置Scene背景颜色

# 二维Frenet标架旋转
class TwoDTransform(Scene):
    def construct(self):
        self.wait()
        axes = Axes(x_range = [-8, 8, 1], y_range = [-4, 4, 1], x_length = 16, y_length = 8)
        red_vector = Arrow(start = axes.c2p(0, -1), end = axes.c2p(2, -1), color = RED, buff = 0)
        green_vector = Arrow(start = axes.c2p(0, -1), end = axes.c2p(0, 1), color = GREEN, buff = 0)
        nred_vector = Arrow(start = axes.c2p(0, -1), end = axes.c2p(0, 0), color = GREEN_A, buff = 0)
        ngreen_vector = Arrow(start = axes.c2p(0, -1), end = axes.c2p(-1, -1), color = RED_A, buff = 0)
        matrix0 = MathTex(r"\begin{pmatrix} \dot{\vec{\alpha }} \\ \dot{\vec{\beta}} \end{pmatrix}", font_size = 44, color = GREEN)
        matrix1 = MathTex(r"=", font_size = 44, color = YELLOW_A)
        matrix2 = MathTex(r"\begin{pmatrix} 0 & \kappa \\ -\kappa & 0 \end{pmatrix}", font_size = 44, color = ORANGE)
        matrix3 = MathTex(r"\begin{pmatrix} \vec{\alpha } \\ \vec{\beta} \end{pmatrix}", font_size = 44, color = RED)
        matrix = VGroup(matrix0, matrix1, matrix2, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.4))
        self.add(red_vector, green_vector, matrix)
        self.play(
            ReplacementTransform(red_vector.copy(), nred_vector), ReplacementTransform(green_vector.copy(), ngreen_vector), run_time = 2
        )
        self.wait()

# 得到三维Frenet标架
class ThreeDimFrame(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 60 * DEGREES, theta = 30 * DEGREES)
        axes = ThreeDAxes(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], z_range = [-2, 6, 1], 
            x_length = 8, y_length = 8, z_length = 8, axis_config = {"tip_width": 0.12, "tip_height": 0.15}
        )
        grid = NumberPlane(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], x_length = 8, y_length = 8, 
            background_line_style = {"stroke_opacity": 0.4}
        )
        red_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(2, 0, 0), color = RED)
        green_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 2, 0), color = GREEN)
        blue_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 0, 2), color = BLUE)
        frame = VGroup(red_vector, green_vector, blue_vector)
        nred_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 1, 0), color = RED_A)
        ngreen_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(-1, 0, 1), color = GREEN_A)
        nblue_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, -1, 0), color = BLUE_A)
        matrix0 = MathTex(
            r"\begin{pmatrix} \dot{\vec{\alpha }} \\ \dot{\vec{\beta}} \\ \dot{\vec{\gamma}} \end{pmatrix}", 
            font_size = 44, color = BLUE
        )
        matrix1 = MathTex(r"=", font_size = 44, color = YELLOW_A)
        matrix2 = MathTex(r"\begin{pmatrix} ? & ? & ? \\ ? & ? & ? \\ ? & ? & ? \end{pmatrix}", font_size = 44, color = GREEN)
        matrix3 = MathTex(r"\begin{pmatrix} \vec{\alpha } \\ \vec{\beta} \\ \vec{\gamma} \end{pmatrix}", font_size = 44, color = RED)
        matrix = VGroup(matrix0, matrix1, matrix2, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.add_fixed_in_frame_mobjects(matrix)
        self.add(red_vector, green_vector, blue_vector).wait()
        self.play(
            ReplacementTransform(red_vector.copy(), nred_vector), ReplacementTransform(green_vector.copy(), ngreen_vector), 
            ReplacementTransform(blue_vector.copy(), nblue_vector), run_time = 2
        )
        self.wait()
        by_grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-8, 8, 1], x_length = 16, y_length = 16, 
            background_line_style = {"stroke_color": GREEN_A, "stroke_opacity": 0.4}, axis_config = {"stroke_opacity": 0},
            faded_line_style = {"stroke_color": GREEN, "stroke_opacity": 0.4}
        ).rotate(PI / 2, axis = UP)
        self.play(FadeOut(nred_vector), FadeOut(ngreen_vector), FadeOut(nblue_vector), run_time = 1.3)
        self.wait()
        self.play(GrowFromCenter(by_grid), run_time = 1.4)
        red_vector0 = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 1.1, 1), color = RED_A)
        red_vector1 = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 1.7, 0.6), color = RED_A)
        red_vector2 = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 1, 0), color = RED_A)
        self.play(ReplacementTransform(red_vector.copy(), red_vector0), run_time = 1.2)
        self.wait(0.8)
        self.play(ReplacementTransform(red_vector0, red_vector1), run_time = 1.2)
        self.wait(0.8)
        self.play(ReplacementTransform(red_vector1, red_vector2), run_time = 1.2)
        ad_label = MathTex(
            r"\dot{\vec{\alpha}}=?\vec{\beta}+?\vec{\gamma}", font_size = 44, color = RED_A
        ).rotate(PI / 2).move_to(axes.c2p(0, 3.2, 1.8)).rotate(PI / 2, axis = UP)
        self.play(Write(ad_label), run_time = 1.4)
        self.wait()
        self.play(FadeOut(red_vector2), FadeOut(by_grid), FadeOut(ad_label), run_time = 1.4)
        self.wait()
        nmatrix2 = MathTex(r"\begin{pmatrix} 0 & ? & ? \\ ? & ? & ? \\ ? & ? & ? \end{pmatrix}", font_size = 44, color = GREEN)
        nmatrix = VGroup(matrix0, matrix1, nmatrix2, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.remove(matrix).add_fixed_in_frame_mobjects(nmatrix)
        self.wait()
        ay_grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-8, 8, 1], x_length = 16, y_length = 16, 
            background_line_style = {"stroke_color": GREEN_A, "stroke_opacity": 0.4}, axis_config = {"stroke_opacity": 0},
            faded_line_style = {"stroke_color": GREEN, "stroke_opacity": 0.4}
        ).rotate(PI / 2, axis = RIGHT)
        bgreen_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(-1, 0, 1), color = GREEN_A)
        bd_label = MathTex(
            r"\dot{\vec{\beta}}=?\vec{\alpha}+?\vec{\gamma}", font_size = 44, color = GREEN_A
        ).rotate(PI).move_to(axes.c2p(3.6, 0, 2.5)).rotate(-PI / 2, axis = RIGHT)
        self.play(GrowFromCenter(ay_grid), Create(bgreen_vector), Write(bd_label), run_time = 1.4)
        self.wait()
        self.play(FadeOut(ay_grid), FadeOut(bd_label), FadeOut(bgreen_vector))
        self.wait()
        ab_grid = NumberPlane(
            x_range = [-8, 8, 1], y_range = [-8, 8, 1], x_length = 16, y_length = 16, 
            background_line_style = {"stroke_color": GREEN_A, "stroke_opacity": 0.4}, axis_config = {"stroke_opacity": 0},
            faded_line_style = {"stroke_color": GREEN, "stroke_opacity": 0.4}
        )
        yblue_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, -1, 0), color = BLUE_A)
        yd_label = MathTex(
            r"\dot{\vec{\gamma}}=?\vec{\alpha}+?\vec{\beta}", font_size = 44, color = BLUE_A
        ).move_to(axes.c2p(1.5, 2.8, 0)).rotate(PI / 2)
        self.play(GrowFromCenter(ab_grid), Write(yd_label), Create(yblue_vector), run_time = 1.4)
        self.wait()
        self.play(FadeOut(ab_grid), FadeOut(yd_label), FadeOut(yblue_vector))
        self.wait()
        nmatrix22 = MathTex(r"\begin{pmatrix} 0 & ? & ? \\ ? & 0 & ? \\ ? & ? & 0 \end{pmatrix}", font_size = 44, color = GREEN)
        nnmatrix = VGroup(matrix0, matrix1, nmatrix22, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.remove(nmatrix).add_fixed_in_frame_mobjects(nnmatrix)
        self.wait()
        agreen_vector = Arrow3D(start = axes.c2p(0, 0, 0), end = axes.c2p(0, 1, 0), color = GREEN_A)
        self.play(ReplacementTransform(red_vector.copy(), agreen_vector), run_time = 1.4)
        ad_label = MathTex(r"\dot{\vec{\alpha}}=\kappa \vec{\beta}", font_size = 44, color = GREEN_A).move_to(axes.c2p(3.2, 1))
        self.add_fixed_in_frame_mobjects(ad_label)
        nmatrix23 = MathTex(r"\begin{pmatrix} 0 & \kappa & 0 \\ ? & 0 & ? \\ ? & ? & 0 \end{pmatrix}", font_size = 44, color = GREEN)
        nnmatrix2 = VGroup(matrix0, matrix1, nmatrix23, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.wait()
        self.play(FadeOut(agreen_vector), run_time = 1.2)
        self.remove(nnmatrix).add_fixed_in_frame_mobjects(nnmatrix2)
        self.wait()
        nad_label = MathTex(
            r"\Rightarrow \dot{\vec{\alpha}} \cdot \vec{\beta}=\kappa \vec{\beta} \cdot \vec{\beta}", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(4.1, 0.2))
        self.add_fixed_in_frame_mobjects(nad_label)
        self.wait()
        nad_label2 = MathTex(
            r"\Rightarrow \dot{\vec{\alpha}} \cdot \vec{\beta}=\kappa \left | \vec{\beta} \right |^2", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(4.05, -0.6))
        self.add_fixed_in_frame_mobjects(nad_label2)
        self.wait()
        nad_label3 = MathTex(
            r"\Rightarrow \dot{\vec{\alpha}} \cdot \vec{\beta}=\kappa", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(3.65, -1.4))
        self.add_fixed_in_frame_mobjects(nad_label3)
        self.wait()
        inner_product = MathTex(r"\vec{\alpha}} \cdot \vec{\beta}=0", font_size = 44, color = GREEN_A).move_to(axes.c2p(-4.2, 1))
        self.add_fixed_in_frame_mobjects(inner_product)
        self.wait()
        inner_pro_d = MathTex(
            r"\Rightarrow \dot{\vec{\alpha}}} \cdot \vec{\beta}+\dot{\vec{\beta}} \cdot \vec{\alpha}=0", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(-3.2, 0.2))
        self.add_fixed_in_frame_mobjects(inner_pro_d)
        self.wait()
        neg_kappa = MathTex(
            r"\Rightarrow \dot{\vec{\beta}}} \cdot \vec{\alpha}= -\kappa", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(-3.7, -0.6))
        self.add_fixed_in_frame_mobjects(neg_kappa)
        self.wait()
        nmatrix24 = MathTex(
            r"\begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & ? \\ ? & ? & 0 \end{pmatrix}", font_size = 44, color = GREEN
        )
        nnmatrix3 = VGroup(matrix0, matrix1, nmatrix24, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.remove(
            ad_label, nad_label, nad_label2, nad_label3, inner_product, inner_pro_d, neg_kappa, nnmatrix2
        ).add_fixed_in_frame_mobjects(nnmatrix3)
        self.wait()
        nmatrix25 = MathTex(
            r"\begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & ? \\ 0 & ? & 0 \end{pmatrix}", font_size = 44, color = GREEN
        )
        nnmatrix4 = VGroup(matrix0, matrix1, nmatrix25, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.remove(nnmatrix3).add_fixed_in_frame_mobjects(nnmatrix4)
        self.wait()
        nmatrix26 = MathTex(
            r"\begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & x \\ 0 & -x & 0 \end{pmatrix}", font_size = 44, color = GREEN
        )
        nnmatrix5 = VGroup(matrix0, matrix1, nmatrix26, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        self.remove(nnmatrix4).add_fixed_in_frame_mobjects(nnmatrix5)
        self.wait()

        def circle_func(t):
            return axes.c2p(2 * np.cos(t), 2 * np.sin(t), 0)
        
        circle = ParametricFunction(circle_func, t_range = [0, 2 * PI], color = TEAL_A)
                
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
            lambda: Dot3D(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), color = YELLOW
            )
        )
        moving_a_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0) + get_tangent_vector(circle_func, t_tracker.get_value()), 
                color = RED
            )
        )
        moving_b_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0) + get_normal_vector(circle_func, t_tracker.get_value()), 
                color = GREEN
            )
        )
        moving_y_vector = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), 0) + get_binormal_vector(circle_func, t_tracker.get_value()), 
                color = BLUE
            )
        )
        moving_frame = VGroup(moving_a_vector, moving_b_vector, moving_y_vector)
        self.play(
            Create(axes), Create(grid), Create(moving_dot), Create(circle), nnmatrix5.animate.shift(4 * RIGHT),
            ReplacementTransform(frame, moving_frame), run_time = 1.8
        )
        self.wait()
        self.play(t_tracker.animate.set_value(2 * PI), run_time = 4)
        self.wait()
        moving_a_vector.clear_updaters(), moving_b_vector.clear_updaters(), moving_dot.clear_updaters(), moving_y_vector.clear_updaters()
        self.play(FadeOut(moving_frame))
        self.wait()
        t_tracker = ValueTracker(0)

        def helix_func_one(t):
            return axes.coords_to_point(2 * np.cos(t), 2 * np.sin(t), t / 4)
        
        helix1 = ParametricFunction(helix_func_one, t_range = [0, 2 * PI], color = TEAL_A)
        moving_dot2 = always_redraw(
            lambda: Dot3D(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4), color = YELLOW
            )
        )
        moving_a_vector2 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4) + get_tangent_vector(helix_func_one, t_tracker.get_value()), 
                color = RED
            )
        )
        moving_b_vector2 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4) + get_normal_vector(helix_func_one, t_tracker.get_value()), 
                color = GREEN
            )
        )
        moving_y_vector2 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 4) + get_binormal_vector(helix_func_one, t_tracker.get_value()), 
                color = BLUE
            )
        )
        moving_frame2 = VGroup(moving_dot2, moving_a_vector2, moving_b_vector2, moving_y_vector2)
        _yvector2 = moving_y_vector2.copy()
        self.play(ReplacementTransform(circle, helix1), Create(moving_frame2), Create(_yvector2), run_time = 1.5)
        self.wait()
        self.play(t_tracker.animate.set_value(PI), run_time = 2)
        self.wait()
        target_point = np.array([4, 0, -0.25 * PI])
        y_vector2 = moving_y_vector2.copy()
        self.play(y_vector2.animate.shift(target_point), run_time = 1.2)
        self.wait()
        self.play(FadeOut(moving_frame2), FadeOut(y_vector2), FadeOut(_yvector2))
        self.wait()
        moving_a_vector2.clear_updaters(), moving_b_vector2.clear_updaters()
        moving_dot2.clear_updaters(), moving_y_vector2.clear_updaters()
        t_tracker = ValueTracker(0)

        def helix_func_two(t):
            return axes.coords_to_point(2 * np.cos(t), 2 * np.sin(t), t / 2)
        
        helix2 = ParametricFunction(helix_func_two, t_range = [0, 2 * PI], color = TEAL_A)
        moving_dot3 = always_redraw(
            lambda: Dot3D(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), color = YELLOW
            )
        )
        moving_a_vector3 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_tangent_vector(helix_func_two, t_tracker.get_value()), 
                color = RED
            )
        )
        moving_b_vector3 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_normal_vector(helix_func_two, t_tracker.get_value()), 
                color = GREEN
            )
        )
        moving_y_vector3 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() / 2) + get_binormal_vector(helix_func_two, t_tracker.get_value()), 
                color = BLUE
            )
        )
        moving_frame3 = VGroup(moving_dot3, moving_a_vector3, moving_b_vector3, moving_y_vector3)
        _yvector3 = moving_y_vector3.copy()
        self.play(ReplacementTransform(helix1, helix2), Create(moving_frame3), Create(_yvector3), run_time = 1.5)
        self.wait()
        self.play(t_tracker.animate.set_value(PI), run_time = 2)
        self.wait()
        target_point = np.array([4, 0, -0.5 * PI])
        y_vector3 = moving_y_vector3.copy()
        self.play(y_vector3.animate.shift(target_point), run_time = 1.2)
        self.wait()
        self.play(FadeOut(moving_frame3), FadeOut(y_vector3), FadeOut(_yvector3))
        self.wait()
        moving_a_vector3.clear_updaters(), moving_b_vector3.clear_updaters()
        moving_dot3.clear_updaters(), moving_y_vector3.clear_updaters()
        t_tracker = ValueTracker(0)

        def helix_func_three(t):
            return axes.coords_to_point(2 * np.cos(t), 2 * np.sin(t), 0.75 * t)
        
        helix3 = ParametricFunction(helix_func_three, t_range = [0, 2 * PI], color = TEAL_A)
        moving_dot4 = always_redraw(
            lambda: Dot3D(
                axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75), 
                color = YELLOW
            )
        )
        moving_a_vector4 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75) + get_tangent_vector(helix_func_three, t_tracker.get_value()), 
                color = RED
            )
        )
        moving_b_vector4 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75) + get_normal_vector(helix_func_three, t_tracker.get_value()), 
                color = GREEN
            )
        )
        moving_y_vector4 = always_redraw(
            lambda: Arrow3D(
                start = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75), 
                end = axes.c2p(2 * np.cos(t_tracker.get_value()), 2 * np.sin(t_tracker.get_value()), t_tracker.get_value() * 0.75) + get_binormal_vector(helix_func_three, t_tracker.get_value()), 
                color = BLUE
            )
        )
        moving_frame4 = VGroup(moving_dot4, moving_a_vector4, moving_b_vector4, moving_y_vector4)
        _yvector4 = moving_y_vector4.copy()
        self.play(ReplacementTransform(helix2, helix3), Create(moving_frame4), Create(_yvector4), run_time = 1.5)
        self.add_fixed_in_frame_mobjects(nnmatrix5)
        self.wait()
        self.play(t_tracker.animate.set_value(PI), run_time = 2)
        self.wait()
        target_point = np.array([4, 0, -0.75 * PI])
        y_vector4 = moving_y_vector4.copy()
        self.play(y_vector4.animate.shift(target_point), run_time = 1.2)
        self.wait()
        self.play(FadeOut(y_vector4), FadeOut(_yvector4), FadeOut(moving_dot))
        self.wait()
        yd_label = MathTex(r"\dot{\vec{\gamma}} = -x \vec{\beta}", font_size = 44, color = GREEN_A).move_to(axes.c2p(4.1, 1))
        yd_label2 = MathTex(
            r"\Rightarrow \left \| \dot{\vec{\gamma}} \right \| =\left | x \right | \cdot \left | \vec{\beta} \right |", 
            font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(4.85, 0.2))
        yd_label3 = MathTex(
            r"\Rightarrow \left | x \right | = \left \| \dot{\vec{\gamma}} \right \|", font_size = 44, color = GREEN_A
        ).move_to(axes.c2p(4.4, -0.6))
        self.add_fixed_in_frame_mobjects(yd_label), self.wait()
        self.add_fixed_in_frame_mobjects(yd_label2), self.wait()
        self.add_fixed_in_frame_mobjects(yd_label3), self.wait()
        ydi_label = VGroup(yd_label, yd_label2, yd_label3)
        tau = MathTex(r"\tau", font_size = 340, color = YELLOW_A)
        moving_a_vector4.clear_updaters(), moving_b_vector4.clear_updaters()
        moving_dot4.clear_updaters(), moving_y_vector4.clear_updaters()
        self.play(
            ydi_label.animate.set_opacity(0), helix3.animate.set_stroke(opacity = 0.3), grid.animate.set_stroke(opacity = 0.3),
            axes.animate.set_stroke(opacity = 0.3), nnmatrix5.animate.set_opacity(0.3), moving_dot4.animate.set_opacity(0.1),
            moving_a_vector4.animate.set_opacity(0.1), moving_b_vector4.animate.set_opacity(0.1), 
            moving_y_vector4.animate.set_opacity(0.1), run_time = 1.4
        )
        self.add_fixed_in_frame_mobjects(tau)
        self.wait()
        self.remove(tau).play(
            helix3.animate.set_stroke(opacity = 1), grid.animate.set_stroke(opacity = 0.4), axes.animate.set_stroke(opacity = 1), 
            nnmatrix5.animate.set_opacity(1), moving_dot4.animate.set_opacity(1), moving_a_vector4.animate.set_opacity(1), 
            moving_b_vector4.animate.set_opacity(1), moving_y_vector4.animate.set_opacity(1), run_time = 1.4
        )
        nmatrix27 = MathTex(
            r"\begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{pmatrix}", font_size = 44, color = GREEN
        )
        nnmatrix6 = VGroup(matrix0, matrix1, nmatrix27, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        nnmatrix6.shift(4 * RIGHT)
        self.remove(nnmatrix5).add_fixed_in_frame_mobjects(nnmatrix6)
        self.wait()
        rmatrix = SurroundingRectangle(nnmatrix6, color = YELLOW, buff = 0.1, stroke_width = 4)
        self.add_fixed_in_frame_mobjects(rmatrix)
        self.wait()

# 旋转镜头，环绕整个场景一周
class Rotation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 60 * DEGREES, theta = 30 * DEGREES)
        axes = ThreeDAxes(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], z_range = [-2, 6, 1], 
            x_length = 8, y_length = 8, z_length = 8, axis_config = {"tip_width": 0.12, "tip_height": 0.15}
        )
        grid = NumberPlane(
            x_range = [-4, 4, 1], y_range = [-4, 4, 1], x_length = 8, y_length = 8, 
            background_line_style = {"stroke_opacity": 0.4}
        )

        def helix_func(t):
            return axes.coords_to_point(2 * np.cos(t), 2 * np.sin(t), 0.75 * t)
        
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
        
        helix3 = ParametricFunction(helix_func, t_range = [0, 2 * PI], color = TEAL_A)
        matrix0 = MathTex(
            r"\begin{pmatrix} \dot{\vec{\alpha }} \\ \dot{\vec{\beta}} \\ \dot{\vec{\gamma}} \end{pmatrix}", 
            font_size = 44, color = BLUE
        )
        matrix1 = MathTex(r"=", font_size = 44, color = YELLOW_A)
        matrix2 = MathTex(
            r"\begin{pmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{pmatrix}", font_size = 44, color = GREEN
        )
        matrix3 = MathTex(r"\begin{pmatrix} \vec{\alpha } \\ \vec{\beta} \\ \vec{\gamma} \end{pmatrix}", font_size = 44, color = RED)
        matrix = VGroup(matrix0, matrix1, matrix2, matrix3).arrange(RIGHT, buff = 0.1).move_to(axes.c2p(0, 2.8))
        matrix.shift(4 * RIGHT)
        rmatrix = SurroundingRectangle(matrix, color = YELLOW, buff = 0.1, stroke_width = 4)
        dot = Dot3D(axes.c2p(-2, 0, 0.75 * PI), color = YELLOW)
        red_vector = Arrow3D(
            start = axes.c2p(-2, 0, 0.75 * PI), end = axes.c2p(-2, 0, 0.75 * PI) + get_tangent_vector(helix_func, PI), color = RED
        )
        green_vector = Arrow3D(
            start = axes.c2p(-2, 0, 0.75 * PI), end = axes.c2p(-2, 0, 0.75 * PI) + get_normal_vector(helix_func, PI), color = GREEN
        )
        blue_vector = Arrow3D(
            start = axes.c2p(-2, 0, 0.75 * PI), end = axes.c2p(-2, 0, 0.75 * PI) + get_binormal_vector(helix_func, PI), color = BLUE
        )
        frame = VGroup(dot, red_vector, green_vector, blue_vector)
        self.add(axes, grid, helix3, frame).add_fixed_in_frame_mobjects(matrix, rmatrix)
        self.wait()
        self.begin_ambient_camera_rotation(rate = 0.1 * PI)
        self.wait(20)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.play(FadeOut(matrix), FadeOut(rmatrix), run_time = 1.5)
        self.wait()
        self.begin_ambient_camera_rotation(rate = 0.1 * PI)
        self.wait(20)
        self.stop_ambient_camera_rotation()
        self.wait()
