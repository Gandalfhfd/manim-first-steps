from math import sin, cos
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

    x0 = -PI # Start value
    x1 = PI # End value

    # Moves smoothly from x0 to wherever we choose.
    k = ValueTracker(x0)


    ## AXES
    # Cartesian coordinate axes, final argument in x_range must divide the range
    # evenly
    ax0 = (
      Axes(x_range=[x0,x1,(x1-x0)/4],
        y_range=[-1,1,0.5],
        x_length=6,
        y_length=6)
      .to_edge(LEFT)
      .set_color(WHITE)
    )

    # Cartesian coordinate axes
    ax1 = (
      Axes(x_range=[x0,x1,(x1-x0)/4],
        y_range=[-1,1,0.5],
        x_length=6,
        y_length=6)
      .to_edge(RIGHT)
      .set_color(WHITE)
    )

    # Cartesian coordinate axes
    ax2 = (
      Axes(x_range=[x0,x1,(x1-x0)/4],
        y_range=[-1,1,0.5],
        x_length=6,
        y_length=6)
      .to_edge(RIGHT)
      .set_color(WHITE)
    )

    # Cartesian coordinate axes
    ax3 = (
      Axes(x_range=[x0,x1,(x1-x0)/4],
        y_range=[-1,1,0.5],
        x_length=6,
        y_length=6)
      .to_edge(RIGHT)
      .set_color(WHITE)
    )

    # Cartesian coordinate axes
    ax4 = (
      Axes(x_range=[x0,x1,(x1-x0)/4],
        y_range=[-1,1,0.5],
        x_length=6,
        y_length=6)
      .to_edge(RIGHT)
      .set_color(WHITE)
    )

    ## FUNCTIONS
    # Function we wish to take the derivative of
    func = ax0.plot(lambda x: sin(x), x_range=[x0,x1], color=BLUE)

    # First derivative function
    deriv1 = ax1.plot(lambda x: sin(PI/2-x), x_range=[x0,x1], color=YELLOW)

    # Second derivative function
    deriv2 = ax2.plot(lambda x: -sin(x), x_range=[x0,x1], color=YELLOW)

    # Third derivative function
    deriv3 = ax3.plot(lambda x: -sin(PI/2-x), x_range=[x0,x1], color=YELLOW)

    # Fourth derivative function
    deriv4 = ax4.plot(lambda x: sin(x), x_range=[x0,x1], color=YELLOW)


    ## TANGENT LINES
    # Tangent line to the function
    tangent0 = always_redraw( # Keep it updated
      lambda: ax0.get_secant_slope_group( # Find a tangent and put it on ax0
        x=k.get_value(), # vary x based on value of k
        graph=func, # the specific function we're interested in
        dx=0.01, # precision of the tangent line
        secant_line_color=YELLOW,
        secant_line_length=1,
      )
    )

    # Tangent line to the first derivative
    tangent1 = always_redraw( # Keep it updated
      lambda: ax1.get_secant_slope_group( # Find a tangent and put it on ax1
        x=k.get_value(), # vary x based on value of k
        graph=deriv1, # the specific function  we're interested in
        dx=0.01, # precision of the tangent line
        secant_line_color=YELLOW,
        secant_line_length=1,
      )
    )

    # Tangent line to the second derivative
    tangent2 = always_redraw( # Keep it updated
      lambda: ax2.get_secant_slope_group( # Find a tangent and put it on ax2
        x=k.get_value(), # vary x based on value of k
        graph=deriv2, # the specific function we're interested in
        dx=0.01, # precision of the tangent line
        secant_line_color=YELLOW,
        secant_line_length=1,
      )
    )

    # Tangent line to the third derivative
    tangent3 = always_redraw( # Keep it updated
      lambda: ax3.get_secant_slope_group( # Find a tangent and put it on ax3
        x=k.get_value(), # vary x based on value of k
        graph=deriv3, # the specific function we're interested in
        dx=0.01, # precision of the tangent line
        secant_line_color=YELLOW,
        secant_line_length=1,
      )
    )


    ## POINTS
    # Point showing where the 1st tangent line is
    pt0 = always_redraw(
        lambda: Dot(color=RED).move_to(
          ax0.c2p(k.get_value(), func.underlying_function(k.get_value()))
        )
    )

    # Point showing where the 2nd tangent line is
    pt1 = always_redraw(
      lambda: Dot(color=RED).move_to(
        ax1.c2p(k.get_value(), deriv1.underlying_function(k.get_value()))
      )
    )

    # Point showing where the 2rd tangent line is
    pt2 = always_redraw(
      lambda: Dot(color=RED).move_to(
        ax2.c2p(k.get_value(), deriv2.underlying_function(k.get_value()))
      )
    )

    # Point showing where the 4th tangent line is
    pt3 = always_redraw(
      lambda: Dot(color=RED).move_to(
        ax3.c2p(k.get_value(), deriv3.underlying_function(k.get_value()))
      )
    )

    # Point showing where the 4th derivative is
    pt4 = always_redraw(
      lambda: Dot(color=RED).move_to(
        ax4.c2p(k.get_value(), deriv4.underlying_function(k.get_value()))
      )
    )

    ## LABELS
    # Labels for function
    labels_func = ax0.get_axis_labels(
      x_label='x', y_label='f(x)')

    # Labels for first derivative
    labels_deriv1 = always_redraw(
      lambda: ax1.get_axis_labels(
        x_label='x', y_label='f^{\prime}(x)')
    )

    # Labels for second derivative
    labels_deriv2 = always_redraw(
      lambda: ax2.get_axis_labels(
        x_label='x', y_label='f^{\prime\prime}(x)')
    )

    # Labels for third derivative
    labels_deriv3 = always_redraw(
      lambda: ax3.get_axis_labels(
        x_label='x', y_label='f^{\prime\prime\prime}(x)')
    )

    # Labels for fourth derivative
    labels_deriv4 = always_redraw(
      lambda: ax4.get_axis_labels(
        x_label='x', y_label='f^{\prime\prime\prime\prime}(x)=f(x)')
    )
  
    
    ## TITLES
    # Title for the function
    title_func = always_redraw(
      lambda: MathTex('\sin(x)').next_to(ax0, DOWN, buff=0.25)
    )

    # Title for the first derivative
    title_deriv1 = always_redraw(
      lambda: MathTex('\cos(x)').next_to(ax1, DOWN, buff=0.25)
    )

    # Title for the second derivative
    title_deriv2 = always_redraw(
      lambda: MathTex('-\sin(x)').next_to(ax2, DOWN, buff=0.25)
    )

    # Title for the third derivative
    title_deriv3 = always_redraw(
      lambda: MathTex('-\cos(x)').next_to(ax3, DOWN, buff=0.25)
    )

    # Title for the fourth derivative
    title_deriv4 = always_redraw(
      lambda: MathTex('\sin(x)').next_to(ax4, DOWN, buff=0.25)
    )

    ## Labels which show derivative
    # works like a value tracker
    x_var = Variable(x0, 'x')
    
    # Label showing gradient of function
    grad_lab0 = (
      Variable(
        cos(x0),
        MathTex(r'\frac{d(\sin(x))}{dx}=\cos(x)'), # r shows this is raw text
        num_decimal_places=3)
        .to_edge(UP, buff=0)
        .scale(0.7)
    )

    grad_lab0.add_updater(
      lambda v: v.tracker.set_value(cos(x_var.tracker.get_value()))
    )

    # Label showing gradient of first derivative
    grad_lab1 = (
      Variable(
        -sin(x0),
        MathTex(r'\frac{d(\cos(x))}{dx}=-\sin(x)'), # r shows this is raw text
        num_decimal_places=3)
        .to_edge(UP, buff=0)
        .scale(0.7)
    )

    grad_lab1.add_updater(
      lambda v: v.tracker.set_value(-sin(x_var.tracker.get_value()))
    )
    
    # Label showing gradient of second derivative
    grad_lab2 = (
      Variable(
        -cos(x0),
        MathTex(r'\frac{d(-\sin(x))}{dx}=-\cos(x)'), # r shows this is raw text
        num_decimal_places=3)
        .to_edge(UP, buff=0)
        .scale(0.7)
    )

    grad_lab2.add_updater(
      lambda v: v.tracker.set_value(-cos(x_var.tracker.get_value()))
    )

    # Label showing gradient of third derivative
    grad_lab3 = (
      Variable(
        sin(x0),
        MathTex(r'\frac{d(-\cos(x))}{dx}=\sin(x)'), # r shows this is raw text
        num_decimal_places=3)
        .to_edge(UP, buff=0)
        .scale(0.7)
    )

    grad_lab3.add_updater(
      lambda v: v.tracker.set_value(sin(x_var.tracker.get_value()))
    )

    ### ANIMATE
    ## STEP 1
    # Create axes and label them
    self.add(ax0, labels_func, title_func, func, pt0)

    self.play(
      Create(ax1),
      Write(labels_deriv1),
      Write(title_deriv1),
      Write(grad_lab0)
    )

    # Create the tangent lines and the points
    self.play(Create(tangent0), Create(pt1))

    # Draw the 1st derivative and move the tangent line
    self.play(
      Create(deriv1),
      k.animate.set_value(x1),
      x_var.tracker.animate.set_value(x1),
      run_time=4)

    # Make LHS disappear
    self.play(
      FadeOut(ax0),
      FadeOut(pt0),
      FadeOut(func),
      FadeOut(tangent0),
      FadeOut(labels_func),
      FadeOut(title_func),
      FadeOut(grad_lab0),
      k.animate.set_value(x0),
    )

    # Reset x_var
    x_var.tracker.set_value(x0)

    # Create second tangent line
    self.play(Create(tangent1))

    # Move the first derivative to the left
    self.play(
      ax1.animate.to_edge(LEFT),
      deriv1.animate.to_edge(LEFT).set_color(BLUE))

    ## STEP 2
    # Create the axes for second derivative and label them
    self.play(
      Create(ax2),
      Write(labels_deriv2),
      Write(title_deriv2),
      Write(grad_lab1)
    )

    # Create the point which will draw the second derivative
    self.play(Create(pt2))

    # Draw the second derivative
    self.play(
      k.animate.set_value(x1),
      x_var.tracker.animate.set_value(x1),
      Create(deriv2),
      run_time=4
    )

    # Make LHS disappear
    self.play(
      FadeOut(ax1),
      FadeOut(pt1),
      FadeOut(deriv1),
      FadeOut(tangent1),
      FadeOut(labels_deriv1),
      FadeOut(title_deriv1),
      FadeOut(grad_lab1),
      k.animate.set_value(x0)
    )

    # Reset x_var
    x_var.tracker.set_value(x0)

    # Create third tangent line
    self.play(Create(tangent2))

    # Move the second derivative to the left
    self.play(
      ax2.animate.to_edge(LEFT),
      deriv2.animate.to_edge(LEFT).set_color(BLUE))

    ## PART 3
    # Create the axes for third derivative and label them
    self.play(
      Create(ax3),
      Write(labels_deriv3),
      Write(title_deriv3),
      Write(grad_lab2)
    )

    # Create the point which will draw the third derivative
    self.play(Create(pt3))

    # Draw the third derivative
    self.play(
      k.animate.set_value(x1),
      x_var.tracker.animate.set_value(x1),
      Create(deriv3),
      run_time=4
    )

    # Make LHS disappear
    self.play(
      FadeOut(ax2),
      FadeOut(pt2),
      FadeOut(deriv2),
      FadeOut(tangent2),
      FadeOut(labels_deriv2),
      FadeOut(title_deriv2),
      FadeOut(grad_lab2),
      k.animate.set_value(x0)
    )

    # Reset x_var
    x_var.tracker.set_value(x0)

    # Create fourth tangent line
    self.play(Create(tangent3))

    # Move the third derivative to the left
    self.play(
      ax3.animate.to_edge(LEFT),
      deriv3.animate.to_edge(LEFT).set_color(BLUE))

    ## PART 4
    # Create the axes for fourth derivative and label them
    self.play(
      Create(ax4),
      Write(labels_deriv4),
      Write(title_deriv4),
      Write(grad_lab3)
    )

    # Create the point which will draw the fourth derivative
    self.play(Create(pt4))

    # Draw the fourth derivative
    self.play(
      k.animate.set_value(x1),
      x_var.tracker.animate.set_value(x1),
      Create(deriv4),
      run_time=4
    )

    ## RESET
    labels_deriv5 = ax4.get_axis_labels(x_label='x', y_label='f(x)')
    # transform labels_deriv4 into labels_deriv5

    self.wait(3)

    # Make LHS disappear
    self.play(
      FadeOut(ax3),
      FadeOut(pt3),
      FadeOut(deriv3),
      FadeOut(tangent3),
      FadeOut(labels_deriv3),
      FadeOut(title_deriv3),
      FadeOut(grad_lab3),
      k.animate.set_value(x0)
    )

    # Change labels_deriv4 into labels_deriv5
    self.play(Transform(labels_deriv4, labels_deriv5))
    self.remove(labels_deriv4)

    # Move the fourth derivative to the left
    self.play(
      ax4.animate.to_edge(LEFT),
      deriv4.animate.to_edge(LEFT).set_color(BLUE),
      Transform(labels_deriv5, labels_func)
      )
# Make dot movement synchronise with graph creation
