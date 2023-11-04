import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius


print(f'Welcome to the Circle Tester')

while True:
    try:
        my_radius = float(input("Enter a radius: \n> "))
        c1 = Circle(my_radius)
        print(f'Diameter: {c1.calculate_diameter()}')
        print(f'Circumference: {c1.calculate_circumference()}')
        print(f'Area: {c1.calculate_area()}')

        while True:
            grow_circle = input('Would you like your circle to grow? (y/n) \n> ').lower()

            if grow_circle == 'y':
                print('Standby while your circle magically grows...')
                c1.grow()
                print(f'Diameter: {c1.calculate_diameter()}')
                print(f'Circumference: {c1.calculate_circumference()}')
                print(f'Area: {c1.calculate_area()}')

            elif grow_circle == 'n':
                print('Goodbye')
                break

            else:
                print('I am sorry, that entry is invalid. Please try again.')

        break

    except ValueError:
        print('I am sorry, that entry is invalid. Please enter a number.')
