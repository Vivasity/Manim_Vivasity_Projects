from manim import *

config.background_color = "#000012"  # 设置Scene背景颜色
config.frame_rate = 1
config.save_last_frame = True

# 生成视频封面
class Thumbnail(Scene):
    def construct(self):
        axes = Axes(x_range = [-7, 7, 1], y_range = [-4, 4, 1], x_length = 15, y_length = 9, axis_config = {"include_ticks": False})
        axes.x_axis.set_stroke(width = 5)
        axes.y_axis.set_stroke(width = 5)
        grid = NumberPlane(
            x_range = [-7, 7, 1], y_range = [-4, 4, 1], 
            x_length = 15, y_length = 9, 
            background_line_style = {"stroke_opacity": 0.4}
        )
        graph = axes.plot(lambda x: np.power(x, 0.5) - 1, x_range = [0, 7], color = YELLOW, stroke_width = 4)
        x0 = MathTex("x_0", font_size = 50, color = YELLOW_B).move_to(axes.coords_to_point(4, -0.4))
        x0_l = MathTex(
            "x_0-\delta", font_size = 50, tex_to_color_map = {"x_0": YELLOW_B, "-\delta": GREEN_B}
        ).move_to(axes.coords_to_point(2.2, -0.4))
        x0_r = MathTex(
            "x_0+\delta", font_size = 50, tex_to_color_map = {"x_0": YELLOW_B, "+\delta": GREEN_B}
        ).move_to(axes.coords_to_point(5.8, -0.4))
        y0 = MathTex("y_0", font_size = 50, color = YELLOW_B).move_to(axes.coords_to_point(-0.45, 1))
        y0_d = MathTex(
            "y_0-\epsilon", font_size = 50, tex_to_color_map = {"y_0": YELLOW_B, "-\epsilon": BLUE_B}
        ).move_to(axes.coords_to_point(-0.85, 0.4))
        y0_u = MathTex(
            "y_0+\epsilon", font_size = 50, tex_to_color_map = {"y_0": YELLOW_B, "+\epsilon": BLUE_B}
        ).move_to(axes.coords_to_point(-0.85, 1.6))
        x = VGroup(x0, x0_l, x0_r)
        y = VGroup(y0, y0_d, y0_u)
        hole = Circle(
            radius = 0.08, color = YELLOW, fill_color = "#000012", fill_opacity = 1, stroke_width = 2
        ).move_to(axes.coords_to_point(4, 1))
        points0 = [axes.coords_to_point(4, 0), axes.coords_to_point(0, 1)]
        points1 = [axes.coords_to_point(3, 0.732), axes.coords_to_point(5, 1.236)]
        dots0 = VGroup(*[Dot(point, color = ORANGE) for point in points0])
        dots1 = VGroup(*[Dot(point, color = YELLOW) for point in points1])
        rect_v = Rectangle(
            width = 2.14, height = 9, fill_color = GREEN_B, fill_opacity = 0.4, stroke_width = 0
        ).shift(4.29 * RIGHT)
        dashed_v = DashedVMobject(
            Rectangle(width = 2.14, height = 9, stroke_width = 3), num_dashes = 45, dashed_ratio = 0.5
        ).shift(4.29 * RIGHT)
        rect_h = Rectangle(
            width = 15, height = 0.567, fill_color = BLUE_B, fill_opacity = 0.4, stroke_width = 0
        ).shift(1.125 * UP)
        dashed_h = DashedVMobject(
            Rectangle(width = 15, height = 0.567, stroke_width = 3), num_dashes = 65, dashed_ratio = 0.5
        ).shift(1.125 * UP)
        label = MathTex(
            "\epsilon-\delta", font_size = 220, color = YELLOW_E
        ).set_opacity(0.6).set_stroke(width = 4, color = YELLOW_A, opacity = 0.6).move_to(axes.coords_to_point(3.3, 2.5))
        line0 = Line(axes.c2p(0, 1), axes.c2p(4, 1), color = TEAL_E).set_stroke(width = 6).set_opacity(0.6)
        line1 = Line(axes.c2p(4, 0), axes.c2p(4, 1), color = TEAL_E).set_stroke(width = 6).set_opacity(0.6)
        dashed = VGroup(line0, line1)
        integrity = VGroup(axes, grid, rect_v, dashed_v, rect_h, dashed_h, x, y, dashed, graph, hole, dots0, dots1, label)
        self.add(integrity)
        self.wait(0.1)
