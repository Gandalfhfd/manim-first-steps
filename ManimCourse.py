from cmath import sin
from manim import *

class Testing(Scene):
  def construct(self):

    name = Text("Gandalf").to_edge(UL, buff=0.5)
    sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(
          LEFT * 3
    )
    tri = Triangle().scale(0.6).to_edge(DR)

    self.play(Write(name))
    self.play(DrawBorderThenFill(sq), run_time=2)
    self.play(Create(tri))
    self.wait()

    self.play(name.animate.to_edge(UR), run_time=2)
    self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time = 3)
    self.wait()

class Getters(Scene):
  def construct(self):

    rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
    circ = Circle().to_edge(DOWN)
    arrow = always_redraw(lambda : Line(
                          start=rect.get_bottom(), end=circ.get_top()
                          ).add_tip())

    self.play(Create(VGroup(rect, circ, arrow)))
    self.wait()
    self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)

class Updaters(Scene):
  def construct(self):
    num = MathTex("ln(2)")
    box = always_redraw(lambda : SurroundingRectangle(
        num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5
      )
    )
    name = always_redraw(lambda : Tex
    ("Gandalf").next_to(box, DOWN, buff=0.25))

    self.play(Create(VGroup(num, box, name)))
    self.play(num.animate.shift(RIGHT * 2), run_time=2)
    self.wait()

class ValueTrackers(Scene):
  def construct(self):

    k = ValueTracker(0)
    num = always_redraw(lambda : DecimalNumber()
                        .set_value(k.get_value()))

    self.play(FadeIn(num))
    self.wait()
    self.play(k.animate.set_value(5000), run_time=5,
              rate_func=there_and_back_with_pause)
    self.wait(2)

class Graphing(Scene):
  def construct(self):

    # Background/coordinate axes
    plane = (NumberPlane(
      x_range=[-PI,PI,2], x_length=8, y_range=[-1,1,0.5], y_length=6)
      .to_edge(DOWN, buff=1)
      .add_coordinates()
    )

    # Labels, duh!
    labels = plane.get_axis_labels(x_label="x", y_label="sin(x)")

    # The mathematical function which will be plotted
    func = plane.plot(lambda x: sin(x), x_range=[-PI,PI], color=GREEN)

    area = plane.get_riemann_rectangles(
      graph=func, x_range=[-PI,PI], dx=0.08, stroke_width=0.1, stroke_color=WHITE
    )

    # Shows the area
    total_area = plane.get_area(graph=func, x_range=[-0,PI])

    # Draw everything
    self.play(DrawBorderThenFill(plane)) # Create the plane

    # Draw function and labels simultaneously
    self.play(Create(func), Create(labels))
    self.wait()
    self.play(Create(area), run_time=2)
    self.wait()

class UpdaterGraphing(Scene):
  def construct(self):

    k = ValueTracker(-4)

    ax = (
        Axes(x_range=[-4,4,1], y_range=[-2,16,2], x_length=10, y_length=6)
        .to_edge(DOWN)
        .add_coordinates()
    ).set_color(WHITE)

    func = ax.plot(lambda x: x**2, x_range=[-4,4], color=BLUE)

    tangent = always_redraw(
          lambda: ax.get_secant_slope_group(
            x=k.get_value(),
            graph=func,
            dx=0.01,
            secant_line_color=GREEN,
            secant_line_length=3,
          )
    )

    pt = always_redraw(
        lambda: Dot().move_to(
          ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
        )
    )

    self.play(Create(ax), Create(func))
    self.play(Create(tangent))
    self.add(pt)
    self.wait()
    self.play(k.animate.set_value(4), run_time=5)

class MapDerivatives(Scene):
  def construct(self):

    # Moves smoothly from -4 to wherever we choose.
    k = ValueTracker(-4)

    # Cartesian coordinate axes
    ax1 = (
      Axes(x_range=[-4,4,2], y_range=[-1,1,0.5], x_length=6, y_length=6)
      .to_edge(LEFT)
      # .add_coordinates()
      .set_color(WHITE)
    )

    # Cartesian coordinate axes
    ax2 = (
      Axes(x_range=[-4,4,2], y_range=[-1,1,0.5], x_length=6, y_length=6)
      .to_edge(RIGHT)
      # .add_coordinates()
      .set_color(WHITE)
    )

    # Function we wish to take the derivative of
    func = ax1.plot(lambda x: sin(x), x_range=[-4,4], color=BLUE)

    # Derivative function
    deriv = ax2.plot(lambda x: sin(PI/2-x), x_range=[-4,4], color=YELLOW)

    # Tangent line to the function
    tangent = always_redraw( # Keep it updated
      lambda: ax1.get_secant_slope_group( # Find the tangent to ax1 contents
        x=k.get_value(), # vary x based on value of k
        graph=func, # the specific function on ax1 we're interested in
        dx=0.01, # precision of the tangent line
        secant_line_color=PURE_GREEN,
        secant_line_length=2,
      )
    )

    # Point showing where the tangent line is
    pt1 = always_redraw(
        lambda: Dot(color=RED).move_to(
          ax1.c2p(k.get_value(), func.underlying_function(k.get_value()))
        )
    )

    # Point "drawing" the derivative
    pt2 = always_redraw(
      lambda: Dot(color=RED).move_to(
        ax2.c2p(k.get_value(), deriv.underlying_function(k.get_value()))
      )
    )

    # Animate everything
    self.play(Create(ax1), Create(ax2)) # Create axes
    self.play(Create(func)) # Draw the function
    self.play(Create(tangent), Create(pt1), Create(pt2))
    self.wait()
    self.play(
      Create(deriv),
      k.animate.set_value(4),
      run_time=5)
    self.play(FadeOut(pt2))

    # Make LHS disappear
    self.play(FadeOut(ax1), FadeOut(pt1), FadeOut(func), FadeOut(tangent))
    self.play(ax2.animate.to_edge(LEFT), deriv.animate.to_edge(LEFT))

    # Show that the sin derivatives are circular
    