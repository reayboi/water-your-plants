import datetime

class Plant:
    def __init__(self, name, age, last_watered, needs_watered=False, water_frequency=7):
        self.name = name
        self.age = age
        self.needs_watered = needs_watered
        self.last_watered = last_watered
        self.water_frequency = water_frequency
    def check_water_status(self):
        if(self.last_watered + datetime.timedelta(days=self.water_frequency) < datetime.datetime.now()):
            self.needs_watered == True
            print(f"{self.name} needs watered today!")
        else:
            print(f"{self.name} does not need watered today")
    def water_plant(self):
        self.needs_watered = False
        self.last_watered = datetime.datetime.now()
        print(f"{self.name} was just watered!")


Kiki = Plant("Kiki", "2 year", datetime.datetime(2023, 4, 9, 12, 30))
Kiki.check_water_status()
