class tower:
    def __init__(self, power, tower_type, size= 50, rate_of_fire = 10) -> None:
        self.power = power
        self.tower_type = tower_type
        self.size = size
        self.rate_of_fire = rate_of_fire
        self.health = 100
    
    def fire(self, unit_armour):
        new_power = self.power - unit_armour
        if 0 > new_power:
            new_power = 0
        return self.rate_of_fire * new_power
    
    def take_damage(self, shot_power):
        if shot_power >= self.health:
            self.health = 0
            self.size = 0
            return
        self.health -= shot_power
        self.size = int(self.size * (self.health/100))

def test_tower_init():
    t = tower(5, "cannon")
    assert t.power == 5
    assert t.tower_type == "cannon"
    assert t.size == 50
    assert t.rate_of_fire == 10

def test_tower_fire():
    t = tower(5, "cannon")
    assert t.fire(4) == 10
    assert t.fire(5) == 0
    assert t.fire(500) == 0
    assert t.fire(0) == 50

def test_take_damage():
    t = tower(5, "cannon")
    t.take_damage(0)
    assert t.health == 100
    assert t.size == 50
    t.take_damage(50)
    assert t.health == 50
    assert t.size == 25
    t.take_damage(60)
    assert t.health == 0
    assert t.size == 0
    t.take_damage(10)
    assert t.health == 0
    assert t.size == 0