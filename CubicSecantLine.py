from manim import *

class sec(Scene):
  def construct(self):

    ## BORING STUFF

    k = ValueTracker(4)
    dt = ValueTracker(3)

    ax = (
      Axes(
      x_range=[-1,10,1],
      y_range=[-1,6,1],
      x_length=12,
      y_length=7)
    ).add_coordinates()

    A = -0.1
    B = 1.1
    C = -2.2
    D = -0.2

    cubic_func = ax.plot(
      lambda x: A*x**3+B*x**2+C*x+D,
      x_range=[-1,10],
      color=BLUE)

    # Create a line at x=k.get_value() on the graph cubic_function
    tangent = always_redraw(
      lambda: ax.get_secant_slope_group(
        x=k.get_value(),
        graph=cubic_func,
        dx=dt.get_value(), # Shown as dt in the animation
        secant_line_color=GREEN,
        secant_line_length=10,
        dx_label='dt',
        dy_label='ds'
      )
    )

    # Lower point
    pt1 = always_redraw(
        lambda: Dot().move_to(
          ax.c2p(k.get_value(),
          cubic_func.underlying_function(k.get_value()))
        )
    )
    
    # Higher point
    pt2 = always_redraw(
        lambda: Dot().move_to(
          ax.c2p(k.get_value()+dt.get_value(),
          cubic_func.underlying_function(k.get_value()+dt.get_value()))
        )
    )

    self.play(Create(ax), Create(cubic_func))
    self.play(Create(tangent), Create(pt1), Create(pt2))
    self.play(
      dt.animate.set_value(0.01),
      k.animate.set_value(0),
      run_time=4)

    self.wait()

class Quadratic(Scene):
  def construct(self):

    k = ValueTracker(-3)
    dt = ValueTracker(6)

    ax = (
      Axes(
      x_range=[-5,5],
      y_range=[-1,10],
      x_length=12,
      y_length=7)
    ).add_coordinates()

    A = 0
    B = 1
    C = 0
    D = 0

    cubic_func = ax.plot(
      lambda x: A*x**3+B*x**2+C*x+D,
      x_range=[-3,3],
      color=BLUE)

    # Create a line at x=k.get_value() on the graph cubic_function
    tangent = always_redraw(
      lambda: ax.get_secant_slope_group(
        x=k.get_value(),
        graph=cubic_func,
        dx=dt.get_value(), # Shown as dt in the animation
        secant_line_color=GREEN,
        secant_line_length=10,
        dx_label='dt',
        dy_label='ds'
      )
    )

    # Lower point
    pt1 = always_redraw(
        lambda: Dot().move_to(
          ax.c2p(k.get_value(),
          cubic_func.underlying_function(k.get_value()))
        )
    )
    
    # Higher point
    pt2 = always_redraw(
        lambda: Dot().move_to(
          ax.c2p(k.get_value()+dt.get_value(),
          cubic_func.underlying_function(k.get_value()+dt.get_value()))
        )
    )

    label = always_redraw(
      lambda: Text('test').move_to(
        ax.c2p(k.get_value()+dt.get_value(),
          cubic_func.underlying_function(k.get_value()+dt.get_value())+0.2)
      )
    )

    self.play(Create(ax), Create(cubic_func))
    self.play(Create(tangent),
    Create(pt1),
    Create(pt2),
    Create(label))

    self.play(
      dt.animate.set_value(0.0001),
      k.animate.set_value(0),
      run_time=4)

    self.wait()
