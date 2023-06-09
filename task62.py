class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def movement(self):
        print(self.name, " - ", self.speed*int(input()))

class Gus_Robot(Robot):
    def __init__(self, name, speed, territory):
        Robot.__init__(self, name, speed)
        self.territory = territory

class Wheel_Robot(Robot):
    def __init__(self, name, speed, mark):
        Robot.__init__(self, name, speed)
        self.mark = mark
