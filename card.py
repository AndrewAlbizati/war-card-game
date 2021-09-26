class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit.lower()
        
    def get_name(self):
        if (self.value == 1):
            return "Ace of " + self.suit.capitalize()

        if (self.value == 11):
            return "Jack of " + self.suit.capitalize()

        if (self.value == 12):
            return "Queen of " + self.suit.capitalize()

        if (self.value == 13):
            return "King of " + self.suit.capitalize()
        
        return f"{self.value} of {self.suit.capitalize()}"
    
    # A card's ID is the value + first letter of the suit
    # e.g. 2d, 3c, 4s, 5h
    def get_id(self):
        return f"{self.value}{self.suit[0]}"
