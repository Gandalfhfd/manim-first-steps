from manim import *
from math import sin, cos

class TextChange(Scene):
  def construct(self):
    x0 = -PI
    x1 = PI

    x_var = Variable(x0, 'x')

    grad_lab = always_redraw(
      lambda: Variable(
        cos(x0),
        MathTex(r'\frac{d(\sin(x))}{dx}'), # r shows this is raw text
        num_decimal_places=3).scale(0.5).to_edge(DOWN, buff=0.25)
    )


    grad_lab.add_updater(
      lambda v: v.tracker.set_value(cos(x_var.tracker.get_value()))
    )

    grad_lab.scale(0.5)

    self.add(grad_lab)
    self.play(
      x_var.tracker.animate.set_value(x1), 
      run_time=2)
    self.wait(1)
