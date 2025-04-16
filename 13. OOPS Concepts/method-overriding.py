# Polymorphism means "many forms". It allows us to define methods in a parent class and override them in child classes.
# Method overiding and method overloading are two different concepts of polymorphism.

# Method Overiding
# Explain through an car example


# Define a class named Car
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start(self):
        return f"{self.name} is starting!"

    def stop(self):
        return f"{self.name} is stopping!"

    def accelerate(self):
        return f"{self.name} is accelerating to {self.speed} km/h!"


# Define a class named SportsCar that inherits from Car
class SportsCar(Car):
    def __init__(self, name, speed, turbo_speed):
        super().__init__(name, speed)
        self.turbo_speed = turbo_speed

    def accelerate(self):
        return f"{self.name} is accelerating to {self.turbo_speed} km/h with turbo!"


c = Car("Maruti", 60)
print(c.accelerate())


s = SportsCar("BMW", 80, 160)
print(s.accelerate())
