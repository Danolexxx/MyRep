class GeometryFigure:
    def __init__(self, Square, Perimetr):
        self.Square = Square
        self.Perimetr = Perimetr

    def say_figure(self):
        print("Площадь = ", self.Square, ", периметр = ", self.Perimetr)

Figure1 = GeometryFigure(25,20)
Figure1.say_figure()
