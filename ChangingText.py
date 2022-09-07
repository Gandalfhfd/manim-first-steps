from manim import *
from math import sin, cos

class TextChange(Scene):
  def construct(self):
    x0 = -PI
    x1 = PI

    x_var = Variable(x0, 'x')

    grad_lab = Variable(
      cos(x0),
      MathTex(r'\frac{d(\sin(x))}{dx}'), # r shows this is raw text
      num_decimal_places=3)

    grad_lab.add_updater(
      lambda v: v.tracker.set_value(cos(x_var.tracker.get_value()))
    )

    self.add(grad_lab)
    self.play(
      x_var.tracker.animate.set_value(x1), 
      run_time=2)
    self.wait(1)
