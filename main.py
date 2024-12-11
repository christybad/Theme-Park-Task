class Attraction():
    def __init__(self,name,capacity):
        self._name = name
        self._capacity = capacity
        self._status = False

    def get_details(self):
        print(f'Attraction name: {self._name}')
        print(f'Attraction capacity: {self._capacity}')

    def start(self):
        print('The attraction is starting')

    def open_attraction(self):
        self._status = True

    def close_attraction(self):
        self._status = False
    
class ThrillRide(Attraction):
    def __init__(self,name,capacity,_min_height):
        super().__init__(name,capacity)
        self._min_height = _min_height

    def start(self):
        if self._status == True:
            print(f'Thrill Ride {self._name} is now starting. Hold on tight!')
        else:
           print(f'{self._name} is closed')

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
        if self._status == True:
            print(f"Family Ride {self._name} is now starting. Enjoy the fun!")
        else:
            print(f'{self._name} is closed')
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
        print(f"Staff {self._name} is performing their role: {self.role}.")

staff1 = Staff('Mr Mahdi','tech')
staff2 = Staff('Mr Walkden','tech')

class Manager(Staff):
    def __init__(self,name,role):
        super().__init__(name,role)
        self._team = []

    def add_staff(self,staff):
        self._team.append(staff)

    def get_team_summary(self):
        for x in self._team:
            print(f'{x._name} Role: {x._role}')

manager = Manager('Mr Balon','headteacher')
manager.add_staff(staff1)
manager.add_staff(staff2)
manager.get_team_summary()
class Visitor():
    def __init__(self,name,age,height):
        self._name = name
        self._age = age
        self._height = height

    def ride(self,attraction):
        print(f'{self._name} wants to ride {attraction._name}')
        attraction.is_eligible(self._height)
        attraction.is_eligible(self._age)

    
dragonCoaster = ThrillRide('Dragon Coaster',20,140)
saw = ThrillRide('SAW',30,140)
merryGoRound = FamilyRide('Merry-Go-Round',30,4)
visitor1 = Visitor('Fathima',3,100)

visitor1.ride(dragonCoaster)
visitor1.ride(merryGoRound)
#dragonCoaster.open_attraction()
merryGoRound.open_attraction()
dragonCoaster.start()
merryGoRound.start()






