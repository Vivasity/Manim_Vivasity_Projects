from manim import *
import math
from scipy.optimize import minimize

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

# 第三部分：距离的本质
class ChapterThree(Scene):
    def construct(self):
        title = MathTex(
            r"\text{三、}\text{距离}\text{的}\text{本质}", tex_template = chinese_template, font_size = 40,
            tex_to_color_map = {r"\text{距离}": TEAL, r"\text{本质}": ORANGE}
        ).scale(1.8)
        self.wait(0.4)
        self.play(Write(title), run_time = 1.6)
        self.wait(2)
        self.play(FadeOut(title), run_time = 0.9)
        ed_limit0 = MathTex(r"\forall\epsilon>0,", font_size = 54, color = GREEN_B)
        ed_limit1 = MathTex(r"\exists\delta>0,", font_size = 54, color = YELLOW)
        ed_limit2 = MathTex(r"\forall x:0<\left |x-x_0\right |<\delta,", font_size = 54, color = ORANGE)
        ed_limit3 = MathTex(r"\left |f(x)-c\right |<\epsilon", font_size = 54, color = GREEN_B)
        ed_limit = VGroup(ed_limit0, ed_limit1, ed_limit2, ed_limit3).arrange(RIGHT, buff = 0.3)
        self.play(Write(ed_limit), run_time = 1.8)
        self.wait(2)
        ed_rect2 = SurroundingRectangle(ed_limit2, color = TEAL_A, buff = 0.1, stroke_width = 4)
        self.play(ShowPassingFlash(ed_rect2), time_width = 0.7, run_time = 1.6)
        self.wait()
        twodfunction = MathTex(r"\lim_{(x,y) \to (x_0,y_0)} f(x,y)", font_size = 64, color  =YELLOW_A)
        self.play(AnimationGroup(ed_limit.animate.shift(2 * UP), Write(twodfunction), lag_ratio = 1.2), run_time = 2.4)
        self.wait()
        self.play(FadeOut(ed_limit), FadeOut(twodfunction), run_time = 1.4)
        self.wait(1.5)
        x = MathTex(r"\mathbf{x} =\left ( x_1, x_2,\cdots ,x_n \right )", font_size = 50, color = YELLOW_A)
        y = MathTex(r"\mathbf{y} =\left ( y_1, y_2,\cdots ,y_n \right )", font_size = 50, color = YELLOW_A)
        xy_distance = MathTex(
            r"d=\left | \mathbf{x}-\mathbf{y}  \right | =\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots +(x_n-y_n)^2}", font_size = 50, 
            color = YELLOW_A
        )
        x_y = VGroup(x, y, xy_distance).arrange(DOWN, buff = 0.3)
        self.play(DrawBorderThenFill(x_y), run_time = 2.2)
        self.wait(2.5)
        self.play(FadeOut(x_y), run_time = 1.7)
        self.wait(1.6)
        axes = Axes( 
            x_range = [-3, 8.25, 1], y_range = [-2.5, 5, 1], x_length = 15, y_length = 10, axis_config = {"include_ticks": True}
        )
        grid = NumberPlane(
            x_range = [-3, 8.25, 1], y_range = [-2.5, 5, 1], 
            x_length = 15, y_length = 10, 
            background_line_style = {"stroke_opacity": 0.4}
        ).set_stroke(background = True)
        self.play(Create(axes), Create(grid), run_time = 1.7)
        self.wait(0.6)
        b = Dot(axes.coords_to_point(4, 3), color = RED)
        a = Dot(axes.coords_to_point(1, 0), color = GREEN)
        label_a = MathTex(r"A(a_1,a_2)", font_size = 44, color = GREEN).next_to(a, DOWN, buff = 0.2)
        label_b = MathTex(r"B(b_1,b_2)", font_size = 44, color = RED).next_to(b, UP, buff = 0.2)
        self.play(Create(a), Write(label_a), Create(b), Write(label_b), run_time = 1.3)
        self.wait(0.9)
        coords0 = [(1, 0), (4, 0), (4, 3)]
        scene_points0 = [axes.coords_to_point(x, y) for x, y in coords0]
        poly_line0 = VMobject(stroke_color = YELLOW, stroke_width = 4)
        poly_line0.set_points_as_corners(scene_points0)
        self.play(Create(poly_line0), run_time = 3)
        self.wait()
        coords1 = [(1, 0), (3, 0), (3, 2), (4, 2), (4, 3)]
        scene_points1 = [axes.coords_to_point(x, y) for x, y in coords1]
        poly_line1 = VMobject(stroke_color = ORANGE, stroke_width = 4)
        poly_line1.set_points_as_corners(scene_points1)
        self.play(Create(poly_line1), run_time = 3)
        line = Line(axes.coords_to_point(1, 0), axes.coords_to_point(4, 3), stroke_width = 4, color = YELLOW_A)
        self.wait()
        self.play(Create(line), run_time = 1.8)
        self.wait(2)
        self.remove(line)
        self.wait(2)
        distance = MathTex(r"d=\left |AB \right |=\left |a_1-b_1\right |+\left |a_2-b_2\right |", font_size = 48, color = YELLOW_A)
        distance.to_corner(UR, buff = 0.3)
        self.play(Write(distance), run_time = 1.4)
        self.wait(2)
        self.play(
            FadeOut(axes), FadeOut(grid), FadeOut(poly_line1), FadeOut(poly_line0), FadeOut(a), FadeOut(b), FadeOut(label_a),
            FadeOut(label_b), distance.animate.shift(1.5 * UP), run_time = 1.9
        )
        self.wait()
        distance_axiom = MathChi(r"\text{度量公理}").scale(1.4).to_edge(UP)
        line = Line(stroke_width = 4, color = TEAL_A).set_length(12).next_to(distance_axiom, DOWN)
        self.play(Write(distance_axiom), GrowFromCenter(line), run_time = 1.8)
        self.wait()
        one = MathTex(
            r"\text{正定性}:d(x,y)\ge 0,\text{且}d(x,y)=0\Leftrightarrow x=y", tex_template = chinese_template, color = YELLOW_A,
            font_size = 54
        )
        two = MathTex(
            r"\text{对称性}:d(x,y)=d(y,x)", tex_template = chinese_template, color = YELLOW_A,
            font_size = 54
        )
        three = MathTex(
            r"\text{三角不等式}:d(x,z)\le d(x,y)+d(y,z)", tex_template = chinese_template, color = YELLOW_A,
            font_size = 54
        )
        integrity = VGroup(distance_axiom, line)
        self.play(integrity.animate.set_opacity(0.2))
        self.play(Write(one), run_time = 1.6)
        rect = SurroundingRectangle(one, color = YELLOW, buff = 0.4, stroke_width = 4)
        self.play(ShowPassingFlash(rect), time_width = 0.7, run_time = 1.6)
        self.wait(0.8)
        self.play(one.animate.shift(1.8 * UP), integrity.animate.set_opacity(1), run_time = 1.5)
        integrity.add(one)
        self.wait(1.7)
        self.play(integrity.animate.set_opacity(0.2))
        self.play(Write(two), run_time = 1.6)
        rect = SurroundingRectangle(two, color = YELLOW, buff = 0.4, stroke_width = 4)
        self.play(ShowPassingFlash(rect), time_width = 0.7, run_time = 1.6)
        self.wait(0.8)
        self.play(two.animate.shift(0.6 * UP), integrity.animate.set_opacity(1), run_time = 1.5)
        integrity.add(two)
        self.wait(1.7)
        self.play(integrity.animate.set_opacity(0.2))
        self.play(Write(three), run_time = 1.6)
        rect = SurroundingRectangle(three, color = YELLOW, buff = 0.4, stroke_width = 4)
        self.play(ShowPassingFlash(rect), time_width = 0.7, run_time = 1.6)
        self.wait(0.8)
        self.play(three.animate.shift(0.6 * DOWN), integrity.animate.set_opacity(1), run_timee = 1.5)
        integrity.add(three)
        self.wait(2.3)
        self.play(FadeOut(integrity), run_time = 1.8)

# 二元函数极限动画演示
class TwoDFunction(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 0 * DEGREES, theta = -90 * DEGREES)
        axes = ThreeDAxes(
            x_range = [-4, 4, 0.5], y_range = [-4, 4, 0.5], z_range = [-2, 2, 0.5], 
            x_length = 12, y_length = 12, z_length = 6, axis_config = {"tip_width": 0.12, "tip_height": 0.15}
        )
        xy_grid = NumberPlane(
            x_range = [-4, 4, 0.5], y_range = [-4, 4, 0.5], x_length = 12, y_length = 12,
            background_line_style = {"stroke_opacity": 0.4}
        ).move_to([0, 0, 0]).set_stroke(background = True)

        def f(x, y):
            return np.sin(math.sqrt(x**2 + y**2))
        
        def g(x, y):
            return math.sqrt(x**2 + y**2)
        
        f_surface = Surface(
            lambda u, v: axes.c2p(u, v, f(u, v)), u_range = [-4, 4], v_range = [-4, 4], resolution = (40, 40), fill_opacity = 0.5, stroke_width = 0
        )
        g_surface = Surface(
            lambda u, v: axes.c2p(u, v, g(u, v)), u_range = [-4, 4], v_range = [-4, 4], resolution = (40, 40), fill_opacity = 0.6, stroke_width = 0
        ).set_color(RED)
        self.play(Create(axes), Create(xy_grid), run_time = 2)
        self.wait(0.6)
        a = MathTex(r"\mathbf{a}=(x_1, y_1)", font_size = 48).shift(3.3 * UP + 5.3 * RIGHT)
        b = MathTex(r"\mathbf{b}=(x_2, y_2)", font_size = 48).shift(2.5 * UP + 5.3 * RIGHT)
        d = MathTex(
            r"d=\left |\mathbf{a}-\mathbf{b}\right |=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}", font_size = 48, color = YELLOW
        ).shift(2.4 * UP + 2.6 * LEFT)
        ax_tracker, ay_tracker, bx_tracker, by_tracker = ValueTracker(3), ValueTracker(0.5), ValueTracker(1), ValueTracker(1)
        vector_a = always_redraw(lambda: 
            Arrow(
                start = axes.c2p(0, 0, 0), end = axes.c2p(ax_tracker.get_value(), ay_tracker.get_value(), 0), buff = 0, stroke_width = 4,
                max_tip_length_to_length_ratio = 0.04
            )
        )
        vector_b = always_redraw(lambda: 
            Arrow(
                start = axes.c2p(0, 0, 0), end = axes.c2p(bx_tracker.get_value(), by_tracker.get_value(), 0), buff = 0, stroke_width = 4,
                max_tip_length_to_length_ratio = 0.07
            )  
        )
        neoa = always_redraw(
            lambda: MathTex(
                r"\mathbf{a}=(" + f"{ax_tracker.get_value():.2f}" + r"," + f"{ay_tracker.get_value():.2f}" + r")", font_size = 48
            ).shift(3.3 * UP + 5 * RIGHT)
        )
        neob = always_redraw(
            lambda: MathTex(
                r"\mathbf{b}=(" + f"{bx_tracker.get_value():.2f}" + r"," + f"{by_tracker.get_value():.2f}" + r")", font_size = 48
            ).shift(2.5 * UP + 5 * RIGHT)
        )
        neod = always_redraw(
            lambda: MathTex(
                r"d=\left |\mathbf{a}-\mathbf{b}\right |=" + 
                f"{math.sqrt((ax_tracker.get_value() - bx_tracker.get_value())**2 + (ay_tracker.get_value() - by_tracker.get_value())**2):.2f}", font_size = 48, color = YELLOW
            ).shift(2.4 * UP + 4.8 * LEFT)
        )
        distance = always_redraw(
            lambda: Line(
                axes.c2p(ax_tracker.get_value(), ay_tracker.get_value(), 0), 
                axes.c2p(bx_tracker.get_value(), by_tracker.get_value(), 0), color = YELLOW, stroke_width = 4
            )
        )
        label_a = always_redraw(
            lambda: MathTex(
                r"\mathbf{a}", font_size = 40).next_to(axes.c2p(ax_tracker.get_value(), ay_tracker.get_value(), 0), UR, buff = 0.1
            )
        )
        label_b = always_redraw(
            lambda: MathTex(
                r"\mathbf{b}", font_size = 40).next_to(axes.c2p(bx_tracker.get_value(), by_tracker.get_value(), 0), UL, buff = 0.1
            )
        )
        self.play(Create(vector_a), Create(vector_b), Write(label_a), Write(label_b), Write(a), Write(b), run_time = 1.6)
        self.play(Write(d), Create(distance), run_time = 1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(d, neod), ReplacementTransform(a, neoa), ReplacementTransform(b, neob), run_time = 1.5)
        self.wait(1.4)
        self.play(
            ax_tracker.animate.set_value(2.87), ay_tracker.animate.set_value(0.76), 
            bx_tracker.animate.set_value(0.45), by_tracker.animate.set_value(2.15), run_time = 1.8
        )
        self.wait(1.4)
        self.play(
            ax_tracker.animate.set_value(1.44), ay_tracker.animate.set_value(-1.56), 
            bx_tracker.animate.set_value(-2.45), by_tracker.animate.set_value(0.65), run_time = 1.8
        )
        self.wait(1.4)
        self.play(
            ax_tracker.animate.set_value(-1.57), ay_tracker.animate.set_value(1.96), 
            bx_tracker.animate.set_value(-2.45), by_tracker.animate.set_value(-2.15), run_time = 1.8
        )
        self.wait(1.4)
        ab = VGroup(neoa, neob)
        fxy = MathTex(r"f(x,y)=\sin(\sqrt{x^2+y^2})", font_size = 48, color = YELLOW_A).shift(3.3 * UP + 4 * RIGHT)
        self.play(
            FadeOut(neod), FadeOut(distance), FadeOut(vector_a), FadeOut(vector_b), FadeOut(label_a), FadeOut(label_b),
            ReplacementTransform(ab, fxy), run_time = 2.1
        )
        self.add_fixed_in_frame_mobjects(fxy)
        self.play(Create(f_surface), Create(g_surface), run_time = 1.7)
        self.wait(0.7)
        self.move_camera(phi = 70 * DEGREES, theta = 120 * DEGREES, distance = 0, run_time = 3.5)
        self.wait(1.6)
        x = MathTex(r"\mathbf{x}=(x,y)", font_size = 48, color = ORANGE).shift(2.4 * UP + 5 * RIGHT).set_opacity(0)
        x0 = MathTex(r"\mathbf{x_0}=(0,0)", font_size = 48, color = ORANGE).shift(1.8 * UP + 5 * RIGHT).set_opacity(0)
        twod_limit0 = MathTex(r"\forall \epsilon >0,", font_size = 48, color = GREEN_B)
        twod_limit1 = MathTex(r"\exists \delta =\epsilon,", font_size = 48, color = YELLOW)
        twod_limit2 = MathTex(r"\forall \mathbf{x}:0<\left | \mathbf{x}-\mathbf{x_0} \right | <\delta,", font_size = 48, color = ORANGE)
        twod_limit3 = MathTex(
            r"\left | \sin(\left | \mathbf{x} \right | )-0 \right |<\left | \mathbf{x} \right | <\epsilon", font_size = 48, 
            color = GREEN_B
        )
        twod_limit = VGroup(twod_limit0, twod_limit1, twod_limit2, twod_limit3).arrange(RIGHT, buff = 0.3).set_opacity(0)
        self.add_fixed_in_frame_mobjects(x, x0)
        self.play(x.animate.set_opacity(1), x0.animate.set_opacity(1), run_time = 1.3)
        self.wait(1.6)
        integrity = VGroup(xy_grid, f_surface, g_surface, axes)
        self.play(integrity.animate.set_opacity(0.15), run_time = 1.8)
        self.add_fixed_in_frame_mobjects(twod_limit)
        self.play(twod_limit.animate.set_opacity(1), run_time = 1.6)
        arrow = MathTex(r"\Leftrightarrow", font_size = 54, color  =YELLOW_A).rotate(PI/2).set_opacity(0)
        limit = MathTex(r"\lim_{\mathbf{x} \to \mathbf{x_0}}\sin(\left | \mathbf{x} \right | ) =0", font_size = 54, color = YELLOW_A)
        limit.set_opacity(0)
        al = VGroup(arrow, limit).arrange(DOWN, buff = 0.2)
        al.shift(1.2 * DOWN)
        self.add_fixed_in_frame_mobjects(al)
        self.wait()
        self.play(al.animate.set_opacity(1), run_time = 1.1)
        self.wait(2.5)
        label = VGroup(fxy, x, x0, twod_limit)
        self.play(integrity.animate.set_opacity(0), label.animate.shift(6 * UP), al.animate.shift(5 * DOWN), run_time = 2.6)
        self.wait(0.5)

# 曲面上的距离的可视化
class SurfaceExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 70 * DEGREES, theta = 30 * DEGREES)
        sphere = Sphere(
            radius = 2, resolution = (30, 30), u_range = [0, TAU], v_range = [0, PI], fill_opacity = 0.5, stroke_width = 0     
        ).set_color(GREEN_B)
        point1 = np.array([1.6, -1.2, 0])
        point2 = np.array([1, 1, np.sqrt(2)])
        dot1 = Dot3D(point = point1, color = YELLOW, radius = 0.06)
        dot2 = Dot3D(point = point2, color = YELLOW, radius = 0.06)

        # 创建大圆圆弧
        def create_great_circle_arc(p1, p2, radius):
            p1_norm = p1/np.linalg.norm(p1)
            p2_norm = p2/np.linalg.norm(p2)
            dot_product = np.dot(p1_norm, p2_norm)
            angle = np.arccos(np.clip(dot_product, -1, 1))
            arc = ParametricFunction(
                lambda t: radius * (np.sin((1 - t) * angle) * p1_norm + np.sin(t * angle) * p2_norm)/np.sin(angle), 
                t_range = [0, 1, 0.01], color = YELLOW_A, stroke_width = 4
            )
            return arc

        def func(x, y):
            return np.sin(np.sqrt(x**2 + y**2))
        
        # 计算优化测地线
        def compute_optimized_geodesic(p1, p2, num_points = 70):
            x1, y1, z1 = p1
            x2, y2, z2 = p2
            initial_guess = []
            for i in range(1, num_points - 1):
                t = i/(num_points - 1)
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                initial_guess.extend([x, y])

            # 计算路径长度(目标函数)
            def path_length(params):
                points = []
                points.append([x1, y1])
                for i in range(0, len(params), 2):
                    points.append([params[i], params[i + 1]])
                points.append([x2, y2])
                length = 0
                for i in range(len(points) - 1):
                    x1_, y1_ = points[i]
                    x2_, y2_ = points[i + 1]
                    z1_ = np.sin(np.sqrt(x1_**2 + y1_**2))
                    z2_ = np.sin(np.sqrt(x2_**2 + y2_**2))
                    dx = x2_ - x1_
                    dy = y2_ - y1_
                    dz = z2_ - z1_
                    length += np.sqrt(dx**2 + dy**2 + dz**2)
                return length
            
            result = minimize(path_length, initial_guess, method = 'CG')
            geodesic_points = []
            geodesic_points.append([x1, y1, z1])
            optimized_params = result.x
            for i in range(0, len(optimized_params), 2):
                x = optimized_params[i]
                y = optimized_params[i + 1]
                z = np.sin(np.sqrt(x**2 + y**2))
                geodesic_points.append([x, y, z])
            geodesic_points.append([x2, y2, z2])
            return np.array(geodesic_points)

        # 创建三维的测地曲线
        def create_3d_curve(points):
            curve = VMobject(stroke_color = YELLOW_A, stroke_width = 4)
            curve.set_points_smoothly(points)
            return curve

        surface = Surface(
            lambda u, v: np.array([u, v, func(u, v)]), u_range = [-3, 3], v_range = [-3, 3], resolution = (30, 30), fill_opacity = 0.5, 
            stroke_width = 0
        )
        connecting_curve = create_great_circle_arc(point1, point2, sphere.radius)
        self.play(Create(sphere), run_time = 1.6)
        self.wait(0.5)
        self.play(Create(dot1), Create(dot2), run_time = 1.1)
        self.wait(0.8)
        self.play(Create(connecting_curve), run_time = 1.8)
        self.wait(1.6)
        self.play(FadeOut(connecting_curve), FadeOut(dot1), FadeOut(dot2), run_time = 0.9)
        self.wait(0.4)
        self.play(ReplacementTransform(sphere, surface), run_time = 2)
        point1 = np.array([2.4, 1, np.sin(np.sqrt(6.76))])
        point2 = np.array([1.2, -1.2, np.sin(np.sqrt(2.88))])
        dot1 = Dot3D(point = point1, color = YELLOW, radius = 0.06)
        dot2 = Dot3D(point = point2, color = YELLOW, radius = 0.06)
        geodesic_points = compute_optimized_geodesic(point1, point2)
        geodesic_curve = create_3d_curve(geodesic_points)
        self.wait()
        self.play(Create(dot1), Create(dot2), run_time = 1.1)
        self.wait(0.8)
        self.play(Create(geodesic_curve), run_time = 1.8)
        self.wait(1.6)
        self.move_camera(phi = 0 * DEGREES, theta = 30 * DEGREES, distance = 0.5, run_time = 3)
        self.wait()
        self.move_camera(phi = 70 * DEGREES, theta = -60 * DEGREES, distance = 0.5, run_time = 3)
        self.wait()
        integrity = VGroup(dot1, dot2, geodesic_curve, surface)
        self.play(FadeOut(integrity), run_time = 1.6)
        self.wait(0.4)
