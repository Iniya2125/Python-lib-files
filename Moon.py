import turtle

def draw_third_day_moon():
  """Draws a crescent moon representing the third day of the lunar cycle."""

  # Create a turtle object
  moon = turtle.Turtle()
  moon.speed(0)  # Set the drawing speed to fastest

  # Set up the drawing window
  screen = turtle.Screen()
  screen.bgcolor("black")  # Set the background color to black

  # Draw the outer circle (full moon)
  moon.color("white")
  moon.begin_fill()
  moon.circle(25)
  moon.end_fill()

  # Draw the inner circle (dark side of the moon)
  moon.color("black")
  moon.begin_fill()
  moon.circle(20)
  moon.end_fill()

  # Hide the turtle
  moon.hideturtle()

  # Keep the drawing window open until clicked
  turtle.done()

if __name__ == "__main__":
  draw_third_day_moon()


