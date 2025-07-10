# 4. Cree las siguientes clases:
#    1. `Head`
#    2. `Torso`
#    3. `Arm`
#    4. `Hand`
#    5. `Leg`
#    6. `Feet`
#    7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.

class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.arms = [Arm("left"), Arm("right")]
        self.legs = [Leg("left"), Leg("right")]
        
        self.torso.head = self.head
        self.torso.arms = self.arms
        self.torso.legs = self.legs
        
        for leg in self.legs:
            leg.foot = Foot(leg.side)

    def __str__(self):
        return f"{self.name}"

class Head:
    def __init__(self):
        self.eyes = True
        self.ears = True
        self.mouth = True
    
    def __str__(self):
        return "Head"

class Torso:
    def __init__(self):
        self.head = None
        self.arms = []
        self.legs = []
    
    def __str__(self):
        return "Torso"

class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand(side)
    
    def __str__(self):
        return f"{self.side} Arm"

class Hand:
    def __init__(self, side):
        self.side = side
        self.fingers = True
    
    def __str__(self):
        return f"{self.side} Hand"

class Leg:
    def __init__(self, side):
        self.side = side
        self.foot = None
    
    def __str__(self):
        return f"{self.side} Leg"

class Foot:
    def __init__(self, side):
        self.side = side
        self.toes = True
    
    def __str__(self):
        return f"{self.side} Foot"


person = Human("Juan")

print(f"{person} has:")
print(f"- {person.head} with eyes, ears, and mouth")
print(f"- {person.torso} connecting:")
print(f"  * {person.arms[0]} with {person.arms[0].hand}")
print(f"  * {person.arms[1]} with {person.arms[1].hand}")
print(f"  * {person.legs[0]} with {person.legs[0].foot}")
print(f"  * {person.legs[1]} with {person.legs[1].foot}")