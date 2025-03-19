class Character:
    def __init__(self, name, character_class, health=100):
        """Constructor that sets up the character's name, class, and health."""
        self.name = name
        self.character_class = character_class
        self.health = health

    def take_damage(self, damage):
        """Reduces health when the character takes damage."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} took {damage} damage. Health: {self.health}")

    def heal(self, amount):
        """Restores health when the character heals."""
        self.health += amount
        print(f"{self.name} healed {amount} points. Health: {self.health}")

# Creating characters
warrior = Character("Arthur", "Warrior", 120)
mage = Character("Merlin", "Mage", 80)

# Simulating gameplay
warrior.take_damage(30)  # Warrior takes 30 damage
mage.heal(20)  # Mage heals 20 health
mage.take_damage(90)  # Mage takes too much damage and is defeated