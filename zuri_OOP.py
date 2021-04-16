class Car:
    """
    This is a class representing a car
    """
    def __init__(self, name, color, drive):
        self.name = name
        self.color = color
        self.drive = drive

    
    def accelerate(self):
        print(f'{self.name} accelerates at 1000mph')


car_1 = Car('Benz', 'Red', '4 wheel drive')
car_2 = Car('Bmw', 'Blue', '4 wheel drive')
print(car_1.name)
print(car_1.drive)
print(car_1.color)
car_1.accelerate()
car_2.accelerate()

print(help(Car))