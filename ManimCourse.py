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

    total_area = plane.get_area(graph=func, x_range=[-0,PI])

    # Draw everything
    self.play(DrawBorderThenFill(plane)) # Create the plane

    # Draw function and labels simultaneously
    self.play(Create(func), Create(labels))
    self.wait()
    # self.play(Create(area), run_time=2)
    # self.wait()
    self.play(Create(total_area))
    self.wait()
