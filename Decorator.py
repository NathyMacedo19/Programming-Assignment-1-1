class Player:
    """Base player class with standard movement"""
    def move(self):
        return "Player moves normally"
class PowerUpDecorator:
    """Base class for power-up decorators"""
    def __init__(self, player):
        self.player = player  # Stores the original player object

    def move(self):
        return self.player.move()  # Default behaviour
    
class DoubleJump(PowerUpDecorator):
    """Decorator that adds double jump ability"""
    def move(self):
        return self.player.move() + " and can Double Jump"

class Shield(PowerUpDecorator):
    """Decorator that adds a shield for protection"""
    def move(self):
        return self.player.move() + " and has a Shield"

# Create a basic player
player = Player()
print(player.move())  # Output: "Player moves normally"

# Add a Double Jump power-up
player = DoubleJump(player)
print(player.move())  # Output: "Player moves normally and can Double Jump"

# Add a Shield power-up on top of Double Jump
player = Shield(player)
print(player.move())  # Output: "Player moves normally and can Double Jump and has a Shield"        