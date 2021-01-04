import random


class Car:
    type = 'basic car'

    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        print(f'{self.name} goes')

    def stop(self):
        print(f'{self.name} stops')
        self.speed = 0

    def turn(self):
        turn_dict = {0: 'left', 1: 'right'}
        print(f'{self.name} turns {turn_dict[random.randint(0, 1)]}')

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')


class TownCar(Car):
    type = 'town car'

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')
        if self.speed > 60:
            print('Over speed!')


class SportCar(Car):
    type = 'sport car'


class WorkCar(Car):
    type = 'work car'

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')
        if self.speed > 40:
            print('Over speed!')


class PoliceCar(Car):
    type = 'police car'


car = Car(random.randint(0, 140), 'red', 'Mazda', False)
town_car = TownCar(random.randint(0, 140), 'black', 'Honda', False)
sport_car = SportCar(random.randint(0, 140), 'pink', 'Bugatti', False)
work_car = WorkCar(random.randint(0, 140), 'gold', 'BMW', False)
police_car = PoliceCar(random.randint(0, 140), 'blue', 'Audi', True)

print(f'{car.type}: {car.name}, {car.color}, {"" if car.is_police else "not"} police')
car.go()
car.show_speed()
car.turn()
car.stop()
car.show_speed()
print()

print(f'{town_car.type}: {town_car.name}, {town_car.color}, {"" if town_car.is_police else "not"} police')
town_car.go()
town_car.show_speed()
town_car.turn()
town_car.stop()
town_car.show_speed()
print()

print(f'{sport_car.type}: {sport_car.name}, {sport_car.color}, {"" if sport_car.is_police else "not"} police')
sport_car.go()
sport_car.show_speed()
sport_car.turn()
sport_car.stop()
sport_car.show_speed()
print()

print(f'{work_car.type}: {work_car.name}, {work_car.color}, {"" if work_car.is_police else "not"} police')
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.stop()
work_car.show_speed()
print()

print(f'{police_car.type}: {police_car.name}, {police_car.color}, {"" if police_car.is_police else "not"} police')
police_car.go()
police_car.show_speed()
police_car.turn()
police_car.stop()
police_car.show_speed()
