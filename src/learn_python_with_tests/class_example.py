class Car:
    def __init__(self, make, model_number, color):
        self.make = make
        self.model_number = model_number
        self.color = color

    def drive(self, direction):
        print("drive in direction:", direction)

    def honk_horn(self):
        print("bwagh")

    def details(self):
        print("details are ", self.make, self.model_number, self.color)


new_car = Car("ferrari", 34, "red")

new_car.drive("forward")
new_car.honk_horn()
new_car.details()
