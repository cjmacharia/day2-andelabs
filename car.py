class Car:
    model = 'GM'
    name = 'General'
    car_type = ''
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='General', model='GM', car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.init_properties()

    def init_properties(self):
        two_doors = ['Porshe', 'Koenigsegg']
        if self.name in two_doors:
            self.num_of_doors = 2

        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    def drive(self, speed):
        self.speed = speed
        return self

    def is_saloon(self):
        return self.car_type != 'trailer'
print(Car('general'))
       