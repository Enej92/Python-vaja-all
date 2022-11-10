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


lebron = BasketballPlayer(first_name="LeBron", last_name="James", height_cm=203, weight_kg=113, points=27)
kevin = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2)

print(lebron.first_name)
print(kevin.first_name)

seznam = [lebron, kevin]

for player in seznam:
    print(f"{player.first_name} {player.last_name}")
