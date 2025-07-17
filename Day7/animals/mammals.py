class Dog:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def print_info(self):
        print(f'품종: {self.breed}')
        print(f'나이 {self.age}')
