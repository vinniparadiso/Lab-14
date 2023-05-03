#Sarah, Vinni, Breanna
class Mug:
    """Represents a coffee mug
    attributes capacity, shape, material, color"""

coffee = Mug()
coffee.capacity = 8
coffee.shape = "cylinder"
coffee.materal = "ceramic"
coffee.amount = 6

def coffee_drinking_sim(c, y):
    if c.amount > 0:
        x=c.amount-y
        return x
    else:
        return "empty"

print (coffee_drinking_sim(coffee, 2))
