# Krav för godkänt
# Du ska skapa attribut for klassen Bottle.
# Skriv fardigt __init__-metoden sa att alla metoder fungerar.

class Bottle:
    def __init__(self) -> None:
        # TODO Skriv metoden
        # Fundera pa vilka attribut som behovs for att metoderna ska fungera.
        pass

    def __str__(self) -> str:
        return f"The bottle has {self.contents} ml left of the starting volume of {self.volume} ml."

    def fill(self, ml):
        self.contents += ml
        if self.contents > self.volume:
            print("Water is spilling over, but the bottle is full.")
            self.contents = self.volume
        else:
            print(f"The bottle is now {100*self.contents/self.volume} % full.")

    def empty(self):
        if self.contents == 0:
            print("The bottle is already empty.")
        self.contents = 0


# Testfall (ska fungera nar __init__ ar klar)
if __name__ == "__main__":
    bottle_a = Bottle(500, 200)
    print(bottle_a)
    bottle_a.fill(100)
    print(bottle_a)
    bottle_a.fill(300)  # ska spilla over och sluta pa maxvolym
    print(bottle_a)

    bottle_b = Bottle(1000, 0)
    print(bottle_b)
    bottle_b.empty()  # ska skriva att den redan ar tom
    bottle_b.fill(1000)
    print(bottle_b)
    bottle_b.empty()
    print(bottle_b)
