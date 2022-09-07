from math import sin
from manim import *

class Plot(Scene):
  def construct(self):

    x0 = -PI
    x1 = PI

    k = ValueTracker(-PI)

    ax1 = (
      Axes(x_range=[x0,x1, x1/2], y_range=[-1,1,0.5], x_length=6, y_length=6)
      .to_edge(RIGHT)
      # .add_coordinates()
      .set_color(WHITE)
    )
    
    func = ax1.plot(
      lambda x: sin(x),
      x_range=[-PI,PI],
      color=BLUE)

    pt = always_redraw(
      lambda: Dot().move_to(
        ax1.c2p(k.get_value(), sin(k.get_value()))
      )
    )

    self.play(Create(ax1))
    self.play(Create(pt))
    self.play(Create(func), k.animate.set_value(PI), run_time=4)
    self.wait()
