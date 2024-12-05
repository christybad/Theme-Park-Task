class Attraction():
    def __init__(self,name,capacity):
        self._name = name
        self._capacity = capacity

    def get_details(self):
        print(f'Attraction name: {self._name}')
        print(f'Attraction capacity: {self._capacity}')

    def start(self):
        print('The attraction is starting')

    
class ThrillRide(Attraction):
    def __init__(self,name,capacity,_min_height):
        super().__init__(name,capacity)
        self._min_height = _min_height

    def start(self):
        return f'Thrill Ride {self._name} is now starting. Hold on tight!'

    def is_eligible(self,height):
        if height < self._min_height:
           print('You are not tall enough to go on this ride')
        else:
            print('You are tall enough to go on this ride')

class FamilyRide(Attraction):
    def __init__(self,name,capacity,_min_age):
        super().__init__(name,capacity)
        self._min_age = _min_age

    def start(self):
        return f"Family Ride {self._name} is now starting. Enjoy the fun!"
    
    def is_eligible(self,age):
        if age < self._min_age:
            print('You are not old enough to go on this ride')
        else:
            print('You are old enough to go on this ride')


class Staff():
    def __init__(self,name,role):
        self._name = name
        self._role = role

    def work(self):
        return f"Staff {self._name} is performing their role: {self.role}."
    
class Visitor():
    def __init__(self,name,age,height):
        self._name = name
        self._age = age
        self._height = height

    def ride(self,attraction):
        print(f'{self._name} wants to ride {attraction._name}')
        attraction.is_eligible(self._height)

    
dragonCoaster = ThrillRide('Dragon Coaster',20,140)
merryGoRound = FamilyRide('Merry-Go-Round',30,4)
visitor1 = Visitor('Fathima',17,100)

visitor1.ride(dragonCoaster)
visitor1.ride(merryGoRound)
