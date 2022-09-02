from manim import *

class Rings(Scene):
  def construct(self):
    # set background colour to white
    self.camera.background_color = WHITE
    
    wdth = 13 # Width of the rings
    voffset = 0.5 # Vertical offset of the rings

    # Create circles and move them into position
    blue_ring = Circle(color=BLUE).shift(UP*voffset, LEFT*2.3)
    black_ring = Circle().shift(UP*voffset)
    red_ring = Circle().shift(UP*voffset, RIGHT*2.3)

    yellow_ring = Circle().shift(UP*voffset, DOWN*1.2, LEFT*1.2)
    green_ring = Circle().shift(UP*voffset, DOWN*1.2, RIGHT*1.2)


    # Set ring colours
    blue_ring.set_stroke(color=BLUE, width=wdth)
    black_ring.set_stroke(color=BLACK, width=wdth)
    red_ring.set_stroke(color=RED, width=wdth)

    yellow_ring.set_stroke(color=YELLOW, width=wdth)
    green_ring.set_stroke(color=GREEN, width=wdth)

    title = Text("Olympic Flag", color=BLACK).scale(1).to_edge(DOWN, buff=0.5)

    # Animate it
    self.play(Create(blue_ring), Create(black_ring), Create(red_ring),
              Create(yellow_ring), Create(green_ring), Write(title))
    self.wait(1)
