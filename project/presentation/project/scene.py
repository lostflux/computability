from manim import *

class CreateCircle(Scene):
  def construct(self):
    # circle = Circle()  # create a circle
    # circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
    # self.play(Create(circle))  # show the circle on screen

    circle = Circle()  # create a circle
    circle.set_fill(PINK, opacity=0.5)  # set color and transparency

    square = Square()  # create a square
    square.rotate(PI / 4)  # rotate a certain amount

    self.play(Create(square))  # animate the creation of the square
    self.play(Transform(square, circle))  # interpolate the square into the circle
    self.play(FadeOut(square))  # fade out animation

    # show integral of f(x) = x^2
    integral = MathTex(r"\int_{0}^{1} x^2 dx = \frac{1}{3}")
    self.play(Create(integral))  # show the integral on screen
    self.play(FadeOut(integral))  # fade out the integral

    # category theory diagram
    diagram = MathTex(r"\text{Sets} \rightarrow \text{Groups} \rightarrow \text{Ring}")
    self.play(Create(diagram))  # show the diagram on screen
    # wait for 2 seconds
    self.wait(4)
    self.play(FadeOut(diagram))  # fade out the diagram

    # draw category-theory diagram of maps between categories (\phi, \psi)
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{tikz-cd}")
    diagram = Tex(r"""
      \begin{tikzcd}
        A \arrow[d, "g"] \arrow[r, "f"] & B \arrow[r, "\alpha"] \arrow[d, "\gamma"] & D \arrow[d, "\beta"] \\
        C \arrow[rru, "h"] & B' \arrow[r, "\lambda"] & D'
      \end{tikzcd}
    """,
    tex_template=myTemplate)
    
    self.play(Create(diagram))  # show the diagram on screen
    self.wait(4)  # wait for 4 seconds
    self.play(FadeOut(diagram))  # fade out the diagram


