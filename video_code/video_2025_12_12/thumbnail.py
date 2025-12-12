from manim import *

config.background_color = "#000012"  # 设置Scene背景颜色
config.frame_rate = 1
config.save_last_frame = True

# 生成视频封面
class Thumbnail(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 60 * DEGREES, theta = 30 * DEGREES)
        axes_2d = Axes(
            x_range = [-1.8, 1.8, 1], y_range = [-1.8, 1.8, 1], x_length = 3.6, y_length = 3.6, 
            x_axis_config = {"tip_length": 0.07, "tip_width": 0.05},
            y_axis_config = {"tip_length": 0.07, "tip_width": 0.05},
            axis_config = {"include_ticks": False}
        ).shift(3.2 * LEFT)
        x_label_2d = MathTex(r"x", font_size = 50).next_to(axes_2d.x_axis, RIGHT, buff = 0.2)
        y_label_2d = MathTex(r"y", font_size = 50).next_to(axes_2d.y_axis, UP, buff = 0.2)
        circle = Circle(radius = 1, color = YELLOW_B, stroke_width = 5).move_to(axes_2d.get_center())
        equa_l = MathTex(r"x^2+y^2=1", font_size = 54).next_to(axes_2d, DOWN, buff = 0.2)
        g = MathTex(r"F(", font_size = 54)
        alpha = MathTex(r"\alpha,", font_size = 54, color = RED)
        beta = MathTex(r"\beta,", font_size = 54, color = GREEN)
        gamma = MathTex(r"\gamma", font_size = 54, color = BLUE)
        end = MathTex(r")=", font_size = 54)
        quest = MathTex(r"?", font_size = 96, color = ORANGE)
        equa_r = VGroup(g, alpha, beta, gamma, end, quest).arrange(RIGHT, buff = 0.1).next_to(equa_l, RIGHT, buff = 3.6)
        separator = DashedLine(start = UP * 4, end = DOWN * 4, stroke_width = 6, dash_length = 0.4, color = WHITE)
        axes_2d.x_axis.set_stroke(width = 4)
        axes_2d.y_axis.set_stroke(width = 4)

        # 定义螺线参数方程
        def helix_func(t):
            return np.array([1.6 * np.cos(t), 1.6 * np.sin(t), t / 2])
        
        # 计算切向量
        def tangent(t, delta = 0.01):
            r_t = helix_func(t)
            r_t_plus = helix_func(t + delta)
            return (r_t_plus - r_t) / np.linalg.norm(r_t_plus - r_t)
        
        # 计算法向量
        def normal(t, delta = 0.01):
            T_t = tangent(t)
            T_t_plus = tangent(t + delta)
            return (T_t_plus - T_t) / np.linalg.norm(T_t_plus - T_t)
        
        # 计算副法向量
        def binormal(t):
            T = tangent(t)
            N = normal(t)
            return np.cross(T, N)
        
        ta = tangent(-3.28 * PI)
        no = normal(-3.28 * PI)
        bino = binormal(-3.28 * PI)
        point = np.array([1.6 * np.cos(-3.28 * PI), 1.6 * np.sin(-3.28 * PI), -1.64 * PI])
        dot = Dot3D(point, radius = 0.1, color = WHITE).shift(9.2 * LEFT)
        a = Arrow3D(start = point, end = point + 2 * ta, color = RED).shift(9.2 * LEFT)
        b = Arrow3D(start = point, end = point + 2 * no, color = GREEN).shift(9.2 * LEFT)
        y = Arrow3D(start = point, end = point + 2 * bino, color = BLUE).shift(9.2 * LEFT)
        alpha_ = MathTex(r"\alpha", font_size = 48, color = RED)
        beta_ = MathTex(r"\beta", font_size = 48, color = GREEN)
        gamma_ = MathTex(r"\gamma", font_size = 48, color = BLUE)
        alpha_.shift(3.7 * RIGHT + 1.05 * UP)
        beta_.shift(2.6 * RIGHT + 0.35 * DOWN)
        gamma_.shift(4.55 * RIGHT + 0.85 * UP)
        helix = ParametricFunction(helix_func, t_range = [-5.3 * PI, 4 * PI], color = YELLOW_B, stroke_width = 5).shift(9.2 * LEFT)
        self.add(helix, dot, a, b, y)
        self.add_fixed_in_frame_mobjects(axes_2d, separator, circle, equa_l, equa_r, x_label_2d, y_label_2d, alpha_, beta_, gamma_)
        self.wait(0.1)
