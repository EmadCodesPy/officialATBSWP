class person:
    def __init__(self, name, country, DOB) -> None:
        self.name = name
        self.country = country
        self.DOB = DOB
        pass
    def find_age(self):
        age = 2024 - self.DOB
        return f'The age of {self.name} from {self.country} is {age} years old'
    def origin(self):
        return f'{self.name} is from {self.country}'
    
    


p1 = person('Emad', 'Yemen', 2005)

print(p1.find_age())
print(p1.origin())
