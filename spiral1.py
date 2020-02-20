import turtle
def spiral(sides,turn,color,width):
	t=turtle.Turtle()
	t.color(color)
	t.width(width)
	for n in range(100):
		t.forward(n)
		t.right(turn)

spiral(150,-30,"blue",10)