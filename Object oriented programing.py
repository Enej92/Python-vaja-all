# var: str = "string"
# var2: int = 33
# var3: bool = True

# var4: list = ["sdd", 2, True]
# var5: dict = {"Neki": 30}

# OOP - Object oriented programing (napredni dictionary) class = model

# class BasketballPlayer():
#  def __init__(self, first_name, last_name, height_cm, weight_kg, ppg):
#      self.first_name = first_name
#      self.last_name = last_name
#       self.height_cm = height_cm
#       self.weight_kg = weight_kg
#       self.ppg = ppg

from dataclasses import dataclass


@dataclass
class BasketballPlayer:
    first_name: str
    last_name: str
    height_cm: int
    weight_kg: float
    points: float

    def __str__(self):
        return f"{self.first_name} {self.last_name}{self.height_cm}{self.weight_kg}{self.points}"

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.


lebron = BasketballPlayer(first_name="LeBron", last_name="James", height_cm=203, weight_kg=113, ppg=27)
kevin = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, ppg=27.2)

print(lebron.first_name)
print(kevin.first_name)

seznam = [lebron, kevin]

for player in seznam:
    print(f"{player.first_name} {player.last_name}")
