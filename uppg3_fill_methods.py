# Krav för godkänt
# Ditt namn
# Din klass
# Datum
# Skriv färdigt metoderna så att de gör det som beskrivs
# Fundera på vad varje metod ska göra och hur den påverkar spelarens attribut

class FootballPlayer:
    def __init__(self, name, age, goals, assists, team):
        self.name = name
        self.age = age
        self.goals = goals
        self.assists = assists
        self.team = team

    def age_up(self):
        # TODO Metoden age_up ska öka spelarens ålder med 1
        pass

    def make_goals(self, amount):
        # TODO Metoden make_goal ska öka spelarens antal mål med värdet på parametern amount
        pass

    def make_assists(self, amount):
        # TODO Metoden make_assists ska öka spelarens antal assist med värdet på parametern amount
        pass

    def change_team(self, new_team):
        # TODO Metoden change_team ska ändra spelarens lag till
        pass

    def change_lastname(self, new_lastname):
        # Svårare
        # TODO Metoden change_team ska ändra spelarens efternamn till parametern new_lastname
        # Exempel: namn = Lionel Messi
        # Metoden kallas med new_lastname = Ronaldo
        # Nytt namn = Lionel Ronaldo
        pass
